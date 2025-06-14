// Function to change the main display image
function changeImage(imageUrl, description) {
    const modalImage = document.getElementById('modalMainImage');
    modalImage.src = imageUrl; // Update the main image source
    // Optional: You can also update the description if needed
    // document.getElementById('imageDescription').innerText = description;
  }
  // Function to handle thumbnail image click
  function changeModalImage(thumbnailElement) {
    const imageUrl = thumbnailElement.src; // Get the source of the thumbnail clicked
    changeImage(imageUrl, ''); // Update the main image
  }