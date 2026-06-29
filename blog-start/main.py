from flask import Flask, render_template
import requests
from post import Post

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blogs = response.json()
    return render_template("index.html" , all_blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True)
