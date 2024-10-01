document.addEventListener("DOMContentLoaded", function() {
  const sections = document.querySelectorAll(".section");
  const nextButton = document.getElementById("next");
  const prevButton = document.getElementById("prev");
  let currentSectionIndex = 0;

  function showSection(index) {
    sections.forEach((section, i) => {
      section.classList.toggle("active", i === index);
    });

    // Role suavemente até o topo da página
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });

    // Atualiza a visibilidade dos botões
    updateButtonVisibility();
  }

  function updateButtonVisibility() {
    // Oculta o botão "Anterior" na primeira seção
    prevButton.style.display = currentSectionIndex === 0 ? "none" : "inline-block";

    // Oculta o botão "Próximo" na última seção
    nextButton.style.display = currentSectionIndex === sections.length - 1 ? "none" : "inline-block";
  }

  nextButton.addEventListener("click", () => {
    currentSectionIndex = (currentSectionIndex + 1) % sections.length;
    showSection(currentSectionIndex);
  });

  prevButton.addEventListener("click", () => {
    currentSectionIndex = (currentSectionIndex - 1 + sections.length) % sections.length;
    showSection(currentSectionIndex);
  });

  document.querySelectorAll(".sidebar-link").forEach((link, index) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      currentSectionIndex = index;
      showSection(currentSectionIndex);
    });
  });

  showSection(currentSectionIndex);
});