from flask_smorest import Api, Blueprint, abort
from service import author_service
from service.author_scheme import AuthorScheme

blp = Blueprint(
    'authors', 'authors', url_prefix='/authors',
    description='Operaciones sobre los autores'
)

@blp.route('/', methods=['GET'])
#@blp.arguments(FilterRequestSchema, location="query")
@blp.response(AuthorScheme(many=True))
def api_all():
    """Obtener libros de acuerdo a criterios"""
    #return book_service.get_books()
    return author_service.get_authors_by_filter()
