from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    context = {
        'username': 'Diego'
        }
    return render_template('index.html', **context)

@app.route('/hello', methods=['GET'])
def hello():
    context = {
        'username': 'Diego'
        }
    return render_template('hello.html', **context)

@app.route('/courses', methods=['GET'])
def show_courses():
    context = {
        'courses': [
            {'name': 'Python', 'is_premiun': True},
            {'name': 'Ruby', 'is_premiun': False},
            {'name': 'Java', 'is_premiun': True}
            ]
        }
    return render_template('courses.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=9000)
