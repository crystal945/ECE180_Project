import os
import requests

def get_data():
	'''
		Author: 		Matthew Wnuk
		Last Edit:		Feb 2018
		Param: 			SourceMaterials, type dictionary
		
		Description:	Defines a dictionary containing descriptive labels for data contained at URLs
						associated with various primary source data. Downloads source material and 
						saves as xls named as Key of dictionary
	'''
	SourceMaterials = {}
	SourceMaterials['Ownership_Rates'] = 'https://github.com/wnukmat/San_Diego_Data/blob/master/HOWNRATEACS006073.xls?raw=true'
	SourceMaterials['All_Transaction_Prices'] = 'https://github.com/wnukmat/San_Diego_Data/blob/master/all_transaction_home_price.xls?raw=true'
	SourceMaterials['Approved_Construction_Rates'] = 'https://github.com/wnukmat/San_Diego_Data/blob/master/approved_construction_rates.xls?raw=true'
	SourceMaterials['Consumer_Price_Index'] = 'https://github.com/wnukmat/San_Diego_Data/blob/master/consumer_price_index.xls?raw=true'
	SourceMaterials['Unemployment_Rate'] = 'https://github.com/wnukmat/San_Diego_Data/blob/master/CASAND5URN.xls?raw=true'
	SourceMaterials['Resident_Population'] = 'https://github.com/wnukmat/San_Diego_Data/blob/master/resident_population.xls?raw=true'
	SourceMaterials['Median_Income'] = 'https://github.com/wnukmat/San_Diego_Data/blob/master/median_household_income.xls?raw=true'
	SourceMaterials['Labor_Statistics'] = 'https://github.com/wnukmat/San_Diego_Data/blob/master/labor_statistics.xlsx?raw=true'

	ZillowMaterials = {}
	ZillowMaterials['SFM_Sale_Price'] = 'http://files.zillowstatic.com/research/public/County/County_Zhvi_SingleFamilyResidence.csv'
	ZillowMaterials['SFM_Rent_Price'] = 'http://files.zillowstatic.com/research/public/County/County_MedianRentalPrice_Sfr.csv'
	ZillowMaterials['Price2Rent_Ratio'] = 'http://files.zillowstatic.com/research/public/County/County_PriceToRentRatio_AllHomes.csv'

	try:
		os.stat('data')
	except:
		os.mkdir('data')
	
	for key in SourceMaterials:
		resp = requests.get(SourceMaterials[key])
		output = open('data/' + key + '.xls', 'wb')
		output.write(resp.content)
		output.close()

	for key in ZillowMaterials:
		resp = requests.get(ZillowMaterials[key])
		output = open('data/' + key + '.csv', 'wb')
		output.write(resp.content)
		output.close()
		
	return SourceMaterials, ZillowMaterials
	
	
if __name__ == '__main__':
	Source, ZillowMaterials = get_data()