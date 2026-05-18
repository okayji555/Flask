from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("login.html")

@app.route('/success/<name>')
def success(name):
  return render_template("success.html", kyanaam = name)

@app.route('/login', methods = ['POST', 'GET'])
def login():
  if request.method == 'POST':
    user = request.form['nm']
    return redirect(url_for('success', name = user))

  else:
    user = request.args.get['nm']
    return redirect(url_for('success', name = user))

if __name__ = "__main__":
  app.run(debug = True)
    
