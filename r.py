import json
import requests
url=requests.get("https://api.merakilearn.org/courses")
js=url.json()
with open("courses.json","w") as file:
    json.dump(js , file , indent=4)
r = open("courses.json","r")
read = r.read()
data = json.loads(read)
print()
print("Welcome to Navgurukul and learn basic promming language")
print()
i = 0
while i < len(data):
    print(str(i+1)+".",data[i]["name"],data[i]["id"])
    i+=1
user_input = int(input("enter the courses no. :"))
print(data[user_input-1]["name"],data[user_input-1]["id"])
print()

a = data[user_input-1]["name"]+"_"+data[user_input-1]["id"]+".json"
s = "http://api.merakilearn.org/courses/"+data[user_input-1]["id"]+"/exercises"
ur = requests.get(s)
d = ur.json()
with open(a,"w") as f :
    json.dump(d,f,indent=4)
rr = open(a,"r")
read = rr.read()
deta = json.loads(read)
i = 0
while i < len(deta["course"]["exercises"]):
    print(str(i+1)+".",deta["course"]["exercises"][i]["name"])
    i+=1
topic=int(input("enter the topic no:- "))
i = 0
while i < len(deta["course"]["exercises"][topic-1]["content"]):
    print(deta["course"]["exercises"][topic-1]["content"][i]["value"])
    print()
    i+=1
i =0
while i < len(deta["course"]["exercises"][topic-1]["content"]):
    ask=input("choose your previous or next (p&n):- ")
    if ask=="p":
        print(deta["course"]["exercises"][topic-2]["content"][i]["value"])
        i = 0
        while i < len(deta["course"]["exercises"][topic-2]["content"]):
            print(deta["course"]["exercises"][topic-2]["content"][i]["value"])
            print()
            i+=1
    if ask=="n":
        print(deta["course"]["exercises"][topic]["content"][i]["value"])
        break
    i+=1        