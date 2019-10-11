from flask import Flask, Response, url_for, request
from json2xml import json2xml, readfromurl, readfromstring, readfromjson


app = Flask(__name__)

@app.route("/")
def index():
    '''
    try:
        import googleclouddebugger
        googleclouddebugger.enable()
    except ImportError:
        pass
    '''
    
    '''
    headers = {
        "Authorization": "Bearer your_access_token",
        "Lw-Client": "your_client_id"
    }
    data = readfromurl('https://api.learnworlds.com/courses', headers=headers)
    '''

    #get the data from local sample file
    data = readfromurl(request.url + 'static/courses.json')
    
    resp = Response(response=json2xml.Json2xml(data).to_xml(),
                    status=200,
                    mimetype="application/xml")
    
    #resp = 'Hello'

    return resp


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)



