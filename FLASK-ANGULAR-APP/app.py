
from flask import Flask, request, jsonify, url_for, render_template
from flask_restplus import Resource, Api
import json
from bson import json_util
# from flask_mysqldb import MySQL
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename

from markupsafe import escape

# import pyrebase

# local uploads or temp
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENTIONS = {'png', 'jpg', 'jpeg', 'gif'}

# filter mime-types

def allowed_files(filename):
  return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENTIONS

app = Flask(__name__)
#config
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskpoststut'
# mongodb
app.config['MONGO_URI']='mongodb://localhost:27017/flaskpoststut'
mongo=PyMongo(app)
CORS(app)

# firebase config
config = {}


@app.route("/api/posts", methods = ['GET'])
def index():
  if request.method == 'GET':
    return jsonify(data = "post main response")

@app.route("/api/addpost", methods = ['POST'])
def addpost():
  if request.method == 'POST':

    title = request.form.get('title')
    content = request.form.get('content')
    cover = request.files['cover']

    if cover and allowed_files(cover.filename):
      filename = str(uuid.uuid4())
      filename += "."
      filename += cover.filename.split('.')[1]

      # secure name
      filename_secure = secure_filename(filename)
      # save the file inside uploads folder
      cover.save(os.path.join(app.config["UPLOAD_FOLDER"], filename_secure))

      # local file
      local_filename = "./uploads/"
      local_filename += filename_secure

      cur = mysql.connection.cursor()
      cur.execute("""INSERT INTO flaskpoststut (title, content, cover, covername) VALUES (%s, %s, %s, %s)""" % (title, content, filename_secure, filename_secure))

      return jsonify(data = 'The post was created successfully.')

@app.route('/user/<username>')
def show_user_profile(username):
  return 'User %s' % escape(username)


@app.route('/projects')
def projects():
  return 'The project page'

@app.route('/about')
def about():
  return 'The about page'

@app.route('/login', methods = ['GET', 'POST', 'PUT'])
def login():
  error = None
  if request.method == 'POST':
    return 'POST access'
  elif request.method == 'GET':
    return 'GET access'
  else:
    return 'cj'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):

  data = {
    'cj': 'cj',
    'iu': 'iu',
    'name': name
  }
  # return data
  return jsonify([data, 2,3, 4 ])

api = Api(app)
todos = {}

@api.route('/todos/<string:todo_id>')
class TodoSimple(Resource):
  def get(self, todo_id):
    return {todo_id: todos[todo_id]}

  def put(self, todo_id):
    todos[todo_id] = request.form['data']
    print(todos)

    return {todo_id: todos[todo_id]}

@api.route('/test/mongodb')
@api.route('/test/mongodb/<string:title>')
class TestMongodb(Resource):
  def get(self):

    get_data = mongo.db.flaskpoststut.find()
    print(type(get_data))
    return jsonify(json.loads(json_util.dumps(get_data)))

  def put(self, title):
    title = request.form['title']
    content = request.form['content']
    cover = request.form['cover']
    covername = request.form['covername']
    _insert = mongo.db.flaskpoststut.insert({
      "title": title,
      "content": content,
      "covername": covername,
      "cover": cover
    })
    return jsonify(data = title)


if __name__ == '__main)__':
  app.run(debug=True)


