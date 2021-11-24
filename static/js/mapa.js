
const tilesProvider = 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}'  
let mapa = L.map('mapid').setView([27.6408952,-7.8692974], 3)
L.tileLayer(tilesProvider,{
    maxZoom: 18,
}).addTo(mapa)


var pesos = new Array(10);
for (var i = 0; i < pesos.length; i++) {
    pesos[i] = new Array(2);
}
var datos = JSON.parse(document.getElementById("datos").dataset.datos);

for (var i=0; i < datos.length; i++){
    L.marker(datos[i]).addTo(mapa);
    for(var j=0; j < datos.length; j++){
        if (i != j){
            pesos[i][j] = (getDis(datos[i], datos[j]));
            var vertice = new L.polyline([datos[i], datos[j]],{color: 'red'});
            vertice.bindLabel(`${pesos[i][j]}`);
            vertice.addTo(mapa);
        }               
    }
}    

var pesos = [...new Set([].concat(...pesos))];


function getDis(data1,data2){
    var latlng1 = L.latLng(data1)
    var latlng2 = L.latLng(data2)
    return Math.round((L.GeometryUtil.length([latlng2, latlng1]))/1000);
}

document.getElementById("formPesos").onclick = function () {
    document.getElementById("pesos").value = pesos;
}

