from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    robot = "neutral.png"
    sentiment_text = ""
    sentiment_class = ""
    user_text = ""   

    if request.method == "POST":
        user_text = request.form.get("text", "")
        polarity = TextBlob(user_text).sentiment.polarity

        if polarity > 0:
            robot = "happy.png"
            sentiment_text = "HAPPY 😊"
            sentiment_class = "happy"

        elif polarity < 0:
            robot = "sad.png"
            sentiment_text = "SAD 😢"
            sentiment_class = "sad"

        else:
            robot = "neutral.png"
            sentiment_text = "NEUTRAL 😐"
            sentiment_class = "neutral"

    return render_template(
        "index.html",
        robot_image=robot,
        sentiment_text=sentiment_text,
        sentiment_class=sentiment_class,
        user_text=user_text   
    )

if __name__ == "__main__":
    app.run(debug=True)
