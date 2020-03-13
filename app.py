import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import bcrypt
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('env.py')
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config["MONGODB_NAME2"] = os.environ.get('MONGODB_NAME2')
app.config["MONGODB_NAME"] = os.environ.get('MONGODB_NAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)
users = mongo.db.users
reviews = mongo.db.reviews
dateTimeObj = datetime.now()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login_page')
def login_page():
    if 'username' in session:
        return redirect(url_for('account'))

    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),
                         login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('login_page'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('get_reviews'))

        return 'that username already exists'

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html", reviews=mongo.db.reviews.find())


@app.route('/add_review')
def add_review():
    return render_template("addreview.html")


@app.route('/update_review/<review_id>', methods=['POST'])
def update_review(review_id):
    reviews.update({'_id': ObjectId(review_id)},
                   {
                       'review_name': request.form.get('review_name'),
                       'book_name': request.form.get('book_name'),
                       'review_description': request.form.get('review_description'),
                       'rating': request.form.get('rating'),
                       'username': request.form.get('username'),
                       'author': request.form.get('author'),
                       'date': request.form.get('date'),
                       'book_cover': request.form.get('book_cover')
                   })
    return redirect(url_for('account'))


@app.route('/insert_review', methods=['POST'])
def insert_review():
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template('editreview.html', review=the_review)


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('account'))


@app.route('/account')
def account():
    if 'username' not in session:
        return redirect(url_for('login_page'))
    return render_template("account.html", reviews=mongo.db.reviews.find({'username': session.get('username')}))


@app.route('/store')
def store():
    return render_template('store.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
