################################### All Packages ################################
import pandas as pd
import os                         #To download folder which contains stocks data
import numpy as np
#from matplotlib import pyplot as plt

################################# Benchmark Strategy: ######################################
cwd = os.path.abspath('C:/Users/yamini/Desktop/50 Stocks Data/')
files = os.listdir(cwd)             #folder was downloaded

#all the excel was concatenated into a list
tmp = []
for i, file in enumerate(files[1:], 1):
    if file.endswith('.xlsx'):
        tmp.append(pd.read_excel('C:/Users/yamini/Desktop/50 Stocks Data/' + file))

df = pd.concat(tmp, axis=1)
df.head(5)
df.columns

#converted the concatenated files to excel and saved it into 50_stocks.
df.to_excel('C:/Users/yamini/Desktop/50_stocks.xlsx')

#accessed the excel file
data=pd.read_excel('C:/Users/yamini/Desktop/50_stocks.xlsx')
data.head(5)
data.columns


#getting all the column names along with index for an easy access.
{data.columns.get_loc(c): c for idx, c in enumerate(data.columns)}

data1=data[["VALUE ","VALUE .1","VALUE .2","VALUE .3","VALUE .4","VALUE .5","VALUE .6","VALUE .7",
      "VALUE .8","VALUE .9","VALUE .10","VALUE .11","VALUE .12","VALUE .13","VALUE .14","VALUE .15",
      "VALUE .16","VALUE .17","VALUE .18","VALUE .19","VALUE .20","VALUE .21","VALUE .22","VALUE .23",
      "VALUE .24","VALUE .25","VALUE .26","VALUE .27","VALUE .28","VALUE .29","VALUE .30","VALUE .31",
      "VALUE .32","VALUE .33","VALUE .34","VALUE .35","VALUE .36","VALUE .37","VALUE .38","VALUE .39",
      "VALUE .40","VALUE .41","VALUE .42","VALUE .43","VALUE .44","VALUE .45","VALUE .46","VALUE .47",
      "VALUE .48"]]
data1.head(5)

#getting the sum of all the stocks for daily value.
data2 = data1.sum(axis = 1)
data2


#getting the equal allocation
initial_investment=1000000
Equal_allocation=initial_investment/50
Equal_allocation              #20000 on each stock

#getting the percentages of our investment that goes into every stock
Equal_allocation_percentage_Benchmark_Strategy=(Equal_allocation/data2)*100
Equal_allocation_percentage_Benchmark_Strategy


#cagr:
begin_Benchmark_Strategy=Equal_allocation_percentage_Benchmark_Strategy. iloc[0]
final_Benchmark_Strategy=Equal_allocation_percentage_Benchmark_Strategy. iloc[273]
cagr_Benchmark_Strategy=(((begin_Benchmark_Strategy/final_Benchmark_Strategy)**(1/2))-1)*100
cagr_Benchmark_Strategy

#Daily returns
data2
value_on_t=data2
value_on_day_minusone=data2-1
daily_returns=(value_on_t/value_on_day_minusone)-1
daily_returns

#volatility:
volatality_Benchmark_Strategy=((np.std(daily_returns))**(1/252))*100
volatality_Benchmark_Strategy

#Sharpe Ratio
Sharpe_Ratio_Benchmark_Strategy=(np.mean(daily_returns)/np.std(daily_returns))**1/252
Sharpe_Ratio_Benchmark_Strategy


data2=pd.DataFrame(data2) 
Equity_Values_file = pd.concat([data, data2], axis=1)
Equity_Values_file.columns
{Equity_Values_file.columns.get_loc(c): c for idx, c in enumerate(Equity_Values_file.columns)}

# Rename column name by index
Equity_Values_file.rename(columns={Equity_Values_file.columns[245]: 'Equity Curve'},inplace=True)
print(Equity_Values_file.columns)
Equity_Values_file.to_csv('Equity_Values .csv')

####################################### Sample Strategy #########################################
#We are taking main data into data2
data2=data
data2.columns

#Taking last 100 days of stocks
data3=data2.tail(100-1)
data3.columns
{data3.columns.get_loc(c): c for idx, c in enumerate(data3.columns)}

#taking only close prices
data4=data3[["close ","close .1","close .2","close .3","close .4","close .5","close .6","close .7",
      "close .8","close .9","close .10","close .11","close .12","close .13","close .14","close .15",
      "close .16","close .17","close .18","close .19","close .20","close .21","close .22","close .23",
      "close .24","close .25","close .26","close .27","close .28","close .29","close .30","close .31",
      "close .32","close .33","close .34","close .35","close .36","close .37","close .38","close .39",
      "close .40","close .41","close .42","close .43","close .44","close .45","close .46","close .47",]]
data4.columns
data4       #can see 99 rows as it starts from 0.. So totally 100 days.

#getting the sum of all the stocks for daily value.
data5 = data4.sum(axis = 1)
data5

#percenatge_returns=(Close (last day) / Close (100th day before last day) - 1)
percenatge_returns=(data5.loc[273]/data5.loc[175])-1
percenatge_returns
type(percenatge_returns)

#sorted the values in descending order. So that we can get the top 10 stocks on the basis of percentage_returns
percenatge_returns = np.linspace(percenatge_returns,stop=False)
len(percenatge_returns)
sorted_percenatge_returns=sorted(percenatge_returns,reverse=True)
sorted_percenatge_returns

#took top 10 stocks and converted into dataframe
type(sorted_percenatge_returns)
top_10_stocks = sorted_percenatge_returns[0:10]
top_10_stocks
type(top_10_stocks)
top_10_stocks=pd.DataFrame(top_10_stocks)       
type(top_10_stocks)

#inital investment for top 10 stocks
initial_investment=1000000
Equal_allocation=initial_investment/10
Equal_allocation              #100000 on each stock
type(Equal_allocation)

#We got the percentages of our investment that goes into every stock
Equal_allocation_percentage_Sample_Strategy=(Equal_allocation/top_10_stocks)*100
Equal_allocation_percentage_Sample_Strategy


#cagr_Sample_Strategy
begin_Sample_Strategy=Equal_allocation_percentage_Sample_Strategy. iloc[0]
final_Sample_Strategy=Equal_allocation_percentage_Sample_Strategy. iloc[9]
cagr_Sample_Strategy=(((final_Sample_Strategy/begin_Sample_Strategy)**(1/2))-1)*100
cagr_Sample_Strategy
type(cagr_Sample_Strategy)
cagr_Sample_Strategy = cagr_Sample_Strategy.values.tolist()
cagr_Sample_Strategy
type(cagr_Sample_Strategy)
cagr_Sample_Strategy=cagr_Sample_Strategy[0]
cagr_Sample_Strategy

#volatility:
#taking 100 days values and suming up for daily returns
vol_data=data3[["VALUE ","VALUE .1","VALUE .2","VALUE .3","VALUE .4","VALUE .5","VALUE .6","VALUE .7",
      "VALUE .8","VALUE .9","VALUE .10","VALUE .11","VALUE .12","VALUE .13","VALUE .14","VALUE .15",
      "VALUE .16","VALUE .17","VALUE .18","VALUE .19","VALUE .20","VALUE .21","VALUE .22","VALUE .23",
      "VALUE .24","VALUE .25","VALUE .26","VALUE .27","VALUE .28","VALUE .29","VALUE .30","VALUE .31",
      "VALUE .32","VALUE .33","VALUE .34","VALUE .35","VALUE .36","VALUE .37","VALUE .38","VALUE .39",
      "VALUE .40","VALUE .41","VALUE .42","VALUE .43","VALUE .44","VALUE .45","VALUE .46","VALUE .47",]]
vol_data

vol_data_sum = vol_data.sum(axis = 1)
vol_data_sum

#Daily returns
vol_data_sum
value_on_t=vol_data_sum
value_on_day_minusone=vol_data_sum-1
daily_returns_Sample_Strategy=(value_on_t/value_on_day_minusone)-1
daily_returns_Sample_Strategy

volatality_Sample_Strategy=((np.std(daily_returns_Sample_Strategy))**(1/252))*100
volatality_Sample_Strategy

#Sharpe Ratio
Sharpe_Ratio_Sample_Strategy=(np.mean(daily_returns_Sample_Strategy)/np.std(daily_returns_Sample_Strategy))**1/252
Sharpe_Ratio_Sample_Strategy

######################################## Nifty Index ##################################################
#taking nifty index data for mentioned period of 2 years
nifty_data=pd.read_excel('C:/Users/yamini/Desktop/NiftyIndex.xlsx')
nifty_data.columns

#converted cr to lakhs for daily returns
nifty_value=nifty_data[['Turnover (Rs. Cr)']]
nifty_value_lakhs=nifty_value*100
nifty_value_lakhs

#Initial investment
initial_investment=1000000

#We got the percentages of our investment that goes into every stock
Equal_allocation_percentage_Nifty_Index=(initial_investment/nifty_value_lakhs)*100
Equal_allocation_percentage_Nifty_Index
type(Equal_allocation_percentage_Nifty_Index)

#cagr
begin_Nifty_Index=Equal_allocation_percentage_Nifty_Index. iloc[0]
final_Nifty_Index=Equal_allocation_percentage_Nifty_Index. iloc[515]
cagr_Nifty_Index=(((final_Nifty_Index/begin_Nifty_Index)**(1/2))-1)*100
cagr_Nifty_Index

type(cagr_Nifty_Index)
cagr_Nifty_Index = cagr_Nifty_Index.values.tolist()
cagr_Nifty_Index
type(cagr_Nifty_Index)
cagr_Nifty_Index=cagr_Nifty_Index[0]
cagr_Nifty_Index

#Daily returns
Equal_allocation_percentage_Nifty_Index
value_on_t=Equal_allocation_percentage_Nifty_Index
value_on_day_minusone=Equal_allocation_percentage_Nifty_Index-1
daily_returns_Nifty_Index=(value_on_t/value_on_day_minusone)-1
daily_returns_Nifty_Index

#volatility:
volatality_Nifty_Index=((np.std(daily_returns_Nifty_Index))**(1/252))*100
volatality_Nifty_Index

type(volatality_Nifty_Index)
volatality_Nifty_Index = volatality_Nifty_Index.values.tolist()
volatality_Nifty_Index
type(volatality_Nifty_Index)
volatality_Nifty_Index=volatality_Nifty_Index[0]
volatality_Nifty_Index

#Sharpe Ratio
Sharpe_Ratio_Nifty_Index=(np.mean(daily_returns_Nifty_Index)/np.std(daily_returns_Nifty_Index))**1/252
Sharpe_Ratio_Nifty_Index

type(Sharpe_Ratio_Nifty_Index)
Sharpe_Ratio_Nifty_Index = Sharpe_Ratio_Nifty_Index.values.tolist()
Sharpe_Ratio_Nifty_Index
type(Sharpe_Ratio_Nifty_Index)
Sharpe_Ratio_Nifty_Index=Sharpe_Ratio_Nifty_Index[0]
Sharpe_Ratio_Nifty_Index

###########################################################################################
df = pd.DataFrame({
   'CAGR %': [cagr_Benchmark_Strategy,cagr_Sample_Strategy,cagr_Nifty_Index],
   'Volatility %': [volatality_Benchmark_Strategy,volatality_Sample_Strategy,volatality_Nifty_Index],
   'Sharpe':[Sharpe_Ratio_Benchmark_Strategy,Sharpe_Ratio_Sample_Strategy,Sharpe_Ratio_Nifty_Index]
   }, index=['Equal Alloc Buy Hold','Nifty','Performance_Strat'])

################################################ Output ######################################
print(df)
lines = df.plot.line()




