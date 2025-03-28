from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This will look for templates/index.html

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # Make sure it listens on 0.0.0.0 to accept connections
