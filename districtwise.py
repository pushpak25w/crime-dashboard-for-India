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
