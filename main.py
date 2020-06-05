from flask import Flask

app = Flask(__name__

@app.route('/hello', methods=['GET'])
def hello():
    return '<h2>Hello World - Flask</h2>'

if __name__ == '__main__':
    app.run(debug=True, port=9000)
