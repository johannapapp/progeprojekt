from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load questions and answers from the file
def load_data():
    with open("vastused.txt", "r") as f:
        questions = f.readline().strip().split("\t")[1:]
        data = {}
        for line in f:
            parts = line.strip().split("\t")
            name = parts[0]
            answers = parts[1:]
            data[name] = {questions[i]: answers[i] for i in range(len(questions))}
    return questions, data

questions, data = load_data()

@app.route('/')
def index():
    # Initialize session variables if they don't exist
    if 'questions' not in session:
        session['questions'] = questions.copy()
    if 'nimed' not in session:
        session['nimed'] = list(data.keys())
    if 'current_question' not in session or session['current_question'] is None:
        session['current_question'] = random.choice(session['questions']) if session['questions'] else None
    
    return render_template('index.html', question=session['current_question'])

@app.route('/answer', methods=['POST'])
def answer():
    user_answer = request.form.get('answer')
    question = session['current_question']

    # Debugging output
    print(f"User answered: {user_answer}")
    print(f"Question: {question}")
    
    session['questions'].remove(question)

    new_nimed = [name for name in session['nimed'] if data[name][question] == user_answer]
    session['nimed'] = new_nimed

    # Debugging output
    print(f"Remaining names: {session['nimed']}")

    if session['questions']:
        session['current_question'] = random.choice(session['questions'])
    else:
        session['current_question'] = None

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
