document.addEventListener("DOMContentLoaded", () => {
    const category = "learning_&_educational"; 
    const newsCards = document.getElementById("newsCards");

    fetch("http://localhost:5000/get_data")
        .then(response => response.json())
        .then(data => {
            const filteredData = data.filter(article => article.Category === category);
            filteredData.forEach(article => {
                const card = document.createElement("div");
                card.classList.add("news-card");

                card.innerHTML = `
                    <img src="${article.Image || 'https://via.placeholder.com/300x150'}" alt="News Image" class="news-image">
                    <div class="news-content">
                        <h3 class="news-title">${article.Title || "Untitled"}</h3>
                        <p class="news-text">${article.Text ? article.Text.substring(0, 100) + "..." : "No content available"}</p>
                       <div class="sentiment-container">
                            <span class="sentiment ${article.Sentiment.toLowerCase()}">${article.Sentiment || "No sentiment"}</span>
                        </div>
                        <a href="${article.Source}" class="news-source" target="_blank">Read More</a>
                    </div>
                `;

                newsCards.appendChild(card);
            });
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            alert("Failed to load data. Make sure the backend is running.");
        });
});
