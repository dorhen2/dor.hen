from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = '123'

prog = ["Java", "Python"]
level = ["Professional", "Beginner"]


@app.route('/')
def hello_world():
    return render_template('cv.html')


@app.route('/hi')
def assignment():
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
    return render_template(
        user={'firstName': "", 'gender': "Ms"},
        len=len(prog),
        prog=prog,
        level=level)


@app.route('/skills')
def my_skill():
    return render_template('skill.html'
                           , user={'firstName': "", 'gender': "Ms"},
                           len=len(prog),
                           prog=prog,
                           level=level)


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    if 'userFirst' in session:
        userFirst, userLast = session['userFirst'], session['userLast']
    else:
        if 'userFirst' in request.args:
            userFirst = request.args['userFirst']
            session['userFirst'] = userFirst
        else:
            userFirst = ''
        if 'userLast' in request.args:
            userLast = request.args['userLast']
            session['userLast'] = userLast
        else:
            userLast = ''

    if 'role' in request.args:
        role = request.args['role']
    else:
        role = ''
    if 'logOut' in request.args:
        userFirst = ''

    return render_template('assignment9.html',
                           role=role,
                           userFirst=userFirst,
                           userLast=userLast)


if __name__ == '__main__':
    app.run()
