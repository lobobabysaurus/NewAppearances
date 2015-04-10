/**
 * Location app related Javascript
 * @module Location
 */

function Location () {
    var salonLatLng = new google.maps.LatLng(39.946707,-75.302254);
    var directionService = new google.maps.DirectionsService();
    var directionsToSalon = new google.maps.DirectionsRenderer();

    this.initializeMaps = function () {
        var mapOptions = {
            center: salonLatLng,
            zoom: 17
        };

        var map = new google.maps.Map(document.getElementById('storeMap'),
            mapOptions);

        var marker = new google.maps.Marker({
            position: salonLatLng,
            map: map,
            title: "New Appearances"
        });
        directionsToSalon.setMap(map);
        directionsToSalon.setPanel(document.getElementById('directions'));
    };

    this.calculateRoute = function () {
        var request = {
            origin: "1514 Green St, Philadelphia, PA 19130",
            destination: salonLatLng,
            travelMode: google.maps.TravelMode.DRIVING
        };
        directionService.route(request, function (response, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                directionsToSalon.setDirections(response);
            }
        });
    };
}

$(document).ready(function (){
    var local = new Location();
    google.maps.event.addDomListener(window, 'load', local.initializeMaps);
    $("#routeCalculate").click(local.calculateRoute);
});


