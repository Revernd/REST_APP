from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse, marshal_with, fields
import datetime as dt


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('principal_amount', type=float, help='Principal amount must be a number', location='form')
parser.add_argument('period', type=int, help="No. of Years must be an integer", location='form')
parser.add_argument('rate', type=float, help='Rate must be a number', location='form')


resource_fields = {
    'simple_interest': fields.Raw,
    'computed_on': fields.DateTime(dt_format='rfc822')
}


class SimpleInterest(Resource):
    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        p = args['principal_amount']
        n = args['period']
        r = args['rate']
        si = (p*n*r)/100.0
        return {'simple_interest':si, 'computed_on': dt.datetime.now()}


