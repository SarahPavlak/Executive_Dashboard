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

#input failure if doesnt have right input

r = request.urlopen('https://raw.githubusercontent.com/SarahPavlak/Executive_Dashboard/master/data/' + str(user_input)).read().decode('utf8').split("\n")
reader = csv.reader(r)
for line in reader:
    print(line)

  
bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

x = []
y = []

for i in range(0, len(bar_data)):
    x.append(bar_data[i]['genre'])
    y.append(bar_data[i]['viewers'])
data = [go.Bar(
            x=x,
            y=y
    )]
layout = go.Layout(title='Viewers Per Genre')
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

