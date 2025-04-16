$(document).ready(function () {
    let isAnimating = false
  
    $('.navbar-toggler').click(function () {
      // Check if animation is in progress
      if (isAnimating) {
        return false // Prevent click if still in cooldown
      }
  
      // Set cooldown flag
      isAnimating = true
  
      // Toggle animation class
      $('.animated-icon1').toggleClass('open')
  
      // Reset cooldown after 1 second
      setTimeout(function () {
        isAnimating = false
      }, 500)
    })
  });

  $(document).ready(function() {
    let isAnimating = false;
    $('.navbar-toggler').click(function() {
      // Check if animation is in progress
      if (isAnimating) {
        return false; // Prevent click if still in cooldown
      }
      
      // Set cooldown flag
      isAnimating = true;
      
      // Toggle animation class
      $('#navIcon').toggleClass('open');
      
      // Reset cooldown after animation completes
      setTimeout(function() {
        isAnimating = false;
      }, 500);
    });
    
    // Close the menu when a link is clicked on mobile
    $('.navbar-nav .nav-link').click(function() {
      if ($(window).width() < 992) {
        $('.navbar-collapse').collapse('hide');
        if ($('#navIcon').hasClass('open')) {
          $('#navIcon').removeClass('open');
        }
      }
    });
  });
  document.addEventListener('DOMContentLoaded', function () {
    const profileSidebar = document.getElementById('profile-sidebar')
  
    profileSidebar.addEventListener('click', function (e) {
      // Only toggle on mobile
      if (window.innerWidth <= 1000) {
        // Toggle the expanded class
        this.classList.toggle('expanded')
      }
    })
  
    // Close the popup when clicking outside
    document.addEventListener('click', function (e) {
      if (window.innerWidth <= 1000 && !profileSidebar.contains(e.target)) {
        profileSidebar.classList.remove('expanded')
      }
    })
  });