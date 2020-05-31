from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route('/')
def quz(name=None):
	 return render_template('question.html',name='Ajesh')