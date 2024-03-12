from flask import *

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/products')
def products():
	return render_template('products.html')

@app.route('/services')
def services():
	return render_template('services.html')

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)