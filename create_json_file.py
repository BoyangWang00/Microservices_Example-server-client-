import json
 
# Creating a dictionary
Dictionary ={1:{}, 
             2:{},
             3:{}, 
             4:{},
             5:{}}

Dictionary[1] = {'name': 'Gulu',
                  'age': '5',
                  'type':'Cat',
                  'from': 'Jersey City',
                  #three items in order list are 'time','services','rate'
                  'orders':{1:['2021-03-10','SPA','4'],
                            2:['2021-04-22','Home Visit','5']}}
Dictionary[2] = {'name': 'Hulu',
                  'age': '5',
                  'type':'Cat',
                  'from': 'Jersey City',
                  'orders':{1:['2021-02-14','Home Visit','5'],
                            2:['2021-03-12','Home Visit','4.5'],
                            3:['2021-04-16','SPA','5']}}
Dictionary[3] = {'name': 'Maki',
                  'age': '2',
                  'type':'Dog',
                  'from': 'New York City',
                  'orders':{1:['2021-01-14','SPA','3'],
                            2:['2021-03-17','Home Visit','4.5'],
                            3:['2021-06-16','SPA','5'],
                            4:['2021-09-20','Home Visit','5']}}
Dictionary[4] = {'name': 'Petter',
                  'age': '10',
                  'type':'Bird',
                  'from': 'Hoboken',
                  'orders':{1:['2021-01-18','Home Visit','5'],
                            2:['2021-04-22','Home Visit','3'],
                            3:['2021-07-01','Home Visit','5']}}
Dictionary[5] = {'name': 'Amy',
                  'age': '4',
                  'type':'Cat',
                  'from': 'Hoboken',
                  'orders':{1:['2021-10-14','SPA','5'],
                            2:['2021-11-12','SPA','4'],
                            3:['2021-12-16','SPA','5'],
                            4:['2021-01-03','SPA','4']}}


with open('data.txt', 'w') as outfile:
    json.dump(Dictionary, outfile)
