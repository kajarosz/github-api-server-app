## github-api-server-app

Simple Flask server app that retrieves user profile details from Github API and processes it using dedicated functions. App returns data for requested user:
* list of repositories (repo name & number of stars)
* sum of stars from all repositories
* three mostly used programming languages (based of number of bytes of code)

Data is returned in JSON and whole app works as REST API.

### How to start server?

Fork this repo and clone it to your choosen directory (alternatively you can just download a .zip file and unpack it).
```
git clone https://github.com/kajarosz/github-api-server-app.git
```

Install dependencies - required packages are listed in requirements.txt file. You may need to use pip3 instead of just pip.
```
pip install -r requirements.txt
```

Run run_app.py file in Python. You may need to use python3 instead of just python.
```
python run_app.py
```

### How to make requests?

Go to ...

### How to run tests?

Go to project directory and run in Python:
```
pytest
```

### Improvements

This is a simple project designed mostly for personal use - it utilizes Github API without authentication. High traffic is not expected for this app, so I decided that there's no reason to complicate the code. Authentication would require client to privide Github token, which can lead to some unnecessary safety concerns. However, lack of authentication means that app use is limited to 60 requests per hour (Github API limitations). If project grows and there's higher volume of requests, to fullfil client needs authenticated Github API access should be developed. 
