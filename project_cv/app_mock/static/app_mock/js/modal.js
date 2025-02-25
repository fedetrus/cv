document.addEventListener('DOMContentLoaded', () => {
  function openModal($el) {
    $el.classList.add('is-active');
  }

  function closeModal($el) {
    $el.classList.remove('is-active');
  }

  function closeAllModals() {
    document.querySelectorAll('.modal.is-active').forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Abre el modal al hacer clic en una imagen
  document.querySelectorAll('.js-modal-trigger').forEach(($trigger) => {
    const modalId = $trigger.dataset.target;
    const $modal = document.getElementById(modalId);

    if ($modal) {
      $trigger.addEventListener('click', () => {
        openModal($modal);
      });
    }
  });

  // Cierra el modal cuando se haga clic en el fondo o en el botón de cierre
  document.querySelectorAll('.modal-background, .modal-close').forEach(($close) => {
    $close.addEventListener('click', () => {
      closeAllModals();
    });
  });

  // Cierra el modal con la tecla "Escape"
  document.addEventListener('keydown', (event) => {
    if (event.key === "Escape") {
      closeAllModals();
    }
  });


  // Encuentra todos los modales con sliders
  const sliders = document.querySelectorAll(".image-slider");

  sliders.forEach(slider => {
      const projectId = slider.id.replace("slider-", "");
      const images = slider.querySelectorAll(".slider-item");
      let currentIndex = 0;

      // Botones de navegación
      const prevButton = document.querySelector(`.slider-prev[data-project="${projectId}"]`);
      const nextButton = document.querySelector(`.slider-next[data-project="${projectId}"]`);

      if (prevButton && nextButton) {
          prevButton.addEventListener("click", function () {
              images[currentIndex].style.display = "none";
              currentIndex = (currentIndex - 1 + images.length) % images.length;
              images[currentIndex].style.display = "block";
          });

          nextButton.addEventListener("click", function () {
              images[currentIndex].style.display = "none";
              currentIndex = (currentIndex + 1) % images.length;
              images[currentIndex].style.display = "block";
          });
      }
  });

  // Cerrar modales y resetear la imagen a la primera
  document.querySelectorAll(".modal-close").forEach(closeButton => {
      closeButton.addEventListener("click", function () {
          const modal = closeButton.closest(".modal");
          if (modal) {
              const projectId = modal.id.replace("modal-", "");
              const images = modal.querySelectorAll(".slider-item");
              images.forEach(img => img.style.display = "none");
              images[0].style.display = "block"; // Reinicia a la primera imagen
          }
      });
  });

});
