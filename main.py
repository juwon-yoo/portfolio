from flask import Flask, render_template, redirect, request, url_for
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/contact', methods=['GET'])
def contact():
    if request.method=='GET':
        return render_template('contact.html')

if __name__ == "__main__":
    #서버 시작
    app.run(debug=True, host='0.0.0.0', port=80)