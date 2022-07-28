from flask import Flask, render_template
import datetime
import logging
import random

app = Flask(__name__)
logging.basicConfig(level=logging.WARNING, format = 'Warning Structure Fomrat')


@app.route('/')
def start():

    return render_template('index.html')

@app.route('/log')
def log():

    # generate random number between 0 and 31423413
    x = random.randint(0, 31423413)

    if x % 2 == 0:

        logging.warning('Log Message')

    elif x % 3 == 0:

        logging.critical('Log Message')

    else:

        logging.error('Log Message')

    return render_template('index.html')



@app.route('/time')
def time():
    
    result = {
        "current_time"  : datetime.datetime.now().strftime("%H:%M:%S"),
        "current_date"  : datetime.datetime.now().strftime("%Y-%m-%d")
    }

    return result

if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)