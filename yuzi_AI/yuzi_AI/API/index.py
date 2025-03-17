from flask import Flask, jsonify, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    return jsonify({
        'time': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'user': 'liboyu666'
    })

@app.route('/')
def serve_index():
    return send_from_directory('../public', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))