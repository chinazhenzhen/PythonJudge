from app.models.problem import Problem
from app.forms.problem import ProblemForm
from app.models.problem import db

#data = ProblemForm()

class ProblemDb():

    def __init__(self):
        self.db = Problem()

    def saveinformation(self,data):

        self.db.title = data.title.data
        self.db.description = data.description.data
        self.db.input_description = data.input_description.data
        self.db.output_description = data.output_description.data
        self.db.input_example = data.input_example.data
        self.db.output_example = data.output_example.data
        self.db.hint = data.hint.data
        self.db.source = data.source.data
        self.db.input_test = data.input_test.data
        self.db.output_test = data.output_test.data

        db.session.add(self.db)

