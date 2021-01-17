import json
x=list(" "*1680)

for y in range(60):
    x[y] = "-"
    x[y+1620] = "-"
for y in range(1,28):
    x[60*y] = "-"
    x[60*y +59] = "-"

with open('template.json', "w") as f:
    json.dump(x,f)

