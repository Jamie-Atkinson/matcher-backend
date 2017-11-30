# coding: utf-8
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

# Set the location where uploaded files will be stored (/tmp/ is probably ok)
# Note that at present these will remain on the server until it is rebooted.

# Set the app secret key to prevent CSRF

app.secret_key = os.urandom(24)

# Demonstrate access to an attached database using sqlalchemy and pandas

@app.route('/', methods=['GET'])
def return_json_from_db():
    """
    Access the test table on postgres and return
    """

    db_string = os.getenv('DATABASE_URL')
    print('String created')
    engine = create_engine(db_string)
    print(engine)
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
