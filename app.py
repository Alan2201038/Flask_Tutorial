from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/trash')
def trash():
    return render_template('trash1.html')

if __name__ == "__main__":
    app.run(debug=True)

# To run flask app, use this command
# flask run --debug -h ( ipv4 address )
