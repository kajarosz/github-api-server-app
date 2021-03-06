from flask import abort, jsonify

try:
    from flask_app.request_data.github_api import github_languages, github_stars, github_repos, github_languages
except:
    from request_data.github_api import github_languages, github_stars, github_repos, github_languages

def configure_routes(app):

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    @app.route('/user/<user_name>/repos', methods=['GET'])
    def get_user_repos(user_name):
        response = github_repos(user_name)
        if response is None:
            abort(404, description="Resource not found")
        return response

    @app.route('/user/<user_name>/stars', methods=['GET'])
    def get_user_stars(user_name):
        response = github_stars(user_name)
        if response is None:
            abort(404, description="Resource not found")
        return response

    @app.route('/user/<user_name>/top3-languages', methods=['GET'])
    def get_user_languages(user_name):
        response = github_languages(user_name)
        if response is None:
            abort(404, description="Resource not found")
        return response