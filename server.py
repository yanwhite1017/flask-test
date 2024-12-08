from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
  return "<h1>get started</h1>"

if __name__ == '__main__':
  app.run(debug=True, port=80, host="0.0.0.0")