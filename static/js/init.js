(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();
 	var options = [
      {selector: '#staggered-test', offset: 300, callback: function(el) {
        Materialize.toast("This is our ScrollFire Demo!", 1500 );
      } },
      {selector: '#staggered-test', offset: 325, callback: function(el) {
        Materialize.toast("Please continue scrolling!", 1500 );
      } },
      {selector: '#image-test', offset: 350, callback: function(el) {
        Materialize.fadeInImage($(el));
      } }
    ];
    Materialize.scrollFire(options);
    $('.modal').modal();

  }); // end of document ready
})(jQuery); // end of jQuery name space