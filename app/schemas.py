from marshmallow import Schema, fields


class QuestionSchema(Schema):
    question = fields.Str()
    answer = fields.Str()
