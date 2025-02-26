document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contact-form");
  const messageDisplay = document.getElementById("form-message");

  if (!form) return;

  form.addEventListener("submit", function (event) {
      event.preventDefault();
      const formData = new FormData(form);
      const submitButton = form.querySelector(".btn-submit");

      submitButton.disabled = true;

      fetch(form.action, {
          method: "POST",
          body: formData,
          headers: {
              "X-Requested-With": "XMLHttpRequest"
          }
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
