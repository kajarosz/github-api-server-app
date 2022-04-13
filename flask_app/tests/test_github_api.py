from flask import Flask
from flask_app.request_data.github_api import github_details, github_languages, github_stars, github_repos, github_languages

# test if function returns list object if username is valid
def test_github_details_valid():
    result = github_details('kajarosz')
    assert isinstance(result, list)

# test if function returns json data if username is valid
def test_github_repos_valid():
    result = github_repos('kajarosz')
    assert result.content_type == 'application/json'

# test if function returns None if username is not valid
def test_github_repos_invalid():
    result = github_repos('kajarosz')
    assert result.get_data() == None