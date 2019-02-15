import urllib.request as request
import csv
import os
import json
from urllib.parse import urlparse
import pip 
import plotly as py
import plotly.graph_objs as go

print("-----------------------------------------------------")
print("Welcome! Let's get ready to discover some insights!")
print("-----------------------------------------------------")

l=[]
year = input ("Please type the year in the following format YYYY:")
month = input ("Please type the month in the following format MM:")
user_input = "sales-" + year + month + ".csv"
print ("Your Input Was " + user_input)

while True:
    if user_input == 'sales-201710.csv'or 'sales-201711.csv' or 'sales-201712.csv': #need to fix!!

    #input failure if doesnt have right input

        r = request.urlopen('https://raw.githubusercontent.com/SarahPavlak/Executive_Dashboard/master/data/' + str(user_input)).read().decode('utf8').split("\n")
        reader = csv.reader(r)
        for line in reader:
            print(line)

        
        bar_data = [
            {"Product": "Super Soft Sweater", "Revenue": 123456},
            {"Product": "Super Soft Hoodie", "Revenue": 234567},
            {"Product": "Vintage Logo Tee", "Revenue": 987654},
            {"Product": "Winter Hat", "Revenue": 876543},
            {"Product": "Sticker Pack", "Revenue": 283105},
            {"Product": "Button-Down Shirt", "Revenue": 544099},
            {"Product": "Khaki Pants", "Revenue": 121212},
            {"Product": "Brown Boots", "Revenue": 121212}
        ]

        print("----------------")
        print("GENERATING BAR CHART WITH BUSINESS INSIGHTS...")
        #print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

        x = []
        y = []

        for i in range(0, len(bar_data)):
            x.append(bar_data[i]['Product'])
            y.append(bar_data[i]['Revenue'])
        data = [go.Bar(
                    x=x,
                    y=y
            )]
        layout = go.Layout(title='Product Profits ' + str(user_input))
        figure = go.Figure(data = data,layout=layout)
        py.offline.plot(figure, filename='basic-bar.html', auto_open = True)

        #bar data code adopted from class version

        #creating charts    
            
            #to figure out how to add a chart functionality here
            #code adapted form: https://stackoverflow.com/questions/51351804/extract-csv-file-from-github-library-with-python
        csv_filename = "sales-201803.csv"
        csv_file_path = 0
        #csv_file_path = os.path.join(os.path.dirname(__file__), "data", csv_filename) #need to adjust this line to work
        with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"


            reader = csv.DictReader(csv_file) # assuming your CSV has headers
            for row in reader:
                d = dict(row)
                d = {"date": row["date"], "product": row["product"], "unit price": float(row["unit price"]), "units sold": row["units sold"], "sales price": row["sales price"]}
                print(type(d), d["name"], d["price"])
                products.append(d)

    else: print("Oh no!")
