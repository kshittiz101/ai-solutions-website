// Set current year in footer
document.getElementById("year").textContent = new Date().getFullYear();

// Navbar scroll effect
document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.getElementById("navbar");
  const navbarBg = document.getElementById("navbar-bg");

  if (navbar && navbarBg) {
    window.addEventListener("scroll", function () {
      const scrollTop =
        window.pageYOffset || document.documentElement.scrollTop;

      if (scrollTop > 50) {
        // Add background when scrolled
        navbarBg.style.backgroundColor = "#0F2229";
        navbarBg.style.borderBottomColor = "rgba(6, 182, 212, 0.2)";
        navbarBg.classList.remove("border-transparent");
      } else {
        // Remove background when at top
        navbarBg.style.backgroundColor = "transparent";
        navbarBg.style.borderBottomColor = "transparent";
        navbarBg.classList.add("border-transparent");
      }
    });
  }
});

// Mobile navigation toggle
const navBtn = document.getElementById("navBtn");
const mobileNav = document.getElementById("mobileNav");
const iconOpen = document.getElementById("navIconOpen");
const iconClose = document.getElementById("navIconClose");

if (navBtn && mobileNav && iconOpen && iconClose) {
  navBtn.addEventListener("click", () => {
    mobileNav.classList.toggle("hidden");
    iconOpen.classList.toggle("hidden");
    iconClose.classList.toggle("hidden");
  });
}

// Toast notification system
function closeToast(button) {
  console.log("Closing toast...", button);
  const toast = button.closest(".toast-item");
  if (toast) {
    console.log("Toast found, applying exit animation");
    toast.classList.remove("toast-enter");
    toast.classList.add("toast-exit");
    setTimeout(() => {
      console.log("Removing toast from DOM");
      toast.remove();
      // If no more toasts, remove the container
      const container = document.getElementById("toast-container");
      if (container && container.children.length === 0) {
        console.log("Removing empty toast container");
        container.remove();
      }
    }, 300);
  } else {
    console.log("Toast not found!");
  }
}

// Auto-close toasts after 5 seconds
document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM loaded, setting up toasts");
  const toasts = document.querySelectorAll("#toast-container .toast-item");
  console.log("Found toasts:", toasts.length);

  toasts.forEach((toast, index) => {
    console.log(`Setting up auto-close for toast ${index + 1}`);
    setTimeout(() => {
      const closeButton = toast.querySelector(".toast-close");
      if (closeButton) {
        console.log(`Auto-closing toast ${index + 1}`);
        closeToast(closeButton);
      }
    }, 1500);
  });
});
