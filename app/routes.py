from flask import Flask, render_template
from flask_restful import Api, Resource
from app.schemas import QuestionSchema
from app.modules import open_file, rand_quest
from pathlib import Path

app = Flask(__name__)
api = Api(app)

file_path = Path(__file__).resolve().parent.parent / 'questions.txt'


class QuestionResource(Resource):
    def get(self):
        questions = open_file(file_path)
        selected = rand_quest(questions, 10)
        schema = QuestionSchema(many=True)
        return schema.dump(selected), 200


class AllQuestionsResource(Resource):
    def get(self):
        questions = open_file(file_path)
        schema = QuestionSchema(many=True)
        return schema.dump(questions), 200


# по адресу http://127.0.0.1:5000/ вернет просто 10 вопросов рандомно
# по адресу http://127.0.0.1:5000/questions/25 вернется 25 вопрсов? число можно ставить свое
# но если число больше количество вопрсоов - то вернет все вопросы
@app.route('/')
@app.route('/questions/<int:count>')
def show_questions(count=10):
    questions = open_file(file_path)
    selected = rand_quest(questions, count)
    return render_template('questions.html', questions=selected)


# отвечает за вывод всех вопросов и ответов
@app.route('/all')
def show_all_questions():
    all_questions = open_file(file_path)
    return render_template('all_questions.html', questions=all_questions)


# Можно побаловаться через постман , по сути у нас есть api свое
api.add_resource(QuestionResource, '/api/questions', '/api/questions/')
api.add_resource(AllQuestionsResource, '/api/questions/all', '/api/questions/all/')
