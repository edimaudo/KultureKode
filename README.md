# KultureKode 

A Flask web application that helps users explore and understand different countries' cultures, traditions, architecture, and cultural nuances using Google's Gemini AI.

## Features

- **Cultural Insights**: Deep dive into values, customs, and social norms
- **Traditions**: Learn about festivals and ceremonial practices
- **Architecture**: Explore iconic structures and design styles
- **Cultural Nuances**: Understand dos, don'ts, and local etiquette
- **70+ Countries**: Comprehensive coverage of countries worldwide

## Project Structure

```
kulture-kode/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── templates/
│   ├── index.html             # Landing page
│   └── app.html               # Main application page
│
└── static/
    ├── css/
    │   └── style.css          # Application styles
    └── js/
        └── app.js             # Client-side JavaScript
```

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

## Installation

1. **Clone or download the project**

2. **Navigate to the project directory**
   ```bash
   cd kulture-kode
   ```

3. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your Gemini API key**
   
   **Option 1: Environment Variable (Recommended)**
   ```bash
   # On Windows (Command Prompt)
   set GEMINI_API_KEY=your_api_key_here
   
   # On Windows (PowerShell)
   $env:GEMINI_API_KEY="your_api_key_here"
   
   # On macOS/Linux
   export GEMINI_API_KEY=your_api_key_here
   ```
   
   **Option 2: .env File**
   Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to**
   ```
   http://localhost:5000
   ```

3. **Explore!**
   - Click "Start Exploring" on the landing page
   - Select a country from the dropdown
   - Click "Explore Culture" to get AI-powered insights

## Usage

1. **Landing Page**: Welcome page with feature overview
2. **Main App**: 
   - Select a country from the alphabetically sorted dropdown
   - Click "Explore Culture" to generate cultural information
   - View comprehensive insights about:
     - Culture & Social Norms
     - Traditions & Celebrations
     - Architecture & Landmarks
     - Cultural Nuances
3. **Search Another Country**: Reset to explore more countries

## API Endpoints

- `GET /` - Landing page
- `GET /app` - Main application page
- `POST /get-culture-info` - Fetch cultural information for a selected country
  - Request body: `{"country": "Country Name"}`
  - Response: `{"country": "Country Name", "information": "..."}`

## Technologies Used

- **Backend**: Flask (Python)
- **AI Integration**: Google Gemini API
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with gradient themes

## Customization

### Adding More Countries

Edit the `COUNTRIES` list in `app.py`:

```python
COUNTRIES = [
    "Your Country Here",
    # ... other countries
]
```

### Changing Color Scheme

Modify the color variables in `static/css/style.css`:

```css
/* Current blue gradient */
background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);

/* Change to your preferred colors */
```

### Customizing Prompts

Modify the prompt in the `get_culture_info()` function in `app.py` to change what information Gemini provides.

## Troubleshooting

### API Key Issues
- Ensure your API key is correctly set in environment variables
- Verify the key is valid at [Google AI Studio](https://makersuite.google.com/)

### Import Errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're using the correct Python version (3.8+)

### Port Already in Use
- Change the port in `app.py`: `app.run(port=5001)`

## Contributing

Feel free to fork this project and customize it for your needs!

## License

This project is open source and available for educational purposes.

## Credits

Built with using Flask and Google Gemini AI
