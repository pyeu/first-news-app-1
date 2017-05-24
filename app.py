"""
Compare this with the app.py found in the
finished, original first-news-app repo:

http://first-news-app.readthedocs.io/en/latest/#act-2-hello-flask

https://github.com/ireapps/first-news-app/blob/436ab704bcb6a9e506846f2113e29b7211edb407/app.py
"""

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
    return render_template('tet.html')

### Now, the real routes
# the homepage/wide view
@myapp.route("/")
def homepage():
    incidents = get_la_riot_deaths()
    return render_template('homepage.html', incidents=incidents)

# almost the same as the homepage...
@myapp.route("/race/<racename>")
def byrace(racename):
    rname = racename.lower()
    rincidents = []
    all_incidents = get_la_riot_deaths()
    for i in all_incidents:
        if i['race'].lower() == rname:
            rincidents.append(i)

    return render_template('race.html', incidents=rincidents, racename=racename)


# the incident-level view
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
    myapp.run( debug=True, use_reloader=True)
