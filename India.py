import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

fp = "gadm36_IND_shp/gadm36_IND_2.shp"
map_df = gpd.read_file(fp)
states_to_ui=map_df['NAME_1'].unique()
#map_df = map_df[['NAME_2', 'geometry']]
data01to14=pd.read_csv('data/01_District_wise_crimes_committed_IPC_2001_2012.csv')
def clean_states(data01to14):
	district=[]
	check={}
	for i in data01to14['STATE/UT']:
	    if ' ' in i and i not in check:
	        temp=i.find(' ')
	        if i.count(' ')==1:
	            district.append(i[0]+i[1:temp+1].lower()+i[temp+1]+i[temp+2:].lower())
	            check[i]=1
	        else:
	            temp2=i.rfind(' ')
	            district.append(i[0]+i[1:temp+1].lower()+i[temp+1]+i[temp+2:temp2].lower()+i[temp2+1]+i[temp2+2:].lower())
	            check[i]=1
	    elif i not in check:
	        district.append(i[0]+i[1:].lower())
	        check[i]=1
	return district
def all_districts(data01to14):
	district=[]
	for i in data01to14['DISTRICT']:
	    if ' ' in i:
	        temp=i.find(' ')
	        if i.count(' ')==1 and temp<len(i)-1:
	            district.append(i[0]+i[1:temp+1].lower()+i[temp+1]+i[temp+2:].lower())
	        else:
	            district.append(i)
	    else:
	        district.append(i[0]+i[1:].lower())
	return district

data01to14['DISTRICT']=all_districts(data01to14)

def murder(data01to14):
	district=data01to14['DISTRICT']
	murder=pd.DataFrame({'DISTRICT':district,'MURDER':data01to14['MURDER']})
	finalmurder=dict()
	for i in district:
	    finalmurder[i]=sum(murder[murder['DISTRICT']==i]['MURDER'])
	return finalmurder

def theft(data01to14):
	district=data01to14['DISTRICT']
	theft=pd.DataFrame({'district':district,'theft':data01to14['THEFT'],'robbery':data01to14['ROBBERY'],'burglary':data01to14['BURGLARY']})
	finaltheft=dict()
	for i in district:
	    useme=theft[theft['district']==i]
	    finaltheft[i]=sum(useme['theft'])+sum(useme['robbery'])+sum(useme['burglary'])
	return finaltheft

def women(data01to14):
	district=data01to14['DISTRICT']
	women=pd.DataFrame({'district':district,'kidnap':data01to14['KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS'],'rape':data01to14['RAPE'],'assault':data01to14['ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY'],'insult':data01to14['INSULT TO MODESTY OF WOMEN'],'husband':data01to14['CRUELTY BY HUSBAND OR HIS RELATIVES'],'dowry':data01to14['DOWRY DEATHS']})
	finalwomen=dict()
	for i in district:
	    useme=women[women['district']==i]
	    finalwomen[i]=sum(useme['rape'])+sum(useme['kidnap'])+sum(useme['assault'])+sum(useme['insult'])+sum(useme['husband'])+sum(useme['dowry'])
	return finalwomen

def merge_murder(finalmurder,state,map_df):
	map_df = map_df[['NAME_1', 'NAME_2', 'geometry']]
	map_df = map_df[map_df['NAME_1']==state]
	murder=pd.DataFrame({'DISTRICT':finalmurder.keys(),'MURDER':finalmurder.values()})
	mergedmurder = map_df.set_index('NAME_2').join(murder.set_index('DISTRICT'))
	mergedmurder['MURDER'].fillna(mergedmurder['MURDER'].mean(), inplace=True)
	return mergedmurder

def merge_theft(finaltheft,state,map_df):
	map_df = map_df[['NAME_1', 'NAME_2', 'geometry']]
	map_df = map_df[map_df['NAME_1']==state]
	theft=pd.DataFrame({'district':finaltheft.keys(),'theft':finaltheft.values()})
	mergedtheft=map_df.set_index('NAME_2').join(theft.set_index('district'))
	mergedtheft['theft'].fillna(mergedtheft['theft'].mean(), inplace=True)
	return mergedtheft

def merge_women(finalwomen,state,map_df):
	map_df = map_df[['NAME_1', 'NAME_2', 'geometry']]
	map_df = map_df[map_df['NAME_1']==state]
	women=pd.DataFrame({'district':finalwomen.keys(),'women':finalwomen.values()})
	mergedwomen=map_df.set_index('NAME_2').join(women.set_index('district'))
	mergedwomen['women'].fillna(mergedwomen['women'].mean(), inplace=True)
	return mergedwomen

def districtwise(crime,district):
	fp = "gadm36_IND_shp/gadm36_IND_2.shp" 
	map_df=gpd.read_file(fp)
	district_wise = data01to14[data01to14['STATE/UT']==district]
	if crime=='MURDER':
		merged=merge_murder(murder(district_wise),district,map_df)
	elif crime=='theft':
		merged=merge_theft(theft(district_wise),district,map_df)
	elif crime=='women':
		merged=merge_women(women(district_wise),district,map_df)
	fig, ax = plt.subplots(1, figsize=(8,8))
	ax.axis('off')
	ax.set_title(district, fontdict={'fontsize': '25', 'fontweight' : '3'})
	merged.plot(column=crime, cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
	fig.savefig("static/images/District_wise.png", dpi=100)

def multi_crime_plot(district,crime):
    district_wise = data01to14[data01to14['DISTRICT'] == district]
    gr_plt=district_wise.set_index('YEAR')[crime].plot(kind = 'line', figsize = (10,10))
    plt.xlabel('Years')
    plt.ylabel('No. of Cases in '+district)
    plt.title(','.join(crime))
    fig = gr_plt.get_figure()
    fig.savefig("static/images/plot.png")


#def merge_any(finalany,crime,mapdf):
	

def plot_map_any(crime):
	for i in crime:
		crime=i
	fp = "gadm36_IND_shp/gadm36_IND_2.shp"
	map_df = gpd.read_file(fp)
	map_df = map_df[['NAME_2', 'geometry']]
	final=dict()
	for i in data01to14['DISTRICT'].unique():
		final[i]=sum(data01to14[crime][data01to14['DISTRICT']==i])
	d={'district':final.keys(),crime:final.values()}
	district_wise=pd.DataFrame(d)
	merged=map_df.set_index('NAME_2').join(district_wise.set_index('district'))
	merged.fillna(merged[crime].mean(),inplace=True)
	fig, ax = plt.subplots(1, figsize=(20,20))
	ax.axis('off')
	ax.set_title(crime, fontdict={'fontsize': '25', 'fontweight' : '3'})
	merged.plot(column=crime, cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
	fig.savefig("static/images/District_wise.png", dpi=100)
