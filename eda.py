from collections import defaultdict
from customer_simulations import *

''' Exploratory Data Analysis'''

# Total number of customers during the week
cum = 0
for day in week:
    cum += day.customer_no.max()
cum

# Total number of customers by section
df[['customer_no','location']].groupby('location').count()
plt.hist(df['location'])

# Last location visited whitout buying anything
last_location = []
for name, group in df.sort_values(by=['day','customer_no','timestamp']).groupby(['day','customer_no']):
    last_location.append(group.iloc[-1]['location'])
not_buy = {'dairy':last_location.count('dairy'),'spices':last_location.count('spices'),'drinks':last_location.count('drinks'),'fruit':last_location.count('fruit')}
not_buy

# Total number of customers by section over time
plt.plot(df[['location','hour','customer_no']][df['location']=='dairy'].groupby('hour').sum(),label='Dairy')
plt.plot(df[['location','hour','customer_no']][df['location']=='spices'].groupby('hour').sum(),label='Spices')
plt.plot(df[['location','hour','customer_no']][df['location']=='fruit'].groupby('hour').sum(),label='Fruit')
plt.plot(df[['location','hour','customer_no']][df['location']=='drinks'].groupby('hour').sum(),label='Drinks')
plt.plot(df[['location','hour','customer_no']][df['location']=='checkout'].groupby('hour').sum(),label='Checkout')
plt.legend()

# Total number of customers at checkout over time
plt.plot(mon[['location','hour','customer_no']][mon['location']=='checkout'].groupby('hour').sum(),label='Monday')
plt.plot(tue[['location','hour','customer_no']][tue['location']=='checkout'].groupby('hour').sum(),label='Tuesday')
plt.plot(wed[['location','hour','customer_no']][wed['location']=='checkout'].groupby('hour').sum(),label='Wednesday')
plt.plot(thu[['location','hour','customer_no']][thu['location']=='checkout'].groupby('hour').sum(),label='Thursday')
plt.plot(fri[['location','hour','customer_no']][fri['location']=='checkout'].groupby('hour').sum(),label='Friday')
plt.legend()

# Total number of customers present in the supermarket over time

# Sum of customers by hour of the day
plt.plot(df[['day','hour','customer_no']].groupby('hour').count())
# Distribution of customers over the week and hour of the day
plt.figure(figsize=(12,8))
plt.plot(mon[['hour','customer_no']].groupby('hour').count(),label='Monday')
plt.plot(tue[['hour','customer_no']].groupby('hour').count(),label='Tuesday')
plt.plot(wed[['hour','customer_no']].groupby('hour').count(),label='Wednesday')
plt.plot(thu[['hour','customer_no']].groupby('hour').count(),label='Thursday')
plt.plot(fri[['hour','customer_no']].groupby('hour').count(),label='Friday')
plt.legend()
