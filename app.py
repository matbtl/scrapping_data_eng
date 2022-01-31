import flask
from flask import Flask, redirect, url_for, render_template, request
from rt_like import plot_rt
from search_hashtags import hashtags_df
from sentiment import plot_sent


app = Flask(__name__)
plot_rt()



@app.route('/')
def todo():
    return render_template('index.html')



@app.route('/rtlike', methods=['GET', 'POST'])
def rtlike():
    return render_template('rtlike.html')

@app.route('/hashtags', methods=['GET', 'POST'])
def hashtags():
    if request.method == "POST":
        word = request.form.get("word")
        nofTwit = request.form.get("nofTwit")
        df = hashtags_df(word, int(nofTwit))



        print(df)
        return render_template('hashtags.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
    else:
        return render_template('hashtags.html')


@app.route('/sentiments', methods=['GET', 'POST'])
def sentiment():
    if request.method == "POST":
        
        key_word = request.form.get("key_word")
        nbTweet = request.form.get("nbTweet")
        plot_sent(key_word, int(nbTweet))
        return redirect(url_for('sentiment'))
    else:
        return render_template('sentiment.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    


