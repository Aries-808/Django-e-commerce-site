// Function to scroll left by a certain amount
function scrollLeft(distance) {
    const scrollableDiv = document.getElementById('scrollableDiv');
    scrollableDiv.scrollLeft -= distance;
  }
  
  // Function to scroll right by a certain amount
  function scrollRight(distance) {
    const scrollableDiv = document.getElementById('scrollableDiv');
    scrollableDiv.scrollLeft += distance;
  }
  
  // Get the left and right scroll buttons
  const scrollLeftButton = document.getElementById('scrollLeftButton');
  const scrollRightButton = document.getElementById('scrollRightButton');
  
  // Add click event listeners to the left and right buttons
  scrollLeftButton.addEventListener('click', function() {
    scrollLeft(100); // Scroll left by 50 pixels (adjust the value as needed)
  });
  
  scrollRightButton.addEventListener('click', function() {
    scrollRight(100); // Scroll right by 50 pixels (adjust the value as needed)
  });
  