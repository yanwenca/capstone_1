from flask import Flask, flash, render_template, redirect, request
import requests
from models import db, connect_db, Survey
from forms import SurveyForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///survey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = 'abcde'
API_KEY = '5V19FYHM3UJZ6F5P'

@app.route("/")
def root():
    """Homepage: redirect to /survey."""

    return redirect("/survey")


@app.route("/survey", methods=["GET", "POST"])
def survey():
	form = SurveyForm()

	print(form.validate_on_submit())
	

	if form.validate_on_submit():
		q1 = form.q1.data
		q2 = form.q2.data
		q3 = form.q3.data
		q4 = form.q4.data
		q5 = form.q5.data
		
		new_response = Survey(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
		db.session.add(new_response)
		db.session.commit()
		


		flash(f"Response Received")
		return redirect("/currency")
	else:
		return render_template("survey.html", form=form)
    	
	return render_template('survey.html')


@app.route("/currency", methods=['GET', 'POST'])
def homepage():
	if request.method == 'POST':
		try:
			amount = request.form['amount']
			amount = float(amount)
			from_c = request.form['from_c']
			to_c = request.form['to_c']
			
			url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(from_c, to_c, API_KEY)

			response = requests.get(url=url).json()
			rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
			rate = float(rate)
			result = rate * amount
		
			from_c_code = response['Realtime Currency Exchange Rate']['1. From_Currency Code']
			from_c_name = response['Realtime Currency Exchange Rate']['2. From_Currency Name']
			to_c_code = response['Realtime Currency Exchange Rate']['3. To_Currency Code']
			to_c_name = response['Realtime Currency Exchange Rate']['4. To_Currency Name']
			time = response['Realtime Currency Exchange Rate']['6. Last Refreshed']
			return render_template('index.html', result=round(result, 2), amount=amount,
								from_c_code=from_c_code, from_c_name=from_c_name,
								to_c_code=to_c_code, to_c_name=to_c_name, time=time)
		except Exception as e:
			return '<h1>Bad Request : {}</h1>'.format(e)

	else:
		return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)
