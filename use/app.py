from flask import Flask, flash, redirect, render_template, \
     request, url_for
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
	data01to14=pd.read_csv('data/01_District_wise_crimes_committed_IPC_2001_2012.csv')
	district=[]
	for i in data01to14['DISTRICT']:
	    if ' ' in i:
	        temp=i.find(' ')
	        if i.count(' ')==1:
	            district.append({'name':i[0]+i[1:temp+1].lower()+i[temp+1]+i[temp+2:].lower()})
	        else:
	            temp2=i.rfind(' ')
	            district.append({'name':i[0]+i[1:temp+1].lower()+i[temp+1]+i[temp+2:temp2].lower()+i[temp2+1]+i[temp2+2:].lower()})
	    else:
	        district.append({'name':i[0]+i[1:].lower()})
	return render_template('index.html',data=district)

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is

if __name__=='__main__':
    app.run(debug=True)