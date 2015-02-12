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
 * Find out the current time
 *
 * @returns Time string formatted as "hh:mm:ss :yyyy"
 */
function getCurrentTime() {
    var time = new Date();
    var year = time.getFullYear();
    var hours = time.getHours();
    //Add padding 0s to minutes and seconds if they are less than ten for formatting reasons
    var minutes = addPaddingZeroIfNecessary(time.getMinutes());
    var seconds = addPaddingZeroIfNecessary(time.getSeconds());
    document.getElementById("time").innerText = hours + ":" + minutes + ":" +seconds+" "+year;

    /**
     * If a time is less than 10 add a padding 0 to the front of the time value
     * @param time Time in minutes/seconds
     * @returns {string} either the original value or a 0 padded value
     */
    function addPaddingZeroIfNecessary(time) {
        return (time < 10 ? "0" : "") + time
    }
}
/**
 * Update the time every second to simulate a clock
 *
 * @returns null
 */
function runClock(){
    getCurrentTime();
    setInterval(function() {getCurrentTime();},1000);
}

/**
 * Helper function used to call all functions that need to be executed when the page loads
 *
 * @returns null
 */
function baseOnLoad(){
    runClock();
    setContentHeight();
}
/**
 * Get the height of all relatively constant size divs that are top level to the body.  Find the difference of the
 * window size and this values and assign the content div to be this size
 *
 * @returns null
 */
function setContentHeight(){
    var navHeight = getElementHeight("navBarContainer") +
            getElementHeight("templateFooter") +
            getElementHeight("templateHeader");

    document.getElementById("templateContent").style.height =
        (window.innerHeight-navHeight)+"px";

    /**
     * Get the height of an element
     * @param id HTML  id of an element
     * @returns {number} Height of element specified by id
     */
    function getElementHeight(id) {
        return document.getElementById(id).offsetHeight;
    }
}