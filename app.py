from flask import Flask, request, Response, send_from_directory
import requests
from io import BytesIO

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return 'URL parameter is required', 400
    
    try:
        response = requests.get(url, stream=True)
        if response.status_code != 200:
            return f'Failed to fetch image: {response.status_code}', response.status_code
        
        return Response(
            response.content,
            content_type=response.headers['Content-Type']
        )
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
