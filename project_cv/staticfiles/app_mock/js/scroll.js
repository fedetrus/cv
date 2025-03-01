document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll(".navbar-item[href^='#']");
    const navbar = document.querySelector(".navbar");
    const navbarHeight = navbar ? navbar.offsetHeight : 0; // Obtiene la altura del navbar

    navLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();

            const targetId = this.getAttribute("href");
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({ behavior: "smooth", block: "start" });
            } else {
                // Si NO está en la página actual, redirigir a `main.html` con el ID
                window.location.href = `/${targetId}`;
            }

            // Cierra el menú en móviles si está abierto
            const navbarBurger = document.querySelector(".navbar-burger");
            const navbarMenu = document.querySelector(".navbar-menu");
            if (navbarBurger.classList.contains("is-active")) {
                navbarBurger.classList.remove("is-active");
                navbarMenu.classList.remove("is-active");
            }
        });
    });
});