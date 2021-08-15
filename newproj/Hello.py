from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return ("Hello World")
    
@app.route("/hello")
def hello_Rubin():
   return ("Hello Rubin")

if __name__ == '__main__':
   app.run()