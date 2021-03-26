$(document).ready(
    function(){

        // sticky nav
        $('.section-content').waypoint(
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
                offset: '500px'
            }
        )

        // scroll
        // $('a').click(function(event){
        //     $('html, body').animate({
        //         scrollTop: $( $.attr(this, 'href') ).offset().top
        //     }, 700);
        //     event.preventDefault();
        // });

        // // mobile navigation
        // $('.mobile-nav-icon').click(
        //     function(){
        //         $('.main-nav').slideToggle(200);

        //         if($('.mobile-nav-icon').hasClass('fa-bars')){
        //             $('.mobile-nav-icon').addClass('fa-times');
        //             $('.mobile-nav-icon').removeClass('fa-bars')
        //         }
        //         else{
        //             $('.mobile-nav-icon').addClass('fa-bars');
        //             $('.mobile-nav-icon').removeClass('fa-times')
        //         }
        //     }
        // )
    }
)