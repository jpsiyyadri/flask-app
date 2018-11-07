from flask import Flask, request, render_template
import json
import markdown
import os
app = Flask(__name__)


@app.route("/api")
def api():
    with open(os.path.dirname(app.root_path)+'/book_manager/book-store-api.md', 'r') as markdown_file:
	    content = markdown_file.read()
	    return markdown.markdown(content)

@app.route("/index")
def hello():
    return render_template('index.html')


@app.route("/signup", methods=['GET'])
def signup():
    if(request.method == 'GET'):

        print("cool ",request.args.get('regemail'))
        if(1):
            return json.dumps({'data':[], 'status': 200})
        return json.dumps({'data':[], 'status': 201})
    return render_template('404.html')

@app.route("/bookCategories")
def getBookCategories():
    with open(os.path.dirname(app.root_path)+'/book_manager/static/data/book_categories.json', 'r') as json_file:
        json_dict = json.loads(json_file.read())[0]
        return json.dumps(json_dict)
    return "null"
@app.route("/")
def showBooks():
    return render_template('books.html')

@app.route("/welcome/<name>")
def welcome(name):
    return "welcome "+name

# /addBook?book_id=&name=&author=&price=
@app.route("/addBook", methods=['GET'])
def add():
    if(request.method == 'GET'):
        print("cool ",request.args.get('book_id'))
        if(request.args.get('book_id')):
            return json.dumps({'data':[], 'status': 200})
        return json.dumps({'data':[], 'status': 201})
    return render_template('404.html')

# /delBook?book_id=
@app.route("/delBook")
def delete():
    return "welcome to hello.py"