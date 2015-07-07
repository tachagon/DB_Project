$(document).scroll(function(e){
    var scrollTop = $(document).scrollTop();
    var hei = $(document).height();
    var headerHei = $('header').height();

    if(hei > 1500){
        if(scrollTop > (headerHei)){
            console.log(scrollTop);
            $('#navbar-menu').removeClass('navbar-static-top').addClass('navbar-fixed-top');
        } else {
            $('#navbar-menu').removeClass('navbar-fixed-top').addClass('navbar-static-top');
        }
    }
});
