from flask import Flask
from flask import jsonify
import random


app = Flask(__name__)


# Mocked response bodies
error_response = [{"Error": "Non ASCII Dataset - DIGM contains characters outside of the ASCII character set"},
                  {"Error": "jeff"},
                  {"Error": "No DIGM in the request body"},
                  {"Error": "Broken or invalid DIGM - Colour index out of range: 4401512"}]


@app.route('/digm2gml', methods=['POST'])
def postdigm():
    return jsonify(random.choice(error_response)), 400


if __name__ == "__main__":
    app.run(debug=True)