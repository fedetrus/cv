let imageIndexes = {};  // Guarda la imagen actual por proyecto
let imagesData = {};    // Guarda la lista de imágenes por proyecto

function openModal(projectId) {
    let modal = document.getElementById(`modal-${projectId}`);
    let modalImage = document.getElementById(`modal-image-${projectId}`);

    // Obtener todas las imágenes del modal
    let images = Array.from(document.querySelectorAll(`#modal-${projectId} .image img`))
                      .map(img => img.src); // Extrae las URLs

    console.log(images); // <-- Añade esta línea para depurar

    if (images.length === 0) {
        console.error(`No hay imágenes para el proyecto ${projectId}`);
        return;
    }

    imagesData[projectId] = images; // Almacena todas las imágenes
    imageIndexes[projectId] = 0; // Inicia en la primera imagen
    modalImage.src = images[0]; // Muestra la primera imagen en el modal
    modal.classList.add("is-active"); // Abre el modal
}

function closeModal(projectId) {
    document.getElementById(`modal-${projectId}`).classList.remove("is-active");
}

function nextImage(projectId) {
    if (!imagesData[projectId] || imagesData[projectId].length === 0) return;

    let modalImage = document.getElementById(`modal-image-${projectId}`);
    imageIndexes[projectId] = (imageIndexes[projectId] + 1) % imagesData[projectId].length; // Pasa a la siguiente imagen
    modalImage.src = imagesData[projectId][imageIndexes[projectId]];
}

function prevImage(projectId) {
    if (!imagesData[projectId] || imagesData[projectId].length === 0) return;

    let modalImage = document.getElementById(`modal-image-${projectId}`);
    imageIndexes[projectId] = (imageIndexes[projectId] - 1 + imagesData[projectId].length) % imagesData[projectId].length;
    modalImage.src = imagesData[projectId][imageIndexes[projectId]];
}

