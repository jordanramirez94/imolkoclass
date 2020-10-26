import marshmallow as ma

class FilterRequestSchema(ma.Schema):
    author = ma.fields.String()
    year_published = ma.fields.Integer()