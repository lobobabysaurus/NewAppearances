###*
# File to implement all javascript resources that will be
#  available to the products Application
#
# @module Products
###

productObj = {}

$ ->
  productObj.product = new Product()
  productObj.product.prepareImages()
  productObj.product.prepareDialogs()

$(window).resize ->
  productObj.product.prepareImages()

###*
# Class to implement all product display logic
#
# @class Product
# @constructor
###
class Product
  
  ###*
  # Set up the product dialogs/modals for each brand
  #
  # @method prepareDialogs
  ###
  prepareDialogs: ->
    $('div.brands').find('img').each ->
      dialogID = "##{@id}Dialog"
      $(dialogID).dialog
        autoOpen: false
        title: @alt
        width: 'auto'
      $(@).click ->
        $(dialogID).dialog('open')

  ###*
  # Set the sizes and locations of the images
  #
  # @method prepareImages
  ###
  prepareImages: ->
    numImages = $('div.brands').find('img').length
    angleDelta = (Math.PI * 2) / numImages
    imageWidth = $('.content').innerWidth() / numImages
    @setImageSizes(imageWidth)
    @setImageLocations(angleDelta, $('.content'))

  ###*
  # Resize each image to properly fit the page
  # Takes each images and makes its width equal the others so that all images
  # could fit on one row and maintains aspect ratio
  #
  # @method setImageSizes
  # @param {number} imageWidth Width of each image
  ###
  setImageSizes: (imageWidth) ->
    $('div.brands').find('img').each ->
      ratio = @height / @width
      if imageWidth != 0 and (imageWidth * ratio != 0)
        @width = Math.floor(imageWidth)
        @height = Math.round(@width * ratio)

  ###*
  # Set images to be in a ring around the page equidistantly spaced.
  # Since web pages are not square, it treat the ring as independently sized
  # horizonally and vertically.
  # For refernce - en.wikipedia.org/wiki/Circle#Equations
  #
  # @method setImageLocation
  # @param {number} eachAngle Angle in radians of the inter-element spacing
  # @param {Object} body Section of the page that the images will be within
  ###
  setImageLocations: (eachAngle, body) ->
    position = body.position()
    centerX = (body.innerWidth() - position.left ) / 2
    centerY = (body.innerHeight() / 2) -
      (position.top  + $('.footer').innerHeight()) / 4
    $('div.brands').find('img').each (index) ->
      # shift angle to start ring at top
      angle = (eachAngle * index) - Math.PI / 2
      $(@).css
        'left': Math.round(Math.cos(angle) * centerX ) + centerX
        'top': Math.round(Math.sin(angle) * centerY) + centerY
