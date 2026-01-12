from flask import Flask, render_template, request, redirect, url_for
from movies_storage import listMovies, addMovie, removeMovie, findMovie

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
        return render_template('home.html', movies=listMovies())    

@app.route('/addMovie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        movieTitle = request.form.get('title')
        movieYear = request.form.get('year')
        movieActors = request.form.get('actors')
        addMovie(movieTitle, movieYear, movieActors)
        return redirect(url_for('home'))
    else:
        return render_template('add.html')

@app.route('/', methods=['POST'])
def delete_movie():
    movies_to_remove_ids = request.form.getlist('movieToRemove')
    removeMovie(movies_to_remove_ids)
    return redirect(url_for('home'))


@app.route('/search', methods=['GET'])
def search_movie():
    search_query = request.args.get('query')
    if search_query:
        movies = findMovie(search_query)
    else:
        movies = listMovies()
    return render_template('home.html', movies=movies, search_query=search_query)

if __name__ == '__main__':
    app.run()
