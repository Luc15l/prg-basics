winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}
g=0
for przedmiot,  godziny in winter_semester.items():
    g+=godziny
print(f"The total number of hours in the winter semester is {g}")
