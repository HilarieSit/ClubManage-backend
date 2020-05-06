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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
