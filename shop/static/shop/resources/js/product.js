$(document).ready(
    function(){

        $('input[type=submit]').click(function() {
            alert("OK");
        })

        // sticky nav
        $('.product-details').waypoint(
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
                offset: '130px'
            }
        )
        
        $('#btn-next').click(function(event) {
            var slide_sau = $('.active').next();
            if(slide_sau.length!=0){
               $('.active').addClass('bien-mat-ben-trai').one('webkitAnimationEnd', function(event) {
                  $('.bien-mat-ben-trai').removeClass('bien-mat-ben-trai').removeClass('active');
               });
               slide_sau.addClass('active').addClass('di-vao-ben-phai').one('webkitAnimationEnd', function(event) {
                  $('.di-vao-ben-phai').removeClass('di-vao-ben-phai');
               });
            }else{
               $('.active').addClass('bien-mat-ben-trai').one('webkitAnimationEnd', function(event) {
                  $('.bien-mat-ben-trai').removeClass('bien-mat-ben-trai').removeClass('active');
               });
               $('.product-img:first-child').addClass('active').addClass('di-vao-ben-phai').one('webkitAnimationEnd', function(event) {
                  $('.di-vao-ben-phai').removeClass('di-vao-ben-phai');
               });
            }
         });

         $('#btn-prev').click(function(event) {
            var slide_truoc = $('.active').prev();
            if(slide_truoc.length!=0){
                $('.active').addClass('bien-mat-ben-phai').one('webkitAnimationEnd', function(event) {
                    $('.bien-mat-ben-phai').removeClass('bien-mat-ben-phai').removeClass('active');
                });
                slide_truoc.addClass('active').addClass('di-vao-ben-trai').one('webkitAnimationEnd', function(event) {
                    $('.di-vao-ben-trai').removeClass('di-vao-ben-trai');
                });
            }else{
                $('.active').addClass('bien-mat-ben-phai').one('webkitAnimationEnd', function(event) {
                    $('.bien-mat-ben-phai').removeClass('bien-mat-ben-phai').removeClass('active');
                });
                $('.product-img:last-child').addClass('active').addClass('di-vao-ben-trai').one('webkitAnimationEnd', function(event) {
                    $('.di-vao-ben-trai').removeClass('di-vao-ben-trai');
                });
            }
        });
    }
)