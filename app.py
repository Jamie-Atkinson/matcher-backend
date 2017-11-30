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

@app.route('/', methods=['POST'])
def return_json_from_db():


    values = request.get_json()
    print(str(values))
    strings = values.get('strings')
    if strings is None:
        return "Error: Please supply a valid string", 400
        print('{strings}')


    db_string = os.getenv('DATABASE_URL')

    engine = create_engine(db_string)

    
    
    query = """SELECT * FROM "local-authority-eng"     where soundex(name) = soundex('strings')"""
    # Run simple query on database

    data = pd.read_sql(query, engine)

    response = data.to_json()

    # Return the json and a 200 (ok) response

    return response, 200


#    return str(data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
