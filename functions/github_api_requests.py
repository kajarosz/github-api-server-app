import requests

def github_details(user_name):
    github_response = requests.get(f'https://api.github.com/users/{user_name}/repos').json()
    repos =  []
    for repo in github_response:
        name = repo.get('name')
        stars = repo.get('stargazers_count')
        repos.append({'name': name, 'stars': stars})
    return repos

def github_repos(user_name):
    repos = github_details(user_name)
    return {f'{user_name}': repos}

def github_stars(user_name):
    repos = github_details(user_name)
    user_stars =  0
    for repo in repos:
        user_stars = user_stars + repo.get('stars')
    return {'user_stars': user_stars}

def github_languages(user_name):
    repos = github_details(user_name)
    lang_dict = {}
    for repo in repos:
        github_response = requests.get('https://api.github.com/repos/{0}/{1}/languages'.format(user_name, repo.get('name'))).json()
        lang_dict = {k: lang_dict.get(k, 0) + github_response.get(k, 0) for k in set(lang_dict) | set(github_response)}
    lang_list = list(lang_dict.items())
    lang_list.sort(reverse=True, key = lambda x: x[1])
    lang_top3 = lang_list[:3]
    return {k:v for (k,v) in lang_top3}