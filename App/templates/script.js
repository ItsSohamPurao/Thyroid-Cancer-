document.getElementById("prediction-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    let formData = new FormData(this);
    let formObject = {};
    
    formData.forEach((value, key) => formObject[key] = value);

    let response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formObject)
    });

    let result = await response.json();
    document.getElementById("result").innerHTML = `Predicted Risk: <b>${result.prediction}</b>`;
});
