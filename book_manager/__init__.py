from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('login-form.html')

@app.route("/welcome/<name>")
def welcome(name):
    return "welcome "+name

# /addBook?book_id=&name=&author=&price=
@app.route("/addBook", methods=['GET'])
def add():
    if(request.method == 'GET'):
        print("cool ",request.args.get('book_id'))
        return "REQUEST FORM "+request.args.get('book_id', '')
    return render_template('404.html')

# /delBook?book_id=
@app.route("/delBook")
def delete():
    return "welcome to hello.py"