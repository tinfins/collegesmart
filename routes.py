from flask import Flask, render_template, redirect, url_for, request, flash


app = Flask(__name__)


@app.route('/')  # Flask app route decorator
def index():
    return redirect(url_for('home'))
    
@app.route('/home')
def home():
    return render_template('home.html',title='collegeSMART')
    
@app.route('/getting_started')
def getting_started():
    return render_template('getting_started.html',title='collegeSMART - Getting Started')
    
@app.route('/online_colleges')
def online_colleges():
    return render_template('online_colleges.html',title='collegeSMART - Online Colleges')
    
@app.route('/alt_credits')
def alt_credits():
    return render_template('alt_credits.html',title='collegeSMART - Alternative College Credits')
    
@app.route('/contact')
def contact():
    return render_template('/contact.html',title='collegeSMART - Contact')
    
if __name__ == "__main__":
    app.run(debug=True)
