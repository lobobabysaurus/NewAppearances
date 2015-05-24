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
    /**
     * Latitute and Longitude location of New Appearances
     * @property salonLatLng
     * @type {google.maps.LatLng}
     */
    var salonLatLng = new google.maps.LatLng(39.946707,-75.302254);

    /**
     * Street Address location of New Appearances
     * @property salonAddress
     * @type {String}
     */
    var salonAddress = "530 Burmont Road, Drexel Hill, PA 19026";

    /**
     * Direction service to set on map generation and to be used for finding directions
     * @property directionService
     * @type {google.maps.DirectionsService}
     */
    var directionService = new google.maps.DirectionsService();

    /**
     * Renders the directions to the salon after form submission
     * @property directionsToSalon
     * @type {google.maps.DirectionsRenderer}
     */
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
     * @method calculateRoute
     * @param {String} originAddress
     */
    this.calculateRoute = function (originAddress) {
        var request = {
            origin: originAddress,
            destination: salonAddress,
            travelMode: google.maps.TravelMode.DRIVING
        };
        directionService.route(request, function (response, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                directionsToSalon.setDirections(response);
                $("#directionsError").text(null);
            }
            else {
                $("#directionsError").text("Error finding a route to the salon");
                $("#directions").html(null);
            }
        });
    };

    /**
     * Parse the directions form for address data and cast it to a formatted string
     * @method processForm
     * @returns {String} The address which has been entered by the user
     */
    this.processForm = function (){
        var address = "";
        $.each($("#directionsForm").serializeArray() , function(index, formSet){
            var value = formSet['value'];
            if(value){
                if($.inArray(formSet['name'], ["zip", "state"])==-1){
                    address += value + ", ";
                }
                else {
                    address += value + " ";
                }
            }
            //Sets form field value as cookie
            $.cookie(formSet['name'], formSet['value'], {expires:7});
        });
        return address;
    };

    /**
     * Iterates through all fields in the form and populates them with a value stored in Cookies if it exists
     * @method initializeForm
     */
    this.initializeForm = function(){
        var formFields = ["street","city","state","zip"];
        $.each(formFields, function (index, field){
            $("input[name='"+field+"']").val($.cookie(field));
        });
    };
}

$(document).ready(function (){
    var local = new Location();
    local.initializeForm();
    google.maps.event.addDomListener(window, 'load', local.initializeMaps);
    $("#attemptCalculation").click(function (){
        local.calculateRoute(local.processForm());
    });
});


