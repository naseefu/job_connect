// script.js

document.addEventListener('DOMContentLoaded', () => {
    const captions = document.querySelectorAll('.caption');
    let index = 0;
  
    function showCaption() {
      captions[index].style.display = 'inline-block';
      setTimeout(() => {
        captions[index].style.display = 'none';
        index = (index + 1) % captions.length;
        setTimeout(showCaption, 1000); // Delay between captions (5 seconds)
      }, 3000); // Display each caption for 3 seconds
    }
  
    showCaption();
  });
  