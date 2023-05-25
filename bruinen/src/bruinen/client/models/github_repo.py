from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_repo_owner import GithubRepoOwner
    from ..models.github_repo_permissions import GithubRepoPermissions


T = TypeVar("T", bound="GithubRepo")


@attr.s(auto_attribs=True)
class GithubRepo:
    """A github repo

    Attributes:
        id (Union[Unset, str]): The id of the repo
        node_id (Union[Unset, str]): The node id of the repo
        name (Union[Unset, str]): The name of the repo
        full_name (Union[Unset, str]): The full name of the repo
        private (Union[Unset, bool]): Whether the repo is private
        owner (Union[Unset, GithubRepoOwner]): The owner of this github repo
        html_url (Union[Unset, str]): The html url of the repo
        description (Union[Unset, str]): The description of the repo
        fork (Union[Unset, bool]): Whether the repo is a fork
        url (Union[Unset, str]): The url of the repo
        forks_url (Union[Unset, str]): The forks url of the repo
        keys_url (Union[Unset, str]): The keys url of the repo
        collaborators_url (Union[Unset, str]): The collaborators url of the repo
        teams_url (Union[Unset, str]): The teams url of the repo
        hooks_url (Union[Unset, str]): The hooks url of the repo
        issue_events_url (Union[Unset, str]): The issue events url of the repo
        events_url (Union[Unset, str]): The events url of the repo
        assignees_url (Union[Unset, str]): The assignees url of the repo
        branches_url (Union[Unset, str]): The branches url of the repo
        tags_url (Union[Unset, str]): The tags url of the repo
        blobs_url (Union[Unset, str]): The blobs url of the repo
        git_tags_url (Union[Unset, str]): The git tags url of the repo
        git_refs_url (Union[Unset, str]): The git refs url of the repo
        trees_url (Union[Unset, str]): The trees url of the repo
        statuses_url (Union[Unset, str]): The statuses url of the repo
        languages_url (Union[Unset, str]): The languages url of the repo
        stargazers_url (Union[Unset, str]): The stargazers url of the repo
        contributors_url (Union[Unset, str]): The contributors url of the repo
        subscribers_url (Union[Unset, str]): The subscribers url of the repo
        subscription_url (Union[Unset, str]): The subscription url of the repo
        commits_url (Union[Unset, str]): The commits url of the repo
        git_commits_url (Union[Unset, str]): The git commits url of the repo
        comments_url (Union[Unset, str]): The comments url of the repo
        issue_comment_url (Union[Unset, str]): The issue comment url of the repo
        contents_url (Union[Unset, str]): The contents url of the repo
        compare_url (Union[Unset, str]): The compare url of the repo
        merges_url (Union[Unset, str]): The merges url of the repo
        archive_url (Union[Unset, str]): The archive url of the repo
        downloads_url (Union[Unset, str]): The downloads url of the repo
        issues_url (Union[Unset, str]): The issues url of the repo
        pulls_url (Union[Unset, str]): The pulls url of the repo
        milestones_url (Union[Unset, str]): The milestones url of the repo
        notifications_url (Union[Unset, str]): The notifications url of the repo
        labels_url (Union[Unset, str]): The labels url of the repo
        releases_url (Union[Unset, str]): The releases url of the repo
        deployments_url (Union[Unset, str]): The deployments url of the repo
        created_at (Union[Unset, str]): The creation date of the repo
        updated_at (Union[Unset, str]): The update date of the repo
        pushed_at (Union[Unset, str]): The pushed at date of the repo
        git_url (Union[Unset, str]): The git url of the repo
        ssh_url (Union[Unset, str]): The ssh url of the repo
        clone_url (Union[Unset, str]): The clone url of the repo
        svn_url (Union[Unset, str]): The svn url of the repo
        homepage (Union[Unset, str]): The homepage of the repo
        size (Union[Unset, float]): The size of the repo
        stargazers_count (Union[Unset, float]): The stargazers count of the repo
        watchers_count (Union[Unset, float]): The watchers count of the repo
        language (Union[Unset, str]): The language of the repo
        has_issues (Union[Unset, bool]): Whether the repo has issues
        has_projects (Union[Unset, bool]): Whether the repo has projects
        has_downloads (Union[Unset, bool]): Whether the repo has downloads
        has_wiki (Union[Unset, bool]): Whether the repo has a wiki
        has_pages (Union[Unset, bool]): Whether the repo has pages
        forks_count (Union[Unset, float]): The forks count of the repo
        mirror_url (Union[Unset, str]): The mirror url of the repo
        archived (Union[Unset, bool]): Whether the repo is archived
        disabled (Union[Unset, bool]): Whether the repo is disabled
        open_issues_count (Union[Unset, float]): The open issues count of the repo
        license_ (Union[Unset, str]): The license of the repo
        allow_forking (Union[Unset, bool]): Whether the repo allows forking
        is_template (Union[Unset, bool]): Whether the repo is a template
        web_commit_signoff_required (Union[Unset, bool]): Whether the repo requires web commit signoff
        topics (Union[Unset, List[str]]): The topics of the repo
        visibility (Union[Unset, str]): The visibility of the repo
        default_branch (Union[Unset, str]): The default branch of the repo
        permissions (Union[Unset, GithubRepoPermissions]): The permissions object for the repo
    """

    id: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    private: Union[Unset, bool] = UNSET
    owner: Union[Unset, "GithubRepoOwner"] = UNSET
    html_url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fork: Union[Unset, bool] = UNSET
    url: Union[Unset, str] = UNSET
    forks_url: Union[Unset, str] = UNSET
    keys_url: Union[Unset, str] = UNSET
    collaborators_url: Union[Unset, str] = UNSET
    teams_url: Union[Unset, str] = UNSET
    hooks_url: Union[Unset, str] = UNSET
    issue_events_url: Union[Unset, str] = UNSET
    events_url: Union[Unset, str] = UNSET
    assignees_url: Union[Unset, str] = UNSET
    branches_url: Union[Unset, str] = UNSET
    tags_url: Union[Unset, str] = UNSET
    blobs_url: Union[Unset, str] = UNSET
    git_tags_url: Union[Unset, str] = UNSET
    git_refs_url: Union[Unset, str] = UNSET
    trees_url: Union[Unset, str] = UNSET
    statuses_url: Union[Unset, str] = UNSET
    languages_url: Union[Unset, str] = UNSET
    stargazers_url: Union[Unset, str] = UNSET
    contributors_url: Union[Unset, str] = UNSET
    subscribers_url: Union[Unset, str] = UNSET
    subscription_url: Union[Unset, str] = UNSET
    commits_url: Union[Unset, str] = UNSET
    git_commits_url: Union[Unset, str] = UNSET
    comments_url: Union[Unset, str] = UNSET
    issue_comment_url: Union[Unset, str] = UNSET
    contents_url: Union[Unset, str] = UNSET
    compare_url: Union[Unset, str] = UNSET
    merges_url: Union[Unset, str] = UNSET
    archive_url: Union[Unset, str] = UNSET
    downloads_url: Union[Unset, str] = UNSET
    issues_url: Union[Unset, str] = UNSET
    pulls_url: Union[Unset, str] = UNSET
    milestones_url: Union[Unset, str] = UNSET
    notifications_url: Union[Unset, str] = UNSET
    labels_url: Union[Unset, str] = UNSET
    releases_url: Union[Unset, str] = UNSET
    deployments_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    pushed_at: Union[Unset, str] = UNSET
    git_url: Union[Unset, str] = UNSET
    ssh_url: Union[Unset, str] = UNSET
    clone_url: Union[Unset, str] = UNSET
    svn_url: Union[Unset, str] = UNSET
    homepage: Union[Unset, str] = UNSET
    size: Union[Unset, float] = UNSET
    stargazers_count: Union[Unset, float] = UNSET
    watchers_count: Union[Unset, float] = UNSET
    language: Union[Unset, str] = UNSET
    has_issues: Union[Unset, bool] = UNSET
    has_projects: Union[Unset, bool] = UNSET
    has_downloads: Union[Unset, bool] = UNSET
    has_wiki: Union[Unset, bool] = UNSET
    has_pages: Union[Unset, bool] = UNSET
    forks_count: Union[Unset, float] = UNSET
    mirror_url: Union[Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    disabled: Union[Unset, bool] = UNSET
    open_issues_count: Union[Unset, float] = UNSET
    license_: Union[Unset, str] = UNSET
    allow_forking: Union[Unset, bool] = UNSET
    is_template: Union[Unset, bool] = UNSET
    web_commit_signoff_required: Union[Unset, bool] = UNSET
    topics: Union[Unset, List[str]] = UNSET
    visibility: Union[Unset, str] = UNSET
    default_branch: Union[Unset, str] = UNSET
    permissions: Union[Unset, "GithubRepoPermissions"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        name = self.name
        full_name = self.full_name
        private = self.private
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        html_url = self.html_url
        description = self.description
        fork = self.fork
        url = self.url
        forks_url = self.forks_url
        keys_url = self.keys_url
        collaborators_url = self.collaborators_url
        teams_url = self.teams_url
        hooks_url = self.hooks_url
        issue_events_url = self.issue_events_url
        events_url = self.events_url
        assignees_url = self.assignees_url
        branches_url = self.branches_url
        tags_url = self.tags_url
        blobs_url = self.blobs_url
        git_tags_url = self.git_tags_url
        git_refs_url = self.git_refs_url
        trees_url = self.trees_url
        statuses_url = self.statuses_url
        languages_url = self.languages_url
        stargazers_url = self.stargazers_url
        contributors_url = self.contributors_url
        subscribers_url = self.subscribers_url
        subscription_url = self.subscription_url
        commits_url = self.commits_url
        git_commits_url = self.git_commits_url
        comments_url = self.comments_url
        issue_comment_url = self.issue_comment_url
        contents_url = self.contents_url
        compare_url = self.compare_url
        merges_url = self.merges_url
        archive_url = self.archive_url
        downloads_url = self.downloads_url
        issues_url = self.issues_url
        pulls_url = self.pulls_url
        milestones_url = self.milestones_url
        notifications_url = self.notifications_url
        labels_url = self.labels_url
        releases_url = self.releases_url
        deployments_url = self.deployments_url
        created_at = self.created_at
        updated_at = self.updated_at
        pushed_at = self.pushed_at
        git_url = self.git_url
        ssh_url = self.ssh_url
        clone_url = self.clone_url
        svn_url = self.svn_url
        homepage = self.homepage
        size = self.size
        stargazers_count = self.stargazers_count
        watchers_count = self.watchers_count
        language = self.language
        has_issues = self.has_issues
        has_projects = self.has_projects
        has_downloads = self.has_downloads
        has_wiki = self.has_wiki
        has_pages = self.has_pages
        forks_count = self.forks_count
        mirror_url = self.mirror_url
        archived = self.archived
        disabled = self.disabled
        open_issues_count = self.open_issues_count
        license_ = self.license_
        allow_forking = self.allow_forking
        is_template = self.is_template
        web_commit_signoff_required = self.web_commit_signoff_required
        topics: Union[Unset, List[str]] = UNSET
        if not isinstance(self.topics, Unset):
            topics = self.topics

        visibility = self.visibility
        default_branch = self.default_branch
        permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if name is not UNSET:
            field_dict["name"] = name
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if private is not UNSET:
            field_dict["private"] = private
        if owner is not UNSET:
            field_dict["owner"] = owner
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if description is not UNSET:
            field_dict["description"] = description
        if fork is not UNSET:
            field_dict["fork"] = fork
        if url is not UNSET:
            field_dict["url"] = url
        if forks_url is not UNSET:
            field_dict["forks_url"] = forks_url
        if keys_url is not UNSET:
            field_dict["keys_url"] = keys_url
        if collaborators_url is not UNSET:
            field_dict["collaborators_url"] = collaborators_url
        if teams_url is not UNSET:
            field_dict["teams_url"] = teams_url
        if hooks_url is not UNSET:
            field_dict["hooks_url"] = hooks_url
        if issue_events_url is not UNSET:
            field_dict["issue_events_url"] = issue_events_url
        if events_url is not UNSET:
            field_dict["events_url"] = events_url
        if assignees_url is not UNSET:
            field_dict["assignees_url"] = assignees_url
        if branches_url is not UNSET:
            field_dict["branches_url"] = branches_url
        if tags_url is not UNSET:
            field_dict["tags_url"] = tags_url
        if blobs_url is not UNSET:
            field_dict["blobs_url"] = blobs_url
        if git_tags_url is not UNSET:
            field_dict["git_tags_url"] = git_tags_url
        if git_refs_url is not UNSET:
            field_dict["git_refs_url"] = git_refs_url
        if trees_url is not UNSET:
            field_dict["trees_url"] = trees_url
        if statuses_url is not UNSET:
            field_dict["statuses_url"] = statuses_url
        if languages_url is not UNSET:
            field_dict["languages_url"] = languages_url
        if stargazers_url is not UNSET:
            field_dict["stargazers_url"] = stargazers_url
        if contributors_url is not UNSET:
            field_dict["contributors_url"] = contributors_url
        if subscribers_url is not UNSET:
            field_dict["subscribers_url"] = subscribers_url
        if subscription_url is not UNSET:
            field_dict["subscription_url"] = subscription_url
        if commits_url is not UNSET:
            field_dict["commits_url"] = commits_url
        if git_commits_url is not UNSET:
            field_dict["git_commits_url"] = git_commits_url
        if comments_url is not UNSET:
            field_dict["comments_url"] = comments_url
        if issue_comment_url is not UNSET:
            field_dict["issue_comment_url"] = issue_comment_url
        if contents_url is not UNSET:
            field_dict["contents_url"] = contents_url
        if compare_url is not UNSET:
            field_dict["compare_url"] = compare_url
        if merges_url is not UNSET:
            field_dict["merges_url"] = merges_url
        if archive_url is not UNSET:
            field_dict["archive_url"] = archive_url
        if downloads_url is not UNSET:
            field_dict["downloads_url"] = downloads_url
        if issues_url is not UNSET:
            field_dict["issues_url"] = issues_url
        if pulls_url is not UNSET:
            field_dict["pulls_url"] = pulls_url
        if milestones_url is not UNSET:
            field_dict["milestones_url"] = milestones_url
        if notifications_url is not UNSET:
            field_dict["notifications_url"] = notifications_url
        if labels_url is not UNSET:
            field_dict["labels_url"] = labels_url
        if releases_url is not UNSET:
            field_dict["releases_url"] = releases_url
        if deployments_url is not UNSET:
            field_dict["deployments_url"] = deployments_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if pushed_at is not UNSET:
            field_dict["pushed_at"] = pushed_at
        if git_url is not UNSET:
            field_dict["git_url"] = git_url
        if ssh_url is not UNSET:
            field_dict["ssh_url"] = ssh_url
        if clone_url is not UNSET:
            field_dict["clone_url"] = clone_url
        if svn_url is not UNSET:
            field_dict["svn_url"] = svn_url
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if size is not UNSET:
            field_dict["size"] = size
        if stargazers_count is not UNSET:
            field_dict["stargazers_count"] = stargazers_count
        if watchers_count is not UNSET:
            field_dict["watchers_count"] = watchers_count
        if language is not UNSET:
            field_dict["language"] = language
        if has_issues is not UNSET:
            field_dict["has_issues"] = has_issues
        if has_projects is not UNSET:
            field_dict["has_projects"] = has_projects
        if has_downloads is not UNSET:
            field_dict["has_downloads"] = has_downloads
        if has_wiki is not UNSET:
            field_dict["has_wiki"] = has_wiki
        if has_pages is not UNSET:
            field_dict["has_pages"] = has_pages
        if forks_count is not UNSET:
            field_dict["forks_count"] = forks_count
        if mirror_url is not UNSET:
            field_dict["mirror_url"] = mirror_url
        if archived is not UNSET:
            field_dict["archived"] = archived
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if open_issues_count is not UNSET:
            field_dict["open_issues_count"] = open_issues_count
        if license_ is not UNSET:
            field_dict["license"] = license_
        if allow_forking is not UNSET:
            field_dict["allow_forking"] = allow_forking
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if web_commit_signoff_required is not UNSET:
            field_dict["web_commit_signoff_required"] = web_commit_signoff_required
        if topics is not UNSET:
            field_dict["topics"] = topics
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_repo_owner import GithubRepoOwner
        from ..models.github_repo_permissions import GithubRepoPermissions

        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        node_id = d.pop("node_id", UNSET) or UNSET

        name = d.pop("name", UNSET) or UNSET

        full_name = d.pop("full_name", UNSET) or UNSET

        private = d.pop("private", UNSET) or UNSET

        _owner = d.pop("owner", UNSET) or UNSET
        owner: Union[Unset, GithubRepoOwner]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = GithubRepoOwner.from_dict(_owner)

        html_url = d.pop("html_url", UNSET) or UNSET

        description = d.pop("description", UNSET) or UNSET

        fork = d.pop("fork", UNSET) or UNSET

        url = d.pop("url", UNSET) or UNSET

        forks_url = d.pop("forks_url", UNSET) or UNSET

        keys_url = d.pop("keys_url", UNSET) or UNSET

        collaborators_url = d.pop("collaborators_url", UNSET) or UNSET

        teams_url = d.pop("teams_url", UNSET) or UNSET

        hooks_url = d.pop("hooks_url", UNSET) or UNSET

        issue_events_url = d.pop("issue_events_url", UNSET) or UNSET

        events_url = d.pop("events_url", UNSET) or UNSET

        assignees_url = d.pop("assignees_url", UNSET) or UNSET

        branches_url = d.pop("branches_url", UNSET) or UNSET

        tags_url = d.pop("tags_url", UNSET) or UNSET

        blobs_url = d.pop("blobs_url", UNSET) or UNSET

        git_tags_url = d.pop("git_tags_url", UNSET) or UNSET

        git_refs_url = d.pop("git_refs_url", UNSET) or UNSET

        trees_url = d.pop("trees_url", UNSET) or UNSET

        statuses_url = d.pop("statuses_url", UNSET) or UNSET

        languages_url = d.pop("languages_url", UNSET) or UNSET

        stargazers_url = d.pop("stargazers_url", UNSET) or UNSET

        contributors_url = d.pop("contributors_url", UNSET) or UNSET

        subscribers_url = d.pop("subscribers_url", UNSET) or UNSET

        subscription_url = d.pop("subscription_url", UNSET) or UNSET

        commits_url = d.pop("commits_url", UNSET) or UNSET

        git_commits_url = d.pop("git_commits_url", UNSET) or UNSET

        comments_url = d.pop("comments_url", UNSET) or UNSET

        issue_comment_url = d.pop("issue_comment_url", UNSET) or UNSET

        contents_url = d.pop("contents_url", UNSET) or UNSET

        compare_url = d.pop("compare_url", UNSET) or UNSET

        merges_url = d.pop("merges_url", UNSET) or UNSET

        archive_url = d.pop("archive_url", UNSET) or UNSET

        downloads_url = d.pop("downloads_url", UNSET) or UNSET

        issues_url = d.pop("issues_url", UNSET) or UNSET

        pulls_url = d.pop("pulls_url", UNSET) or UNSET

        milestones_url = d.pop("milestones_url", UNSET) or UNSET

        notifications_url = d.pop("notifications_url", UNSET) or UNSET

        labels_url = d.pop("labels_url", UNSET) or UNSET

        releases_url = d.pop("releases_url", UNSET) or UNSET

        deployments_url = d.pop("deployments_url", UNSET) or UNSET

        created_at = d.pop("created_at", UNSET) or UNSET

        updated_at = d.pop("updated_at", UNSET) or UNSET

        pushed_at = d.pop("pushed_at", UNSET) or UNSET

        git_url = d.pop("git_url", UNSET) or UNSET

        ssh_url = d.pop("ssh_url", UNSET) or UNSET

        clone_url = d.pop("clone_url", UNSET) or UNSET

        svn_url = d.pop("svn_url", UNSET) or UNSET

        homepage = d.pop("homepage", UNSET) or UNSET

        size = d.pop("size", UNSET) or UNSET

        stargazers_count = d.pop("stargazers_count", UNSET) or UNSET

        watchers_count = d.pop("watchers_count", UNSET) or UNSET

        language = d.pop("language", UNSET) or UNSET

        has_issues = d.pop("has_issues", UNSET) or UNSET

        has_projects = d.pop("has_projects", UNSET) or UNSET

        has_downloads = d.pop("has_downloads", UNSET) or UNSET

        has_wiki = d.pop("has_wiki", UNSET) or UNSET

        has_pages = d.pop("has_pages", UNSET) or UNSET

        forks_count = d.pop("forks_count", UNSET) or UNSET

        mirror_url = d.pop("mirror_url", UNSET) or UNSET

        archived = d.pop("archived", UNSET) or UNSET

        disabled = d.pop("disabled", UNSET) or UNSET

        open_issues_count = d.pop("open_issues_count", UNSET) or UNSET

        license_ = d.pop("license", UNSET) or UNSET

        allow_forking = d.pop("allow_forking", UNSET) or UNSET

        is_template = d.pop("is_template", UNSET) or UNSET

        web_commit_signoff_required = d.pop("web_commit_signoff_required", UNSET) or UNSET

        topics = cast(List[str], d.pop("topics", UNSET) or UNSET)

        visibility = d.pop("visibility", UNSET) or UNSET

        default_branch = d.pop("default_branch", UNSET) or UNSET

        _permissions = d.pop("permissions", UNSET) or UNSET
        permissions: Union[Unset, GithubRepoPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = GithubRepoPermissions.from_dict(_permissions)

        github_repo = cls(
            id=id,
            node_id=node_id,
            name=name,
            full_name=full_name,
            private=private,
            owner=owner,
            html_url=html_url,
            description=description,
            fork=fork,
            url=url,
            forks_url=forks_url,
            keys_url=keys_url,
            collaborators_url=collaborators_url,
            teams_url=teams_url,
            hooks_url=hooks_url,
            issue_events_url=issue_events_url,
            events_url=events_url,
            assignees_url=assignees_url,
            branches_url=branches_url,
            tags_url=tags_url,
            blobs_url=blobs_url,
            git_tags_url=git_tags_url,
            git_refs_url=git_refs_url,
            trees_url=trees_url,
            statuses_url=statuses_url,
            languages_url=languages_url,
            stargazers_url=stargazers_url,
            contributors_url=contributors_url,
            subscribers_url=subscribers_url,
            subscription_url=subscription_url,
            commits_url=commits_url,
            git_commits_url=git_commits_url,
            comments_url=comments_url,
            issue_comment_url=issue_comment_url,
            contents_url=contents_url,
            compare_url=compare_url,
            merges_url=merges_url,
            archive_url=archive_url,
            downloads_url=downloads_url,
            issues_url=issues_url,
            pulls_url=pulls_url,
            milestones_url=milestones_url,
            notifications_url=notifications_url,
            labels_url=labels_url,
            releases_url=releases_url,
            deployments_url=deployments_url,
            created_at=created_at,
            updated_at=updated_at,
            pushed_at=pushed_at,
            git_url=git_url,
            ssh_url=ssh_url,
            clone_url=clone_url,
            svn_url=svn_url,
            homepage=homepage,
            size=size,
            stargazers_count=stargazers_count,
            watchers_count=watchers_count,
            language=language,
            has_issues=has_issues,
            has_projects=has_projects,
            has_downloads=has_downloads,
            has_wiki=has_wiki,
            has_pages=has_pages,
            forks_count=forks_count,
            mirror_url=mirror_url,
            archived=archived,
            disabled=disabled,
            open_issues_count=open_issues_count,
            license_=license_,
            allow_forking=allow_forking,
            is_template=is_template,
            web_commit_signoff_required=web_commit_signoff_required,
            topics=topics,
            visibility=visibility,
            default_branch=default_branch,
            permissions=permissions,
        )

        github_repo.additional_properties = d
        return github_repo

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
