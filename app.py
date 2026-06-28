from flask import Flask, jsonify
import os


app = Flask(__name__)

counter = 0

@app.route("/")
def index():
	return '<h1>DevOps Project 1</h1><p>Visit <a href="/api/counter">/api/counter</a></p>'


@app.route("/api/counter", methods=["GET"])
def get_route():
	global counter
	counter +=1
	return jsonify({"counter": counter})


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
