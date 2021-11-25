from flask import Flask,render_template,request
from covid19dh import covid19
from datetime import date

from networkx.generators.trees import prefix_tree
import datamst 
import math

app =Flask(__name__)

x, src = covid19(cache = False, verbose = False,raw = False,start = date(2021,4,13))
paises = []
nomb = []

#df = x[x.currency == 'EUR'] 
df =  x.sort_values('confirmed',ascending=False)
df = df[:15]

lat = list(df['latitude'])    
lon = list(df['longitude'])
name = list(df['administrative_area_level_1'])

for x in range(len(df)):
    if (not math.isnan(lat[x])) & (not math.isnan(lon[x])):
        paises.append([lat[x],lon[x]])
        nomb.append(name[x])
        
data = datamst.mst(nomb, paises)

@app.route('/')
def index():
    global paises, data 
    return render_template('index.html', datos=paises, data = data, nomb=nomb)


if __name__ == '__main__':
    app.run(debug = True, port=4000)
