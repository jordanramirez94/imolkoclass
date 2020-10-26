from uuid import uuid4
import marshmallow as ma
import uuid

class AuthorScheme(ma.Schema):
    author_id = ma.fields.String(default=uuid.uuid4)
    name = ma.fields.String(required=True)
    birth = ma.fields.Integer()