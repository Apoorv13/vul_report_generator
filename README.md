A simple report generator for creating Excel reports on the vulnerabilities discovered.
Steps to run:
  1. Use pip install -r requirements_test.txt to install the dependencies
  2. Make sure mongo is running with your configuration or db_name = report_helper, collection name = vulnerability
  3. run mongo_import.py to import a sample vulnerability database in mongo
  4. run test_app.py
  5. Navigate to localhost:5000
 
Expected future developments: 
  1. Multi Import images
  2. Object embedded reports as images
