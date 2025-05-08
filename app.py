from flask import Flask, send_from_directory
import os

app = Flask(__name__)
FILE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

@app.route('/files/<path:filename>')
def serve_file(filename):
    return send_from_directory(FILE_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
