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
  });
  