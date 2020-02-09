from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("home.html")

@app.route('/chat')
def chat():
  return render_template("chat.html")

@app.route('/chat2')
def chat2():
  return render_template("chat2.html")  
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port = 5420, threaded = True, debug = True)
