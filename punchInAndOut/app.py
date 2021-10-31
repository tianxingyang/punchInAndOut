from flask import Flask
import flask_restful as restful
from punchInAndOut.resources import auth
from punchInAndOut.resources import punch
from punchInAndOut.common import db

# db.db.create_tables([db.User, db.TripAttendance])

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(auth.Login, '/auth/login')
api.add_resource(punch.PunchIn, '/punch/in')
api.add_resource(punch.PunchOut, '/punch/out')
api.add_resource(punch.Leave, '/punch/leave')
api.add_resource(punch.Arrive, '/punch/arrive')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9528, debug=True)
