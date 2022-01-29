from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def todo():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


# @app.route('/new', methods=['POST'])
# def new():
#     return redirect(url_for('todo'))