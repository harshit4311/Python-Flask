from flask import Flask

'''
creates an instance of the Flask class
which will be your WSGI (Web Server Gateway Interface) application
'''

# WSGI application
app =  Flask(__name__)

@app.route("/")
def welcome():
    return "we're using Flask."

@app.route("/index")
def index():
    return "we're on the index page now"

if __name__ == "__main__":
    app.run(debug=True)
