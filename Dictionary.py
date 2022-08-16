# ediriranje vs. dodavanje

#To edit some data>

team_members = {"QA" :25,"Android": 5}
team_members ["QA"]=22
print(team_members)

team = {"QA":13, "DevOps":2, "Android":4}
team ["QA"] =5
print(team)

#To add some data

total_team = {"QA":5, "Android":6}
total_team ["DevOps"]= 3
print(total_team)

#To delete an element from the list

team = { "QA":12, "Dev":13}
del team["Dev"]
print(team)

# dictionary.keys() dohvacanje samo keys
# dictionary.values() dohvacanje samo values

phones = { "iPhone Xr": "Android", "iPhone 12":"iOS", "Samsung":"Android"}
phones ["iPhone Xr"]= "iOS"
phones ["iPhone 13"]= "iOS"
print(phones)


