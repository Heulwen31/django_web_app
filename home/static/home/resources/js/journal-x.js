$(document).ready(
    function(){

        // sticky nav
        $('.section-end').waypoint(
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
                offset: '2000px'
            }
        )
    }
)