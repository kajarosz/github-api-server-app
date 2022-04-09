from flask import Flask
from functions.github_api_requests import github_languages, github_stars, github_repos, github_languages

app = Flask(__name__)

@app.route('/user/<user_name>/repos', methods=['GET'])
def get_user_repos(user_name):
    response = github_repos(user_name)
    return response

@app.route('/user/<user_name>/stars', methods=['GET'])
def get_user_stars(user_name):
    response = github_stars(user_name)
    return response

@app.route('/user/<user_name>/top3_languages', methods=['GET'])
def get_user_languages(user_name):
    response = github_languages(user_name)
    return response