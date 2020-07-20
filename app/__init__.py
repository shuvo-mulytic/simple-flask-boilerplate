from flask import Flask

app = Flask(__name__)

# app.config.from_pyfile('settings.py')
# env_var = app.config.get('NAME_OF_ENV_VAR')

@app.route("/", methods=["GET"])
def index():
    return "HELLO"

if __name__ == "__main__":
    app.run(host='0.0.0.0')