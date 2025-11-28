
/**
 * Funkcja tworzy gwiazdki w elemencie HTML
 * @param {string} elementId - ID kontenera gwiazdek
 * @param {number} rating - liczba pełnych gwiazdek
 * @param {number} maxStars - maksymalna liczba gwiazdek (domyślnie 5)
 */
function showStars(elementId, rating, maxStars = 5) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = ""; // czyścimy zawartość

    for (let i = 1; i <= maxStars; i++) {
        const star = document.createElement("span");
        star.classList.add("fs-2");          // wielkość (Bootstrap)
        star.classList.add("text-warning");  // kolor (Bootstrap)
        star.innerHTML = i <= rating ? "&#9733;" : "&#9734;"; // pełna / pusta gwiazdka
        container.appendChild(star);
    }
}