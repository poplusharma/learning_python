from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(250), unique=True, nullable=False)
    task_status = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

db.create_all()

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    tasks = db.session.query(Todo).all()

    if request.method == "POST":
        task_name = request.form.get('task')
        task_status = True

        if task_name:
            new_task = Todo(
                task_name = task_name,
                task_status = task_status
            )

            db.session.add(new_task)
            db.session.commit()

            return redirect('home')

        else:
            id = request.form.get('flexCheckDefault')
            if id:
                task = Todo.query.get(id)
                task.task_status = False
                db.session.commit()
            else:
                id = request.form.get('flexCheckChecked')
                task = Todo.query.get(id)
                task.task_status = True
                db.session.commit()

            return redirect('home')
    
    return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)