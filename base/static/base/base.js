/**
 * File to implement all javascript resources that will be available to the base application
 * at least for the main template
 *
 * @creator PRS
 * @created 2/7/2015
 * @last_modified_by PRS
 * @last_modified_date 2/12/2015
 */

/**
 * Jquery to call all functions that need to be executed when the page loads
 *
 * @returns null
 */
$(document).ready( function () {
    //Run page clock
    setCurrentTime();
    setInterval(setCurrentTime,1000);
    //Set content section height
    setContentHeight();
    //Associate Nav bar click reactions
    $("#home").click(function () {
        window.location.href = '/';
    });
    $("#services").click(function () {
        window.location.href = "/services/";
    });
});

/**
 * Reset the size of the content section if the window is resized
 *
 * @returns null
 */
$(window).resize( function () {
    setContentHeight();
});

/**
 * Gets the current time in the format of "HH:mm:ss DD MMMM YYYY"
 *
 * @returns time string formatted as HH:mm:ss DD MMMM YYYY
 */
function getCurrentTime(){return moment( new Date()).format("HH:mm:ss DD MMMM YYYY")}

/**
 * Set the current time on the 'time' element
 * @returns null
 */
function setCurrentTime() {
    $("#time").text(getCurrentTime());
}

/**
 * Get the height of all relatively constant size divs that are top level to the body.  Find the difference of the
 * window size and this values and assign the content div to be this size
 *
 * @returns null
 */
function setContentHeight(){
    //height of all body elements
    var navHeight = $("#navBarContainer").outerHeight() +
            $("#templateFooter").outerHeight() +
            $("#templateHeader").outerHeight();
    //set the content element to be the difference between the window size and all other body elements
    $("#templateContent").height(window.innerHeight - navHeight);
}