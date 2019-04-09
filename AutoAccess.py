from flask import Flask, render_template
import motorController
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def check():
    print "AutoAccess Server Running..."
    return render_template('index.html')


@app.route('/light/on', methods=['GET'])
def lighOn():
    print "Turning Light ON !"
    result = motorController.light_on()
    return jsonify({'result': result})


@app.route('/light/on/interval/<interval>', methods=['GET'])
def lighOnInterval(interval):
    try:
        print "Turning Light ON !"
        motorController.light_interval(int(interval))
        return jsonify({'result': True})
    except:
        print "ERROR: Cannot read interval value"
        return jsonify({'result': False})


@app.route('/light/off', methods=['GET'])
def lighOff():
    print "Turning Light OFF !"
    motorController.light_off()
    return jsonify({'result': True})


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
