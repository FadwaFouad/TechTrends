import sqlite3

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort
from flask import json
import logging
import sys


stout_handler = logging.StreamHandler(sys.stdout)
stderr_handler = logging.StreamHandler(sys.stderr)

logging.basicConfig(level=logging.DEBUG,
    format='%(levelname)s:%(name)s: %(asctime)s, %(message)s',
     handlers=[stderr_handler, stout_handler])




# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    global db_connection_count
    app.config['COUNER']+=1
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
      app.logger.info('"404 page" retrieved!')
      return render_template('404.html'), 404
    else:
      app.logger.info('Article \"'+post['title']+'\" retrieved!')
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about(): 
    app.logger.info('The "About Us" page is retrieved.')
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()
            app.logger.info('New Article "'+title+'" created!.')


            return redirect(url_for('index'))

    return render_template('create.html')
    
# check health status 
@app.route('/healthz')
def healthz():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    try:
        connection = get_db_connection()
        connection.execute('SELECT 1 FROM posts').fetchone()
    except Exception as e:
        response = app.response_class(
            response=json.dumps({"result":"ERROR - unhealthy"}),
            status=500,
            mimetype='application/json'
         )
         
    return response

# check metrics
@app.route('/metrics')
def metrics():
    connection = get_db_connection()
    result = connection.execute('SELECT COUNT(*) FROM posts').fetchone()
    post_count=result[0]
    
    response = app.response_class(
            response=json.dumps({"db_connection_count": app.config['COUNER'] , 
            "post_count": post_count}),
            status=200,
            mimetype='application/json'
    )
    return response

# start the application on port 3111
if __name__ == "__main__":
   app.config['COUNER'] = 0
   app.run(host='0.0.0.0', port='3111')

