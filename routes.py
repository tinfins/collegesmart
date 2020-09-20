import os
import pathlib

from flask import Flask, render_template, redirect, url_for
import tasks

app = Flask(__name__)


@app.route('/')  # Flask app route decorator
def index():
    """ Route for index page, redirects to home """
    return redirect(url_for('home'))


@app.route('/home')
def home():
    """ Route for home page """
    return render_template('home.html',title='collegeSMART')


@app.route('/getting_started')
def getting_started():
    """ Route for getting started page"""
    return render_template('getting_started.html',title='collegeSMART - Getting Started')


@app.route('/online_colleges')
def online_colleges():
    """ Route for online colleges page. Uses json list to generate page body """
    college_list = tasks.json_list(os.path.join(pathlib.Path(__file__).parent.absolute(),'static/college_info.json'))
    return render_template('online_colleges.html',title='collegeSMART - Online Colleges',colleges=college_list)


@app.route('/alt_credits')
def alt_credits():
    """ Route for alt credits page. Uses json list to generate page body """
    alternate_credits = tasks.json_list(os.path.join(pathlib.Path(__file__).parent.absolute(),'static/alt_credits.json'))
    return render_template('alt_credits.html',title='collegeSMART - Alternative College Credits',alt_credits=alternate_credits)


@app.route('/links')
def links():
    """ Route for links page. Uses json to generate page body """
    links_list = tasks.json_list(os.path.join(pathlib.Path(__file__).parent.absolute(),'static/links.json'))
    return render_template('links.html',title='collegeSmart - Helpful Links',links=links_list)


@app.route('/contact')
def contact():
    """ Route for contacts page. Uses json to generate page body """
    contact_list = tasks.json_list(os.path.join(pathlib.Path(__file__).parent.absolute(),'static/contact.json'))
    return render_template('/contact.html',title='collegeSMART - Contact',contact=contact_list)
    
if __name__ == "__main__":
    app.run(debug=True)
