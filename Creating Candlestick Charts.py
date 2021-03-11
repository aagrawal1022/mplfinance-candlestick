#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install mplfinance
#!pip install yfinance


# In[2]:


#importing necessay library
import yfinance as yf
import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt 


# In[3]:


data=yf.Ticker('MUTHOOTFIN.NS')


# https://in.finance.yahoo.com/quote/MUTHOOTFIN.NS?p=MUTHOOTFIN.NS&.tsrc=fin-srch 
# 
# Muthooth Finance Stock has been visualized in this code, we can just get the symbol and put it in Ticker and run whole code
# for similar outcome
# 
# Ticker returns class 'yfinance.ticker.Ticker' of the data where all history,financial,etc are present

# In[18]:


name=data.info['longName'] #Saving company name for using while plotting
save=data.info['shortName'] #Saving to downlad the plot
data.info#to get information about all the data


# In[5]:


#importing historical data of stock with maximum avilable
stock_data=data.history(period='max')
#data is retured as pandas dataframe
stock_data.head()
#DATE is set as an index but mplfinance accepts date column in datetime format whereas it is given in object type.


# In[6]:


#Resetting index to none
stock_data.reset_index(inplace=True)
stock_data.columns


# In[7]:


stock_data.Date=pd.to_datetime(stock_data.Date)
stock_data.info()


# Now Date Column is convereted into Datetime datatype.
# 
# Now setting it back to index

# In[8]:


stock=stock_data.set_index('Date')
stock.head()


# In[9]:


stock.info()


# In[10]:


#Function to save figure
import time,os
def figsave(horizan):
    if os.path.exists('{}_{}.png'.format(save,horizan)):
        fname='{}_{}_{}.png'.format(save,horizan,int(time.time()))
    else:
        fname='{}_{}.png'.format(save,horizan)
    return fname
        


# In[11]:


#Full Historical Chart
mpf.plot(stock,volume=True,type='candle',
        #savefig=dict(fname=figsave("full"),dpi=1200)
        )


# In[12]:


mpf.plot(stock['2020-03'],
         volume=True,
         tight_layout=True,
         #savefig=dict(fname=figsave("thisMonth"),dpi=1200)
        )


# In[13]:


import datetime
x=datetime.datetime.now()
y=str(x.year-1)+'-'+str(x.strftime("%m"))
z=str(x.year)+'-'+str(int(x.strftime("%m"))-1)


# In[14]:


#Last one year chart
s  = mpf.make_mpf_style(base_mpf_style='charles',mavcolors=['#1f77b4','#ff7f0e','#2ca02c'])
mpf.plot(stock[y:],
         volume=True,
         type='candle',
        figratio=(24,10),
         mav=(20,50,100),
         style= s,
         ylabel='Price (₹)',
         title=name,
         ylabel_lower='Traded\nVolume',
         tight_layout=False,
         #savefig=dict(fname=figsave("Year"),dpi=1200)
         #show_nontrading=True if needed to show trading day gaps
        )


# In[15]:


#Last One Month
s  = mpf.make_mpf_style(base_mpf_style='charles',mavcolors=['#1f77b4','#ff7f0e','#2ca02c'])
mpf.plot(stock[z:],
         volume=True,
         type='candle',
        figratio=(24,10),
         mav=(20,50,100),
         style= s,
         ylabel='Price (₹)',
         title=name,
         ylabel_lower='Traded\nVolume',
         tight_layout=False,
         #savefig=dict(fname=figsave("Month"),dpi=1200)
         #show_nontrading=True if needed to show trading day gaps
        )


# # To Save the figure plotted just remove # from savefig (given in all plot ) and run the code , It will not display plot on jyupter notebook but will save in current directory.

# To save while displaying, currently inprogress therefore code will be updated once its done.
