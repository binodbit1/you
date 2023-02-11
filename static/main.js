// Get the element with the class "card-content"
const cardContent = document.querySelector(".card-content");

// Define the text to be typed out
const text = cardContent.innerHTML;

// Clear the innerHTML of the "card-content" element
cardContent.innerHTML = "";

// Create a function to type out the text
function typeWriter() {
  // Split the text into an array of characters
  const characters = text.split("");
  
  // Initialize an empty string to store the typed out text
  let typedText = "";
  
  // Use a for loop to iterate through the characters
  for (let i = 0; i < characters.length; i++) {
    // Use setTimeout to add a delay between characters
    setTimeout(() => {
      // Add the current character to the typedText
      typedText += characters[i];
      
      // Update the innerHTML of the "card-content" element
      cardContent.innerHTML = typedText;
    }, i * 50); // Adjust the delay (in milliseconds) as needed
  }
}

// Call the typeWriter function
typeWriter();
