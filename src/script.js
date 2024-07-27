// Get the banner images
const images = document.querySelectorAll('#banner img');

// Set the current image index
let currentIndex = 0;

// Function to change the image
function changeImage() {
  // Hide all images
  images.forEach((image) => {
    image.style.display = 'none';
  });

  // Show the current image
  images[currentIndex].style.display = 'block';

  // Increment the current index
  currentIndex++;

  // Reset the current index if it exceeds the number of images
  if (currentIndex >= images.length) {
    currentIndex = 0;
  }
}

// Call the changeImage function every 3 seconds
setInterval(changeImage, 3000);