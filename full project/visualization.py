# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:52:27 2021

@author: guillaume
"""



import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_dt():
    global dt

    dt = pd.read_csv("D:\PythonProject/backup_1.csv",index_col=(0))

load_dt()


# =============================================================================
# Data visualization
# =============================================================================

# add an index col for the visualization part 

dt["idx"]=1

# plot 1 : bar plot of prices repartition

def plot_price():
    
    global dt

    price_group = dt.groupby(['price_range']).sum()
    price_group

    all_prices =[ prix for prix,df in dt.groupby('price_range')]

    fig = plt.bar(all_prices,price_group['idx'],log = True,color= "royalblue")

    plt.xticks(all_prices,rotation  =-60,size= 7 )
    plt.xlabel("video games price intervals (in £)")
    plt.ylabel("number(log10)")
    plt.title("Number of video games per interval")

    for bar in fig :
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    plt.show()

plot_price()

# plt.savefig('games_prices.png',bbox_inches="tight",dpi=450)


# =============================================================================
# bar plot of platforms proportions
# =============================================================================


def plot_plat():
    global dt
    platform_group = dt.groupby(['platform']).sum()

    all_platforms =[plat for plat,df in dt.groupby('platform')]

    fig = plt.bar(all_platforms,platform_group["idx"],log=True, color='royalblue')
    plt.xticks(all_platforms,rotation  ='vertical',size= 7 )
    plt.xlabel("platforms list")
    plt.ylabel("number of video games")
    plt.title("number of video games per platform")
    for bar in fig :
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
    plt.show()
    
plot_plat()

# plt.savefig('game_platgforms.png',bbox_inches="tight",dpi=450)

# =============================================================================
# # bar plot of the 10 most present game genres in datas 
# =============================================================================

def plot_10most():
    
    global dt
    n = 10

    sns.set_theme(style='darkgrid' )
    ax = sns.countplot(dt["category"], order=pd.value_counts(dt["category"]).iloc[:n].index.tolist(),palette="Set2")
    plt.xticks(rotation='vertical')
    plt.title('10 most present game categories')
    plt.show()

plot_10most()

# plt.savefig('10_most_present_genres.png',bbox_inches="tight",dpi=450)

# =============================================================================
# plot of prices statistics per platform
# =============================================================================

def plot_stats():
    global dt

    sub_data = dt[['platform','price']]

    sub_ps4 = sub_data[(sub_data['platform'] =="PS4" )]
    sub_one = sub_data[(sub_data['platform'] =="Xbox One" )]
    sub_switch = sub_data[(sub_data['platform'] =="Nintendo Switch" )]
    sub_3ds = sub_data[(sub_data['platform'] =="Nintendo 3DS" )]
    sub_pc = sub_data[(sub_data['platform'] =="PC" )]
    sub_ps5 = sub_data[(sub_data['platform'] =="PS5" )]
    sub_ps3 = sub_data[(sub_data['platform'] =="PS3" )]
    sub_x = sub_data[(sub_data['platform'] =="Xbox Series X" )]

    sub_data = pd.concat([sub_ps4,sub_one,sub_switch,sub_3ds,sub_pc,sub_ps5,sub_ps3,sub_x])

    sub_data.groupby('platform').describe()

    mean_price = sub_data.groupby("platform").mean()
    std_price = sub_data.groupby('platform').std()
    med_price = sub_data.groupby('platform').median()

    mean_price.columns = ["mean_price"]
    std_price.columns = ['std_price']
    med_price.columns = ['med_price']

    mean_price= list(mean_price['mean_price'])
    std_price = list(std_price['std_price'])
    med_price = list(med_price['med_price'])

    stats = pd.DataFrame(list(zip(mean_price,std_price,med_price)),
                     columns =['MEAN','STD','MEDIAN'])

    stats = stats.set_index(pd.Index(['Nintendo 3DS','Nintendo Switch','PC','PS3','PS4','PS5','Xbox One','Xbox Series X']))

    fig = stats.plot(kind='bar',subplots=True,figsize=(8,8),
           title='Mean, Std and Median price for each platform')
    
plot_stats()

#plt.savefig('desc_stats_price',bbox_inches="tight",dpi=450)


# =============================================================================
# pie chart of the disponibility 
# =============================================================================

def plot_disp():
    global dt
    #creating an empty col in the dataframe

    dt['']=""

    #plot

    fig1, ax1 = plt.subplots()

                    
    (dt.groupby('disponibilty').count()/dt.count()*100)[''].plot.pie(
                                                                             figsize=(6,6),
                                                                             autopct='%1.1f%%',
                                                                             fontsize=15,
                                                                             labels=("Available","Pre-order"),
                                                                             startangle=45, 
                                                                             pctdistance=0.85,
                                                                             colors=['#66b3ff','#ffcc99'],
                                                                             title='Proportion of games available immediatly and available for pre-order')
    #draw circle
    centre_circle = plt.Circle((0,0),0.7,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.show()
    
plot_disp()

#plt.savefig('proportion of game disponibility',bbox_inches="tight",dpi=450)
