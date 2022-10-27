from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

posts = requests.get("https://api.npoint.io/eea8271d2266556eb370").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/blog')
def blog():
    return render_template("index.html", posts=post_objects)

@app.route('/post/<int:num>')
def show_post(num):
    requested_post = None
    for post in post_objects:
        if post.id == num:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
