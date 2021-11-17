
const tilesProvider = 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}'  
let mapa = L.map('mapid').setView([52.9228487,17.2842787], 4)
L.tileLayer(tilesProvider,{
    maxZoom: 18,
}).addTo(mapa)


var pais = {'spa':[46.23,2.21],
            'fra':[40.0,-4.21],
            'bel':[50.83 ,4.0]}

L.marker(pais['spa']).addTo(mapa).bindPopup('France');
L.marker(pais['fra']).addTo(mapa).bindPopup('Spain');
L.marker(pais['bel']).addTo(mapa).bindPopup('Belga');

L.polyline([pais['fra'], pais['bel']], {color: 'red'}).addTo(mapa);



//'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png'



