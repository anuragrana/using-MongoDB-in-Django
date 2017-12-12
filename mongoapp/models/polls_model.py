from mongoengine import *

connect('PollsDB')

class ChoiceModel(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)


class PollModel(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(ChoiceModel))