document.getElementById("sendButton").onclick = async function() {
    const prompt = document.getElementById("prompt").value;
    const show = document.getElementById("showcase");

    const res = await fetch("/ai", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({prompt})
    })

    const data = await res.json();

    show.innerHTML = data.text;
};