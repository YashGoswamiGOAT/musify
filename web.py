from flask import Flask
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/<i>")
def id(i):
    you = YouTube("https://www.youtube.com/watch?v="+i)
    return you.streams.get_audio_only().url

if __name__=="__main__":
    app.run(debug=True)