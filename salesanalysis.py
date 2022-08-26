import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import pandas as pd
import numpy as np

df = pd.read_csv("Sales_April_2019.csv")
df2 = pd.read_csv("Sales_May_2019.csv")
df3 = pd.read_csv("Sales_June_2019.csv")
df4 = pd.read_csv("Sales_July_2019.csv")
df5 = pd.read_csv("Sales_August_2019.csv")
df6 = pd.read_csv("Sales_September_2019.csv")
df7 = pd.read_csv("Sales_October_2019.csv")
df8 = pd.read_csv("Sales_November_2019.csv")
df9 = pd.read_csv("Sales_December_2019.csv")
df10 = pd.read_csv("Sales_January_2019.csv")
df11 = pd.read_csv("Sales_February_2019.csv")
df12 = pd.read_csv("Sales_March_2019.csv")
list1 = [df , df2 , df3 , df4, df5 , df6, df7 , df8 , df9 , df10 , df11 , df12]

##for i in list1:
   ## print(i.head(5))
    ##print("--------------------------------------------")

md = pd.DataFrame()

for i in list1:
    md = pd.concat([md , i])
    
md.to_csv("all_data.csv" , index=False)

mdf = pd.read_csv("all_data.csv")
mdf = mdf.dropna()
##print(mdf.loc[mdf["Quantity Ordered"]=="Quantity Ordered"])
mdf = mdf.drop(mdf.index[mdf["Quantity Ordered"]=="Quantity Ordered"])
print(mdf.loc[mdf["Quantity Ordered"]=="Quantity Ordered"])
##finding which moonth had the highest sales
mdf["Month"] = mdf["Order Date"].str[0:2]
mdf["TotalSales"] = mdf["Quantity Ordered"].astype(str).astype(int) * mdf["Price Each"].astype(str).astype(float)
##print(mdf.iloc[:,2:9].head(20))
sales = mdf.groupby("Month").sum()

months = range(1,13)
mp.subplot(2 , 2, 1)
mp.plot(months , sales["TotalSales"] , marker="o")
mp.ylabel("Sales")
mp.xlabel("Month")
mp.title("Sales by month")
##mp.show()

def getcity(addr):
    return addr.split(",")[1]

def getcode(addr):
    return addr.split(",")[2].split(" ")[1]


mdf["City"] = mdf["Purchase Address"].apply(lambda xin : getcity(xin)+""+getcode(xin))
y1 = mdf.groupby("City").sum()
cities = [city for city,df in mdf.groupby("City")]
print(mdf.head())
mp.subplot(2,2,2)
mp.plot(cities , y1 , marker="o")
mp.xticks(fontsize = 5)
mp.title("Sales per state")
##mp.show()

mdf["Order Time"] = pd.to_datetime(mdf["Order Date"])
mdf["Hour"] = mdf["Order Time"].dt.hour
mdf["Hour"] = mdf["Order Time"].dt.minute
time1 = [t for t,df in mdf.groupby("Hour")]

mp.subplot(2 , 2 , 3)
mp.plot(  time1 ,mdf.groupby(["Hour"]).count())
mp.xlabel("Hours")
mp.xticks(time1 , fontsize=5)
mp.ylabel("Sales Rate")
mp.show()##best time to advertise