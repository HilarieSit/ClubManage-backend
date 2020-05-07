from flask import Flask, request
from db import db
import dao
import json

app = Flask(__name__)
db_filename = "club.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

@app.route('/api/clubs/')
def get_clubs():
    return success_response(dao.get_all_clubs())

@app.route('/api/clubs/', methods=['POST'])
def create_club():
    body = json.loads(request.data)
    club = dao.create_course(
        name = body.get('name'),
        description = body.get('description')
    )
    return success_response(club, 201)

@app.route('/api/clubs/<int:club_id>/')
def get_club(club_id):
    club = dao.get_club_by_id(club_id)
    if club is None:
        return failure_response("Club not found")
    return success_response(club)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
