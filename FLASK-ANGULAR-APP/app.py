from flask import Flask, request, jsonify
import json
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
import pyrebase

# import pyrebase

# local uploads or temp
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENTIONS = {'png', 'jpg', 'jpeg', 'gif'}

# filter mime-types

def allowed_files(filename):
  return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENTIONS

app = Flask(__name__)
#config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskpoststut'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mysql = MySQL(app)
CORS(app)

# firebase config
config = {}


@app.route("/api/posts", methods = ['GET'])
def index():
  if request.method == 'GET':
    return jsonify(data = "post mian response")

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
      cur.execute("""INSERT INTO flaskpoststut (title, content, cover, covername) VALUES (%s, %s, %s, %s)""", (title, content, filename_secure, filename_secure))

      return jsonify(data = 'The post was created successfully.')





if __name__ == '__main)__':
  app.run(debug=True)


