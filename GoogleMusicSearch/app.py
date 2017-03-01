from flask import Flask, render_template, json, request
from google import search
import os


app = Flask(__name__)

@app.route("/search",methods = ['POST'])
def search1():
        search_query = ""
        if request.form['format'] != '':
                search_query = request.form['format']

        if request.form['song_name'] != '':
                search_query = search_query + ":" + request.form['song_name']

        if request.form['artist_name'] != '':
                search_query = search_query + " artist:" + request.form['artist_name']

        if request.form['movie_name'] != '':
                search_query = search_query + " movie:" + request.form['movie_name']

        print(search_query)
        search_results = {}
        i = 1
        for url in search(search_query,stop=10):
                search_results[i] = url
                i += 1

        return render_template("result.html", result=search_results)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

	
