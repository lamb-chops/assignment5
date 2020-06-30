#!/usr/bin/env python3

# ------------------------------------------------------------------
# assignments/assignment5.py
# Fares Fraij
# ------------------------------------------------------------------

#-----------
# imports
#-----------

from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
import random
import json

app = Flask(__name__)

books = [{'title': 'Software Engineering', 'id': '1'}, \
         {'title': 'Algorithm Design', 'id':'2'}, \
         {'title': 'Python', 'id':'3'}]

@app.route('/book/JSON/')
def bookJSON():
    r = json.dumps(books)
    return Response(r)

@app.route('/')
@app.route('/book/')
def showBook():
    return render_template('showBook.html', books = books)
    
@app.route('/book/new/', methods=['GET', 'POST'])
def newBook():
    if request.method == 'POST':
        newName = request.form['name']
        highest = 0
        for i in books:
            if int(i['id']) > int(highest):
                highest = i['id']
        #finds the highest number then adds one, thats the new spot. once again the prof said this is fine @183
        highest = int(highest) + 1
        new_dict = {'title': newName , 'id' : str(highest)}
        books.append(new_dict)
        return redirect(url_for('showBook')) 
    else:
        return render_template('newBook.html')

@app.route('/book/<int:book_id>/edit/', methods=['GET','POST'])
def editBook(book_id):
    if request.method == 'POST':
        newName = request.form['name']
        #put in dict then return front page of book list to check
        for i in books:
            if i['id'] == str(book_id):
                i['title'] = newName
                return redirect(url_for('showBook'))
    else:
        return render_template('editBook.html', book_id = id)

@app.route('/book/<int:book_id>/delete/', methods = ['GET', 'POST'])
def deleteBook(book_id):
    if request.method == 'POST':
        for i in books:
            if i['id'] == str(book_id):
                books[:] = [d for d in books if d.get('id') != str(book_id)]
                return redirect(url_for('showBook'))
    else:
        return render_template('deleteBook.html', book_id = id)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
    

