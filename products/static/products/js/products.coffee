###
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

###
# Class to implement all product display logic
#
# @class Product
# @constructor
###
class Product
  ###
  # Set up the product dialogs/modals for each brand
  #
  # @method prepareDialogs
  ###
  prepareDialogs: ->
    $('div.brands').find('img').each( ->
      # Create the dialog name based on the current id
      dialogID = "##{@id}Dialog"
      # Set the dialog functionality
      $(dialogID).dialog
        autoOpen: false
        title: @alt
        width: 'auto'
      # Open the dialog on image click
      $(@).click ->
        $(dialogID).dialog(open)
    )

  ###
  # Set the image size to be a fourth of the screen and to maintain the
  # aspect ratio. Also arrange the images in a circle around the page
  #
  # @method prepareImages
  ###
  prepareImages: ->
    # Find number of images to display
    numImages = $('div.brands').find('img').length

    # Width of the body section
    bodyWidth = $('.content').innerWidth()
    # Height of the body section
    bodyHeight = $('.content').innerHeight()
    # Angle between each image if they were all in a circle
    angleDelta = (Math.PI * 2)/numImages

    # Set each image size
    @setImageSizes(numImages, bodyWidth)
    # Set each image width
    @setImageLocations(angleDelta, bodyWidth, bodyHeight)

  ###
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
      if((bodyWidth / numImages) != 0 && ((bodyWidth / numImages) * ratio != 0))
        # Set the width to be the setion with divided by the image count
        @width = Math.floor($('.content').width() / numImages)
        # Make the height be the rounded value of the new width times the
        # original aspect ratio.  If the value is not rounded it will be the
        # floor of the correct value, xand shrink of the page pixel by pixel
        @height = Math.round(@width * ratio)

  ###
  # Set images to be in a ring around the page equidistantly spaced
  # from one another
  #
  # @method setImageLocation
  # @param {number} eachAngle Angle in radians of the inter-element spacing
  # @param {number} bodyWidth Width of the body container
  # @param {number} bodyHeight Height of the body container
  ###
  setImageLocations: (eachAngle, bodyWidth, bodyHeight) ->
    # Find the center of the page to be the center of the imaginary ring
    centerX = bodyWidth / 2
    centerY = bodyHeight / 2
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
      imgLeft = Math.round(
        Math.cos(angle) * centerX) + (centerX - @width / 2)

      # Since the ring will normally be an oval, act as though the ova was the
      # height of the entire body and shift to vertically center image
      imgTop = Math.round(
        Math.sin(angle) * centerY) + (centerY - this.height / 2)

      # If the top of the image is too high, pad it down
      if imgTop < 0
        imgTop += @height / 1.9
      # If the bottom of the image is too low, pad it up
      else if imgTop + @height > bodyHeight
        imgTop -= @height / 1.9
      # If the left side of the image is too far left, pad it right
      if imgLeft < 0
        imgLeft += @width / 1.9
      # If the right side of the image is too far right, pad it left
      else if imgLeft + @width > bodyWidth
        imgLeft -= @width / 1.9

      # Set the new top and upper left
      $(@).css
        'left': imgLeft
        'top': imgTop
