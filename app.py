#!/usr/bin/python3
from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            meme_large = data["url"]
            subreddit = data["subreddit"]
            return meme_large, subreddit
        else:
            return None, None
    except Exception as e:
        print(f"Error fetching meme: {e}")
        return None, None

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    if meme_pic:
        return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)
    else:
        return "Failed to load meme. Try again later."

if __name__ == '__main__':
    app.run(debug=True)
