from flask import Flask, render_template, request, redirect, url_for
import ConfigReader
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index():
    cfg = ConfigReader.GetConfig()
    strip = cfg['strip']
    brightness = strip['night_brightness']
    red = strip['active_color']['R']
    green = strip['active_color']['G']
    blue = strip['active_color']['B']
    return render_template("index.html", brightness=brightness, red=red, green=green, blue=blue)

@app.route('/update_settings', methods=['POST'])
def update_settings():
    print request.form.get('manual')
    cfg = ConfigReader.GetConfig()
    cfg['strip']['night_brightness'] = request.form['brightness']
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
        strip['count'] = request.form.get('ledCount')
        strip['pin'] = request.form.get('pinNum')
        geo['enabled'] = request.form.get('geoEnabled')
        geo['api_key'] = request.form.get('apiKey')
        geo['location'] = request.form.get('location')
        geo['default_latitude'] = request.form.get('lat')
        geo['default_longitude'] = request.form.get('lon')
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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')