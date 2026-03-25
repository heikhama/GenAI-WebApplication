async function sendQuery() {
    const prompt = document.getElementById('userInput').value;
    const responseDiv = document.getElementById('response');
    
    responseDiv.innerText = "Thinking...";

    try {
        const result = await fetch('http://localhost:5000/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: prompt })
        });

        const data = await result.json();
        responseDiv.innerText = data.response;
    } catch (error) {
        responseDiv.innerText = "Error connecting to backend.";
    }
}
