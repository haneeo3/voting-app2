from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import boto3
import json

app = Flask(__name__)
CORS(app)

s3 = boto3.client(
    "s3",
    endpoint_url="http://127.0.0.1:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

BUCKET = "voting-app2"

def get_votes():
    try:
        obj = s3.get_object(Bucket=BUCKET, Key="votes.json")
        return json.loads(obj["Body"].read())
    except:
        return {"Python": 0, "JavaScript": 0, "Terraform": 0, "Docker": 0}

def save_votes(votes):
    s3.put_object(Bucket=BUCKET, Key="votes.json", Body=json.dumps(votes))


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json()
    option = data.get("option")
    votes = get_votes()
    if option not in votes:
        return jsonify({"error": "Invalid option"}), 400
    votes[option] += 1
    save_votes(votes)
    return jsonify({"message": f"Vote cast for {option}", "option": option})

@app.route("/results", methods=["GET"])
def results():
    votes = get_votes()
    total = sum(votes.values())
    return jsonify({
        "votes": votes,
        "total": total,
        "percentages": {
            k: round((v / total * 100), 1) if total > 0 else 0
            for k, v in votes.items()
        }
    })

@app.route("/reset", methods=["POST"])
def reset():
    votes = get_votes()
    for key in votes:
        votes[key] = 0
    save_votes(votes)
    return jsonify({"message": "Votes reset"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)