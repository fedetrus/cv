function copyEmail() {
    let emailText = document.getElementById("email-link").textContent;

    if (!navigator.clipboard) {
        // Si clipboard API no está disponible, usa execCommand (método legacy)
        let tempInput = document.createElement("textarea");
        tempInput.value = emailText;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand("copy");
        document.body.removeChild(tempInput);
    } else {
        navigator.clipboard.writeText(emailText).catch(err => {
            console.error("Error al copiar: ", err);
        });
    }

    let msg = document.getElementById("copy-message");
    msg.classList.remove("is-hidden");
    setTimeout(() => msg.classList.add("is-hidden"), 1500);




}
