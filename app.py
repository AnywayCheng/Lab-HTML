from flask import Flask, render_template

app = Flask(__name__,template_folder='HTML')

@app.route('/')
def home():
    return render_template('HomePage.html')

if __name__ == '__main__':
    app.run(port=8000)