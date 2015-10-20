###
# Module to implement all javascript resources that will be available to the base application
# at least for the main template
#
# @module Base
###

#Container for module-wide variables
BaseObj = {};

$ ->
  BaseObj.base = new Base()
  #Set content section height
  BaseObj.base.setContentHeight()

$(window).resize(() ->
  BaseObj.base.setContentHeight())

###
# Class representing the base functionality
# @class Base
# @constructor Initializes the original text size
###
Base = () ->
  ###
  # Get the height of all relatively constant size divs that are top level to the body.  Find the difference of the
  # window size and this values and assign the content div to be this size
  #
  # @method setContentHeight
  ###
  this.setContentHeight = () ->
      navHeight = $("#navBarContainer").outerHeight() +
          $("#templateFooter").outerHeight() +
          $("#templateHeader").outerHeight()
      $("#templateContent").innerHeight(window.innerHeight - navHeight)
