document.addEventListener('DOMContentLoaded', function() {
    var owl = $('.owl-carousel');
    owl.owlCarousel({
        nav: false,
        dots: false,
        loop: true,
        margin: 12,
        autoplay: true,
        autoplayTimeout: 4000,
        autoplayHoverPause: true,
        responsive: {
            0: { items: 1 },
            600: { items: 2 },
            960: { items: 3 },
            1200: { items: 3 }
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
  // Seleciona todos os botões de "Veja mais"
  const seeMoreButtons = document.querySelectorAll('.see-more-btn');

  seeMoreButtons.forEach(button => {
    button.addEventListener('click', function () {
      const cardBody = this.closest('.card-body');
      const fullContent = cardBody.querySelector('.full-content');
      const preview = cardBody.querySelector('.preview');

      // Alterna entre exibir e esconder o conteúdo completo
      if (fullContent.style.display === 'none') {
        fullContent.style.display = 'block'; // Mostra o conteúdo completo
        preview.style.display = 'none';      // Esconde o preview
        this.innerHTML = 'Veja menos <i class="fas fa-chevron-up arrow"></i>'; // Atualiza o texto e seta
        this.classList.add('active');
      } else {
        fullContent.style.display = 'none';  // Esconde o conteúdo completo
        preview.style.display = 'block';     // Mostra o preview
        this.innerHTML = 'Veja mais <i class="fas fa-chevron-down arrow"></i>'; // Atualiza o texto e seta
        this.classList.remove('active');
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const seeMoreButtons = document.querySelectorAll('.see-more-btn');

  seeMoreButtons.forEach(button => {
    button.addEventListener('click', function () {
      const card = this.closest('.card');
      const fullContent = card.querySelector('.full-content');

      // Alterna a classe 'expanded' no card
      card.classList.toggle('expanded');

      // Exibe ou oculta o conteúdo completo
      if (card.classList.contains('expanded')) {
        fullContent.style.display = 'block'; // Mostra o conteúdo completo
      } else {
        fullContent.style.display = 'none'; // Esconde o conteúdo completo
      }
    });
  });
});