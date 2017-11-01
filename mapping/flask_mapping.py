"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
# Brevet time calculations
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY
app.api_key = CONFIG.API_KEY

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    flask.g.api_key = app.api_key
    f = open('long_lat.txt', 'r')
    poi = []
    for line in f:
        x = { }
        line = line.strip()
        if len(line) == 0 or line[0] == "#":
            app.logger.debug("Skipping")
            continue
        else:   
            parts = line.split(':')
            parts = line.split(",")
            print("THESE ARE THE PARTS: ", parts)
            x[parts[0]] = [parts[1], parts[2]]
            poi.append(x)
            print(poi)
            flask.g.poi = poi #to use in jinja
    return flask.render_template('map.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('not_found.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
