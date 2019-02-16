import urllib.request as request
import csv
import os
import json
from urllib.parse import urlparse
import pip 
import plotly as py
import plotly.graph_objs as go
import pandas

print("--------------------------------------------------------------------------------")
print("Welcome! Let's get ready to discover some business insights courtesy of Sarah!")
print("--------------------------------------------------------------------------------")

l=[]
year = input ("Please type the csv year in the following format YYYY:")
month = input ("Please type the csv month in the following format MM:")
user_input = "sales-" + year + month + ".csv"

def month_lookup(month):
	month_input={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return month_input[month] #month_lookup adapted from hiep's github

sales = [
    'sales-201710.csv','sales-201711.csv','sales-201712.csv', 'sales-201801.csv', 'sales-201802.csv', 'sales-201803.csv', 'sales-201804.csv', 'sales-201805.csv', 'sales-201806.csv', 'sales-201807.csv', 'sales-201808.csv', 'sales-201809.csv', 'sales-201810.csv', 'sales-201811.csv', 'sales-201812.csv', 'sales-201901.csv', 'sales-201902.csv', 'sales-201903.csv', 'sales-201904.csv' #finish putting in csvs
]

products = []
productrevenue = {"Super Soft Sweater" : 0,
    "Super Soft Hoodie" : 0, 
    "Vintage Logo Tee": 0,
    "Winter Hat": 0,
    "Sticker Pack": 0,
    "Button-Down Shirt": 0,
    "Khaki Pants": 0,
    "Brown Boots": 0}

if user_input in sales: 

        r = request.urlopen('https://raw.githubusercontent.com/SarahPavlak/Executive_Dashboard/master/data/' + str(user_input)).read().decode('utf8').split("\n") 
        reader = csv.DictReader(r) 
        #above r code adapted from: https://stackoverflow.com/questions/51351804/extract-csv-file-from-github-library-with-python
        for row in reader:
            d = dict(row)
            d = {"date": row["date"], "product": row["product"], "unit price": float(row["unit price"]), "units sold": row["units sold"], "sales price": row["sales price"]}
            products.append(d) #code adapted from class set up
            if row ["product"] in productrevenue:
                productrevenue[row["product"]] += float(row["sales price"])
            else: productrevenue[row["product"]] = float(row["sales price"])

        total = 0
        for keys in productrevenue:
            total += productrevenue[keys]
      
        bar_data = [
            {"Product": "Super Soft Sweater", "Revenue USD": productrevenue["Super Soft Sweater"]},
            {"Product": "Super Soft Hoodie", "Revenue USD": productrevenue["Super Soft Hoodie"]},
            {"Product": "Vintage Logo Tee", "Revenue USD": productrevenue["Vintage Logo Tee"]},
            {"Product": "Winter Hat", "Revenue USD": productrevenue["Winter Hat"]},
            {"Product": "Sticker Pack", "Revenue USD": productrevenue["Sticker Pack"]},
            {"Product": "Button-Down Shirt", "Revenue USD": productrevenue["Button-Down Shirt"]},
            {"Product": "Khaki Pants", "Revenue USD": productrevenue["Khaki Pants"]},
            {"Product": "Brown Boots", "Revenue USD": productrevenue["Brown Boots"]}
        ]

        productsbysales = []
        for products in sorted(productrevenue, key=productrevenue.get, reverse = True):
            productsbysales.append((products,productrevenue[products]))

            #code adapted from: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
            #code reverse true: https://stackoverflow.com/questions/17295060/sort-the-top-ten-results 


        print("-----------------------------------------------------")
        price_usd = "{0: .2f}".format(total)
        print ("Total Monthly Sales: " + "$" + str(price_usd)) 
        print("-----------------------------------------------------")
        print("Top Selling Products: ")
        print("1) " + productsbysales[0][0] + " $" + str(productsbysales[0][1]))
        print("2) " +productsbysales[1][0] + " $" + str(productsbysales[1][1]))
        print("3) " +productsbysales [2][0] + " $" + str(productsbysales [2][1]))
    
            #code learning: https://realpython.com/python-lists-tuples/#python-tuples 
        print("-----------------------------------------------------")

        print("GENERATING BAR CHART WITH BUSINESS INSIGHTS...")

        x = []
        y = []

        for i in range(0, len(bar_data)):
            x.append(bar_data[i]['Product'])
            y.append(bar_data[i]['Revenue USD'])
        data = [go.Bar(
                    x=x,
                    y=y
            )]
        layout = go.Layout(title='Product Profits ' + str(month_lookup(month)) + " " + year) 
        figure = go.Figure(data = data,layout=layout)
        py.offline.plot(figure, filename='basic-bar.html', auto_open = True)

        #bar data code adapted from class version

else: print("Oh no! That's not a csv option! The program will now gracefully close.") 
exit 

#still to do: 
    #format bar chart, add axis, fix to float 2 decimal places
 
 
 
   
