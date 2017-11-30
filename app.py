"""
Simple flask app
"""
import os
from flask import (Flask, request, redirect, url_for, send_from_directory,
                   flash, render_template)
import pandas as pd
from sqlalchemy import create_engine
from werkzeug.utils import secure_filename

app = Flask(__name__)


app.secret_key = os.urandom(24)

@app.route('/', methods=['GET'])
def return_json_from_db():
    """
    Access the test table on postgres and return
    """

    db_string = os.getenv('DATABASE_URL')
    print('String created')
    engine = create_engine(db_string)
    print(engine)
    
    
    query = 'SELECT * FROM "local-authority-eng" WHERE SOUNDEX(name) = SOUNDEX("{strings}")'
    # Run simple query on database

    data = pd.read_sql(query, engine)
    # Convert to a json
    # Return the json and a 200 (ok) response
    return str(data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
