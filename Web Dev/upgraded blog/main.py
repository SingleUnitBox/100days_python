from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/3aa1f4f0330871588d6f").json()
# post_objects = []
# for post in posts:
#     post_objects.append(post)

@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=posts)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/contact')
def get_contact():
    return render_template("contact.html")

@app.route('/post/<int:num>')
def show_post(num):
    requested_post = None
    for post in posts:
        if post['id'] == num:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)