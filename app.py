import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

# @app.route('/vi-assets/<path:p>')
# def override_nyt_assets(p=''):
#     return requests.get('https://www.nytimes.com/vi-assets/{}'.format(p)).content

@app.route('/nyt')
def override_nyt():
    # url = 'https://www.nytimes.com{0}'.format(p)
    # try:
    #     r = requests.get(url)
    # except Exception as e:
    #     return "proxy service error: " + str(e), 503

    # # You can edit the page to your heart's content
    # # or just return r.content without parsing
    # from bs4 import BeautifulSoup
    # soup = BeautifulSoup(r.content, "html.parser")

    # # remove sidebar
    # # soup.find('div', id="adg3-navigation").decompose()
    # # remove all buttons with specified class
    # # selects = soup.findAll('a', class_="aui-button")
    # # for match in selects:
    # #    match.decompose()
    # # remove header breadcrumbs
    # # soup.find('header', class_="app-header").decompose()
    # # soup.find('title').string = 'My Wiki'

    # return str(soup)

    resp = requests.request(
        method=request.method,
        url='https://www.nytimes.com',
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies)
    
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection', 'content-security-policy']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]
    headers.append(('Access-Control-Allow-Origin', '*'))
    headers.append(('Host', 'https://www.nytimes.com'))
    headers.append(('Origin', 'https://www.nytimes.com'))

    soup = BeautifulSoup(resp.content, "html.parser")
    soup.find('link', rel="stylesheet")['href'] = 'https://www.nytimes.com' + soup.find('link', rel="stylesheet")['href']
    print(soup.find('link', rel="stylesheet"))
    
    response = Response(str(soup), resp.status_code, headers)
    return response


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
