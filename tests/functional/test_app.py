import unittest
from flask import Flask

user_name = 'kajarosz'

class TestGetUserRepos(unittest.TestCase):
    # check if status code is 200
    def test_status(self):
        tester = app.test_client(self)
        response = tester.get(f'/user/{user_name}/repos')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

if __name__ == '__main__':
    unittest.main()
