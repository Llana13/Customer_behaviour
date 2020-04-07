'''Feature Engineering'''

import pandas as pd

mon = pd.read_csv(r'data/monday.csv',sep=';')
tue = pd.read_csv(r'data/tuesday.csv',sep=';')
wed = pd.read_csv(r'data/wednesday.csv',sep=';')
thu = pd.read_csv(r'data/thursday.csv',sep=';')
fri = pd.read_csv(r'data/friday.csv',sep=';')

mon['day'] = 'mon'
tue['day'] = 'tue'
wed['day'] = 'wed'
thu['day'] = 'thu'
fri['day'] = 'fri'

week = [mon, tue, wed, thu, fri]
revenues = {'fruit':4,'spices':3,'dairy':5,'drinks':6,'checkout':0}
for day in week:
    day['timestamp'] = pd.to_datetime(day['timestamp'])
    day['date'] = day['timestamp'].dt.date
    day['hour'] = day.loc[:,'timestamp'].dt.hour
    day['minute'] = day.loc[:,'timestamp'].dt.minute
    day['revenue'] = day['location'].map(revenues)

# Create a week dataframe
df = pd.concat(week,ignore_index=True)

##### Creates Transitions Probability Matrix #####

df_trans_prob = df[['date','customer_no','location','timestamp']].sort_values(by=['date','customer_no']).groupby(['date','customer_no']).sum()

def create_transition_col(move):
    '''Create a column with the number of times certain move the customer does'''
    df_trans_prob[move] = pd.Series
    for x in range(len(df_trans_prob['location'])):
        if move in df_trans_prob['location'][x]:
            df_trans_prob[move][x] = df_trans_prob['location'][x].count(move)
        else: df_trans_prob[move][x] = 0

# All posibles moves a customer can do
list_of_transitions = ['dairycheckout','dairyspices','dairydrinks','dairyfruit','spicesdairy','spicescheckout','spicesdrinks','spicesfruit','drinkscheckout','drinksspices','drinksdairy','drinksfruit','fruitcheckout','fruitspices','fruitdairy','fruitdrinks']

# Create one column for each possible move
for x in list_of_transitions:
    create_transition_col(x)

##### Creates Transitions DataFrame #####

# Insert a space after each location, and then summing them to get a string with each location
for word in range(len(df['location'])):
    df['location'][word] = df['location'][word] + ' '

df_trans_prob['location_list'] = df[['date','customer_no','location','timestamp']].sort_values(by=['date','customer_no']).groupby(['date','customer_no']).sum()

for i in range(len(df_trans_prob['location'])):
    df_trans_prob['location_list'][i] = df_trans_prob['location_list'][i].strip()
    df_trans_prob['location_list'][i] = df_trans_prob['location_list'][i].replace('  ',' ')
    df_trans_prob['location_list'][i] = df_trans_prob['location_list'][i].split() # Convert string to list

# Remove unnecesary spaces
for i in range(len(df)):
    df['location'][i] = df['location'][i].strip()

# Returns a df with time spent in the shop by customer and day
semana = ['mon','tue','wed','thu','fri']
time_in = {}
for dia in semana:
    time_in[dia] = {}
    for Id in list(df['customer_no'].unique()):
        temp = df[(df['customer_no']==Id) & (df['day']==dia)].sort_values(by=['date','customer_no'])
        temp.reset_index(inplace=True)
        time1 = temp['timestamp'].diff().sum()
        time_in[dia][Id] = time1
df_time_in = pd.DataFrame.from_dict(time_in)

total_mvs_dairy = df_trans_prob['dairycheckout'].sum() + df_trans_prob['dairyspices'].sum() + df_trans_prob['dairydrinks'].sum() + df_trans_prob['dairyfruit'].sum()
total_mvs_spices = df_trans_prob['spicescheckout'].sum() + df_trans_prob['spicesdairy'].sum() + df_trans_prob['spicesdrinks'].sum() + df_trans_prob['spicesfruit'].sum()
total_mvs_drinks = df_trans_prob['drinkscheckout'].sum() + df_trans_prob['drinksdairy'].sum() + df_trans_prob['drinksspices'].sum() + df_trans_prob['drinksfruit'].sum()
total_mvs_fruit = df_trans_prob['fruitcheckout'].sum() + df_trans_prob['fruitdairy'].sum() + df_trans_prob['fruitspices'].sum() + df_trans_prob['fruitdrinks'].sum()

# Probabilities of each possible move into a DataFrame
data_prob_trans_mat = {'dairy':[0,df_trans_prob['dairyspices'].sum()/total_mvs_dairy,df_trans_prob['dairydrinks'].sum()/total_mvs_dairy,df_trans_prob['dairyfruit'].sum()/total_mvs_dairy,df_trans_prob['dairycheckout'].sum()/total_mvs_dairy],
                       'spices':[df_trans_prob['spicesdairy'].sum()/total_mvs_spices,0,df_trans_prob['spicesdrinks'].sum()/total_mvs_spices,df_trans_prob['spicesfruit'].sum()/total_mvs_spices,df_trans_prob['spicescheckout'].sum()/total_mvs_spices],
                       'drinks':[df_trans_prob['drinksdairy'].sum()/total_mvs_drinks,df_trans_prob['drinksspices'].sum()/total_mvs_drinks,0,df_trans_prob['drinksfruit'].sum()/total_mvs_drinks,df_trans_prob['drinkscheckout'].sum()/total_mvs_drinks],
                       'fruit':[df_trans_prob['fruitdairy'].sum()/total_mvs_fruit,df_trans_prob['fruitspices'].sum()/total_mvs_fruit,df_trans_prob['fruitdrinks'].sum()/total_mvs_fruit,0,df_trans_prob['fruitcheckout'].sum()/total_mvs_fruit]
                       }
prob_matrix = pd.DataFrame(data= data_prob_trans_mat,index=[['dairy','spices','drinks','fruit','checkout']])
prob_matrix.to_csv(r'data/prob_matrix.csv',index=False)

# Create first location column
df_trans_prob['first_location'] = pd.Series
for lo in range(len(df_trans_prob['location_list'])):
    df_trans_prob['first_location'][lo] = df_trans_prob['location_list'][lo][0]

# Probability of each location being the first
dairy1=drinks1=fruit1=spices1 = 0
for location in df_trans_prob['first_location']:
    if location =='dairy':
        dairy1 += 1
    elif location =='drinks':
        drinks1 += 1
    elif location =='fruit':
        fruit1 += 1
    else: spices1 += 1

total = dairy1+drinks1+spices1+fruit1
first_location_prob = pd.DataFrame(data={'dairy':[dairy1/total],'drinks':[drinks1/total],'fruit':[fruit1/total],'spices':[spices1/total]})
first_location_prob.to_csv(r'data/first_location_prob.csv',index=False)
