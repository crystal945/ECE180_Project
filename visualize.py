import pandas as pd
import matplotlib.pyplot as plt
'''
	Author: 		Matthew Wnuk
	Last Edit:		Feb 2018
		
	Description:		Class containing methods for visualization of the various data
'''

class Visualize():
	def Ownership_Rates(self, key):
		df = pd.read_excel('data/' + key + '.xls', skiprows=10)
		plt.plot(df['observation_date'], df['HOWNRATEACS006073'])
		plt.title('Ownership Rates, San Diego County')
		plt.xlabel('Year')
		plt.ylabel('Ownership Rate [%]')
		
	def All_Transaction_Prices(self, key):
		df = pd.read_excel('data/' + key + '.xls', skiprows=10)
		plt.plot(df['observation_date'], df['ATNHPIUS06073A'])
		plt.title('Transaction Prices, San Diego County')
		plt.xlabel('Year')
		plt.ylabel('Transaction Prices')

	def Approved_Construction_Rates(self, key):
		df = pd.read_excel('data/' + key + '.xls', skiprows=10)
		plt.plot(df['observation_date'], df['SAND706BPPRIV'])
		plt.title('New Construction, San Diego County')
		plt.xlabel('Year')
		plt.ylabel('Num of Approved Construction Plans')
	
	def Consumer_Price_Index(self, key):
		df = pd.read_excel('data/' + key + '.xls', skiprows=10)
		plt.plot(df['observation_date'], df['CUUSA424SAH'])
		plt.title('Consumer Price Index, San Diego County')
		plt.xlabel('Year')
		plt.ylabel('CPI for San Diego County')	
	
	def Median_Income(self, key):
		df = pd.read_excel('data/' + key + '.xls', skiprows=11)
		plt.plot(df['observation_date'], df['MHICA06073A052NCEN_20161214'])
		plt.title('Median Income of Resident of San Diego County')
		plt.xlabel('Year')
		plt.ylabel('Median Income 2016 Adjusted [$]')	
	
	def Resident_Population(self, key):
		df = pd.read_excel('data/' + key + '.xls', skiprows=11)
		plt.plot(df['observation_date'], df['CASAND5POP_20170327'])
		plt.title('Resident Population, San Diego County')
		plt.xlabel('Year')
		plt.ylabel('Population [1k]')	
	
	def Unemployment_Rate(self, key):
		df = pd.read_excel('data/' + key + '.xls', skiprows=10)
		plt.plot(df['observation_date'], df['CASAND5URN'])
		plt.title('Unemployment Rate, San Diego County')
		plt.xlabel('Year')
		plt.ylabel('Unemployment Rate [%]')	
		

	
