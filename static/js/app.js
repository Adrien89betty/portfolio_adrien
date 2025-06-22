// Mounting Vue app.
const app = Vue.createApp({
        data() {
          return {
            hardSkills: [],
            projects: [],
            modalProject: null,
            copied: false,
            contact: {
              name: "",
              email: "",
              message: ""
            },
            submitButtonText: "Envoyez votre message !"
          };
        },

        mounted() {
          console.log(this.submitButtonText)
          // Fecth skills from the API
          fetch("/cv/api/skills/")
            .then(res => res.json())
            .then(data => {
              this.hardSkills = data.map(skill => ({
                ...skill,
                logo_url: `${window.STATIC_URL}cv/images/${skill.logo}`
              }));
              console.log("hardSkills:", this.hardSkills);
            })
            .catch(err => console.error(err));

          // fecth projects from the API
          fetch("/projects/api/projects/")
            .then(res => res.json())
            .then(data => {
              this.projects = data.map(proj => ({
                ...proj,
                image_url: `${window.STATIC_URL}projects/images/${proj.image}`
              }));
              console.log("projects:", this.projects);
            })
            .catch(err => console.error(err));
        },

        methods: {
          // Open the modal by opening the project by his ID
          openModal(id) {
            this.modalProject = this.projects.find(p => p.id === id) || null;
          },

          // Close the modal
          closeModal() {
            this.modalProject = null;
          },

          // Email copy feature in contact section
          copyEmail() {
            const emailText = "adrienleveille.contact@gmail.com";
            navigator.clipboard.writeText(emailText).then(() => {
              this.copied = true;

              setTimeout(() => {
                this.copied = false;
              }, 2000);
            }).catch(err => console.error("Erreur lors de la copie :", err));
          },
        }
      });

      app.mount("#app");

// Responsive navbar
document.addEventListener("DOMContentLoaded", () => {
        const btn = document.querySelector(".hamburger");
        const nav = document.querySelector(".nav-links");

        btn.addEventListener("click", () => {
          const isOpen = nav.classList.toggle("open");
          btn.classList.toggle("open", isOpen);
          btn.setAttribute("aria-expanded", isOpen);
        });

        document.querySelectorAll(".nav-links a").forEach(link => {
          link.addEventListener("click", () => {
            nav.classList.remove("open");
            btn.classList.remove("open");
            btn.setAttribute("aria-expanded", false);
          });
        });
      });

// Scroll CTA
window.addEventListener('scroll', () => {
        const cta = document.getElementById('scroll-cta');
        if (window.scrollY > 250) {
          cta.classList.add('hidden');
        }
      });
