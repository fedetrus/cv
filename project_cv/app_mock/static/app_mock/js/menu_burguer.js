document.addEventListener('DOMContentLoaded', () => {
  // Selecciona todos los elementos con la clase 'navbar-burger'
  const $navbarBurgers = document.querySelectorAll('.navbar-burger');

  // Si existen elementos navbar-burger
  if ($navbarBurgers.length > 0) {
      $navbarBurgers.forEach(el => {
          el.addEventListener('click', () => {
              // Obtener el ID del menú objetivo desde data-target
              const target = el.dataset.target;
              const $target = document.getElementById(target);

              // Verificar que el menú existe antes de modificarlo
              if ($target) {
                  el.classList.toggle('is-active');
                  $target.classList.toggle('is-active');
              } else {
                  console.error(`Elemento con ID '${target}' no encontrado.`);
              }
          });
      });
  }
});

