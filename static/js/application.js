$(document).scroll(function(e){
    var scrollTop = $(document).scrollTop();
    var hei = $(document).height();
    var headerHei = $('header').height();
    
    if(scrollTop > (headerHei) && hei > 2000){
        console.log(scrollTop);
        $('#navbar-menu').removeClass('navbar-static-top').addClass('navbar-fixed-top');
    } else {
        $('#navbar-menu').removeClass('navbar-fixed-top').addClass('navbar-static-top');
    }
});
