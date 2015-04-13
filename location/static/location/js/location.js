/**
 * Location app related Javascript
 * @module Location
 */

/**
 * Class for dealing with Location data
 *
 * @constructor
 * @class Location
 */
function Location () {
    var salonLatLng = new google.maps.LatLng(39.946707,-75.302254);
    var directionService = new google.maps.DirectionsService();
    var directionsToSalon = new google.maps.DirectionsRenderer();

    /**
     * Create a Google Map for the page
     * @method initializeMaps
     */
    this.initializeMaps = function () {
        var mapOptions = {
            center: salonLatLng,
            zoom: 15
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

    /**
     * Find the route between the entered location and the salon and display it on the page
     * @param {String} originAddress
     */
    this.calculateRoute = function (originAddress) {
        var request = {
            origin: originAddress,
            destination: salonLatLng,
            travelMode: google.maps.TravelMode.DRIVING
        };
        directionService.route(request, function (response, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                directionsToSalon.setDirections(response);
            }
        });
    };

    /**
     * Parse the directions form for address data and cast it to a formatted string
     * @returns {String} The address which has been entered by the user
     */
    this.processForm = function (){
        var address = "";
        $.each($("#directionsForm").serializeArray() , function(index, formSet){
            var value = formSet['value'];
            if(value){
                if($.inArray(formSet['name'], ["Zip", "State"])==-1){
                    address += value + ", ";
                }
                else {
                    address += value + " ";
                }
            }
        });
        return address;
    };
}

$(document).ready(function (){
    var local = new Location();
    google.maps.event.addDomListener(window, 'load', local.initializeMaps);
    $("")
    $("#attemptCalculation").click(function (){
        local.calculateRoute(local.processForm());
    });
});


