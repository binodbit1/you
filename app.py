from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] == 'wait@7854Shrey!':
            return redirect('/success')
        else:
            error = 'Invalid PIN'
    return render_template('login.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
