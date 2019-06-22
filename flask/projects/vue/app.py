from flask import Flask, render_template, json

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/test')
def test():
	my_dict = { "title": "Bayside", "genre": "Alternative" }
	return json.dumps(my_dict)


if __name__ == "__main__":
	print("Servidor rodando localmente!!!")
	app.run(debug=True)