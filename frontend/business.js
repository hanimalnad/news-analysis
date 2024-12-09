document.addEventListener("DOMContentLoaded", () => {
    const category = "business_&_entrepreneurs"; // Ensure case sensitivity matches backend category
    const newsCards = document.getElementById("newsCards");
    const noResults = document.getElementById("noResults");

    fetch("http://localhost:5000/get_data")
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const filteredData = data.filter(article => article.Category === category);

            if (filteredData.length === 0) {
                noResults.style.display = "block"; // Show 'No articles found' message
                return;
            }

            filteredData.forEach(article => {
                const card = document.createElement("div");
                card.classList.add("news-card");

                // Safeguard for missing data
                const imageSrc = article.Image || "https://via.placeholder.com/300x150";
                const title = article.Title || "Untitled";
                const text = article.Text ? article.Text.substring(0, 100) + "..." : "No content available";
                const sentiment = article.Sentiment || "No sentiment";
                const sentimentClass = sentiment.toLowerCase(); // Ensure CSS compatibility
                const source = article.Source || "#";

                card.innerHTML = `
                    <img src="${imageSrc}" alt="News Image for ${title}" class="news-image">
                    <div class="news-content">
                        <h3 class="news-title">${title}</h3>
                        <p class="news-text">${text}</p>
                        <div class="sentiment-container">
                            <span class="sentiment ${sentimentClass}">${sentiment}</span>
                        </div>
                        <a href="${source}" class="news-source" target="_blank">Read More</a>
                    </div>
                `;

                newsCards.appendChild(card);
            });
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            alert("Failed to load data. Ensure the backend is running and reachable.");
        });
});
