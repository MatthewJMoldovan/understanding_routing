from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f"Hello World"

@app.route('/dojo')
def dojo():
    return f"Dojo"

@app.route('/say/<string:user_name>')
def hi_user(user_name):
    return f"Hi {user_name}!"

@app.route('/repeat/<int:num>/<string:thing>')
def repeat_times(num,thing):
    return f'{thing} '* num

if __name__ == "__main__":
    app.run(debug=True)