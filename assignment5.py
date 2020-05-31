#!/usr/bin/env python3

# ------------------------------------------------------------------
# assignments/assignment5.py
# Fares Fraij
# ------------------------------------------------------------------

#-----------
# imports
#-----------

from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import json

app = Flask(__name__)

books = [{'title': 'Software Engineering', 'id': '1'}, \
		 {'title': 'Algorithm Design', 'id':'2'}, \
		 {'title': 'Python', 'id':'3'}]

@app.route('/book/JSON/')
def bookJSON():
    # <your code>

@app.route('/')
@app.route('/book/')
def showBook():
    # <your code>
	
@app.route('/book/new/', methods=['GET', 'POST'])
def newBook():
    # <your code>

@app.route('/book/<int:book_id>/edit/', methods=['GET','POST'])
def editBook(book_id):
    # <your code>
	
@app.route('/book/<int:book_id>/delete/', methods = ['GET', 'POST'])
def deleteBook(book_id):
    # <your code>

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
	

