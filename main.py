from flask import Flask
app = Flask(__name__)

print(__name__)

#Using app.route
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/Rk7jn49W6tDit0lK7F/giphy.gif"width=200>'

#Variable
@app.route('/username/<name>/<int:number>')
def greet(name,number):
    return f"Hello {name}, you are {number} years old!"


#Decorators to add a tag around text on web page.
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "<b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

if __name__== '__main__':
    app.run(debug=True)
