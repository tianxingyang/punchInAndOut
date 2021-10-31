from flask_restful import Resource, reqparse


class PunchIn(Resource):
    def post(self):
        return {"result": -1}


class PunchOut(Resource):
    def post(self):
        return {"result": -1}


class Leave(Resource):
    def post(self):
        return {"result": -1}


class Arrive(Resource):
    def post(self):
        return {"result": -1}
