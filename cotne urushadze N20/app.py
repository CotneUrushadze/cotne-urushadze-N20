from flask import Flask, render_template, request, redirect

app = Flask(__name__)


movies = ["spiderman", "shrek", "titanic",] 


@app.route('/')
def home():
    return render_template('home_page.html', movies=movies)


@app.route('/about')
def about():
    return render_template('about_page.html')


@app.route('/check/<movie>')
def calculator(movie):
    return render_template('check.html', movie=movie, movies=movies)


if __name__ == '__main__':
    app.run(debug=True)