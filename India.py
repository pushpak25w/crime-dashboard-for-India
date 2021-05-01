import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
def clean(data01to14):
	district=[]
	for i in data01to14['DISTRICT']:
	    if ' ' in i:
	        temp=i.find(' ')
	        if i.count(' ')==1:
	            district.append(i[0]+i[1:temp+1].lower()+i[temp+1]+i[temp+2:].lower())
	        else:
	            temp2=i.rfind(' ')
	            district.append(i[0]+i[1:temp+1].lower()+i[temp+1]+i[temp+2:temp2].lower()+i[temp2+1]+i[temp2+2:].lower())
	    else:
	        district.append(i[0]+i[1:].lower())
	return district
def murder(data01to14):
	murder=pd.DataFrame({'DISTRICT':district,'MURDER':data01to14['MURDER']})
	finalmurder=dict()
	for i in district:
	    finalmurder[i]=sum(murder[murder['DISTRICT']==i]['MURDER'])
	return finalmurder

def theft(data01to14):
	theft=pd.DataFrame({'district':district,'theft':data01to14['THEFT'],'robbery':data01to14['ROBBERY'],'burglary':data01to14['BURGLARY']})
	finaltheft=dict()
	for i in district:
	    useme=theft[theft['district']==i]
	    finaltheft[i]=sum(useme['theft'])+sum(useme['robbery'])+sum(useme['burglary'])
	return finaltheft

def women(data01to14):
	women=pd.DataFrame({'district':district,'kidnap':data01to14['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS'],'rape':data01to14['RAPE'],'assault':data01to14['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY'],'insult':data01to14['INSULT TO MODESTY OF WOMEN'],'husband':data01to14['CRUELTY BY HUSBAND OR HIS RELATIVES'],'dowry':data01to14['DOWRY DEATHS']})
	finalwomen=dict()
	for i in district:
	    useme=women[women['district']==i]
	    finalwomen[i]=sum(useme['rape'])+sum(useme['kidnap'])+sum(useme['assault'])+sum(useme['insult'])+sum(useme['husband'])+sum(useme['dowry'])
	return finalwomen

def merge_murder(finalmurder,map_df):
	murder=pd.DataFrame({'DISTRICT':finalmurder.keys(),'MURDER':finalmurder.values()})
	mergedmurder = map_df.set_index('NAME_2').join(murder.set_index('DISTRICT'))
	mergedmurder['MURDER'].fillna(mergedmurder['MURDER'].mean(), inplace=True)
	return mergedmurder

def merge_theft(finaltheft,map_df):
	theft=pd.DataFrame({'district':finaltheft.keys(),'theft':finaltheft.values()})
	mergedtheft=map_df.set_index('NAME_2').join(theft.set_index('district'))
	mergedtheft['theft'].fillna(mergedtheft['theft'].mean(), inplace=True)
	return mergedtheft

def merge_women(finalwomen,map_df):
	women=pd.DataFrame({'district':finaltheft.keys(),'women':finalwomen.values()})
	mergedwomen=map_df.set_index('NAME_2').join(women.set_index('district'))
	mergedwomen['women'].fillna(mergedwomen['women'].mean(), inplace=True)
	return mergedwomen

fp = "gadm36_IND_shp/gadm36_IND_2.shp" 
map_df=gpd.read_file(fp)
map_df = map_df[['NAME_2', 'geometry']]
data01to14=pd.read_csv('data/01_District_wise_crimes_committed_IPC_2001_2012.csv')
district=clean(data01to14)
crime=input("Enter crime: ")
if crime=="murder":
	finalmurder=murder(data01to14)
	mergedmurder=merge_murder(finalmurder,map_df)
	fig, ax = plt.subplots(1, figsize=(20,20))
	mergedmurder.plot(column='MURDER', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
elif crime=="theft":
	finaltheft=theft(data01to14)
	mergedtheft=merge_theft(finaltheft,map_df)
	fig, ax = plt.subplots(1, figsize=(20,20))
	mergedtheft.plot(column='theft', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
elif crime=="women":
	finalwomen=women(data01to14)
	mergedwomen=merge_women(finalwomen,map_df)
	fig, ax = plt.subplots(1, figsize=(20,20))
	mergedwomen.plot(column='women', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
