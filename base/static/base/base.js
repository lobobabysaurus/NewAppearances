/**
 * File to implement all javascript resources that will be available to the base application
 * at least for the main template
 *
 * @creator PRS
 * @created 2/7/2015
 * @last_modified_by PRS
 * @last_modified_date 2/7/2015
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
    var minutes = (time.getMinutes() < 10 ? "0" : "" ) + time.getMinutes();
    var seconds = (time.getSeconds() < 10 ? "0" : "" ) + time.getSeconds();
    document.getElementById("time").innerText = hours + ":" + minutes + ":" +seconds+" "+year;
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
}
