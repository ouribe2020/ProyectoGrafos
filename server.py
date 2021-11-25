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

df = x[x.currency == 'EUR'] 
df =  df.sort_values('confirmed',ascending=False)
#df = df[:1]

lat = list(df['latitude'])    
lon = list(df['longitude'])
name = list(df['administrative_area_level_1'])

for x in range(len(df)):
    if (not math.isnan(lat[x])) & (not math.isnan(lon[x])):
        paises.append([lat[x],lon[x]])
        nomb.append(name[x])
        
data = datamst.mst(nomb, paises)
mst = []
tuplas=[]
for i in data:
    tuplas.append(list(i))

for i in tuplas:
    y, src = covid19(i,cache = False, verbose = False,raw = False,start = date(2021,4,13))
    lat2 = list(y['latitude'])    
    lon2 = list(y['longitude'])
    for i in range(2):
        if (not math.isnan(lat2[i])) & (not math.isnan(lon2[i])):
            mst.append([lat2[i],lon2[i]])

<<<<<<< HEAD
=======

>>>>>>> main
@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        global paises, data 
<<<<<<< HEAD
        return render_template('index.html', datos=paises, data = data, nomb=nomb)
=======
        return render_template('index.html', datos=paises, data = mst)
>>>>>>> main
    else:     
        pesos = request.form['pesos']
        print(pesos)
        return render_template('index.html', datos=paises)   

if __name__ == '__main__':
    app.run(debug = True, port=4000)
