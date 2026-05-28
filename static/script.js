

const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");


function addMessage(message, sender) {
    const messageDiv = document.createElement("div");

    if (sender === "user") {
        messageDiv.className = "user-message";
    } else {
        messageDiv.className = "bot-message";
    }

    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);

    
    chatBox.scrollTop = chatBox.scrollHeight;
}


async function sendMessage() {
    const message = userInput.value.trim();

    
    if (message === "") {
        return;
    }

    
    addMessage(message, "user");


    userInput.value = "";

    try {
        
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

    
        addMessage(data.reply, "bot");

        
        if (data.end_chat) {
            userInput.disabled = true;
        }

    } catch (error) {
        addMessage("Error: Could not connect to the backend server.", "bot");
    }
}


userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
