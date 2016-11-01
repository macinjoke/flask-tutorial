from local_setting import host
from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!!!!"


@app.route("/user/<username>")
def show_user_profile(username):
    return "User: %s" % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    if post_id == 0:
        return 'post_id は 0ですね'
    return 'Post %d' % post_id

if __name__ == "__main__":
    app.run(host=host.host, debug=True)
