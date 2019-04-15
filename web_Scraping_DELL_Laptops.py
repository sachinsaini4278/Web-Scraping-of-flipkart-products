'''
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:49:50 2019

@author: sachin saini 

"""

#import important libraries
from bs4 import BeautifulSoup as soup  #Beautiful Soup is a Python library for pulling data out of HTML and XML files.
from urllib.request import urlopen as Ureq #urllib is a package that collects several modules for working with URLs.

#first load the url as here i used flipkart dell laptops url
url= "https://www.flipkart.com/search?q=dell+laptops&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_4&otracker1=AS_QueryStore_OrganicAutoSuggest_0_4&as-pos=0&as-type=RECENT&as-backfill=on"
uclient = Ureq(url)  # open url and store it into uclient
page = uclient.read()  #read url data and store into page
uclient.close() #close the uclient

#This module defines a class HTMLParser which serves as the basis for parsing text files formatted in HTML (HyperText Mark-up Language) and XHTML.
page_soup=soup(page,"html.parser") 
print(page_soup)

#open the inspect element in your browser of flipkart page and find the class using mouse hover on the data which is in inspector
containers = page_soup.findAll("div",{"class":"_3O0U0u"})
#using findAll we are going to find the all laptops which are on that page
print(len(containers))#length of total product present on the page of which we extracting information

#to more clear view of html use prettify which is in the beautifulSoup
print(soup.prettify(containers[0])) 


#Now extracting more information 
container = containers[0] #copy first laptop informaton in container from containers list

name = container.findAll("div",{"class":"_3wU53n"})
print(name[0].text)

rating= container.findAll("div",{"class":"hGSR34"})
print(rating[0].text)

description = container.findAll("li",{"class":"tVe95H"})
print(description[0].text)

print(description[1].text) #we use 1st index because tags are same and same tags are stored on different index of list
print(description[2].text)

price=container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
print(price[0].text)
###Now Storing data in CSV file

file_name = "product.csv" #product.csv will be created where your code is located
file = open(file_name,"w",encoding="utf-8") #open file in write mode​
#Desing header of your csv file
header = "Product Name , Price ,Rating\n"
file.write(header)#write your header in file

for container in containers:
    name = container.findAll("div",{"class":"_3wU53n"})
    productName = name[0].text
    
    rating= container.findAll("div",{"class":"hGSR34"})
    Prod_rating=rating[0].text
    
    price=container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
    prod_price=price[0].text
    
    #As price has comma and when you will store it into csv file then it will be seprates so join it
    price_join =''.join(prod_price.split(','))#first split the price with comma then join it
    
    print(productName + ',' + price_join + ',' + Prod_rating + '\n')
    file.write(productName + ',' + price_join + ',' + Prod_rating + '\n')

file.close()
'''

def split(word): 
    return [char for char in word]  
      
# Driver code 
word =  b'\xf82.00\r\n'
print(split(word)) 