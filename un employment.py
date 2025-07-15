import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import datetime as dt
import calendar
import plotly.graph_objects as go
data=pd.read_csv(r"C:\Users\shamn\Downloads\UNEMPLOYMENT ANALYSIS WITH PYTHON\Unemployment_Rate_upto_11_2020.csv")
# print(data)
# print(data.head())
# print(data.tail())
#update columns names
data.columns=["State","date","Frequency"," Estimated Unemployment Rate","Estimated Employed ","Estimated Labour Participation Rate","  Region","longitude","latittude"]
# print(data.tail())
# print(data.shape)
print(data.columns)
# print(data.describe)
# print(data.isnull().sum())
# print(data.duplicated().any())

print(data.State.value_counts())
data['date'] = pd.to_datetime(data['date'],dayfirst=True)
#extracting month from date attribute

data['month_int'] = data['date'].dt.month
# print(data.head())
data['month']= data['month_int'].apply(lambda x: calendar.month_abbr[x])
print(data.head())

# #numeric date gruoped by months

# # data['month']= pd.to_datetime(data['month'])# convert month colomn to datetimr type
# # IND=data.groupby(data['month'].dt.month)[["Calculated Unemloyment rate ","Calculated employed ","calculated labour participation rate"]].mean()
try:

    IND= data.groupby('month')[["Estimated Unemployment Rate","Estimated Employed ","Estimated Labour Participation Rate"]].mean().reset_index()
    print(IND.head())
except KeyError as e:
    print(f"Error: {e}")
   
   
if 'IND' in locals():
    month=IND.month
    Unemloyment_rate=IND[" Estimated Unemployment Rate"]
    Labour_Participation_Rate=IND["Estimated Labour Participation Rate"]
    fig= go.Figure()
    
    fig.add_trace(go.Bar(x = month, y= Unemloyment_rate,name = " Unemployment Rate"))
    fig.add_trace(go.Bar(x = month, y= Labour_Participation_Rate,name = " Labour Participation Rate "))
    fig.update_layout(title=" Unemployment Rate and   Labour Participation Rate",
                       xaxis={"categoryorder":"array","categoryarray":["jan","Feb","Mar","Apr","May","Jun","jul","Aug","Sep","Oct"]})
    fig.show()
else:
    print("IND is not defined due to keyerror: ")

# print(IND.head())

# print(IND)
#barplot
# month=IND.month
# Unemloyment_rate=IND[" Estimated Unemployment Rate"]
# labour_participation_rate=IND["Estimated Labour Participation Rate"]
# fig= go.Figure()

# fig.add_trace(go.Bar(x = month, y= Unemloyment_rate,name = " Unemloyment rate"))
# fig.add_trace(go.Bar(x = month, y= labour_participation_rate,name = "participation rate "))
# fig.update_layout(title=" Unemloyment rate and calculated labour participation rate", xaxis={"categoryorder":"array","categoryarray":{"jan","Feb","Mar","Apr","May","Jun","jul","Aug","Sep","Oct"}})
# print(fig.show())

                  




