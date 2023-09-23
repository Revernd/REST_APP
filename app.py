from flask import Flask
from flask_restful import Api
from .resources.hellofresco import HelloFresco
from .resources.frescoplaycourese import PlayCourses, playcourses_bp
from .resources.SimpleInterest import SimpleInterest


def create_app(testing_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if testing_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(testing_config)

    api = Api()
    api.add_resource(HelloFresco, '/')
    api.add_resource(PlayCourses, '/Courses/', '/Courses/<int:course_id>')
    api.add_resource(SimpleInterest, '/simpleinterest/')
    api.init_app(app)

    app.register_blueprint(playcourses_bp)

    @app.route('/home')
    def home():
        return 'Application working Status : ' + app.config['SECRET_KEY']

    return app