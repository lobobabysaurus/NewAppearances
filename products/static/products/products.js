/**
 * File to implement all javascript resources that will be available to the products Application
 *
 * @creator PRS
 * @created 2/28/2015
 * @last_modified_by PRS
 * @last_modified_date 2/28/2015
 */

$(document).ready( function () {
    setImageSizes()
});
$(window).resize(function (){
    setImageSizes();
});

/**
 * Set the image size to be a fourth of the screen and to maintain the aspect ratio
 * Also arange the images in a circle around the page
 * NOTE: ONLY WORKS WITH multiples of 4 images properly for now
 */
function setImageSizes(){
    //Find number of images to display
    var numImages = $("div.products").find("img").length;
    //Find number of rows of images assuming there doesn't need to be a bottom root
    var numRows = Math.floor(numImages/2)+1;
    //Find the center row assuming there doesn't need to be a bottom row
    var centerRow = Math.floor(numRows/2);
    //Current row
    var currentRow = 0;
    //Point where new row should start
    var previousRowBottom = 0;
    //Maximum height of images in the current row
    var currentMaxHeight =0;

    //For every image in the products div
    $("div.products").find("img").each(function (index) {
        //Original aspect ratio of the image
        var ratio = this.height/this.width;
        //Width of the body section
        var bodyWidth = $(".content").innerWidth();
        //Check to make sure that the width/height don't become 0
        if((bodyWidth/numImages) !=0 && ((bodyWidth/numImages) * ratio != 0)) {
            //Set the width to be a fourth of the body width (magic number for the time being)
            this.width = Math.floor($(".content").width() / 4);
            //Make the height be the rounded value of the new width times the original aspect ratio
            //If the value is not rounded it will be the floor of the correct value, and shrink of the page pixel by pixel
            this.height = Math.round(this.width * ratio);
        }
        //Distance of the current row from either the top or bottom root.  Top and bottom row will be 0, center will be max
        var distanceFromARoot = centerRow - Math.abs(currentRow-centerRow);
        //Shift from the center is the size of the page times the distance from a root, divided by two times the max distance from a root
        var shift = (bodyWidth*distanceFromARoot)/(centerRow*2);
        //left propery of an image
        var left =0;
        //If a right node or first node
        if(index % 2 ==0){
            //If the image is not in the center row
            if(currentRow!=centerRow) {
                //add the shift to the center point of the page and then center the image by shifting the left more
                left = ((bodyWidth / 2) + shift) - this.width / 2;
            }
            //If the image is in the center row
            else {
                //add the shift to the center point of the page, and fit the image by shifting it left by its size
                left = ((bodyWidth / 2) + shift) - this.width;
            }
            //If the current image height is taller than the left image
            if((this.height) > currentMaxHeight){
                //Make the max height the current image height
                currentMaxHeight =  this.height;
            }
            //Move on to the next row on the next iteration
            currentRow++;
        }
        //If the image is on the left
        if(index % 2 ==1){
            //If the image is not in the center row
            if(currentRow!=centerRow) {
                //Shift the image to the left of the section center point and shift a little more left to center the image
                left = ((bodyWidth / 2) - shift) - this.width / 2;
            }
            //If the image is in the center row
            else {
                //Shift the image to the left of the center point
                left = (bodyWidth / 2) - shift;
            }
            //Current max image height in a row is this by default this value since it is the first image in a row
            currentMaxHeight = this.height;
        }
        //Set the leftmost point of the image to be the computed left value, and the height be the bottom of the previous row
        $(this).css({
            "left": left,
            "top": previousRowBottom
        });
        //If the element is a root or the right element
        if(index % 2 == 0){
            //Make the new bottom the old bottom plus the current max height
            previousRowBottom += currentMaxHeight;
            //Reset the current row max height
            currentMaxHeight = 0;
        }
    });
}