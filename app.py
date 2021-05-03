from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from India import districtwise,clean_states,data01to14

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
class Data(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	state=db.Column(db.String(200),nullable=False)
	district=db.Column(db.String(200),nullable=False)
	crime=db.Column(db.String(200),nullable=False)
	number=db.Column(db.Integer)
	year=db.Column(db.Integer)
	date_created=db.Column(db.DateTime,default=datetime.utcnow)
	def __repr__(self):
		return '<Task %r' % self.id
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/main')
def main():
	return render_template('main.html')

@app.route('/info')
def info():
	return render_template('info.html')

@app.route('/compare')
def compare():
	return render_template('compare.html')

@app.route('/graph')
def graph():
	return render_template('graph.html')

@app.route('/map')
def map():
	return render_template('map.html')

@app.route('/select')
def select():
	return render_template('select.html',data=[{'name':i} for i in clean_states(data01to14)])

@app.route('/selected',methods=['GET','POST'])
def selected():
	district_selected=request.form.get('district')
	crime_selected=request.form.get('crime') 
	districtwise(crime_selected,district_selected)
	return render_template('display.html')

@app.route('/insert',methods=['POST','GET'])
def insert():
	if request.method=='POST':
		form_year=request.form['year']
		form_state=request.form['state']
		form_district=request.form['district']
		form_crime=request.form['crime']
		form_number=request.form['number']
		new_data=Data(state=form_state,district=form_district,crime=form_crime,number=form_number,year=form_year)
		if int(form_year)<=14:
			return 'no thanks'
		try:
			db.session.add(new_data)
			db.session.commit()
			return redirect('/insert')
		except:
			data=Data.query.order_by(Data.date_created).all()
			return render_template('insert.html',data=data)
		return 'hello'
	else:
		data_sorted=Data.query.all()
		return render_template('insert.html',data_sorted=data_sorted)

@app.route('/delete/<int:d>')
def delete(id):
	entry_to_delete=Data.query.get_or_404(id)
	try:
		db.session.delete(entry_to_delete)
		db.session.commit()
		return render_template('insert.html')
	except:
		return 'some problem'


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
	app.run(debug=True)