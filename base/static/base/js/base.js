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
 *
 */
$(document).ready( function () {
    BaseObj.base = new Base();
    //Run page clock
    BaseObj.base.setCurrentTime();
    setInterval(function () {BaseObj.base.setCurrentTime();}, 1000);
    //Associate Nav bar click reactions
    BaseObj.base.setButtonLinks();
    //Set the width of the nav buttons
    BaseObj.base.setButtonWidth();
    //Set the size of text content
    BaseObj.base.setTextSize();
    //Set content section height
    BaseObj.base.setContentHeight();
});

/**
 * Reset the size of the content section, nav buttons, and text if the window is resized
 */
$(window).resize( function () {
    BaseObj.base.setButtonWidth();
    BaseObj.base.setContentHeight();
    BaseObj.base.setTextSize();
});

/**
 * Class representing the base functionality
 * @class Base
 * @constructor Initializes the original text size
 */
function Base() {
    this.original_text_size = 0;
    if($(".content p").length >0){
        this.original_text_size = parseInt($(".content p").css("font-size").substring(0, 2));
    }
    /**
     * Set text size for p, input, and label elements
     * @method setTextSize
     */
    this.setTextSize = function() {
        if (this.original_text_size > 0) {
            $(".content p, input, label, select").css("font-size", this.original_text_size * (window.innerHeight / 750));
        }
    };
    /**
     * Set the width for the navbar
     * @method setButtonWidth
     */
    this.setButtonWidth = function() {
        //get the nav bar div
        var navBar = $("div.navBar");
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
    this.setButtonLinks = function() {
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
    this.getCurrentTime = function() {
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
    this.setContentHeight = function() {
        //height of all body elements
        var navHeight = $("#navBarContainer").outerHeight() +
            $("#templateFooter").outerHeight() +
            $("#templateHeader").outerHeight();
        //set the content element to be the difference between the window size and all other body elements
        $("#templateContent").innerHeight(window.innerHeight - navHeight);
    };
}