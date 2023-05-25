from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubProfile")


@attr.s(auto_attribs=True)
class GithubProfile:
    """A github profile

    Attributes:
        login (Union[Unset, str]): The username of the user
        id (Union[Unset, str]): The id of the user
        node_id (Union[Unset, str]): The node id of the user
        avatar_url (Union[Unset, str]): The avatar url of the user
        gravatar_id (Union[Unset, str]): The gravatar id of the user
        url (Union[Unset, str]): The url of the user
        html_url (Union[Unset, str]): The html url of the user
        followers_url (Union[Unset, str]): The followers url of the user
        following_url (Union[Unset, str]): The following url of the user
        gists_url (Union[Unset, str]): The gists url of the user
        starred_url (Union[Unset, str]): The starred url of the user
        subscriptions_url (Union[Unset, str]): The starred url of the user
        organizations_url (Union[Unset, str]): The organizations url of the user
        repos_url (Union[Unset, str]): The repos url of the user
        events_url (Union[Unset, str]): The events url of the user
        received_events_url (Union[Unset, str]): The received events url of the user
        type (Union[Unset, str]): The type of the user
        site_admin (Union[Unset, bool]): Indicates if the user is a site admin
        name (Union[Unset, str]): The name of the user
        company (Union[Unset, str]): The company of the user
        blog (Union[Unset, str]): The blog of the user
        location (Union[Unset, str]): The location of the user
        email (Union[Unset, str]): The email of the user
        hireable (Union[Unset, str]): Indicates whether the user is hireable
        bio (Union[Unset, str]): The bio of the user
        twitter_username (Union[Unset, str]): The twitter username of the user
        public_repos (Union[Unset, float]): The number of public repos for the user
        public_gists (Union[Unset, float]): The number of public gists for the user
        followers (Union[Unset, float]): The number of followers for the user
        following (Union[Unset, float]): The number of following for the user
        created_at (Union[Unset, str]): Account creation date
        updated_at (Union[Unset, str]): Account update date
        private_gists (Union[Unset, float]): The number of private gists for the user
        total_private_repos (Union[Unset, float]): The number of total repos for the user
        owned_private_repos (Union[Unset, float]): The number of owned private repos for the user
        disk_usage (Union[Unset, float]): The user's disk usage
        collaborators (Union[Unset, float]): The number of collaborators for the user
        two_factor_authentication (Union[Unset, bool]): Indicates whether 2FA is required
    """

    login: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    gravatar_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    followers_url: Union[Unset, str] = UNSET
    following_url: Union[Unset, str] = UNSET
    gists_url: Union[Unset, str] = UNSET
    starred_url: Union[Unset, str] = UNSET
    subscriptions_url: Union[Unset, str] = UNSET
    organizations_url: Union[Unset, str] = UNSET
    repos_url: Union[Unset, str] = UNSET
    events_url: Union[Unset, str] = UNSET
    received_events_url: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    site_admin: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    blog: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    hireable: Union[Unset, str] = UNSET
    bio: Union[Unset, str] = UNSET
    twitter_username: Union[Unset, str] = UNSET
    public_repos: Union[Unset, float] = UNSET
    public_gists: Union[Unset, float] = UNSET
    followers: Union[Unset, float] = UNSET
    following: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    private_gists: Union[Unset, float] = UNSET
    total_private_repos: Union[Unset, float] = UNSET
    owned_private_repos: Union[Unset, float] = UNSET
    disk_usage: Union[Unset, float] = UNSET
    collaborators: Union[Unset, float] = UNSET
    two_factor_authentication: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login
        id = self.id
        node_id = self.node_id
        avatar_url = self.avatar_url
        gravatar_id = self.gravatar_id
        url = self.url
        html_url = self.html_url
        followers_url = self.followers_url
        following_url = self.following_url
        gists_url = self.gists_url
        starred_url = self.starred_url
        subscriptions_url = self.subscriptions_url
        organizations_url = self.organizations_url
        repos_url = self.repos_url
        events_url = self.events_url
        received_events_url = self.received_events_url
        type = self.type
        site_admin = self.site_admin
        name = self.name
        company = self.company
        blog = self.blog
        location = self.location
        email = self.email
        hireable = self.hireable
        bio = self.bio
        twitter_username = self.twitter_username
        public_repos = self.public_repos
        public_gists = self.public_gists
        followers = self.followers
        following = self.following
        created_at = self.created_at
        updated_at = self.updated_at
        private_gists = self.private_gists
        total_private_repos = self.total_private_repos
        owned_private_repos = self.owned_private_repos
        disk_usage = self.disk_usage
        collaborators = self.collaborators
        two_factor_authentication = self.two_factor_authentication

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login is not UNSET:
            field_dict["login"] = login
        if id is not UNSET:
            field_dict["id"] = id
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if gravatar_id is not UNSET:
            field_dict["gravatar_id"] = gravatar_id
        if url is not UNSET:
            field_dict["url"] = url
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if followers_url is not UNSET:
            field_dict["followers_url"] = followers_url
        if following_url is not UNSET:
            field_dict["following_url"] = following_url
        if gists_url is not UNSET:
            field_dict["gists_url"] = gists_url
        if starred_url is not UNSET:
            field_dict["starred_url"] = starred_url
        if subscriptions_url is not UNSET:
            field_dict["subscriptions_url"] = subscriptions_url
        if organizations_url is not UNSET:
            field_dict["organizations_url"] = organizations_url
        if repos_url is not UNSET:
            field_dict["repos_url"] = repos_url
        if events_url is not UNSET:
            field_dict["events_url"] = events_url
        if received_events_url is not UNSET:
            field_dict["received_events_url"] = received_events_url
        if type is not UNSET:
            field_dict["type"] = type
        if site_admin is not UNSET:
            field_dict["site_admin"] = site_admin
        if name is not UNSET:
            field_dict["name"] = name
        if company is not UNSET:
            field_dict["company"] = company
        if blog is not UNSET:
            field_dict["blog"] = blog
        if location is not UNSET:
            field_dict["location"] = location
        if email is not UNSET:
            field_dict["email"] = email
        if hireable is not UNSET:
            field_dict["hireable"] = hireable
        if bio is not UNSET:
            field_dict["bio"] = bio
        if twitter_username is not UNSET:
            field_dict["twitter_username"] = twitter_username
        if public_repos is not UNSET:
            field_dict["public_repos"] = public_repos
        if public_gists is not UNSET:
            field_dict["public_gists"] = public_gists
        if followers is not UNSET:
            field_dict["followers"] = followers
        if following is not UNSET:
            field_dict["following"] = following
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if private_gists is not UNSET:
            field_dict["private_gists"] = private_gists
        if total_private_repos is not UNSET:
            field_dict["total_private_repos"] = total_private_repos
        if owned_private_repos is not UNSET:
            field_dict["owned_private_repos"] = owned_private_repos
        if disk_usage is not UNSET:
            field_dict["disk_usage"] = disk_usage
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if two_factor_authentication is not UNSET:
            field_dict["two_factor_authentication"] = two_factor_authentication

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login = d.pop("login", UNSET) or UNSET

        id = d.pop("id", UNSET) or UNSET

        node_id = d.pop("node_id", UNSET) or UNSET

        avatar_url = d.pop("avatar_url", UNSET) or UNSET

        gravatar_id = d.pop("gravatar_id", UNSET) or UNSET

        url = d.pop("url", UNSET) or UNSET

        html_url = d.pop("html_url", UNSET) or UNSET

        followers_url = d.pop("followers_url", UNSET) or UNSET

        following_url = d.pop("following_url", UNSET) or UNSET

        gists_url = d.pop("gists_url", UNSET) or UNSET

        starred_url = d.pop("starred_url", UNSET) or UNSET

        subscriptions_url = d.pop("subscriptions_url", UNSET) or UNSET

        organizations_url = d.pop("organizations_url", UNSET) or UNSET

        repos_url = d.pop("repos_url", UNSET) or UNSET

        events_url = d.pop("events_url", UNSET) or UNSET

        received_events_url = d.pop("received_events_url", UNSET) or UNSET

        type = d.pop("type", UNSET) or UNSET

        site_admin = d.pop("site_admin", UNSET) or UNSET

        name = d.pop("name", UNSET) or UNSET

        company = d.pop("company", UNSET) or UNSET

        blog = d.pop("blog", UNSET) or UNSET

        location = d.pop("location", UNSET) or UNSET

        email = d.pop("email", UNSET) or UNSET

        hireable = d.pop("hireable", UNSET) or UNSET

        bio = d.pop("bio", UNSET) or UNSET

        twitter_username = d.pop("twitter_username", UNSET) or UNSET

        public_repos = d.pop("public_repos", UNSET) or UNSET

        public_gists = d.pop("public_gists", UNSET) or UNSET

        followers = d.pop("followers", UNSET) or UNSET

        following = d.pop("following", UNSET) or UNSET

        created_at = d.pop("created_at", UNSET) or UNSET

        updated_at = d.pop("updated_at", UNSET) or UNSET

        private_gists = d.pop("private_gists", UNSET) or UNSET

        total_private_repos = d.pop("total_private_repos", UNSET) or UNSET

        owned_private_repos = d.pop("owned_private_repos", UNSET) or UNSET

        disk_usage = d.pop("disk_usage", UNSET) or UNSET

        collaborators = d.pop("collaborators", UNSET) or UNSET

        two_factor_authentication = d.pop("two_factor_authentication", UNSET) or UNSET

        github_profile = cls(
            login=login,
            id=id,
            node_id=node_id,
            avatar_url=avatar_url,
            gravatar_id=gravatar_id,
            url=url,
            html_url=html_url,
            followers_url=followers_url,
            following_url=following_url,
            gists_url=gists_url,
            starred_url=starred_url,
            subscriptions_url=subscriptions_url,
            organizations_url=organizations_url,
            repos_url=repos_url,
            events_url=events_url,
            received_events_url=received_events_url,
            type=type,
            site_admin=site_admin,
            name=name,
            company=company,
            blog=blog,
            location=location,
            email=email,
            hireable=hireable,
            bio=bio,
            twitter_username=twitter_username,
            public_repos=public_repos,
            public_gists=public_gists,
            followers=followers,
            following=following,
            created_at=created_at,
            updated_at=updated_at,
            private_gists=private_gists,
            total_private_repos=total_private_repos,
            owned_private_repos=owned_private_repos,
            disk_usage=disk_usage,
            collaborators=collaborators,
            two_factor_authentication=two_factor_authentication,
        )

        github_profile.additional_properties = d
        return github_profile

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
