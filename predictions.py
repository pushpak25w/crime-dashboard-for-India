from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_children = pd.read_csv("data/Statewise Cases Reported of Crimes Committed Against Children 1994-2016.csv", header=None)
children_states=[i for i in data_children[0][1:].unique()]
children_crimes=[i for i in data_children[1][1:].unique()]
children_years=[2017,2018,2019,2020,2021]
data_women = pd.read_csv("data/statewise_crime_against_women_2001_15.csv")
women_states=[i for i in data_women['STATE/UT'].unique()]
women_crimes=[i for i in data_women][2:]
women_years=[2016,2017,2018,2019,2020,2021]

def children_prediction(state,year,crime):
	global data_children
	data=data_children
	year=int(year)
	X=data.iloc[0:1,2:].values[0]
	X_train=np.array([int(i) for i in X])
	data =data[data [0]==state]
	data =data[data [1]==crime]
	print(data.iloc[:,2:])
	y=data.iloc[:,2:].values[0]
	y_train=np.array([int(i) for i in y])
	linear_regression=LinearRegression()
	linear_regression.fit(X_train.reshape(-1,1),y_train)
	print(len(X_train),len(y_train))
	score=linear_regression.score(X_train.reshape(-1,1),y_train)
	b=np.array([])
	if score < 0.60:
		b=np.array([str(i) for i in range(1994,2017)])
		y = list(y)
		years = list(b)
		year = 2016
		output = "Can't predict further"
	else:
		for j in range(2017,year+1):
			prediction = linear_regression.predict(np.array([[j]]))
			if(prediction < 0):
				prediction = 0
			y = np.append(y,prediction)
		b=np.array([str(i) for i in range(1994,year+1)])
		y = list(y)
		years = list(b)
		output = ""
	if output:
		print(output)
	else:
		print(y)
	print(b)
	return (y,years,output)

def women_prediction(state,year,crime):
	global data_women
	data=data_women
	print(year)
	year=int(year)
	data =data[data['STATE/UT']==state]
	X=[i for i in data['Year']]
	X_train=np.array([int(i) for i in X])
	y=[i for i in data[crime]]
	y_train=np.array([int(i) for i in y])
	linear_regression=LinearRegression()
	linear_regression.fit(X_train.reshape(-1,1),y_train)
	print(len(X_train),len(y_train))
	score=linear_regression.score(X_train.reshape(-1,1),y_train)
	b=np.array([])
	if score < 0.60:
		b=np.array([str(i) for i in range(2001,2016)])
		y = list(y)
		years = list(b)
		year = 2015
		output = "Can't predict"
	else:
		for j in range(2016,year+1):
			prediction = linear_regression.predict(np.array([[j]]))
			if(prediction < 0):
				prediction = 0
			y = np.append(y,prediction)
		b=np.array([str(i) for i in range(2001,year+1)])
		y = list(y)
		years = list(b)
		output = ""
	if output:
		print(output)
	else:
		print(y)
	print(b)
	return (y,years,output)

def pred_crime_plot(state,crime,x,y):
    plt.figure(figsize=(10,10)) 
    plt.grid(True)
    plt.xticks(fontsize=8)
    plt.plot(y,x)
    plt.xlabel('Years')
    plt.ylabel('No. of '+crime+' Cases in '+state)
    plt.title(crime)
    plt.savefig('static/images/plot.png')