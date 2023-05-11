import os, requests

# TODO try removing
os.environ['OPENAI_API_KEY'] = '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'
os.environ['BRUINEN_SECRET'] = 'clg79qu20000muk22tlx0tybn'

from langchain.agents import initialize_agent, Tool
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

from tools import BruinenVenmo, BruinenVenmoAuthenticator
from tools import BruinenGmail, BruinenGmailAuthenticator

class DocumentResponder:
    def __init__(self):
        # Venmo source and authenticator
        venmo = BruinenVenmo()
        venmo_tool = Tool(
            name = BruinenVenmo.name,
            description = BruinenVenmo.description,
            func = venmo.run
        )
        venmo_auth = BruinenVenmoAuthenticator()
        venmo_auth_tool = Tool(
            name = BruinenVenmoAuthenticator.name,
            description = BruinenVenmoAuthenticator.description,
            func = venmo_auth.run
        )

        # Gmail source and authenticator
        gmail = BruinenGmail()
        gmail_tool = Tool(
            name = BruinenGmail.name,
            description = BruinenGmail.description,
            func = gmail.run
        )
        gmail_auth = BruinenGmailAuthenticator()
        gmail_auth_tool = Tool(
            name = BruinenGmailAuthenticator.name,
            description = BruinenGmailAuthenticator.description,
            func = gmail_auth.run
        )

        self.tool_classes = [venmo, gmail]
        self.auth_classes = [venmo_auth, gmail_auth]
        self.tools = [venmo_tool, venmo_auth_tool, gmail_tool, gmail_auth_tool]
        self.user_id = ''
        self.user_token = ''

    # When a document is uploaded, run it through a LLM that summarizes the document in a tool format
    # Then, add it to the list of tools that the agent has access to
    # We'll also need to get the agent access to Bruinen data as well
    def embed_document(self, text):
        # TODO check for errors 
        embeddings = OpenAIEmbeddings()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separator='.')
        texts = text_splitter.split_text(text)
        docsearch = Chroma.from_texts(
            texts,
            embeddings,
            metadatas=[{"source": str(i)} for i in range(len(texts))],
        )

        # Run the embedded document through an LLM to create a summary
        # Then, store that summary as a tool for the query agent to use
        qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type='stuff', retriever=docsearch.as_retriever())
        title_query = '''
        Write a concise title for the provided document in the following format:

        [Insert title here] QA System
        '''
        # docs = docsearch.get_relevant_documents(query)
        title_result = qa.run({'query': title_query})

        # TODO maybe improve this to find the documents better, get better results
        summary_query = '''
        Write a one sentence summary of the provided document in the following format:

        Useful for when you need to answer questions about [insert summary here].
        '''
        summary_result = qa.run({'query': summary_query})

        doc_tool = Tool(
            name=title_result.strip(),
            func=qa.run,
            description=summary_result.strip() + ' Input should be a fully formed question.',
            # args_schema=self.QueryInput
        )

        self.tools.append(doc_tool)

        return 'complete'

    def perform_query(self, query, email):
        # If the user token isn't already set we'll need to find it, and pass it to the tools
        if self.user_token == '':
            secret = os.environ['BRUINEN_SECRET']
            args = {
                'email': email
            }
            headers = {
                'Content-Type': 'application/json',
                'X-API-Key': secret
            }

            res_user = requests.post('https://api.bruinen.co/users/find-or-create', json=args, headers=headers)
            self.user_id = res_user.json()['id']

            res_token = requests.get(f'https://api.bruinen.co/auth/{self.user_id}', headers=headers)
            self.user_token = res_token.json()['accessToken']

            # Make sure to pass the ID and token to the classes that need them
            for tool_class in self.tool_classes:
                tool_class.user_id = self.user_id
            for auth_class in self.auth_classes:
                auth_class.user_token = self.user_token

        llm = OpenAI(temperature=0)
        agent = initialize_agent(self.tools, llm, agent='chat-zero-shot-react-description', verbose=True)
        result = agent.run(query)
        
        return result


# Could use MapReduce chain
# https://twitter.com/hwchase17/status/1587458155021099008?lang=en

# Use this step: each source should be a tool
# https://python.langchain.com/en/latest/modules/agents/agent_executors/examples/agent_vectorstore.html