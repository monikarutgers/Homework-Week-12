from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# setup mongo connection
   
@app.route("/")
def index():
    mars_list = mongo.db.mars_list.find_one()
    return render_template("index.html", listings=mars_list)


@app.route("/scrape")
def scraper():
    mars_list = mongo.db.mars_list
    mars_data = scrape_mars.scrape()
    mars_list.update({}, mars_data, upsert=True)
    return "Scraping Successful!"


if __name__ == "__main__":
    app.run(debug=True)
