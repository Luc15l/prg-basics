countries = [
{"name":"Poland", "population":38000000},
{'name':'italy',  'population':58990000},
{"name": "USA", "population": 340100000},
{"name": "japan", "population":124000000},
{'name': "russia",'population': 143500000}
]
print('COUNTRY  POPULATION')
for x in countries:
    print(f"{x['name']:<9}{x['population']}")