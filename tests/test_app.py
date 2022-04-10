from github_app.app import app
import unittest
from app import app
from flask import Flask

# test path: '/user/<user_name>/repos'
class TestGetUserRepos(unittest.TestCase):
    # check if status code is 200
    def test_status(self):
        tester = app.test_client(self)
        response = tester.get('/user/kajarosz/repos')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # check if response is in json
    def test_content_type(self):
        tester = app.test_client(self)
        response = tester.get(f'/user/kajarosz/repos')
        self.assertEqual(response.content_type, 'application/json')

    # check if data is valid
    def test_data(self):
        tester = app.test_client(self)
        response = tester.get(f'/user/kajarosz/repos')
        self.assertTrue(b'kajarosz' in response.data)


# test path: '/user/<user_name>/stars'
class TestGetUserStars(unittest.TestCase):
    # check if status code is 200
    def test_status(self):
        tester = app.test_client(self)
        response = tester.get('/user/kajarosz/stars')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # check if response is in json
    def test_content_type(self):
        tester = app.test_client(self)
        response = tester.get(f'/user/kajarosz/stars')
        self.assertEqual(response.content_type, 'application/json')

    # check if data is valid
    def test_data(self):
        tester = app.test_client(self)
        response = tester.get(f'/user/kajarosz/stars')
        self.assertTrue(b'user_stars' in response.data)


# test path: /user/<user_name>/top3-languages
class TestGetUserRepos(unittest.TestCase):
    # check if status code is 200
    def test_status(self):
        tester = app.test_client(self)
        response = tester.get('/user/kajarosz/top3-languages')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # check if response is in json
    def test_content_type(self):
        tester = app.test_client(self)
        response = tester.get(f'/user/kajarosz/top3-languages')
        self.assertEqual(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
