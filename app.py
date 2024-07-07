from flask import Flask, request
import sys
import os, sys
from flask import send_file, abort, render_template


# app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     try:
#         return "Start machine learning Project "
#     except Exception as e:
#         return str(e)


# if __name__ == "__main__":
#     app.run()

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "Start Machine learning Project"
