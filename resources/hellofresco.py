from flask import Flask
from flask_restful import Resource, Api



class HelloFresco(Resource):
    def get(self):
        return {'message':'Welcome to Fresco Play!!!'}, 201, {'response_header1': 'some-message'}



