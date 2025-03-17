from flask import Flask, jsonify, send_file, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    try:
        return jsonify({
            'time': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'user': 'liboyu666',
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/')
def home():
    try:
        return send_file('public/index.html')
    except Exception:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>简单测试页面</title>
        </head>
        <body>
            <h1>测试页面</h1>
            <p>当前时间：<span id="time">加载中...</span></p>
            <script>
                fetch('/api/time')
                    .then(res => res.json())
                    .then(data => {
                        document.getElementById('time').textContent = data.time;
                    });
            </script>
        </body>
        </html>
        '''

@app.route('/<path:path>')
def catch_all(path):
    try:
        return send_from_directory('public', path)
    except Exception:
        return jsonify({
            'error': 'Path not found',
            'path': path
        }), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)