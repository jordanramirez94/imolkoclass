from flask import request, jsonify
from flask_smorest import Api, Blueprint, abort
from service import author_service
from service.author_scheme import AuthorScheme
from service.book_scheme import BookScheme, BookFileRequest
from service.filter_request_schema import FilterRequestSchema
from service import book_service

blp = Blueprint(
    'books', 'books', url_prefix='/books',
    description='Operaciones para nuestra libreria'
)

@blp.route('/', methods=['GET'])
@blp.arguments(FilterRequestSchema, location="query")
@blp.response(BookScheme(many=True))
def api_all(request):
    """Obtener libros de acuerdo a criterios"""
    print(request)
    #return book_service.get_books()
    return book_service.get_books_by_filter(request)

@blp.route('/<id>', methods=['GET'])
def api_id(id):
    return jsonify(book_service.get_book_by_id(id))

@blp.route('/<id>', methods=['DELETE'])
def api_delete_book(id):
    book_service.delete_book(int(id))
    return "", 204

@blp.route('/', methods=['POST'])
@blp.arguments(BookScheme, location="query")
@blp.response(BookScheme)
def add_book(book):
    print(book)
    book_service.add_book(book)
    return book, 200

@blp.route('/batch', methods=['POST'])
@blp.arguments(BookScheme(many=True))
@blp.response(BookScheme(many=True))
def add_books(lista):
    """Publicar una lista de libros"""
    print(lista)
    books = book_service.add_books(lista)
    return books, 200

@blp.route('/file', methods=['POST'])
@blp.arguments(BookFileRequest, location="query")
@blp.response(BookScheme(many=True))
def add_books(request):
    """Publicar un archivo de libros"""
    print(request)
    result = book_service.load_books_from_file(request)
    return result, 200

@blp.errorhandler(404)
def page_not_found(e):
    return f"<h1>No se encontró el recurso</h1><p>{e}</p>", 404