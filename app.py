from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Render the form page
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    # Render the result page
    return render_template('result.html', first_name=first_name, last_name=last_name, email=email)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')