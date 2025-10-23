from flask import Flask, render_template

app = Flask(__name__) # Flask constructor

@app.route('/')  # route decorator
def index():
  return render_template('index.html')  # render template

@app.route('/hello_world')  # route decorator
def hello_world():
  return "Hello, World!"

@app.route("/hello/<name>")  # dynamic route
def hello(name):
  return f"Hello, {name}!"

@app.route('/blog/<int:post_id>')  # dynamic route with integer
def show_blog(post_id):
  return f"Blog Post ID: {post_id}"

if __name__ == '__main__':
  app.run(debug=True)  # run the Flask app