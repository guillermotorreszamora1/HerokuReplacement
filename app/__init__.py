import io
from flask import Flask
from flask import render_template
from sqlalchemy import create_engine,text
import os
app = Flask(__name__,template_folder='templates')
@app.route('/',methods=["GET","POST"])
def vista_principal():
  return render_template('/index.html')
@app.route('/conection_counter', methods=["GET"])
def conection_counter():
  DATABASE_URI = os.getenv('DATABASE_URL','postgresql://localhost/HerokuReplacement');
  db_engine = create_engine(DATABASE_URI, echo=False)
  db_conn = db_engine.connect()
  result = db_engine.execute("SELECT number FROM numbers;");
  for r in result:
    counter = r[0] +1;
  db_engine.execute("UPDATE numbers SET number= " + str(counter));
  db_conn.close()
  db_engine.dispose()
  return render_template('/conection_counter.html',counter=counter)
