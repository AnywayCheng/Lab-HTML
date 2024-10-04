from flask import Flask, render_template

app = Flask(__name__,template_folder='HTML')

@app.route('/')
def home():
    return render_template('HomePage.html')

@app.route('/professor')
def professor():
    return render_template('Professor.html')

@app.route('/members')
def members():
    return render_template('Member.html')

@app.route('/research')
def research():
    return render_template('Research.html')

@app.route('/publication')
def publication():
    return render_template('Publication.html')

if __name__ == '__main__':
    app.run(debug=True)