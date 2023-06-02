document.addEventListener("DOMContentLoaded", function() {
  // Get the current page URL
  var currentPageURL = window.location.href;

  // Get all navigation links
  var navigationLinks = document.querySelectorAll(".navbar a");

  // Find the link matching the current page URL and add "active" class
  navigationLinks.forEach(function(link) {
    if (link.href === currentPageURL) {
      link.classList.add("active");
    }
  });
});
