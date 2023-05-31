from typing import List
from ...client.models import GithubRepo

# TODO update to include all that we need
from typing import Union, get_origin, get_args, ForwardRef
from ...client.types import Unset

from datetime import datetime
from langchain import SQLDatabase, SQLDatabaseChain
from langchain.llms import OpenAI
from langchain.prompts.prompt import PromptTemplate
from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, Table, Float, JSON, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateTable

def parse_sql_github_repos(input: List["GithubRepo"]):

    class_attrs = {
        '__tablename__': 'github_repo',
        'bruinen_id': Column(Integer, primary_key=True)
    }

    # Could maybe use SQLAlchemy for this mapping
    def map_sql_types(type_var):
        if type_var is str:
            return String
        elif type_var is int:
            return Integer
        elif type_var is datetime:
            return DateTime
        elif type_var is float:
            return Float
        elif type_var is dict:
            # Could use Indexable or JSON
            return JSON
        elif type_var is bool:
            return Boolean
        elif get_origin(type_var) is dict:
            # Not sure here, could use Indexable
            return JSON
        elif get_origin(type_var) is list:
            # Not sure here, could use Indexable
            # For now, just convert to JSON
            return JSON
        elif type(type_var) == ForwardRef:
            # TBD, this might be wrong
            return JSON
        else:
            raise ValueError(f'Unknown type when mapping Typing to SQLAlchemy: {type_var}')

    # TODO figure out another way to pull this that doesn't use dict and annotations
    for k, v in GithubRepo.__dict__['__annotations__'].items():        
        if get_origin(v) is Union:
            # Assume that the first arg is of type Unset
            if get_args(v)[0] is not Unset:
                raise ValueError('Union type with first value not Unset not supported')
            class_attrs[k] = Column(map_sql_types(get_args(v)[1]), nullable=True)
        else:
            class_attrs[k] = Column(map_sql_types(v))

    engine = create_engine('sqlite:///notebooks/github.db', echo=True)
    Base = declarative_base()
    repo_class = type('Repo', (Base,), class_attrs)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    data = []
    for line in input:
        data.append(line.to_dict())
    session.bulk_insert_mappings(repo_class, data)
    session.commit()
    session.close()

    metadata = MetaData()
    metadata.reflect(bind=engine)
    mytable = Table('github_repo', metadata, autoload=True, autoload_with=engine)
    
    template_table = "\nOnly use the following tables:\n" + str(CreateTable(mytable).compile(engine))
    # If the table isn't too large, would be better to also include example data
    template_start = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer. Use the following format:

    Question: "Question here"
    SQLQuery: "SQL Query to run"
    SQLResult: "Result of the SQLQuery"
    Answer: "Final answer here"
    """
    template_end = "Question: {input}"
    
    prompt_template = template_start + template_table + template_end
    print('template')
    print(prompt_template)

    prompt = PromptTemplate(input_variables=['input', 'dialect'], template=prompt_template)
    db = SQLDatabase.from_uri('sqlite:///notebooks/github.db')
    llm = OpenAI(temperature=0)
    db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, prompt=prompt, verbose=True)
    res = db_chain.run('How many repos do I have on Github?')

    # Drop the created table so it doesn't overwrite later
    mytable.drop(engine)

    return res