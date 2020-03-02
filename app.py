import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config.from_pyfile('env.py')
app.config["MONGODB_NAME"] = os.environ.get('MONGODB_NAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html", reviews=mongo.db.reviews.find())


@app.route('/add_review')
def add_review():
    return render_template("addreview.html")


@app.route('/insert_review', methods=['POST'])
def insert_review():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
