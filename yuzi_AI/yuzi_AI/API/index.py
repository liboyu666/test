from flask import Flask, jsonify, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    return jsonify({
        'time': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'user': 'liboyu666',
        'status': 'ok'
    })

@app.route('/')
def serve_index():
    return send_from_directory('public', 'index.html')

# 添加错误处理
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'error': 'Page not found',
        'status': 404
    }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))