import json
import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/proxy', methods=['POST'])
def proxy():
  try:
    data = request.get_json()
    url = data.get('url')
    method = data.get('method')
    headers = data.get('headers')
    body = data.get('body')

    response = requests.request(
      method=method,
      url=url,
      headers=headers,
      data=body,
      timeout=10
    )

    return response.text
  except Exception as e:
    return json.dumps({'error': str(e)}), 500

if __name__ == '__main__':
  app.run(port=3000)