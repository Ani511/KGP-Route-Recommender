from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from topsis import run_topsis
import os

app = Flask(__name__, static_folder='frontend')

# Load dataset
df = pd.read_csv('KGP_Topsis_Dataset.csv')

# Route to serve frontend (index.html)
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

# API to get best route using TOPSIS
@app.route('/get_best_route', methods=['POST'])
def get_best_route():
    data = request.json

    # Ensure correct key names (matching your frontend JS)
    start = data['from_hall']
    destination = data['destination']
    weights = data['weights']  # [safety, time, distance, traffic, road_quality]

    # Filter relevant routes
    filtered_df = df[
        (df['From Hall'] == start) &
        (df['Destination'] == destination)
    ]

    if filtered_df.empty:
        return jsonify({'error': 'No route found'}), 404

    ranked_df = run_topsis(filtered_df, weights)

    # Convert to list of dicts
    results = ranked_df.to_dict(orient='records')
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
