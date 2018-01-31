import pandas as pd
import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
from flask.ext.pymongo import PyMongo, MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'report_helper'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/report_helper'
mongo = PyMongo(app)

app.config['UPLOAD_FOLDER'] = 'static/vul'


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      filename =f.filename
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      print filename
      vul_data = filename.split("-")
      vul_name = vul_data[0]
      vul_class = vul_data[1]
      print "Vulnerability Name from file: "
      print vul_name
      print "Vulnerability Class from File: "
      print vul_class
      client = MongoClient("localhost", 27017, maxPoolSize=50)
      db = client.report_helper
      collection = db['vulnerability']
      cursor = collection.find({})
      for document in cursor:
          print(document['vul_finding'])
          fin_temp = document['vul_finding']
          print "Checking For"
          print fin_temp
          if vul_name in fin_temp:
            print "Vulnerability Name from DB: "
            print document['vul_finding']
            print "Vulnerability Criticality "
            print document['vul_crit']
            print "Vulnerability Description "
            print document['vul_desc']
            print "Vulnerability Risk/ Implication "
            print document['vul__risk']
            print "Vulnerability Recommendation "
            print document['vul_recom']
            diction = {
                'vul_finding' : document['vul_finding'],
                'vul_crit' : document['vul_crit'], 
                'vul_desc' : document['vul_desc'], 
                'vul__risk' : document['vul__risk'], 
                'vul_recom' : document['vul_recom']
                    }
            df = pd.DataFrame(data=diction, index=[0])
            df = (df.T)
            print (df)
            df.to_excel('test.xlsx')
          print "NOT FOUND"
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)