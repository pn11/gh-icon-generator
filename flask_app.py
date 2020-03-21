from flask import Flask
app = Flask(__name__)
import generate_pattern

@app.route('/')
def root_route():
    return generate_pattern.api()
