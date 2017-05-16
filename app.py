from flask import Flask
from flask import render_template
from foo.datahelper import get_la_riot_deaths

myapp = Flask(__name__)

### Some test routes
@myapp.route('/hello')
def hello():
    # html is just text; so are jinja/HTML templates, ultimately
    return 'Hello, world!'

@myapp.route("/test")
def test():
    return render_template('test.html')

### Now, the real routes
@myapp.route("/")
def homepage():
    incidents = get_la_riot_deaths()
    return render_template('homepage.html', incidents=incidents)

@myapp.route('/incidents/<id>/')
def incident(id):
    for d in get_la_riot_deaths():
        if d['id'] == id:
            return render_template('incident.html', incident=d)

    # if we get here, that means the `id` argument
    # doesn't have a corresponding row id...so, we print
    # a sorry message for now
    return 'Sorry, {id} does not exist as an id in our incident data'.format(id=id)

if __name__ == '__main__':

    # this line handles the situation of the app living on
    # heroku and thus needing to use a port number that is not 5000
    # http://virantha.com/2013/11/14/starting-a-simple-flask-app-with-heroku/
    portnum = os.environ.get("PORT") or 5000

    # and this is the standard line to get the app running
    myapp.run(host='0.0.0.0', debug=True,
              use_reloader=True, port=portnum)
