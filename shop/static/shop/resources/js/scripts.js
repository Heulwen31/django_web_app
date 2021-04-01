$(document).ready(
    function(){

        // sticky nav
        $('.product').waypoint(
            function(direction){
                if(direction == "up"){
                    $('.sticky').slideDown(500);
                    $('.sticky').css('background','black');
                    setTimeout(function() {
                        $('.sticky').css('background','none');
                    }, 700);
                } else{
                    $('.sticky').slideUp(500);
                }
            }, {
                offset: '400px'
            }
        )
        //ChangeImg();
    }
)

// function ChangeImg() {
//     if ($('.product-img').hover()) {
//         $('.product-img').attr("src","{{ instant.image2.url }}");
//     } else {
//         $('.product-img').attr("src","{{ instant.image1.url }}");
//     }
// }