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
    register = values.get('register')
    field = values.get('field')
    if register is None:
        return "Error: Please supply a valid register name", 400
        print('{register}')
    if strings is None:
        return "Error: Please supply a valid string", 400
        print('{strings}')
    if field is None:
        return "Error: Please supply a valid field", 400
        print('{field}')


    db_string = os.getenv('DATABASE_URL')
    print('{strings}')
    engine = create_engine(db_string)
    print('{strings}')
    
    
    """
    
    dont excecute as strings
    
    connect it to database and select
    
    """
    
    #lookup = {
    #'local-authorities':['local-authority-eng', 'local-authority-sct'],
    #'gov-orgs':['government-organisation']
    #}
    

    query = 'SELECT * FROM "{}" where soundex({}) = soundex({})'.format( register,'"' + field + '"',"'" + strings + "'")
    
    
    data = pd.read_sql(query, engine)
    #data = pd.read_sql(query, engine,params={"strings":strings})
    print('{strings}')
    response = data.to_json()

    # Return the json and a 200 (ok) response

    return response, 200


#    return str(data)
3
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
