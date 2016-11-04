from flask import Flask
from flask import render_template
import logging, logging.config, yaml

app = Flask(__name__)

def logger():
    # ref: http://stackoverflow.com/questions/17743019/flask
    #             -logging-cannot-get-it-to-write-to-a-file
    logging.config.dictConfig(yaml.load(open('logging.conf')))

@app.route('/')
def home(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    logger()
    app.run(host='0.0.0.0', port=80)
