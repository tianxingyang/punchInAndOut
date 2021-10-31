from flask_restful import Resource, reqparse
import httplib2

from punchInAndOut.common import db


class Login(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('code', type=str, required=True, help='code 不能为空')

    def post(self):
        args = self.reqparse.parse_args()
        h = httplib2.Http()
        para = {"APPID": "wxd6dec455c6298a55",
                "SECRET": "418c82b9e62f3aeaf6d45ceaea1870cb",
                "JSCODE": args.code}
        resp, content = h.request(wx_api.AUTH_PATH.format(**para), "GET")
        print(content)
        return {"result": 0}
