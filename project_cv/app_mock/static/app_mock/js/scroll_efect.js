document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll(".hero");

    // Definir el threshold dinámicamente según el ancho de la pantalla
    let thresholdValue = window.innerWidth < 768 ? 0.1 : 0.3; // 10% en móviles, 30% en desktop

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
            }
        });
    }, {
        threshold: thresholdValue
    });

    sections.forEach(section => {
        observer.observe(section);
    });

    // Reajustar el threshold si cambia el tamaño de la pantalla
    window.addEventListener("resize", () => {
        let newThreshold = window.innerWidth < 768 ? 0.1 : 0.3;
        if (newThreshold !== thresholdValue) {
            thresholdValue = newThreshold;
            observer.disconnect();
            sections.forEach(section => observer.observe(section));
        }
    });
});