from app.models.problem import problem,problem_status
from app.models.problem import db

#data = ProblemForm()

class problem_db():

    def __init__(self):
        self.db_t = problem()

    def save_problem(self,data):
        self.db_t.title = data.title.data
        self.db_t.description = data.description.data
        self.db_t.input_description = data.input_description.data
        self.db_t.output_description = data.output_description.data
        self.db_t.input_example = data.input_example.data
        self.db_t.output_example = data.output_example.data
        self.db_t.hint = data.hint.data
        self.db_t.source = data.source.data
        self.db_t.input_test = data.input_test.data
        self.db_t.output_test = data.output_test.data

        db.session.add(self.db_t)

    def query_problem(self):
        data = problem.query.all()
        return data

    def query_one_problem(self,problem_id):
        data = problem.query.filter_by(id=problem_id).first()
        return data

class problem_db_status():

    def __init__(self):
        self.db_t = problem_status()

    def submit_code(self,data):
        self.db_t.problem_id = data['id']
        self.db_t.language = data['language']
        self.db_t.code = data['code']

        db.session.add(self.db_t)

    def query_db_status(self):
        status_data = problem_status.query.all()
        db.session.rollback()
        return status_data




