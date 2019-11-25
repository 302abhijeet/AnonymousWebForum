from flask import Flask,render_template,request
import json

app = Flask(__name__)


with open('content.json') as f:
    data = json.load(f)
    
@app.route('/')
def home():
    return render_template("home.html",categoryList = data.keys())

@app.route('/',methods=["POST"])
def submitThread():
    category = "Home"
    title = request.form['title']
    content = request.form['content']
    data[category][title] = {}
    data[category][title]["content"] = content
    with open('content.json', 'w') as fp:
        json.dump(data, fp)
    return render_template("thread.html",threadName=title,threadContent=data[category][title])

@app.route('/<category>')
def category(category):
    return render_template("category.html",category = category,threadList = data[category].keys())
    
@app.route('/<category>/<thread>')
def thread(category,thread):
    return render_template("thread.html",threadName = thread,threadContent = data[category][thread])

if __name__ == '__main__':
    app.run(debug=True)
