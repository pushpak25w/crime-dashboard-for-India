from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
data_children = pd.read_csv("data/Statewise Cases Reported of Crimes Committed Against Children 1994-2016.csv", header=None)
children_states=[i for i in data_children[0][1:].unique()]
children_crimes=[i for i in data_children[1][1:].unique()]
children_years=[2017,2018,2019,2020,2021]
def children_prediction(state,year,crime):
	global data_children
	print(state,year,crime)
	X = [int(i) for i in "1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016".split()]
	X_train=np.array([])
	data_children=data_children[data_children[0]==state].values
	data_children=data_children[data_children[1]==crime].values
	for i in X:
	    X_train=np.append(X_train,i)
	print(data_children)
	y = test[2:]
	y_train=np.array([])
	for i in y:
	    y_train=np.append(y_train,i)
	linear_regression=LinearRegression()
	linear_regression.fit(X_train.reshape(-1,1),y_train)
	print(len(X_train),len(y_train))
	score=linear_regression.score(X_train.reshape(-1,1),y_train)
	b=np.array([])
	if score < 0.60:
		for k in range(2001,2017):
			a = str(k)
			b = np.append(b,a)
		y = list(y)
		years = list(b)
		output = "Can't predict"
	else:
		for j in range(2017,year+1):
			prediction = linear_regression.predict(np.array([[j]]))
			if(prediction < 0):
				prediction = 0
			y = np.append(y,prediction)
		y = np.append(y,0)
		for k in range(2001,year+1):
			a = str(k)
			b = np.append(b,a)
		y = list(y)
		years = list(b)
		output = ""
	if output:
	    print(output)
	else:
	    print(y)
	return (y,years,output)