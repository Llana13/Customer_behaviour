import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from tqdm import tqdm
from collections import defaultdict
import random
import time

mon = pd.read_csv(r'/home/alex/Projects/Week8/supermarket/data/monday.csv',sep=';')
tue = pd.read_csv(r'/home/alex/Projects/Week8/supermarket/data/tuesday.csv',sep=';')
wed = pd.read_csv(r'/home/alex/Projects/Week8/supermarket/data/wednesday.csv',sep=';')
thu = pd.read_csv(r'/home/alex/Projects/Week8/supermarket/data/thursday.csv',sep=';')
fri = pd.read_csv(r'/home/alex/Projects/Week8/supermarket/data/friday.csv',sep=';')

# Feature Engineering
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
for x in tqdm(list_of_transitions):
    create_transition_col(x)

# Returns a df with time spent in the shop by customer and day
semana = ['mon','tue','wed','thu','fri']
time_in = {}
for dia in tqdm(semana):
    time_in[dia] = {}
    for Id in list(df['customer_no'].unique()):
        temp = df[(df['customer_no']==Id) & (df['day']==dia)].sort_values(by=['date','customer_no'])
        temp.reset_index(inplace=True)
        time1 = temp['timestamp'].diff().sum()
        time_in[dia][Id] = time1
df_time_in = pd.DataFrame.from_dict(time_in)

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

### Transitions Probability Matrix ###
total_mvs_dairy = df_trans_prob['dairycheckout'].sum()+df_trans_prob['dairyspices'].sum()+df_trans_prob['dairydrinks'].sum()+df_trans_prob['dairyfruit'].sum()
total_mvs_spices = df_trans_prob['spicescheckout'].sum()+df_trans_prob['spicesdairy'].sum()+df_trans_prob['spicesdrinks'].sum()+df_trans_prob['spicesfruit'].sum()
total_mvs_drinks = df_trans_prob['drinkscheckout'].sum()+df_trans_prob['drinksdairy'].sum()+df_trans_prob['drinksspices'].sum()+df_trans_prob['drinksfruit'].sum()
total_mvs_fruit = df_trans_prob['fruitcheckout'].sum()+df_trans_prob['fruitdairy'].sum()+df_trans_prob['fruitspices'].sum()+df_trans_prob['fruitdrinks'].sum()

# Probability of changing location
sns.heatmap(prob_matrix,cmap='BuPu')

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

### Function definition for simulation functions ###
def set_loc(first_move):
    '''
    Set loc variable to the location where the customer is
    '''
    if first_move == 'd':
        x = 'dairy'
    elif first_move == 'r':
        x = 'drinks'
    elif first_move == 's':
        x = 'spices'
    else: x = 'fruit'
    return x

def location_prob_list(loc):
    ''''
    Create a list with location*probability for any non-first location
    '''
    move_prob_list = int(prob_matrix[loc][0]*100)*'d'+int(prob_matrix[loc][1]*100)*'s'+int(prob_matrix[loc][2]*100)*'r'+int(prob_matrix[loc][3]*100)*'f'+int(prob_matrix[loc][4]*100)*'c'
    return move_prob_list

def set_loc_c(move):
    ''''
    Set loc variable to the location where the customer is but including 'checkout'
    '''
    if move == 'd':
        x = 'dairy'
    elif move == 'r':
        x = 'drinks'
    elif move == 's':
        x = 'spices'
    elif move == 'f':
        x = 'fruit'
    else: x = 'checkout'
    return x

def full_simulation():
    '''
    Simulates a customer behaviour in the supermarket
    '''
    # list of location*its probability for the first location
    first_location_prob_list = int(first_location_prob['dairy']*100)*'d'+int(first_location_prob['drinks']*100)*'r'+int(first_location_prob['fruit']*100)*'f'+int(first_location_prob['spices']*100)*'s'

    # randomly choose from the list of locations
    first_move = random.choice(first_location_prob_list)

    loc = set_loc(first_move)

    while loc != 'checkout':

        print('Customer is in: ',loc)
        move_prob_list = location_prob_list(loc)
        move = random.choice(move_prob_list)
        loc = set_loc_c(move)
        # Time each customer spends on each section
        if loc == 'dairy':
            time.sleep(1)
        elif loc == 'spices':
            time.sleep(2)
        elif loc == 'drinks':
            time.sleep(3)
        else: time.sleep(4)
    else: print('Customer left')

def part_simulation(first_location):
    '''
    Simulates a customer behaviour in the supermarket given a first location
    '''
    #print('First location is: ',first_location)
    loc = first_location
    while loc != 'checkout':

        print('Customer is in: ',loc)
        move_prob_list = location_prob_list(first_location)
        move = random.choice(move_prob_list)
        loc = set_loc_c(move)
        # Time each customer spends on each section
        if loc == 'dairy':
            time.sleep(1)
        elif loc == 'spices':
            time.sleep(2)
        elif loc == 'drinks':
            time.sleep(3)
        else: time.sleep(4)
    else: print('Customer left')
