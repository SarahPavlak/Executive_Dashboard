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

def month_lookup(month):
	month_input={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return month_input[month] #adapted from hiep's github

while True:
    if user_input == 'sales-201710.csv'or 'sales-201711.csv' or 'sales-201712.csv': #finish figuring this out

        r = request.urlopen('https://raw.githubusercontent.com/SarahPavlak/Executive_Dashboard/master/data/' + str(user_input)).read().decode('utf8').split("\n")
        reader = csv.reader(r)
        for line in reader:
            print(line)

        #above r code adapted from: https://stackoverflow.com/questions/51351804/extract-csv-file-from-github-library-with-python
        
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

        print("----------------")
        print ("                       ")
        price_usd = "${0: .2f}".format(total)
        print ("Total Monthly Sales: " + str (price_usd)) #need to format it to two decimal points
        print ("                       ")
        print("-----------------------")
        print ("                       ")
        print("Top Selling Products:")
        print("  1) Button-Down Shirt: $6,960.35") #tofix
        print("  2) Super Soft Hoodie: $1,875.00")
        print("  3) etc.")
        print ("                       ")
        print("-----------------------")

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
        layout = go.Layout(title='Product Profits ' + str(month_lookup(month)) + " " + year) #need to fix month part
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
    #make top 3 seller part
    #makes if statement so if it doesnt work you get the oh no error, fail gracefully i.e. avoid runtime errors and exit program
    #have the bar graph express the correct revenues in usd with 2 decimals


#still to do: 
    #tabulate revenues for total monthly sales and express it in dollars
    #make top 3 seller part
    #makes if statement so if it doesnt work you get the oh no error, fail gracefully i.e. avoid runtime errors and exit program
    #have the bar graph express the correct revenues in usd with 2 decimals
