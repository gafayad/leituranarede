document.addEventListener('DOMContentLoaded', function() {
    var owl = $('.owl-carousel');
    owl.owlCarousel({
        nav: false,
        dots: false,
        loop: true,
        margin: 10,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        responsive: {
            0: { items: 3 },
            600: { items: 3 },
            960: { items: 3 },
            1200: { items: 3 }
        }
    });

    owl.on('mousewheel', '.owl-stage', function(e) {
        if (e.deltaY > 0) {
            owl.trigger('next.owl');
        } else {
            owl.trigger('prev.owl');
        }
        e.preventDefault();
    });
});
