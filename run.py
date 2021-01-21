import json

import requests
from flask import Flask
from torrequest import TorRequest

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Hello, World!'


@app.route("/tor")
def tor():
    request = TorRequest()
    response = request.get("http://httpbin.org/ip")
    ip_address = json.loads(response.content)["origin"]
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    data = json.loads(response.content)
    city = data["city"]
    country = data["country"]
    
    return f"{country} - {city}"
    

if __name__ == "__main__":
    app.run(port=8100)
