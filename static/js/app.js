// DOM Elements
const countrySelect = document.getElementById('country-select');
const exploreBtn = document.getElementById('explore-btn');
const resultsSection = document.getElementById('results-section');
const loading = document.getElementById('loading');
const resultsContent = document.getElementById('results-content');
const errorMessage = document.getElementById('error-message');
const countryName = document.getElementById('country-name');
const cultureInfo = document.getElementById('culture-info');
const errorText = document.getElementById('error-text');
const newSearchBtn = document.getElementById('new-search-btn');
const retryBtn = document.getElementById('retry-btn');

// Event Listeners
exploreBtn.addEventListener('click', handleExplore);
newSearchBtn.addEventListener('click', resetSearch);
retryBtn.addEventListener('click', handleExplore);

countrySelect.addEventListener('change', function() {
    exploreBtn.disabled = !this.value;
});

// Handle explore button click
async function handleExplore() {
    const selectedCountry = countrySelect.value;

    if (!selectedCountry) {
        alert('Please select a country first!');
        return;
    }

    // Show results section and loading state
    resultsSection.style.display = 'block';
    loading.style.display = 'block';
    resultsContent.style.display = 'none';
    errorMessage.style.display = 'none';

    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

    try {
        const response = await fetch('/get-culture-info', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ country: selectedCountry })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to fetch cultural information');
        }

        // Display results
        displayResults(data);

    } catch (error) {
        console.error('Error:', error);
        showError(error.message);
    }
}

// Display culture information
function displayResults(data) {
    loading.style.display = 'none';
    resultsContent.style.display = 'block';
    
    countryName.textContent = data.country;
    
    // Format the information with markdown-like rendering
    const formattedInfo = formatCultureInfo(data.information);
    cultureInfo.innerHTML = formattedInfo;
}

// Format culture information for display
function formatCultureInfo(text) {
    // Convert markdown-style headers to HTML
    let formatted = text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')  // Bold
        .replace(/\*(.*?)\*/g, '<em>$1</em>')  // Italic
        .replace(/^### (.*$)/gm, '<h3>$1</h3>')  // H3
        .replace(/^## (.*$)/gm, '<h2>$1</h2>')  // H2
        .replace(/^# (.*$)/gm, '<h1>$1</h1>')  // H1
        .replace(/\n\n/g, '</p><p>')  // Paragraphs
        .replace(/\n/g, '<br>');  // Line breaks

    // Wrap in paragraph tags
    formatted = '<p>' + formatted + '</p>';

    // Clean up any empty paragraphs
    formatted = formatted.replace(/<p><\/p>/g, '');
    formatted = formatted.replace(/<p>\s*<br>\s*<\/p>/g, '');

    return formatted;
}

// Show error message
function showError(message) {
    loading.style.display = 'none';
    errorMessage.style.display = 'block';
    errorText.textContent = message;
}

// Reset search
function resetSearch() {
    resultsSection.style.display = 'none';
    countrySelect.value = '';
    exploreBtn.disabled = true;
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Enable button if country is already selected on page load
if (countrySelect.value) {
    exploreBtn.disabled = false;
}
