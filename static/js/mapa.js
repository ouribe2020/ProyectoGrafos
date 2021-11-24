
const tilesProvider = 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}'  
let mapa = L.map('mapid').setView([52.9228487,17.2842787], 4)
L.tileLayer(tilesProvider,{
    maxZoom: 18,
}).addTo(mapa)


var datos = JSON.parse(document.getElementById("datos").dataset.datos);
var pesos = []
//datos.length-1
for(var i=0; i < datos.length-1; i++){
    pesos.push(getDis(datos[i], datos[i+1]))
    var vertice = new L.polyline([datos[i], datos[i+1]],{color: 'red'});
    vertice.bindLabel(`${pesos[i]}`,{permanent: true});
    vertice.addTo(mapa); 
    L.marker(datos[i]).addTo(mapa);
}

function getDis(cord1, cord2) {
    var lon1 = ((cord1[1])*Math.PI/180)
        lat1 = ((cord1[0])*Math.PI/180)
        lon2 = ((cord2[1])*Math.PI/180)
        lat2 = ((cord2[0])*Math.PI/180)

    var c = Math.pow(Math.sin((lat2 - lat1)/2), 2) + Math.cos(lat1)
    var d = Math.cos(lat2) * Math.pow(Math.sin(lon2 - lon1/2), 2);
    return Math.round((2 * Math.asin(Math.sqrt(c*d))*6371000)/1000)
}


