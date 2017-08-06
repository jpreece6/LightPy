from flask import Flask, render_template, request, redirect, url_for
import ConfigReader
import re
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    cfg = ConfigReader.GetConfig()
    strip = cfg['strip']
    animation_list = cfg['animations']
    start_animation = cfg['start_animation']
    end_animation = cfg['end_animation']
    return render_template("index.html", strip=strip, animation_list=animation_list, start_animation=start_animation, end_animation=end_animation)

@app.route('/update_settings', methods=['POST'])
def update_settings():
    cfg = ConfigReader.GetConfig()
    cfg['strip']['night_brightness'] = int(request.form['brightness'])
    cfg['strip']['less_than_time'] = request.form['onTime']
    cfg['strip']['greater_than_time'] = request.form['endTime']

    rgbaVal = request.form['activeColor']
    cleanVal = re.sub(r'^.*\(',"", rgbaVal)
    processedVal = re.sub(r'\)',"", cleanVal).split(',')
    cfg['strip']['active_color']['R'] = int(processedVal[0])
    cfg['strip']['active_color']['G'] = int(processedVal[1])
    cfg['strip']['active_color']['B'] = int(processedVal[2])

    cfg['start_animation'] = request.form['startAnimation']
    cfg['end_animation'] = request.form['endAnimation']

    cfg = ConfigReader.Dump(cfg)
    return redirect(url_for('index'))

@app.route('/advanced_settings', methods=['GET', 'POST'])
def advanced_settings():
    if request.method == 'GET':
        cfg = ConfigReader.GetConfig()
        strip = cfg['strip']
        geo = cfg['geo']
        return render_template("advanced.html", strip=strip, geo=geo)
    else:
        cfg = ConfigReader.GetConfig()
        strip = cfg['strip']
        geo = cfg['geo']
        strip['count'] = int(request.form.get('ledCount'))
        strip['pin'] = int(request.form.get('pinNum'))
        geo['enabled'] = bool(request.form.get('geoEnabled'))
        geo['api_key'] = str(request.form.get('apiKey'))
        geo['location'] = str(request.form.get('location'))
        geo['default_latitude'] = float(request.form.get('lat'))
        geo['default_longitude'] = float(request.form.get('lon'))
        cfg = ConfigReader.Dump(cfg)
        return redirect('index')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username').lower() == 'josh' and request.form.get('password').lower() == 'sexyjosh':
            return redirect('advanced_settings')
        else:
            return redirect('index')

    elif request.method == 'GET':
        return render_template("login.html")

    return redirect('index')

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


def Start():
    app.run(debug=True, host='0.0.0.0')

def Stop():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Shutting down..."

if __name__ == "__main__":
    Start()