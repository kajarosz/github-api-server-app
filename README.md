## github-api-server-app

Simple Flask server app that retrieves user profile details from Github API and processes it using dedicated functions. App returns data for requested user:
* list of repositories (repo name & number of stars)
* sum of stars from all repositories
* three mostly used programming languages (based of number of bytes of code)

Data is returned in JSON and whole app works as REST API.

### How to start server?

Fork this repo and clone it to your choosen directory (alternatively you can just download a .zip file and unpack it).

Install dependencies - required packages are listed in requirements.txt file.

Run run_app.py file in Python.
'''
python run_app.py
'''
