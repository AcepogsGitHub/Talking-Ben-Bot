from flask import Flask, request, render_template
from threading import Thread

app = Flask('app')

def run():
  app.run(host="0.0.0.0", port=2348)

def start():
  t = Thread(target=run)
  t.start()

@app.route("/app/verify")
def verifypage():
  verifycode = request.args.get('verification')
  if verifycode == 1121:
    return "Verification not avaliable"
  else:
    return "<h1>The requested resource isn't available</h1> <p>A error occured when loading the requested resource.</p>"
