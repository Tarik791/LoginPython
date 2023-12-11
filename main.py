from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    return f'Login successful! Welcome, {username}.'

if __name__ == '__main__':
    app.run(debug=True)
