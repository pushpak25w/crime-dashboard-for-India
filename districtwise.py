def districtwise(crime,district):
	fp = "gadm36_IND_shp/gadm36_IND_2.shp"
	map_df = gpd.read_file(fp)
	district_wise = data01to14[['STATE/UT', 'DISTRICT', crime]]
	district_wise = district_wise[district_wise['STATE/UT']==district]
	merged = map_df.set_index('NAME_2').join(district_wise.set_index('DISTRICT'))
	fig, ax = plt.subplots(1, figsize=(10, 6))
	fig.savefig("District_wise.png", dpi=100)