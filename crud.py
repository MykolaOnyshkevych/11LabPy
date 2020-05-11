from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from main.model_package.abstract_exercise_machine import MainExerciseMachine
import json
import copy


with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class RaceTrackObject(MainExerciseMachine, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price_per_hour = db.Column(db.Integer, unique=False)
    duration_in_minutes = db.Column(db.Integer, unique=False)
    producing_country = db.Column(db.String(64), unique=False)
    model = db.Column(db.String(64), unique=False)
    earl = db.Column(db.String(64), unique=False)

    def __init__(self, price_per_hour=0, duration_in_minutes=0, producing_country="choose",
                 model="nt-200", earl="earl"):
        super().__init__(price_per_hour, duration_in_minutes, producing_country, model)
        self.earl = earl


class RaceTrackSchema(ma.Schema):
    class Meta:
        fields = ('price_per_hour', 'duration_in_minutes', 'producing_country', 'model', 'earl')


racetrack_schema = RaceTrackSchema()
racetracks_schema = RaceTrackSchema(many=True)


@app.route("/racetracks", methods=["POST"])
def add_racetrack():
    price_per_hour = request.json['price_per_hour']
    duration_in_minutes = request.json['duration_in_minutes']
    producing_country = request.json['producing_country']
    model = request.json['model']
    earl = request.json['earl']
    racetrack = RaceTrackObject(price_per_hour,
                                duration_in_minutes,
                                producing_country,
                                model,
                                earl)
    db.session.add(racetrack)
    db.session.commit()
    return racetrack_schema.jsonify(racetrack)


@app.route("/racetracks", methods=["GET"])
def get_racetracks():
    all_racetracks = RaceTrackObject.query.all()
    result = racetracks_schema.dump(all_racetracks)
    return jsonify({'racetracks': result})


@app.route("/racetracks/<id>", methods=["GET"])
def get_racetrack(id):
    racetrack = RaceTrackObject.query.get(id)
    if not racetrack:
        abort(404)
    return racetrack_schema.jsonify(racetrack)


@app.route("/racetracks/<id>", methods=["PUT"])
def racetrack_update(id):
    racetrack = RaceTrackObject.query.get(id)
    if not racetrack:
        abort(404)
    old_smart_home_appliance = copy.deepcopy(racetrack)
    racetrack.price_per_hour = request.json['price_per_hour']
    racetrack.duration_in_minutes = request.json['duration_in_minutes']
    racetrack.producing_country = request.json['producing_country']
    racetrack.model = request.json['model']
    racetrack.earl = request.json['earl']
    db.session.commit()
    return racetrack_schema.jsonify(old_smart_home_appliance)


@app.route("/racetracks/<id>", methods=["DELETE"])
def racetrack_delete(id):
    racetrack = RaceTrackObject.query.get(id)
    if not racetrack:
        abort(404)
    db.session.delete(racetrack)
    db.session.commit()
    return racetrack_schema.jsonify(racetrack)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')