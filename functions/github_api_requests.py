import requests

def github_repos(user_name):
    github_response = requests.get(f'https://api.github.com/users/{user_name}/repos').json()
    repos =  []
    for repo in github_response:
        name = repo.get('name')
        stars = repo.get('stargazers_count')
        repos.append({'name': name, 'stars': stars})
    return {f'{user_name}': repos}

def github_stars(user_name):
    github_response = requests.get(f'https://api.github.com/users/{user_name}/repos').json()
    user_stars =  0
    for repo in github_response:
        repo_stars = repo.get('stargazers_count')
        user_stars = user_stars + repo_stars
    return {'user_stars': user_stars}

def github_languages(user_name):
    github_response = requests.get(f'https://api.github.com/users/{user_name}/repos').json()
    repos =  []
    for repo in github_response:
        name = repo.get('name')
        repos.append(name)
    lang_dict = {}
    for repo in repos:
        github_response = requests.get(f'https://api.github.com/repos/{user_name}/{repo}/languages').json()
        lang_dict = {k: lang_dict.get(k, 0) + github_response.get(k, 0) for k in set(lang_dict) | set(github_response)}
    lang_list = list(lang_dict.items())
    lang_list.sort(reverse=True, key = lambda x: x[1])
    lang_top3 = lang_list[:3]
    return {k:v for (k,v) in lang_top3}