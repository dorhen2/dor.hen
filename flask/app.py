from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
prog = ["Java", "Python"]
level = ["Professional", "Beginner"]


@app.route('/')
def hello_world():
    return render_template('cv.html')

@app.route('/hi')
def assignment8():
    return render_template('assignment8.html',
                           user={'firstName': "", 'gender': "Ms"},
                           len=len(prog),
                           prog=prog,
                           level=level)


@app.route('/colleague')
def colleagues():
    return render_template('Colleague.html')

@app.route('/contact')
def Contacts():
    return render_template('Contact.html')

@app.route('/assignmen8')
def assignmentPage():
    return render_template('assignment8.html')


@app.route('/skills')
def my_skill():
    return render_template('skill.html')



if __name__ == '__main__':
    app.run()
