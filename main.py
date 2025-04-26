from flask import Flask, request, jsonify, send_from_directory
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/getlink', methods=['POST'])
def get_link():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        output = subprocess.check_output(['yt-dlp', '-g', url], text=True)
        link = output.strip()
        return jsonify({'link': link})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
