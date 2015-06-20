/**
 * Module to implement all javascript resources that will be available to the base application
 * at least for the main template
 *
 * @module Base
 */

//Container for module-wide variables
var BaseObj = {};
/**
 * Jquery to call all functions that need to be executed when the page loads
 */
$(document).ready( function () {
    BaseObj.base = new Base();
    //Set content section height
    BaseObj.base.setContentHeight();
});

/**
 * Reset the size of the content section, nav buttons, and text if the window is resized
 */
$(window).resize( function () {
    BaseObj.base.setContentHeight();
});

/**
 * Class representing the base functionality
 * @class Base
 * @constructor Initializes the original text size
 */
function Base() {
    /**
     * Get the height of all relatively constant size divs that are top level to the body.  Find the difference of the
     * window size and this values and assign the content div to be this size
     *
     * @method setContentHeight
     */
    this.setContentHeight = function() {
        //height of all body elements
        var navHeight = $("#navBarContainer").outerHeight() +
            $("#templateFooter").outerHeight() +
            $("#templateHeader").outerHeight();
        //set the content element to be the difference between the window size and all other body elements
        $("#templateContent").innerHeight(window.innerHeight - navHeight);
    };
}
