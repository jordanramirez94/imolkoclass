import marshmallow as ma
import uuid

def calculate_tenure(data):
    year = data["year_published"]
    if year > 2015:
        return "Nuevo"
    if year > 2010:
        return "Viejo"
    return "Viejisimo"


class BookScheme(ma.Schema):
    book_id = ma.fields.String(default=uuid.uuid4, description="Id Unico del Libro", dump_only=True)
    title = ma.fields.String(validate=ma.validate.Length(min=5))
    author = ma.fields.String()
    first_sentence = ma.fields.String()
    year_published = ma.fields.Integer(required=True)
    tenure = ma.fields.Function(calculate_tenure)
    date = ma.fields.Date(required=True)

class BookFileRequest(ma.Schema):
    name = ma.fields.String(required=True)
    separator = ma.fields.String(required=True, enum=[";",",","|"])
    