from flask import Flask,render_template,request
from flask_ngrok import run_with_ngrok

app=Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def homePage():
  return render_template('user.html')

@app.route('/nameAPI',methods=['POST'])
def collectData():
  username=request.form['username']
  print (username)
  return username

if __name__=="__main__":
  app.run()
