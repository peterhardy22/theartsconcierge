# from geopy.geocoders import Nominatim
from app import app
from flask import render_template, jsonify
from app.models import csv_importer


# Route for main page of bay area tracker exhibit carousels
@app.route('/')
def index():
    exhibits = csv_importer()
    return render_template("index.html", exhibits=exhibits)


# Route for Exhibits API
@app.route('/bayareatracker/api/v1/exhibits', methods=['GET'])
def get_exhibits():
    exhibits = csv_importer()
    return jsonify({'exhibits': exhibits})
