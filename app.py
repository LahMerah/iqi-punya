from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')  

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')  

@app.route('/project')
def project():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)