from flask import Flask, redirect, url_for, render_template, send_file
from rt_like import plot_rt

app = Flask(__name__)

@app.route('/')
def todo():
    return render_template('index.html')




def plot_rt_like():
    bytes_obj = plot_rt()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')


@app.route('/rtlike', methods=['GET', 'POST'])
def rtlike():
    plot_rt_like()
    return render_template('rtlike.html')


@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    return render_template('sentiment.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    


# @app.route('/new', methods=['POST'])
# def new():
#     return redirect(url_for('todo'))