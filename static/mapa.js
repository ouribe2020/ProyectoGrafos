
const tilesProvider = 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}'  
let mapa = L.map('mapid').setView([52.9228487,17.2842787], 4)
L.tileLayer(tilesProvider,{
    maxZoom: 18,
}).addTo(mapa)


var lat = (document.getElementById("lat").dataset.lat).split(',');
var lon = (document.getElementById("lon").dataset.lon).split(',');



L.marker([lat[10],lon[10]]).addTo(mapa)
L.marker([lat[11],lon[11]]).addTo(mapa)
L.marker([lat[12],lon[12]]).addTo(mapa)
L.marker([lat[13],lon[13]]).addTo(mapa)
L.marker([lat[14],lon[14]]).addTo(mapa)
L.marker([lat[15],lon[15]]).addTo(mapa)
L.marker([lat[16],lon[16]]).addTo(mapa)
L.marker([lat[17],lon[17]]).addTo(mapa)


//L.polyline([pais['fra'], pais['bel']], {color: 'red'}).addTo(mapa);


