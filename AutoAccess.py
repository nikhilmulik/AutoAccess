from flask import Flask
import motorController
from flask import jsonify

app = Flask(__name__)


@app.route('/light/onn', methods=['GET'])
def lighOn():
    print "Turning Light ON !"
    motorController.light_on()
    return jsonify({'result': True})

@app.route('/light/on/interval/<interval>', methods=['GET'])
def lighOnInterval(interval):
    print "Turning Light ON !"
    motorController.light_interval(interval)
    return jsonify({'result': True})

@app.route('/light/off', methods=['GET'])
def lighOff():
    print "Turning Light OFF !"
    motorController.light_off()
    return jsonify({'result': True})


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
