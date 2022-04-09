import requests

# create decorator to check if given username exits
def if_user_exists(func):
    def inner(user_name):
        response = github_details(user_name)
        if response == {"Message": "User not found"} or response == {"Message": "Unknown error"}:
            return response
        else:
            return func(user_name)
    return inner

# Request Github API to get users repos names and stars
def github_details(user_name):
    response = requests.get(f'https://api.github.com/users/{user_name}/repos')
    response_json = response.json()
    if response.status_code == 200:
        repos =  []
        for repo in response_json:
            # get name value for repo
            name = repo.get('name')
            # get stars count for repo
            stars = repo.get('stargazers_count')
            # create repo dict and append to the list
            repos.append({'name': name, 'stars': stars})
        return repos
    elif response.status_code == 404:
        return {"Message": "User not found"}
    else:
        return {"Message": "Unknown error"}
        

# Define reponse: user repos details
@if_user_exists
def github_repos(user_name):
    repos = github_details(user_name)
    return {f'{user_name}': repos}

# Define reponse: user stars count from all repos
@if_user_exists
def github_stars(user_name):
    repos = github_details(user_name)
    user_stars =  0
    for repo in repos:
        # add repo stars number to user_stars
        user_stars = user_stars + repo.get('stars')
    return {'user_stars': user_stars}

# Define reponse: user stars top 3 languages based on number of bytes of code
@if_user_exists
def github_languages(user_name):
    repos = github_details(user_name)
    lang_dict = {}
    for repo in repos:
        github_response = requests.get('https://api.github.com/repos/{0}/{1}/languages'.format(user_name, repo.get('name'))).json()
        # sum number of bytes of code, if key already exists in lang_dict
        # add new key, value pair, if key doesn't exist in lang_dict
        lang_dict = {k: lang_dict.get(k, 0) + github_response.get(k, 0) for k in set(lang_dict) | set(github_response)}
    # return list of tuples (language, bytes of code) from dictionary
    lang_list = list(lang_dict.items())
    # sort languages list based on second item in a tuple
    lang_list.sort(reverse=True, key = lambda x: x[1])
    # return first three languages from list
    lang_top3 = lang_list[:3]
    return {k:v for (k,v) in lang_top3}