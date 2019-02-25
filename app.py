import requests
from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/nyt')
@app.route('/vi-assets')
def override_nyt(*args, **kwargs):
    resp = requests.request(
        method=request.method,
        url='https://www.nytimes.com',
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response
    #return requests.get('https://www.nytimes.com').content


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
