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
      # Create the dialog name based on the current id
      dialogID = "##{@id}Dialog"
      # Set the dialog functionality
      $(dialogID).dialog
        autoOpen: false
        title: @alt
        width: 'auto'
      # Open the dialog on image click
      $(@).click ->
        $(dialogID).dialog('open')

  ###*
  # Set the image size to be a fourth of the screen and to maintain the
  # aspect ratio. Also arrange the images in a circle around the page
  #
  # @method prepareImages
  ###
  prepareImages: ->
    # Find number of images to display
    numImages = $('div.brands').find('img').length

    # Angle between each image if they were all in a circle
    angleDelta = (Math.PI * 2) / numImages

    # Set each image size
    @setImageSizes(numImages, $('.content').innerWidth())
    # Set each image width
    @setImageLocations(angleDelta, $('.content'))

  ###*
  # Resize each image to properly fit the page
  #
  # @method setImageSizes
  # @param {number} numImages Number of images to fit on the page
  # @param {number} bodyWidth Width of the section that contains the images
  ###
  setImageSizes: (numImages, bodyWidth) ->
    $('div.brands').find('img').each ->
      # Original aspect ratio of the image
      ratio = @height / @width
      # Check to make sure that the width/height don't become 0
      if (bodyWidth / numImages) != 0 && ((bodyWidth / numImages) * ratio != 0)
        # Set the width to be the setion with divided by the image count
        @width = Math.floor($('.content').width() / numImages)
        # Make the height be the rounded value of the new width times the
        # original aspect ratio.  If the value is not rounded it will be the
        # floor of the correct value, xand shrink of the page pixel by pixel
        @height = Math.round(@width * ratio)

  ###*
  # Set images to be in a ring around the page equidistantly spaced
  # from one another
  #
  # @method setImageLocation
  # @param {number} eachAngle Angle in radians of the inter-element spacing
  # @param {Object} body Section of the page that the images will be within
  ###
  setImageLocations: (eachAngle, body) ->
    # Find the center of the page to be the center of the imaginary ring
    position = body.position()
    centerX = (body.innerWidth() / 2) - (position.left / 2)
    centerY = (body.innerHeight() / 2) -
      ((position.top / 2) + ($('.footer').innerHeight() / 2) / 2)
    # For each product image
    $('div.brands').find('img').each (index) ->
      # A Take on parametric equations for a circle
      # en.wikipedia.org/wiki/Circle#Equations
      #
      # Angle becomes the index multiplied by the individual angle to
      # equally space each item, and shifted to make the top item always be key
      angle = (eachAngle * index) - Math.PI / 2

      # Since the ring will normally be an oval, act as though the oval is a
      # circle with the width of the entire body and shift to horizontally
      # center image
      imgLeft = Math.round(
        Math.cos(angle) * centerX ) + centerX

      # Since the ring will normally be an oval, act as though the ova was the
      # height of the entire body and shift to vertically center image
      imgTop = Math.round(
        Math.sin(angle) * centerY) + centerY


      # Set the new top and upper left
      $(@).css
        'left': imgLeft
        'top': imgTop
