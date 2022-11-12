from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response
from requests import get
from json import loads
app = Flask(__name__)
logged_in = False
@app.route('/', methods=['GET', 'POST'])

def index():
    return render_template('index.html')

@app.route('/shop')

def shop():
    ip = get('https://api.ipify.org').text.replace('{"ip":"', '').replace('"}', '')
    response = get(f'https://ipapi.co/{ip}/json').text
    responseinfo = loads(response)
    if responseinfo['region']=="Iowa":
        return redirect('https://account.nebullam.com/checkout/buy/114092', code=302)
    elif responseinfo['region']=="Minnesota":
        return redirect('https://mn.claytonfarms.com/pages/build-your-bundle', code=302)
    else:
        return "<script>alert('Sorry, we are not currently shipping to your state.')</script>"

@app.route('/login')

def login():
    ip = get('https://api.ipify.org').text.replace('{"ip":"', '').replace('"}', '')
    response = get(f'https://ipapi.co/{ip}/json').text
    responseinfo = loads(response)
    if responseinfo['region']=="Iowa":
        return redirect('https://account.nebullam.com/account/auth/login', code=302)
    else:
        return redirect('https://mn.claytonfarms.com/account/login', code=302)

app.run(host="0.0.0.0", port=5000)