/**
 * File to implement all javascript resources that will be available to the products Application
 *
 * @creator PRS
 * @created 2/28/2015
 * @last_modified_by PRS
 * @last_modified_date 3/8/2015
 */

$(document).ready( function () {
    prepareImages();
    prepareDialogs();
});
$(window).resize(function () {
    prepareImages();
});

/**
 * Set up the product dialogs/modals for each brand
 */
function prepareDialogs(){
    $("div.brands").find("img").each(function () {
        //Create the dialog name based on the current id
        var dialogID = "#"+this.id+"Dialog";
        //Set the dialog functionality
        $(dialogID).dialog({
            autoOpen: false,
            title: this.alt
        });
        //Open the dialog on image click
        $(this).click(function () {
            $(dialogID).dialog("open");
        });
    });
}
/**
 * Set the image size to be a fourth of the screen and to maintain the aspect ratio
 * Also arrange the images in a circle around the page
 */
function prepareImages(){
    //Find number of images to display
    var numImages = $("div.brands").find("img").length;

    // Width of the body section
    var bodyWidth = $(".content").innerWidth();
    // Height of the body section
    var bodyHeight = $(".content").innerHeight();
    //Angle between each image if they were all in a circle
    var angleDelta = ((Math.PI) * 2)/numImages;

    //Set each image size
    setImageSizes(numImages, bodyWidth);
    //Set each image width
    setImageLocations(angleDelta, bodyWidth, bodyHeight);
}
   /**
 * Resize each image to properly fit the page
 * @param numImages Number of images to fit on the page
 * @param bodyWidth Width of the part of the page that contains the images
 */
function setImageSizes(numImages, bodyWidth){
    $("div.brands").find("img").each(function () {
        // Original aspect ratio of the image
        var ratio = this.height/this.width;
        // Check to make sure that the width/height don't become 0
        if((bodyWidth/numImages) !=0 && ((bodyWidth/numImages) * ratio != 0)) {
            // Set the width to be a fourth of the body width (magic number for the time being)
            this.width = Math.floor($(".content").width() / numImages);
            // Make the height be the rounded value of the new width times the original aspect ratio
            // If the value is not rounded it will be the floor of the correct value, and shrink of the page pixel by pixel
            this.height = Math.round(this.width * ratio);
        }
    });
}
/**
 * Set images to be in a ring around the page equidistantly spaced from one another
 *
 * @param eachAngle Angle in radians to represent spacing between each element
 * @param bodyWidth Width of the body container
 * @param bodyHeight Height of the body container
 */
function setImageLocations(eachAngle, bodyWidth, bodyHeight){
    // Find the center of the page to be the center of the imaginary ring
    var centerX = bodyWidth/2;
    var centerY = bodyHeight/2;
    // For each product image
    $("div.brands").find("img").each(function (index) {
        // A Take on parametric equations for a circle en.wikipedia.org/wiki/Circle#Equations

        // Angle becomes the index multiplied by the individual angle to equally space each item,
        // and shifted to make the top item always be key
        var angle = (eachAngle * index) - Math.PI/2;

        // Since the ring will normally be an oval, act as though the oval is a circle with the width of the entire body
        // and shift to horizontally
        var imgLeft = Math.round(Math.cos(angle) * centerX) + (centerX - this.width/2);

        // Since the ring will normally be an oval, act as though the ova was the height of the entire body
        // and shift to vertically center image
        var imgTop  = Math.round(Math.sin(angle) * centerY) + (centerY - this.height/2);

        //If the top of the image is too high, move it down with padding
        if(imgTop<0){
            imgTop += this.height/1.9;
        }
        //if the bottom of the image is too low, move it up with padding
        else if(imgTop+this.height > bodyHeight){
            imgTop -= this.height/1.9;
        }
        // If the left side of the image is too far left, move it right with padding
        if(imgLeft<0){;
            imgLeft += this.width/1.9;
        }
        // If the right side of the image is too far right, move it left with padding
        else if(imgLeft+this.width > bodyWidth){
            imgLeft -= this.width/1.9;
        }

        // Set the new top and upper left
        $(this).css({
            "left": imgLeft,
            "top": imgTop
        });
    });
}