import requests

# Create exceptions
class GithubGeneralException(Exception):
    pass

class UserNotFoundException(GithubGeneralException):
    pass

class JsonParsingException(GithubGeneralException):
    pass

# Request Github API to get users repos names and stars
def github_details(user_name):
    response = requests.get(f'https://api.github.com/users/{user_name}/repos')
    response_json = response.json()
    if response.status_code != 200:
        raise UserNotFoundException
    try:
        response_json = response.json()
    except:
        raise JsonParsingException
    repos =  []
    for repo in response_json:
        # get name value for repo
        name = repo.get('name')
        # get stars count for repo
        stars = repo.get('stargazers_count')
        # create repo dict and append to the list
        repos.append({'name': name, 'stars': stars})
    return repos

        
# Define reponse: user repos details
def github_repos(user_name):
    try:
        repos = github_details(user_name)
    except UserNotFoundException:
        return None
    except JsonParsingException:
        return None
    return {f'{user_name}': repos}

# Define reponse: user stars count from all repos
def github_stars(user_name):
    try:
        repos = github_details(user_name)
    except UserNotFoundException:
        return None
    except JsonParsingException:
        return None
    user_stars =  0
    for repo in repos:
        # add repo stars number to user_stars
        user_stars = user_stars + repo.get('stars')
    return {'user_stars': user_stars}

# Define reponse: user stars top 3 languages based on number of bytes of code
def github_languages(user_name):
    try:
        repos = github_details(user_name)
    except UserNotFoundException:
        return None
    except JsonParsingException:
        return None
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
    return {f'user_name': {k:v for (k,v) in lang_top3}}