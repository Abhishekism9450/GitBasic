import uuid
import constants
from flask import Flask, render_template
from github import Github

import UserDetails

app = Flask(__name__)

@app.route("/")
def index():
    """
    starting page of the application
    It fetches all the repositories of the current user
    :return: Index.html (where user can see list of the repository)
    """
    g = Github(constants.Token)
    username = UserDetails.username()
    res = []
    for _ in g.get_user().get_repos():
        k = _.name
        res.append(k)
    return render_template('index.html', header="Repos", galaxies=res, username=username)

@app.route('/repos/<string:repo>')
def repos(repo):
    """
    it fetches all the branches in respective Repository
    :param repo: Current repository name
    :return: Repo.html (where user can see his branches for current repo)
    """
    g = Github(constants.Token)
    username = UserDetails.username()
    g_repo = g.get_repo(username+"/"+repo)
    repos_branch_list = [_ for _ in g_repo.get_branches()]
    return render_template('repo.html', branches=repos_branch_list, repo=repo)

@app.route('/create_branch/<string:branch>')
def create_branch(branch):
    """
    It creates a new branch for respective Repository.
    :param branch: current Repo
    :return: new branch for respective repo
    """
    g = Github(constants.Token)
    source_branch = 'master'
    target_branch = 'newfeature_' + str(uuid.uuid4())
    username = UserDetails.username()
    repo = g.get_repo(username+"/"+branch)
    sb = repo.get_branch(source_branch)
    repo.create_git_ref(ref='refs/heads/' + target_branch, sha=sb.commit.sha)
    return "Branch Created with name " + target_branch


