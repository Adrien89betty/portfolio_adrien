document.addEventListener("DOMContentLoaded", function () {

  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

  const form = document.getElementById("contact-form");
  const messageDisplay = document.getElementById("form-message");
  const csrftoken = getCookie('csrftoken');

  if (!form) return;

  form.addEventListener("submit", function (event) {
      event.preventDefault();
      const formData = new FormData(form);
      const submitButton = form.querySelector(".btn-submit");

      submitButton.disabled = true;

      fetch(form.action, {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": csrftoken    
        },
        body: formData
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              messageDisplay.textContent = data.message;
              messageDisplay.classList.remove("hidden");
              messageDisplay.classList.add("success-message");

              form.reset();

              setTimeout(() => {
                  messageDisplay.classList.add("hidden");
              }, 3000);
          } else {
              messageDisplay.textContent = data.message;
              messageDisplay.classList.remove("hidden");
              messageDisplay.classList.add("error-message");
          }
      })
      .catch(error => {
          console.error("Erreur lors de l'envoi du message :", error);
          messageDisplay.textContent = "Une erreur est survenue.";
          messageDisplay.classList.remove("hidden");
          messageDisplay.classList.add("error-message");
      })
      .finally(() => {
          submitButton.disabled = false;
      });
  });
});
