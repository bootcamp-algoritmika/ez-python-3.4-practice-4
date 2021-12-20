from marshmallow import Schema, pre_dump
from marshmallow.fields import String, Integer


class MessageSchema(Schema):
    id = Integer()
    text = String()
    author = Integer()

    @pre_dump
    def message_predump(self, data, **kwargs):
        result = {'author': data.author.id, 'text': data.text}
        return result


class MessageUserSchema(Schema):
    id = Integer()
    text = String()
