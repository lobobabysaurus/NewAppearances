###*
# Location app related Javascript
#
# @module Location
###

$ ->
  $('#printDirections').hide()
  local = new Location()
  local.initializeForm()
  google.maps.event.addDomListener(window, 'load', local.initializeMaps)
  #Attempt to calculate route and save location
  $('.attemptCalculation').click ->
    local.calculateRoute(local.processForm())
    $.post( '/directions/save', $('.directionsForm').serializeArray())
  $(".printDirections").click ->
    printWindow = window.open('','',
      "width=#{window.innerWidth},height=#{window.innerHeight}")
    printWindow.document.write($('.directionsResult').html())
    printWindow.print()
    printWindow.close()

###*
# Class for dealing with Location data
#
# @constructor
# @class Location
###
class Location
  ###*
  # Latitute and Longitude directions of New Appearances
  #
  # @property salonLatLng
  # @type {google.maps.LatLng}
  ###
  salonLatLng = new google.maps.LatLng(39.946707, -75.302254)

  ###*
  # Street Address directions of New Appearances
  #
  # @property salonAddress
  # @type {String}
  ###
  salonAddress = '530 Burmont Road, Drexel Hill, PA 19026'

  ###*
  # Direction service to set on map generation and to be used
  # for finding directions
  #
  # @property directionService
  # @type {google.maps.DirectionsService}
  ###
  directionService = new google.maps.DirectionsService()

  ###*
  # Renders the directions to the salon after form submission
  #
  # @property directionsToSalon
  # @type {google.maps.DirectionsRenderer}
  ###
  directionsToSalon = new google.maps.DirectionsRenderer()

  ###*
  # Create a Google Map for the page
  # @method initializeMaps
  ###
  initializeMaps: ->
    mapOptions =
      center: salonLatLng,
      zoom: 15

    map = new google.maps.Map(document.getElementById('storeMap'), mapOptions)
    marker = new google.maps.Marker
      position: salonLatLng
      map: map
      title: 'New Appearances'

    directionsToSalon.setMap(map)
    directionsToSalon.setPanel(document.getElementById('directionsResult'))

  ###*
  # Find the route between the entered directions and the salon and
  # display it on the page
  #
  # @method calculateRoute
  # @param {String} originAddress
  ###
  calculateRoute: (originAddress) ->
    request =
      origin: originAddress,
      destination: salonAddress,
      travelMode: google.maps.TravelMode.DRIVING

    directionService.route request, (response, status) ->
      if status == google.maps.DirectionsStatus.OK
        $('.directionsResult').show()
        directionsToSalon.setDirections(response)
        $('.directionsError').text(null)
        $('.printDirections').show()
      else
        $('.directionsError').text('Error finding a route to the salon')
        $('.directionsResult').hide()
        $('.printDirections').hide()

  ###*
  # Parse the directions form for address data and cast it
  # to a formatted string
  #
  # @method processForm
  # @returns {String} The address which has been entered by the user
  ###
  processForm: ->
    address = ''
    $.each($('.directionsForm').serializeArray(), (index, formSet) ->
      value = formSet['value']
      if value
        if $.inArray(formSet['name'], ['zip', 'state']) == -1
          address += "#{value}, "
        else
          address += "#{value} "
        # Sets form field value as cookie
        $.cookie(formSet['name'], formSet['value'], expires:7)
    )
    return address

  ###*
  # Iterates through all fields in the form and populates them with
  # a value stored in Cookies if it exists
  #
  # @method initializeForm
  ###
  initializeForm: ->
    formFields = ['street', 'city', 'state', 'zip']
    $.each formFields, (index, field) ->
      $("input[name='#{field}']").val($.cookie(field))
