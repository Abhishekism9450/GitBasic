# from flask import jsonify
from github import Github

import constants


def username():

    """
    fetches the username of the user
    :return: username
    """

    g = Github(constants.Token)
    id= g.get_user().id
    # print(g.get_user_by_id(id))
    username = g.get_user_by_id(id)
    # print(username.login)
    return username.login
