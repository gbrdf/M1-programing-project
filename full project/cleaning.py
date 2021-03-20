
import pandas as pd

import re

import numpy as np

def load_dt():
    global dt

    dt = pd.read_csv("D:\PythonProject/backup_1.csv",index_col=(0))

load_dt()

## cleaning category

def clean_cat():
    global dt
    dt["category"] = dt["category"].str.replace("Kids &amp;","Kids,")
    dt["category"] = dt["category"].str.replace("Platfor","Platform")
    dt["category"] = dt["category"].str.replace("Platformm","Platform")
    dt["category"] = dt["category"].str.replace("Platformer","Platform")
    dt["category"] = dt["category"].str.replace("Third Person Shooter","TPS")
    dt["category"] = dt["category"].str.replace("Sci-Fi","SF")
    dt["category"] = dt["category"].str.replace("rcade","Arcade")
    dt["category"] = dt["category"].str.replace("baseball","Sports")
    dt = dt.dropna()

clean_cat()

# removing duplicates

def remove_dup():
    global dt
    dt["name"] = dt["name"].drop_duplicates()

    dt = dt.dropna()

remove_dup()

## cleaning platform

def clean_plat():
    global dt

    dt["platform"] = dt["platform"].str.replace("playstation 4|sony playstation 4","PS4",flags=re.IGNORECASE)
    dt["platform"] = dt["platform"].str.replace("microsoft xbox one","Xbox One",flags=re.I)
    dt["platform"] = dt["platform"].str.replace("playstation 5|sony playstation 5","PS5",flags=re.IGNORECASE)
    dt["platform"] = dt["platform"].str.replace("playstation 3|sony playstation 3","PS3",flags=re.IGNORECASE)
    dt["platform"] = dt["platform"].str.replace('Sony PlayStation 2','')
    dt["platform"] = dt["platform"].str.replace('Microsoft Xbox 360','Xbox 360')
    dt["platform"] = dt["platform"].str.replace('Microsoft Xbox','')
    dt["platform"] = dt["platform"].str.replace("Vita|PlayStation Vita","PS Vita")
    dt["platform"] = dt["platform"].str.replace("PS PS Vita","PS Vita")
    dt["platform"] = dt["platform"].str.replace("pc games|windows|windows 8|windows 98|windows xp","PC",flags=re.IGNORECASE)
    dt["platform"] = dt["platform"].str.replace("PC 8|PC 98|PC XP","PC")
    dt["platform"] = dt["platform"].str.replace("Microsoft Xbox Series X","Xbox Series X")
    dt["platform"] = dt["platform"].str.replace("Xbox Series X, Xbox One","Xbox One, Xbox Series X")
    dt["platform"] = dt["platform"].str.replace("PC, Xbox Series X, PS5, Xbox One, PS4 PS3, Xbox 360, ","Multi-Platform")
    dt["platform"] = dt["platform"].str.replace("Xbox One,","Xbox One")
    dt["platform"] = dt["platform"].str.replace(" Series X,","Xbox Series X,")
    dt["platform"] = dt["platform"].str.replace("Xbox Series X Xbox One","Xbox One, Xbox Series X")
    dt["platform"] = dt["platform"].str.replace("Xbox One Xbox Series X","Xbox One, Xbox Series X")
    dt["platform"] = dt["platform"].str.replace("Xbox One PS4, ,","Xbox One, PS4")
    dt["platform"] = dt["platform"].str.replace("Xbox One PS4,","Xbox One, PS4")
    dt["platform"] = dt["platform"].str.replace("Xbox One ","Xbox One")
    dt["platform"] = dt["platform"].str.replace("PC, Xbox Series X, PS5, Xbox One, PS4 PS3, Xbox 360, ","Multi-Platform")
    dt["platform"] = dt["platform"].str.replace("Xbox Series X, Xbox One","Xbox One, Xbox Series X")
    dt["platform"] = dt["platform"].str.replace("PC, Xbox One, Xbox Series X","Multi-Platform")
    dt["platform"] = dt["platform"].str.replace("Xbox One, Xbox Series X","Xbox Series X")
    dt["platform"] = dt["platform"].str.replace("Nintendo Wii","Wii")
    dt["platform"] = dt["platform"].str.replace("Nintendo Wii U","Wii U")
    dt.groupby('platform').count()

clean_plat()


# =============================================================================
# Adding a column with price ranges
# =============================================================================

def price_range():
    global dt

    dt['price'] = pd.to_numeric(dt['price'])

    conditions = [
        (dt['price'] >= 0) & (dt['price'] <= 9.99),
        (dt['price'] >= 9.99) & (dt['price'] <= 19.99),
        (dt['price'] >= 19.99) & (dt['price'] <= 29.99),
        (dt['price'] >= 29.99) & (dt['price'] <= 39.99),
        (dt['price'] >= 39.99) & (dt['price'] <= 49.99),
        (dt['price'] >= 49.99) & (dt['price'] <= 59.99),
        (dt['price'] >= 59.99) & (dt['price'] <= 69.99),
        (dt['price'] >= 69.99) & (dt['price'] <= 79.99),
        (dt['price'] >= 79.99) & (dt['price'] <= 89.99), 
        (dt['price'] >= 89.99) & (dt['price'] <= 99.99), 
        (dt['price'] >= 99.99)
        ]

    val = ['0 - 9.99', '10 - 19.99','20 - 29.99','30 - 39.99',
           '40 - 49.99','50 - 59.99','60 - 69.99','70 - 79.99',
           '80 - 89.99','90 - 99.99','>=100'
           ]

    dt['price_range'] = np.select(conditions, val)

    dt.head(5)

price_range()

# =============================================================================
# fix platform == "Video Game"
# =============================================================================

## Setting With Copy Warning to False

pd.options.mode.chained_assignment = None

## get the index of  rows with 'platform' == 'Video Game

platform_video_game = dt.loc[dt["platform"]=='Video Game']      

platform_video_game["name"]      

## manual fix for each 
                             
dt.loc[dt['name'] == 'NBA 2K21 (Xbox Series X)', 'platform'] = 'Xbox Series X'
dt.loc[dt['name'] == "Assassin's Creed Valhalla (PS4)", 'platform'] = 'PS4'         
dt.loc[dt['name'] == "Oddworld: Abes Oddysee - New n Tasty (Nintendo Switch)", 'platform'] = 'Nintendo Switch'
dt['platform'].groupby(dt["platform"]).count()
