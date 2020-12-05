#!/usr/bin/env python
# coding: utf-8

# In[137]:


#Importing the library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[261]:


#Reading the required files
Denco_Corp=pd.read_csv('CustomerPartSales.csv')


# In[139]:


Denco_Corp.head()


# In[140]:


Denco_Corp.tail()


# In[141]:


# identifying null values
Denco_Corp.isnull().sum()
# There is no null values in Data set


# In[142]:


# Describe the data
Denco_Corp.describe()


# In[143]:


# identifying the unique values
Denco_Corp['CUSTNAME'].unique()


# In[144]:


Denco_Corp['REGION'].unique()


# In[145]:


Denco_Corp['PARTNUM'].unique()


# In[146]:


# Total rows to visible in data
pd.set_option('display.Max_rows',None)


# In[147]:


Denco_Corp


# In[148]:


# Checking the data type
Denco_Corp.dtypes


# In[149]:


# Total number of rows and columns
Denco_Corp.shape


# In[150]:


# Identifying the duplicate rows in data
duplicate_rows_df = Denco_Corp.duplicated().sum()
print("number of duplicate rows:", duplicate_rows_df)


# # Visualization

# In[151]:


sns.boxplot(x=Denco_Corp['COST'])


# In[152]:


sns.boxplot(x=Denco_Corp['REVENUE'])


# In[153]:


sns.boxplot(x=Denco_Corp['MARGIN'])


# In[154]:


c= Denco_Corp.corr()
sns.heatmap(c,cmap='BrBG',annot=True)
c


# In[155]:


sns.scatterplot(Denco_Corp['PARTNUM'], Denco_Corp['COST'])


# In[156]:


Denco_Corp['REGION'].unique()


# In[157]:


Central = Denco_Corp[Denco_Corp['REGION']=='02-Central']
Central


# In[158]:


East = Denco_Corp[Denco_Corp['REGION']=='01-East']
East


# In[159]:


Canada_Direct = Denco_Corp[Denco_Corp['REGION']=='07-Canada Direct']
Canada_Direct


# In[160]:


x_Export = Denco_Corp[Denco_Corp['REGION']=='9x-Export']
x_Export


# In[161]:


House = Denco_Corp[Denco_Corp['REGION']=='05-House']
House


# In[162]:


China = Denco_Corp[Denco_Corp['REGION']=='09-China']
China


# #                                        Answering the Given Questions

# In[163]:


# Task 1. Who are the most loyal customers?
# Task 2. Which customers contribute the most to their revenue?
# Task 3. What part numbers bring in to significant portion of revenue?
# Task 4. What parts have the highest profit margin?


# In[164]:


REVENUE = Denco_Corp['REVENUE']
REVENUE


# In[165]:


REVENUE.max()


# In[166]:


REVENUE.min()


# In[167]:


REVENUE.mean()


# In[168]:


# i am taking the average is cut-off point to devide the loyal customers and non-loyal customers.


# In[169]:


loyal_customers = Denco_Corp[Denco_Corp['REVENUE'] > 31376.21962020313]


# In[170]:


loyal_customers


# In[171]:


px.histogram(loyal_customers,'CUSTNAME','REVENUE',height=700,width=1000)


# In[172]:


px.histogram(loyal_customers,'CUSTNAME','COST',height=700,width=1000)


# In[173]:


px.histogram(loyal_customers,'CUSTNAME','MARGIN',height=700,width=1000)


# In[174]:


TRIUMPH_INSULATION = Denco_Corp[Denco_Corp['CUSTNAME']=='TRIUMPH INSULATION']
TRIUMPH_INSULATION['REVENUE'].sum()


# In[175]:


loyal_customers['REVENUE'].max()


# In[176]:


loyal_customers[loyal_customers['REVENUE']==29800976.28]


# In[177]:


TRIUMPH_INSULATION


# In[178]:


TRIUMPH_INSULATION['COST'].sum()


# In[179]:


TRIUMPH_INSULATION['MARGIN'].sum()


# In[180]:


# here i identified the Most loyal customer is TRIUMPH INSULATION.This Customer generates the revenue is:- 35592531.239999995
# and also the total cost is:- 22621006.61 
# and total Margin is :- 12971524.63


# In[181]:


CORNING_SHARED_SERVICES = Denco_Corp[Denco_Corp['CUSTNAME']=='CORNING SHARED SERVICES']
CORNING_SHARED_SERVICES['REVENUE'].sum()


# In[182]:


CORNING_SHARED_SERVICES['COST'].sum()


# In[183]:


CORNING_SHARED_SERVICES['MARGIN'].sum()


# In[184]:


# here i identified the Most loyal Customer is CORNING SHARED SERVICES.This Customer generates the revenue is:- 12843518.780000001
# and also the total cost is :- 2077213.24
# and total Margin is :- 10766305.540000001


# In[185]:


(10766305.540000001 / 12843518.780000001) # CORNING SHARED SERVICES is generates the 83% profit (formula is Margin / revenue)


# In[186]:


(12971524.63 / 35592531.239999995) #TRIUMPH INSULATION is generates the 36% profit (formula is Margin / revenue)


# In[187]:


# These 2 coustomers are most loyal Customers. Here i identified CORNING SHARED SERVICES is most loyal Customer comparing to TRIUMPH INSULATION 
# Reason:- TRIUMPH INSULATION buying cost is 2,26,21,006.61, the profit is 1,29,71,524.63 and revenue is 3,55,92,531.239999995
# Reason:- CORNING SHARED SERVICES buying cost is 20,77,213.24, the profit is 10,76,6305.540000001 and revue is 1,28,43,518.780000001
# comparing to both CORNING SHARED SERVICES buying cost is low and revenue is high approxmately 6times high 
# The TRIUMPH INSULATION is approxmately just double to the cost
# so i am take the decision is CORNING SHARED SERVICES is Most loyal Customer.


# In[188]:


loyal_customers


# In[189]:


loyal_customers['REVENUE'].max()


# In[190]:


loyal_customers[loyal_customers['REVENUE'] >= 29800976.28]


# In[596]:


px.histogram(loyal_customers,'PARTNUM','REVENUE',color='PARTNUM',barmode='group',height=700,width=2000)


# In[598]:


px.scatter(loyal_customers,'REVENUE','PARTNUM',color='PARTNUM')


# In[192]:


loyal_customers['REVENUE'].max()


# In[193]:


loyal_customers[loyal_customers['REVENUE']==29800976.28]


# In[194]:


loyal_customers[loyal_customers['PARTNUM']==733648000]


# In[195]:


# sorting the values of revenue ex:- df.sort_values(by=['name', 'score'], ascending=[False, True])
Sortedloyal_customers=loyal_customers.sort_values(by=['REVENUE','PARTNUM'],ascending=[False,True])
Sortedloyal_customers


# In[196]:


Sortedloyal_customers=Sortedloyal_customers.set_index('PARTNUM')


# In[197]:


Sortedloyal_customers.sort_values(by='PARTNUM', ascending=True)


# In[198]:


dummy=Sortedloyal_customers.loc[734370000]
dummy['REVENUE'].sum()


# In[199]:


dummy=Sortedloyal_customers.loc[733648000]
dummy['REVENUE'].sum()


# In[200]:


dummy=Sortedloyal_customers.loc[735602000]
dummy['REVENUE'].sum()


# In[201]:


Sortedloyal_customers=Sortedloyal_customers.reset_index(level='PARTNUM')


# In[202]:


px.histogram(Sortedloyal_customers,'PARTNUM','MARGIN',barmode='group',height=700,width=1000)


# In[203]:


Sortedloyal_customers=Sortedloyal_customers.set_index('PARTNUM')


# In[204]:


dummy=Sortedloyal_customers.loc[734370000]
dummy['MARGIN'].sum()


# In[205]:


dummy=Sortedloyal_customers.loc[733648000]
dummy['MARGIN'].sum()


# In[206]:


dummy=Sortedloyal_customers.loc[735602000]
dummy['MARGIN'].sum()


# In[207]:


Sortedloyal_customers.sort_values(by='MARGIN', ascending=False)


# In[ ]:





# In[ ]:





# In[208]:


# What part numbers bring in to significant portion of revenue?
#3,00,50,020.380000003 --- PARTNUM(733648000)
#1,56,52,151.350000001 --- PARTNUM(735602000)
#1,26,41,200.0         --- PARTNUM(734370000)


# In[209]:


# What parts have the highest profit margin?
#1,09,88,584.309999999 --- PARTNUM(733648000)
#1,02,02,203.26 --- PARTNUM(735602000)
#1,06,27,732.81         --- PARTNUM(734370000)


# In[210]:


# Task 1. Who are the most loyal customers?
## ANS to Task1. Here i identified "CORNING SHARED SERVICES" and "TRIUMPH INSULATION" These are the most loyal customers.


# Task 2. Which customers contribute the most to their revenue?
## ANS to Task2. Here i identified the "CORNING SHARED SERVICES" are spending the revenue 1,28,43,518.780000001
## & "TRIUMPH INSULATION" are spending the revenue is 3,55,92,531.239999995.
## So these both customers contribute the most to their revenue.  


# Task 3. What part numbers bring in to significant portion of revenue?
## ANS to Task3. PARTNUM(733648000) ,PARTNUM(735602000), PARTNUM(734370000)these part numbers bring in to significant portion of revenue.


# Task 4. What parts have the highest profit margin?
## ANS to Task4. PARTNUM(733648000) ,PARTNUM(735602000), PARTNUM(734370000)these parts have the highest profit margin.


# # Other Fields to Derivative:

# In[417]:


# MARGIN_PERC
# NUM_CUSTOMER_BUYING_THIS_PART
# NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER
# TOTAL_REVENUE_FROM_THIS_PART
# SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART
# TOTAL_REVENUE_FROM_THIS_CUST
# SHARE_OF_TOTALREVENUE_FROM_THIS_CUST
# SHARE_OF_REVENUE_OF_THIS_PART_FROM_ALLPURCHASES_OF_THIS_CUSTOMER
# SHARE_OF_REVENUE_OF_THIS_CUSTOMER_FROM_ALLSALES_OF_THIS_PART
# NUM_TRANSACTION_FOR_THIS_PARTNUM
# NUM_TRANSACTION_FOR_THIS_CUSTNAME


# In[421]:


# To know the MARGIN_PERC
Denco_Corp['MARGIN_PERC']=(Denco_Corp['MARGIN']/Denco_Corp['REVENUE'])*100


# In[422]:


Denco_Corp.head()


# In[585]:


# To Know the NUM_CUSTOMER_BUYING_THIS_PART 
NUM_CUSTOMER_BUYING_THIS_PART=Denco_Corp.groupby(by=['CUSTNAME','PARTNUM'])['CUSTNAME'].size()


# In[586]:


NUM_CUSTOMER_BUYING_THIS_PART=NUM_CUSTOMER_BUYING_THIS_PART.to_frame()


# In[587]:


NUM_CUSTOMER_BUYING_THIS_PART.head()


# In[588]:


NUM_CUSTOMER_BUYING_THIS_PART.rename(columns={'CUSTNAME': 'NUM_CUSTOMER_BUYING_THIS_PART'}, inplace=True)


# In[589]:


NUM_CUSTOMER_BUYING_THIS_PART.head()


# In[437]:


# Denco_Corp=Denco_Corp.sort_values(by=['PARTNUM'],ascending=[True])


# In[448]:


# Denco_Corp=Denco_Corp.drop(['NUM_CUSTOMER_BUYING_THIS_PART'], axis=1)


# In[449]:


Denco_Corp.head()


# In[590]:


# To know the NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER
NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER=Denco_Corp.groupby(by=['PARTNUM','CUSTNAME'])['PARTNUM'].size()


# In[591]:


NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER=NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER.to_frame()


# In[592]:


NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER.head()


# In[593]:


NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER.rename(columns={'PARTNUM': 'NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER'}, inplace=True)


# In[594]:


NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER.head()


# In[455]:


# To know the TOTAL_REVENUE_FROM_THIS_PART
TOTAL_REVENUE_FROM_THIS_PART=Denco_Corp.groupby(by='PARTNUM')['REVENUE'].sum()


# In[457]:


TOTAL_REVENUE_FROM_THIS_PART=TOTAL_REVENUE_FROM_THIS_PART.to_frame()


# In[458]:


TOTAL_REVENUE_FROM_THIS_PART.head()


# In[459]:


TOTAL_REVENUE_FROM_THIS_PART.rename(columns={'REVENUE': 'TOTAL_REVENUE_FROM_THIS_PART'}, inplace=True)


# In[460]:


TOTAL_REVENUE_FROM_THIS_PART.head()


# In[466]:


# Know the TotalMargin
TotalMargin=Denco_Corp.groupby(by='PARTNUM')['MARGIN'].sum()


# In[467]:


TotalMargin.head()


# In[468]:


TotalMargin=TotalMargin.to_frame()


# In[469]:


TotalMargin.head()


# In[472]:


TotalMargin.rename(columns={'MARGIN': 'TotalMargin'}, inplace=True)


# In[473]:


TotalMargin.head()


# In[484]:


# know the SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART
SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART = TOTAL_REVENUE_FROM_THIS_PART['TOTAL_REVENUE_FROM_THIS_PART']-TotalMargin['TotalMargin']


# In[486]:


SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART.head()


# In[487]:


SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART=SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART.to_frame()


# In[488]:


SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART.head()


# In[491]:


SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART.rename(columns={0: 'SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART'}, inplace=True)


# In[492]:


SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART.head()


# In[493]:


# To know the TOTAL_REVENUE_FROM_THIS_CUST
TOTAL_REVENUE_FROM_THIS_CUST=Denco_Corp.groupby(by='CUSTNAME')['REVENUE'].sum()


# In[494]:


TOTAL_REVENUE_FROM_THIS_CUST=TOTAL_REVENUE_FROM_THIS_CUST.to_frame()


# In[496]:


TOTAL_REVENUE_FROM_THIS_CUST.head()


# In[497]:


TOTAL_REVENUE_FROM_THIS_CUST.rename(columns={'REVENUE': 'TOTAL_REVENUE_FROM_THIS_CUST'}, inplace=True)


# In[498]:


TOTAL_REVENUE_FROM_THIS_CUST.head()


# In[499]:


# Know the TotalMargin_CUST
TotalMargin_CUST=Denco_Corp.groupby(by='CUSTNAME')['MARGIN'].sum()


# In[502]:


TotalMargin_CUST=TotalMargin_CUST.to_frame()


# In[503]:


TotalMargin_CUST.rename(columns={'MARGIN': 'TotalMargin_CUST'}, inplace=True)


# In[504]:


TotalMargin_CUST.head()


# In[505]:


# To know the SHARE_OF_TOTALREVENUE_FROM_THIS_CUST
SHARE_OF_TOTALREVENUE_FROM_THIS_CUST = TOTAL_REVENUE_FROM_THIS_CUST['TOTAL_REVENUE_FROM_THIS_CUST']-TotalMargin_CUST['TotalMargin_CUST']


# In[506]:


SHARE_OF_TOTALREVENUE_FROM_THIS_CUST.head()


# In[508]:


SHARE_OF_TOTALREVENUE_FROM_THIS_CUST=SHARE_OF_TOTALREVENUE_FROM_THIS_CUST.to_frame()


# In[509]:


SHARE_OF_TOTALREVENUE_FROM_THIS_CUST.head()


# In[510]:


SHARE_OF_TOTALREVENUE_FROM_THIS_CUST.rename(columns={0: 'SHARE_OF_TOTALREVENUE_FROM_THIS_CUST'}, inplace=True)


# In[511]:


SHARE_OF_TOTALREVENUE_FROM_THIS_CUST.head()


# In[516]:


# To know the SHARE_OF_REVENUE_OF_THIS_PART_FROM_ALLPURCHASES_OF_THIS_CUSTOMER
SHARE_OF_REVENUE_OF_THIS_PART_FROM_ALLPURCHASES_OF_THIS_CUSTOMER=Denco_Corp.groupby(by=['PARTNUM','CUSTNAME'])['REVENUE'].sum()


# In[518]:


SHARE_OF_REVENUE_OF_THIS_PART_FROM_ALLPURCHASES_OF_THIS_CUSTOMER=SHARE_OF_REVENUE_OF_THIS_PART_FROM_ALLPURCHASES_OF_THIS_CUSTOMER.to_frame()


# In[520]:


SHARE_OF_REVENUE_OF_THIS_PART_FROM_ALLPURCHASES_OF_THIS_CUSTOMER.rename(columns={'REVENUE': 'SHARE_OF_REVENUE_OF_THIS_PART_FROM_ALLPURCHASES_OF_THIS_CUSTOMER'}, inplace=True)


# In[522]:


SHARE_OF_REVENUE_OF_THIS_PART_FROM_ALLPURCHASES_OF_THIS_CUSTOMER.head()


# In[523]:


# to know the SHARE_OF_REVENUE_OF_THIS_CUSTOMER_FROM_ALLSALES_OF_THIS_PART
SHARE_OF_REVENUE_OF_THIS_CUSTOMER_FROM_ALLSALES_OF_THIS_PART=Denco_Corp.groupby(by=['CUSTNAME','PARTNUM'])['REVENUE'].sum()


# In[524]:


SHARE_OF_REVENUE_OF_THIS_CUSTOMER_FROM_ALLSALES_OF_THIS_PART=SHARE_OF_REVENUE_OF_THIS_CUSTOMER_FROM_ALLSALES_OF_THIS_PART.to_frame()


# In[525]:


SHARE_OF_REVENUE_OF_THIS_CUSTOMER_FROM_ALLSALES_OF_THIS_PART.rename(columns={'REVENUE': 'SHARE_OF_REVENUE_OF_THIS_CUSTOMER_FROM_ALLSALES_OF_THIS_PART'}, inplace=True)


# In[526]:


SHARE_OF_REVENUE_OF_THIS_CUSTOMER_FROM_ALLSALES_OF_THIS_PART.head()


# In[572]:


# To know the NUM_TRANSACTION_FOR_THIS_PARTNUM
NUM_TRANSACTION_FOR_THIS_PARTNUM=Denco_Corp.groupby(by=['PARTNUM'])['PARTNUM'].count()


# In[573]:


NUM_TRANSACTION_FOR_THIS_PARTNUM=NUM_TRANSACTION_FOR_THIS_PARTNUM.to_frame()


# In[574]:


NUM_TRANSACTION_FOR_THIS_PARTNUM.rename(columns={'PARTNUM': 'NUM_TRANSACTION_FOR_THIS_PARTNUM'}, inplace=True)


# In[575]:


NUM_TRANSACTION_FOR_THIS_PARTNUM


# In[576]:


# To know the NUM_TRANSACTION_FOR_THIS_CUSTNAME
NUM_TRANSACTION_FOR_THIS_CUSTNAME=Denco_Corp.groupby(by=['CUSTNAME'])['CUSTNAME'].count()


# In[577]:


NUM_TRANSACTION_FOR_THIS_CUSTNAME=NUM_TRANSACTION_FOR_THIS_CUSTNAME.to_frame()


# In[580]:


NUM_TRANSACTION_FOR_THIS_CUSTNAME.rename(columns={'CUSTNAME': 'NUM_TRANSACTION_FOR_THIS_CUSTNAME'}, inplace=True)


# In[581]:


NUM_TRANSACTION_FOR_THIS_CUSTNAME.head()


# In[ ]:





# In[ ]:





# In[461]:


Denco_Corp.head()


# In[595]:


# df.to_csv(r'Path where you want to store the exported CSV file\File Name.csv').
# Exporting CSV files.
Denco_Corp.to_csv(r'C:\Users\DELL\Denco_Corp_with_MARGIN_PERC.csv')
NUM_CUSTOMER_BUYING_THIS_PART.to_csv(r'C:\Users\DELL\NUM_CUSTOMER_BUYING_THIS_PART.csv')
NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER.to_csv(r'C:\Users\DELL\NUM_PARTS_BOUGHT_BY_THIS_CUSTOMER.csv')
TOTAL_REVENUE_FROM_THIS_PART.to_csv(r'C:\Users\DELL\TOTAL_REVENUE_FROM_THIS_PART.csv')
SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART.to_csv(r'C:\Users\DELL\SHARE_OF_TOTAL_REVENUE_FROM_THIS_PART.csv')
TOTAL_REVENUE_FROM_THIS_CUST.to_csv(r'C:\Users\DELL\TOTAL_REVENUE_FROM_THIS_CUST.csv')
SHARE_OF_TOTALREVENUE_FROM_THIS_CUST.to_csv(r'C:\Users\DELL\SHARE_OF_TOTALREVENUE_FROM_THIS_CUST.csv')
SHARE_OF_REVENUE_OF_THIS_PART_FROM_ALLPURCHASES_OF_THIS_CUSTOMER.to_csv(r'C:\Users\DELL\SHARE_OF_REVENUE_OF_THIS_PART_FROM_ALLPURCHASES_OF_THIS_CUSTOMER.csv')
SHARE_OF_REVENUE_OF_THIS_CUSTOMER_FROM_ALLSALES_OF_THIS_PART.to_csv(r'C:\Users\DELL\SHARE_OF_REVENUE_OF_THIS_CUSTOMER_FROM_ALLSALES_OF_THIS_PART.csv')
NUM_TRANSACTION_FOR_THIS_PARTNUM.to_csv(r'C:\Users\DELL\NUM_TRANSACTION_FOR_THIS_PARTNUM.csv')
NUM_TRANSACTION_FOR_THIS_CUSTNAME.to_csv(r'C:\Users\DELL\NUM_TRANSACTION_FOR_THIS_CUSTNAME.csv')


# In[ ]:




