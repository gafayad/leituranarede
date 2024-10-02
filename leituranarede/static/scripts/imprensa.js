document.addEventListener('DOMContentLoaded', function() {
  $('.pdf-popup').click(function(event){
      event.preventDefault(); // Previne o comportamento padrão do link

      // Debugging - Verifica se o evento é capturado
      console.log('PDF link clicked');

      var pdfUrl = window.location.origin + $(this).attr('href');
      var pdfTitle = $(this).data('title');

      // URL do Google Docs Viewer
      var googleDocsViewerUrl = 'https://docs.google.com/gview?url=' + encodeURIComponent(pdfUrl) + '&embedded=true';

      // Configura o título do modal (opcional)
      $('#pdfModalLabel').text(pdfTitle);

      // Configura o src do iframe para carregar o PDF usando Google Docs Viewer
      $('#pdfIframe').attr('src', googleDocsViewerUrl);

      // Abre o modal
      $('#pdfModal').modal('show');
  });
});



function toggleDateFields(value) {
  const dateFields = document.getElementById('dateFields');
  if (value === 'De / até:') {
    dateFields.classList.add('d-flex');
  } else {
    dateFields.classList.remove('d-flex');
  }
}
