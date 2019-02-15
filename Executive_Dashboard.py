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
    if user_input == 'sales-201710.csv'or 'sales-201711.csv' or 'sales-201712.csv': 

        r = request.urlopen('https://raw.githubusercontent.com/SarahPavlak/Executive_Dashboard/master/data/' + str(user_input)).read().decode('utf8').split("\n")
        reader = csv.reader(r)
        for line in reader:
            print(line)

        #code adapted form: https://stackoverflow.com/questions/51351804/extract-csv-file-from-github-library-with-python
        
        super_soft_sweater_revenue = 12345
        super_soft_hoodie_revenue = 12345
        vintage_logo_tee_revenue = 12345
        winter_hat_revenue = 12345
        sticker_pack_revenue = 12345
        button_down_shirt_revenue = 12345
        khaki_pants_revenue = 12345
        brown_boots_revenue = 12345

        bar_data = [
            {"Product": "Super Soft Sweater", "Revenue": super_soft_sweater_revenue},
            {"Product": "Super Soft Hoodie", "Revenue": super_soft_hoodie_revenue},
            {"Product": "Vintage Logo Tee", "Revenue": vintage_logo_tee_revenue},
            {"Product": "Winter Hat", "Revenue": winter_hat_revenue},
            {"Product": "Sticker Pack", "Revenue": sticker_pack_revenue},
            {"Product": "Button-Down Shirt", "Revenue": button_down_shirt_revenue},
            {"Product": "Khaki Pants", "Revenue": khaki_pants_revenue},
            {"Product": "Brown Boots", "Revenue": brown_boots_revenue}
        ]

        print("----------------")
        print ("Your mothly sales was: ")



        print("GENERATING BAR CHART WITH BUSINESS INSIGHTS...")

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

        csv_filename = "sales-201803.csv"
        csv_file_path = 0
        #csv_file_path = os.path.join(os.path.dirname(__file__), "data", csv_filename) #need to adjust this line to work
        with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"


            reader = csv.DictReader(csv_file) #code adapted from in class set up
            for row in reader:
                d = dict(row)
                d = {"date": row["date"], "product": row["product"], "unit price": float(row["unit price"]), "units sold": row["units sold"], "sales price": row["sales price"]}
                print(type(d), d["name"], d["price"])
                products.append(d)

    else: print("Oh no!")


#still to do: 
    #tabulate revenues for total monthly sales and express it in dollars
    #makes if statement so if it doesnt work you get the oh no error
    #have the bar graph express the correct revenues 
