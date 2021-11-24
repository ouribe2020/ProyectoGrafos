from flask import Flask,render_template,request
from covid19dh import covid19
from datetime import date
import datamst 
import math

app =Flask(__name__)

x, src = covid19(cache = False, verbose = False,raw = False,start = date(2021,4,13))
paises = []
nomb = []

df =  x.sort_values('confirmed',ascending=False)
df = df[:10]

lat = list(df['latitude'])    
lon = list(df['longitude'])
name = list(df['administrative_area_level_1'])

for x in range(10):
    if (not math.isnan(lat[x])) & (not math.isnan(lon[x])):
        paises.append([lat[x],lon[x]])
        nomb.append(name[x])
        
data = datamst.mst(nomb, paises)

print(data)
id = list(df.id)
#sex, src = covid19(paises, cache = False, verbose = False,raw = False,start = date(2021,4,13))
print(id)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        global paises, data 
        return render_template('index.html', datos=paises, data = data)
    else:     
        pesos = request.form['pesos']
        print(pesos)
        return render_template('index.html', datos=paises)   

if __name__ == '__main__':
    app.run(debug = True, port=4000)
