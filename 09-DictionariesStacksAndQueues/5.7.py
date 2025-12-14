
hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]
x=[]
prices=[]
for lista in hotels_in_Krakow:
    x.append(lista['name'])
    prices.append(lista["price"])
x= ','.join(x)
sum=0
for p in prices:
    sum+=p
wynikk= sum/len(prices)
y=[]
prices2=[]
for lista in hotels_in_Sopot:
    y.append(lista['name'])
    prices2.append(lista["price"])
y= ','.join(y)
sum2=0
for p in prices2:
    sum2+=p
wyniks= sum2/len(prices2)
if wyniks>wynikk:
    w= 'Sopot'
else:
    w='Kraków'
print(f'Hotels in Krakow: {x}')
print(f"Average hotel price in Krakow: {round(wynikk)}")
print(f'Hotels in Sopot: {y}')
print(f"Average hotel price in Krakow: {round(wyniks)}")
print(f"Cheaper hotels in: {w}")
