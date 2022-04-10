import requests
from flask import Flask

app = Flask(__name__)

username = ''
token = ''
gh_session = requests.Session()
gh_session.auth = (username, token)

@app.route('/user/<user_name>/repos', methods=['GET'])
def get_user_repos(user_name):
    github_response = gh_session.get(f'https://api.github.com/users/{user_name}/repos').json()
    repos =  []
    for repo in github_response:
        name = repo.get('name')
        stars = repo.get('stargazers_count')
        repos.append({'name': name, 'stars': stars})
    return {f'{user_name}': repos}

@app.route('/user/<user_name>/stars', methods=['GET'])
def get_user_stars(user_name):
    github_response = gh_session.get(f'https://api.github.com/users/{user_name}/repos').json()
    user_stars =  0
    for repo in github_response:
        repo_stars = repo.get('stargazers_count')
        user_stars = user_stars + repo_stars
    return {'user_stars': user_stars}


@app.route('/user/<user_name>/top3_languages', methods=['GET'])
def get_user_languages(user_name):
    github_response = gh_session.get(f'https://api.github.com/users/{user_name}/repos').json()
    repos =  []
    for repo in github_response:
        name = repo.get('name')
        repos.append(name)
    lang_dict = {}
    for repo in repos:
        github_response = gh_session.get(f'https://api.github.com/repos/{user_name}/{repo}/languages').json()
        lang_dict = {k: lang_dict.get(k, 0) + github_response.get(k, 0) for k in set(lang_dict) | set(github_response)}
    lang_list = list(lang_dict.items())
    lang_list.sort(reverse=True, key = lambda x: x[1])
    lang_top3_list = lang_list[:3]
    lang_top3_dict = {k:v for (k,v) in lang_top3_list}
    return {user_name: lang_top3_dict}