import urllib.request as request
import csv
import os
import json
from urllib.parse import urlparse
import pip 
import plotly as py
import plotly.graph_objs as go
import pandas

print("-----------------------------------------------------")
print("Welcome! Let's get ready to discover some insights!")
print("-----------------------------------------------------")

l=[]
year = input ("Please type the year in the following format YYYY:")
month = input ("Please type the month in the following format MM:")
user_input = "sales-" + year + month + ".csv"
print ("Your Input Was " + user_input)

def month_lookup(month):
	month_input={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return month_input[month] #month_lookup adapted from hiep's github

sales = [
    'sales-201710.csv','sales-201711.csv','sales-201712.csv', 'sales-201801.csv', 'sales-201802.csv', 'sales-201803.csv', 'sales-201804.csv', 'sales-201805.csv', 'sales-201806.csv', 'sales-201807.csv', 'sales-201808.csv', 'sales-201809.csv', 'sales-201810.csv', 'sales-201811.csv', 'sales-201812.csv', 'sales-201901.csv', 'sales-201902.csv', 'sales-201903.csv', 'sales-201904.csv' #finish putting in csvs
]

products = []
productrevenue = {}
if user_input in sales: 

        r = request.urlopen('https://raw.githubusercontent.com/SarahPavlak/Executive_Dashboard/master/data/' + str(user_input)).read().decode('utf8').split("\n") #above r code adapted from: https://stackoverflow.com/questions/51351804/extract-csv-file-from-github-library-with-python
        reader = csv.DictReader(r) #code adapted from class set up
        for row in reader:
            d = dict(row)
            d = {"date": row["date"], "product": row["product"], "unit price": float(row["unit price"]), "units sold": row["units sold"], "sales price": row["sales price"]}
            print(type(d), d["product"], d["unit price"])
            products.append(d)

            if row ["product"] in productrevenue:
                productrevenue[row["product"]] += row["sales price"]
            else: productrevenue[row["product"]] = row["sales price"]

            print(productrevenue)


    

        super_soft_sweater_revenue = 12345
        super_soft_hoodie_revenue = 12345
        vintage_logo_tee_revenue = 12345
        winter_hat_revenue = 12345
        sticker_pack_revenue = 12345
        button_down_shirt_revenue = 12345
        khaki_pants_revenue = 12345
        brown_boots_revenue = 12345

        total = 0
        total = total + super_soft_sweater_revenue
        total = total + super_soft_hoodie_revenue
        total = total + vintage_logo_tee_revenue
        total = total + winter_hat_revenue
        total = total + sticker_pack_revenue
        total = total + button_down_shirt_revenue
        total = total + khaki_pants_revenue
        total = total + brown_boots_revenue
      
        bar_data = [
            {"Product": "Super Soft Sweater", "Revenue USD": super_soft_sweater_revenue},
            {"Product": "Super Soft Hoodie", "Revenue USD": super_soft_hoodie_revenue},
            {"Product": "Vintage Logo Tee", "Revenue USD": vintage_logo_tee_revenue},
            {"Product": "Winter Hat", "Revenue USD": winter_hat_revenue},
            {"Product": "Sticker Pack", "Revenue USD": sticker_pack_revenue},
            {"Product": "Button-Down Shirt", "Revenue USD": button_down_shirt_revenue},
            {"Product": "Khaki Pants", "Revenue USD": khaki_pants_revenue},
            {"Product": "Brown Boots", "Revenue USD": brown_boots_revenue}
        ]

        print("----------------------------------------")
        price_usd = "${0: .2f}".format(total)
        print ("Total Monthly Sales:" + str (price_usd)) 
        print("----------------------------------------")
        print("Top Selling Products:")
        print("  1) Button-Down Shirt: $6,960.35") #tofix
        print("  2) Super Soft Hoodie: $1,875.00")
        print("  3) etc.")
        print("----------------------------------------")

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
    #make top 3 seller part
    #finish bar graph
