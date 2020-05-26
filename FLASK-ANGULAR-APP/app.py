from flask import Flask, request, jsonify, url_for, render_template, send_file
from flask_restplus import Resource, Api, fields
import json
from bson import json_util
# from flask_mysqldb import MySQL
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
from werkzeug.contrib.fixers import ProxyFix
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



@app.route("/api/posts", methods = ['GET'])
def index():
  if request.method == 'GET':
    '''
      Get all posts from MongoDB
    '''
    docs = mongo.db.flaskpoststut.find({}, {'_id': False})
    # print('Type of docs is %s' % type(docs))
    # print(docs)
    # ds=json_util.dumps(docs)
    # print('Type of ds is %s' % type(ds))
    # print(ds)
    # print('Type of docs is %s' % type(docs))
    # lds=json.loads(ds)
    # print('Type of lds is %s' % type(lds))
    # print(lds)

    return jsonify(data = list(docs))

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
      local_filename = os.path.join(app.config["UPLOAD_FOLDER"], filename_secure)
      cover.save(local_filename)

      mongo.db.flaskpoststut.insert({
      "title": title,
      "content": content,
      "covername": filename_secure,
      "cover": filename_secure
      })

      return jsonify(data = 'The post was created successfully.')

@app.route("/api/image/<filename>", methods = ['GET'])
def get_image(filename=None):
  if request.method == 'GET':
    if filename is None:
      return 'no image'
    else:
      filename = os.path.join(app.config["UPLOAD_FOLDER"], filename)
      if not os.path.exists(filename):
        return 'No image'
      else:
        return send_file(filename, mimetype='image/gif')

@app.route('/api/post/<title>', methods=['GET'])
def singlepost(title):
  record = mongo.db.flaskpoststut.find_one({'title': title}, {'_id': False})
  return jsonify(data = dict(record))


# not in use ------------
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
# test mongdb
@api.route('/testm/mongodb')
@api.route('/testm/mongodb/<string:title>')
class TestMongodb(Resource):
  def get(self):

    get_data = mongo.db.flaskpoststut.find()
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


