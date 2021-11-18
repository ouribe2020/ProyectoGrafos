from flask import Flask,render_template
from covid19dh import covid19
from datetime import date

app =Flask(__name__)

@app.route('/')
def index():
    x, src = covid19(cache = False, verbose = False,raw = False,start = date(2021,4,13),end = "2021-04-13")
    lat = x['latitude'].tolist()
    lon = x['longitude'].tolist()
    return render_template('index.html',lat=lat,lon=lon) 



if __name__ == '__main__':
    app.run(debug = True, port=4000)
