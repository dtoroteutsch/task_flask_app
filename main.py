from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/hello', methods=['GET'])
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True, port=9000)
