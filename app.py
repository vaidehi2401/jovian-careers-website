from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
  return "Ae Hallo"
if __name__ == "__main__":
 app.run(host="0.0.0.0", debug=True)