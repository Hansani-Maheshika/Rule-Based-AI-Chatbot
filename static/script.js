// static/script.js
// Handles frontend chat actions

const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");

// Function to add message into chatbox
function addMessage(message, sender) {
    const messageDiv = document.createElement("div");

    if (sender === "user") {
        messageDiv.className = "user-message";
    } else {
        messageDiv.className = "bot-message";
    }

    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);

    // Automatically scroll to latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Function runs when Send button is clicked
async function sendMessage() {
    const message = userInput.value.trim();

    // Do not send empty message
    if (message === "") {
        return;
    }

    // Show user message in chatbox
    addMessage(message, "user");

    // Clear input field
    userInput.value = "";

    try {
        // Send message to Flask backend
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        // Show bot reply
        addMessage(data.reply, "bot");

        // Disable input if user types bye or exit
        if (data.end_chat) {
            userInput.disabled = true;
        }

    } catch (error) {
        addMessage("Error: Could not connect to the backend server.", "bot");
    }
}

// Press Enter key to send message
userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
