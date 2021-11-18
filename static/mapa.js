
const tilesProvider = 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}'  
let mapa = L.map('mapid').setView([52.9228487,17.2842787], 4)
L.tileLayer(tilesProvider,{
    maxZoom: 18,
}).addTo(mapa)


var datos = JSON.parse(document.getElementById("datos").dataset.datos);
var pesos = []
//datos.length-1
for(var i=0; i < 10; i++){
    L.marker(datos[i]).addTo(mapa);
    L.polyline([datos[i], datos[i+1]], {color: 'pink'}).addTo(mapa); 
    pesos.push(Math.round(mapa.distance(datos[i],datos[i+1])/1000000));
}