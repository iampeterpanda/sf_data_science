from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/time')
def current_time():
    return {'time': datetime.datetime.now()}
if __name__ == '__main__':
    app.run('localhost', 5000)