/**
 * Location app related Javascript
 * @module Location
 */

function initializeMaps () {
    var mapOptions = {
        center: {lat: -34.397, lng: 150.644},
        zoom: 8
    };
    var map = new google.maps.Map(document.getElementById('storeMap'),
        mapOptions);
}
google.maps.event.addDomListener(window, 'load', initializeMaps);



