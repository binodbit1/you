from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] == '0502':
            return redirect('/success')
        else:
            error = 'Invalid PIN'
    return render_template('login.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
