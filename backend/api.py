from flask import (Flask, render_template)
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)


@app.route('/index')
@cross_origin()
def get_tree():
    return {"name": "bob"}


if __name__ == '__main__':
    app.run(debug=True)
