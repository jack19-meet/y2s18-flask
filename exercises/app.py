from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    like_same_sport=False
    arr=["Michael Phelps","Missy Franklin","Mark Spitz","Matt Biondi","Kristin Otta"]
    if like_same_sport:
            return render_template("index.html",player_list=arr,like_same_sport=like_same_sport)
    return render_template("index.html",like_same_sport=like_same_sport)
if __name__ == '__main__':
   app.run(debug = True)