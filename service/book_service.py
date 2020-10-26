from os import error
from flask import jsonify
from flask import json
from flask.globals import request
import csv
from .book_scheme import BookScheme

books = [
    {'book_id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': 1992},
    {'book_id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'year_published': 1973},
    {'book_ids': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'year_published': 1975},
    {'book_ids': 3,
     'title': 'Prueba',
     'author': 'Probando',
     'first_sentence': 'Prueba por Autor',
     'year_published': 2020}     ,
    {'book_ids': 4,
     'title': 'Prueba_2',
     'author': 'Probando',
     'first_sentence': 'Prueba por Autor 2',
     'year_published': 1948}
]

def get_books():
    return books

def get_book_by_id(id):
    print(f"el id recibido es {id}")
    id = int(id)
    results = [book for book in books if book['book_id'] == id]
    return results

def get_books_by_filter(filter):
    global books
    results = books 
    if "author" in filter and filter["author"] != "":
        results = [book for book in results if book['author'] == filter["author"]]
    if "year_published" in filter and filter["year_published"] > 0:
        results = [book for book in results if book['year_published'] == filter["year_published"]]
    return results

def delete_book(id):
    global books
    new_list = [book for book in books if book['book_id'] != id]
    books = new_list

def add_book(book):
    global books
    books.append(book)
    return book

def add_books(lista):
    global books
    books = books + lista
    return books

def load_books_from_file(request):
    global books
    file_name = request["name"]
    #root = "C:\Prueba\\"
    path = file_name
    try:
        content = open(file=path, mode="r")
    except FileNotFoundError as error:
        raise Exception("Archivo No Encontrado")
    
    reader = csv.DictReader(content,
                            skipinitialspace=True,
                            delimiter=request["separator"])
    errors = []
    for index, linea in enumerate(reader):
        has_errors = BookScheme().validate(linea)
        if has_errors: 
            errors.append({"linea_"+str(index):has_errors})
        else:
            books.append(BookScheme().load(linea))
    
    print(errors)
    return books