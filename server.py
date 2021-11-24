from flask import Flask,render_template
from covid19dh import covid19
from datetime import date
import math
app =Flask(__name__)

x, src = covid19(cache = False, verbose = False,raw = False,start = date(2021,4,13))
paises = []
df = x[x.currency=='EUR']

lat = list(df['latitude'])    
lon = list(df['longitude'])
for x in range(len(df)):
    if (not math.isnan(lat[x])) & (not math.isnan(lon[x])):
        paises.append([lat[x],lon[x]])

@app.route('/')
def index():
    global paises
    return render_template('index.html', datos=paises) 

if __name__ == '__main__':
    app.run(debug = True, port=4000)
