from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<int:num>')
def get_post(num):
    for post in all_posts:
        if post['id'] == num:
            title = post['title']
            body = post['body']
            subtitle = post['subtitle']
    return render_template("post.html", title=title, body=body, subtitle=subtitle)


if __name__ == "__main__":
    app.run(debug=True)
