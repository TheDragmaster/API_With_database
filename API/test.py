import requests

BASE = "http://127.0.0.1:5000/"

#data = [{"likes": 2035, "name": "How to solve 2x2 rubix cube", "views": 100000},
#        {"likes": 30000, "name": "How to get free robux", "views": 1000000},
#        {"likes": 11, "name": "Corvette motor exploded", "views": 267},]

#for i in range(len(data)):
#    response = requests.put(BASE + "video/" + str(i), data[i])
#   print(response.json())    the above only needed the first time to put into database

input()
response = requests.patch(BASE + "video/2", {"views": 99})
print(response.json())