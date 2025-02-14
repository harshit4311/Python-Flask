from flask import Flask, render_template, request

'''
creates an instance of the Flask class
which will be your WSGI (Web Server Gateway Interface) application
'''

# WSGI application
app =  Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1> we're using flask </H1></html>"

@app.route("/index", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/about-us")
def about_us():
    return render_template('about-us.html')

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        pass
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
