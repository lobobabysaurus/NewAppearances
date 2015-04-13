/**
 * Module to implement all javascript resources that will be available to the base application
 * at least for the main template
 *
 * @module Base
 */

/**
 * Jquery to call all functions that need to be executed when the page loads
 *
 */
$(document).ready( function () {
    var base = new Base();
    //Run page clock
    base.setCurrentTime();
    setInterval(function () {base.setCurrentTime();}, 1000);
    //Set content section height
    base.setContentHeight();
    //Associate Nav bar click reactions
    base.setButtonLinks();
    //Set the width of the nav buttons
    base.setButtonWidth();
});

/**
 * Reset the size of the content section and nav buttons if the window is resized
 *
 */
$(window).resize( function () {
    var base = new Base();
    base.setContentHeight();
    base.setButtonWidth();
});

/**
 * Class representing the base functionality
 * @class Base
 * @constructor
 */
function Base() {

    /**
     * Set the width for the navbar
     * @method setButtonWidth
     */
    this.setButtonWidth = function(){
        //get the nav bar div
        var navBar = $("div.navBar")
        //Find number of buttons to display
        var numButtons = navBar.find("button").length;
        //set the width each button to be the size of the container divided by the number of images
        var size = navBar.innerWidth()/numButtons;
        navBar.find("button").outerWidth(size);
        //Bullshit fix to a weird rollover issue
        navBar.find("button").last().outerWidth(size-1);
    };

    /**
     * Set button click functionality
     * @method setButtonLinks
     */
    this.setButtonLinks= function(){
        $("div.navBar").find("button").each(function () {
            $(this).click(function () {
                window.location.href = "/"+this.id+"/";
            })
        });
    };

    /**
     * Gets the current time in the format of "HH:mm:ss DD MMMM YYYY"
     *
     * @method getCurrentTime
     * @return {String} Time formatted as HH:mm:ss DD MMMM YYYY
     */
    this.getCurrentTime = function(){
        return moment(new Date()).format("HH:mm:ss DD MMMM YYYY");
    };

    /**
     * Set the current time on the 'time' element
     *
     * @method setCurrentTime
     */
    this.setCurrentTime = function() {
        $("#time").text(this.getCurrentTime());
    };

    /**
     * Get the height of all relatively constant size divs that are top level to the body.  Find the difference of the
     * window size and this values and assign the content div to be this size
     *
     * @method setContentHeight
     */
    this.setContentHeight = function(){
        //height of all body elements
        var navHeight = $("#navBarContainer").outerHeight() +
            $("#templateFooter").outerHeight() +
            $("#templateHeader").outerHeight();
        //set the content element to be the difference between the window size and all other body elements
        $("#templateContent").height(window.innerHeight - navHeight);
    };
}