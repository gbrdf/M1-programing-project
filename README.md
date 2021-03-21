![](https://raw.githubusercontent.com/gbrdf/M1-programing-project/main/Unimportant%20folder/data-analytics-header-image.jpg)

# A 3-layered Data Science Project : Web Scraping/Visualization/Color Recognition

## Table of Content
  
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Details](#details)
  * [Demo](#demo)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
 






## Overview
This is a simple 3-layered code that scraps a video game shopping website, in our case [go2games](https://www.go2games.com), visualizes the data and downloads images of all games on their site in order to determine the Pegi rating.

## Motivation
There is nothing more fun than finding your own data to analyze… or at least that is how we think. To accomplish that goal we would need a web-scraping tool. In our case we chose Beautiful soup. Although we are still new when it comes to the subject of data visualization we wanted to push the boundaries even further and try to see if we can analyze specific pictures in order to group them following a certain criteria : in our case a Pegi rating. We tried our best to do the project as professionally as possible and to show our passion for the subject at hand. 

## Technical Aspect

This project is divided into 3 parts:

1. Web scraping video game details on the site in order to find as many information as possible (name, price, genre, availability, supported console) and then grouping it all in a single data frame. We will be using the following modules : 

```bash
import requests
from bs4 import BeautifulSoup
import time  
import re
import pandas as pd
```
2. Data analysis and visualization of said data frame with these additional modules :

```bash
import seaborn as sns
import matplotlib.pyplot as plt
```
3. The last part revolves around downloading all the video game images from the site (also done with Beautiful Soup) and then analyzing said images for their Pegi rating using color detection : 

```bash
import PIL
from colorthief import ColorThief
import io
```
## Installation

The Code is written in Python 3.8.5 . If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip.


## Details


> STEP 1


#### Linux and macOS User

We don't have a system with Mac OS or Linux, but the code should be running smoothly as long as Python is correctly installed.


#### Windows User

The whole project is built on a Windows OS.  



> STEP 2


#### Understanding the scarper 

We have already set two URLs in our code to make it easier when it comes to finding the appropriate webpage to scrap. We did this because of the HTML itself that is used. Its structure is a bit “janky” so we needed to find a different method in order to get the information needed. That being said ` def page_number()` provides us with the info about the total page number we need to scrap and ` def scraper()` gets us all the data we want and compiles it all in a data frame for us to use in the 2nd section.

If you see` time.sleep()` inside the code that means we want to take a small pause (in seconds) before going to the next page. This way we are not going to overwhelm the servers since we don’t know if they are built to withstand high traffic. Although keep in mind that the scraping process might take a few hours to finish. 


#### Analyzing the data  

An important thing to note here is that the visualization and cleaning section **works only with the specific pre-built data frame** that you can find in the full project section. We were unable to standardize the process due to a lack of time but we will try to finish it nonetheless. 


> STEP 3 (incomplete)


#### Getting the pegi information 

Unfortunately, we were not able to fully finish this part of the project. We used Beautiful Soup to scrap the images, but we were unable to accurately measure the color in those images. The idea was to determine the color gradient in a certain area of the image and then conclude if the game is let’s say Pegi 3, Pegi 8 or Pegi 18. You can still find some chunks of our code [here](https://github.com/gbrdf/M1-programming-project/tree/main/pegi%20project%20(unfinished)). 


> STEP 4 

#### Using the main script 

The `main_script.py` defines modules from all 3 different scripts and calls all the functions present in said scripts:
```bash
import scraper as sc

sc.scraper()


import cleaning as cl

cl.clean_cat()
cl.remove_dup()
cl.clean_plat()
cl.price_range()
cl.fix_video_games()


import visualization as vs

vs.plot_price()
vs.plot_plat()
vs.plot_10most()
vs.plot_stats()
vs.plot_disp()
```
It’s important to stock all files present in the full project in one folder on your PC and then define that folder as your directory before running the code. Python won’t be able to find those modules otherwise. This allows you to run all the scripts with one click without needing to run them individually one by one.


## Demo
You can find a demo version of our scraping script that takes the information from only one page in our repository. The only difference is that we will be taking` str(numbers)`and replacing it with the exact page (integer) we want to scrap.



## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)



## Team

Lucas Jeanneau

Nikola Zizic

Guillaume Burdloff
