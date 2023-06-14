from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)


# @app.route('/<timex>')
# def index(timex):      
#     from toggle_m_power import toggle_m
#     timex = int(timex)   
#     toggle_m(timex)
#     return f"Done, monitor is off for {timex} seconds " 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/WebFlood')
def webflood():
    from LINKER import web_crash
    web_crash()
    return "Done The WebFlood is running"

@app.route('/cdCARDIO')
def cdcardio():
    from LINKER import cd_open_close
    cd_open_close()
    return "Done The cdCARDIO is running"

@app.route('/duck')
def duck():
    from LINKER import duck
    duck()
    return "Done The duck is running"

@app.route('/explorer')
def explorer():
    from LINKER import exp_sh
    exp_sh()
    return "Done The explorer is running"

@app.route('/mouse')
def mouse():
    from LINKER import interupt
    interupt()
    return "Done The mouse is running"

@app.route('/power')
def power():
    from LINKER import power_sh
    power_sh()
    return "Done The power is running"

@app.route('/taskbar')
def taskbar():
    from LINKER import taskbar_sh
    taskbar_sh()
    return "Done The taskbar is running"

@app.route('/taskmanager')
def taskmanager():
    from LINKER import taskmaneger_sh
    taskmaneger_sh()
    return "Done The taskmanager is running"

@app.route('/toggle')
def toggle():
    from LINKER import toggle_m
    toggle_m()
    return "Done The toggle is running"

@app.route('/wallpaper')
def wallpaper():
    from LINKER import blackwall
    blackwall()
    return "Done The wallpaper is running"

@app.route('/volume')
def volume():
    from LINKER import vol_cc
    vol_cc()
    return "Done The volume is running"





        

    
app.run(debug=True, host= '192.168.0.116')