from flask import Flask, redirect, url_for, render_template, send_file, request
from sympy import plot
from rt_like import plot_rt
from sentiment import plot_sent
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
from flask import Response
import matplotlib.pyplot as plt


app = Flask(__name__)
# plot_rt()
# plot_sent()



@app.route('/')
def todo():
    
    return render_template('index.html')






@app.route('/rtlike', methods=['GET', 'POST'])
def rtlike():
    return render_template('rtlike.html')

@app.route('/hashtags', methods=['GET', 'POST'])
def hashtags():
    return render_template('hashtags.html')


@app.route('/sentiments', methods=['GET', 'POST'])
def sentiment():
    if request.method == "POST":
        key_word = request.form.get("keyword")
        nbTweet = request.form.get("nbTweet")
        plot_sent(key_word,nbTweet)
        return render_template('sentiment.html', key_word=key_word, nbTweet=nbTweet)
    else:
        return render_template('sentiment.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    


# @app.route('/new', methods=['POST'])
# def new():
#     return redirect(url_for('todo'))