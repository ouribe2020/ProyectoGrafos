
const tilesProvider = 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}'  
let mapa = L.map('mapid').setView([52.9228487,17.2842787], 4)
L.tileLayer(tilesProvider,{
    maxZoom: 18,
}).addTo(mapa)

for(var i=0; i < myVar.length-1; i++){
    L.marker(myVar[i], {color: 'blue',radius: 10}).addTo(mapa);
    L.polyline([myVar[i], myVar[i+1]], {color: 'red'}).addTo(mapa);
}       
    //L.polyline([pais['fra'], pais['bel']], {color: 'red'}).addTo(mapa);

