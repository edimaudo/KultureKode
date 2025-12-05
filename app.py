import os
import json
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai.errors import APIError
from google.genai import types
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
# Set your API key as an environment variable or in .env file
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')



if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
        


# List of countries in alphabetical order
COUNTRIES = [
    "Afghanistan", "Albania", "Algeria", "Argentina", "Australia", "Austria",
    "Bangladesh", "Belgium", "Brazil", "Bulgaria", "Canada", "Chile", "China",
    "Colombia", "Croatia", "Cuba", "Czech Republic", "Denmark", "Egypt",
    "Ethiopia", "Finland", "France", "Germany", "Ghana", "Greece", "Hungary",
    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kenya", "South Korea", "Lebanon",
    "Malaysia", "Mexico", "Morocco", "Nepal", "Netherlands", "New Zealand",
    "Nigeria", "Norway", "Pakistan", "Peru", "Philippines", "Poland", "Portugal",
    "Romania", "Russia", "Saudi Arabia", "Singapore", "South Africa", "Spain",
    "Sweden", "Switzerland", "Syria", "Taiwan", "Thailand", "Turkey", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States", "Venezuela",
    "Vietnam", "Zimbabwe"
]

@app.route('/')
def index():
    """Landing page route"""
    return render_template('index.html')

@app.route('/app')
def main_app():
    """Main application page route"""
    return render_template('app.html', countries=COUNTRIES)

@app.route('/get-culture-info', methods=['POST'])
def get_culture_info():
    """API endpoint to get cultural information using Gemini"""
    try:
        if not GEMINI_API_KEY:
            return jsonify({
                'error': 'API key not configured. Please set GEMINI_API_KEY environment variable.'
            }), 500

        data = request.get_json()
        country = data.get('country', '')

        if not country:
            return jsonify({'error': 'Country not provided'}), 400

 
        # CRUCIAL: Instruct the model to generate a *specific* JSON object.
        system_instruction = (
            "You are a World renowned travel and cultural expert. Your goal is to provide cultural insights and nuances for different countries in the world "
            "and provide insights into cultural nuances, traditions, landmarks, architecture, cultural and social norms.  Can recommend key things to look out for. **The output MUST be a strict JSON object.** "
            "DO NOT include any Markdown formatting, explanations, or text outside of the JSON block."
        )

        # Create detailed prompt for Gemini
        prompt = f"""Provide a comprehensive but concise overview of {country} covering the following aspects:

1. **Culture & Social Norms**: Describe the cultural values, social etiquette, and daily life customs.

2. **Traditions & Celebrations**: Highlight major festivals, traditional practices, and ceremonial customs.

3. **Architecture & Landmarks**: Describe architectural styles and notable landmarks or structures.

4. **Cultural Nuances**: Explain important dos and don'ts, communication styles, and unique cultural traits visitors should know.

Please format the response in a clear, organized manner with headers and concise paragraphs. Keep the total response under 500 words while being informative and engaging."""


        # Generate response using Gemini
        response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        # *** THE FIX: Force the model to generate valid JSON ***
                        #response_mime_type="application/json", 
                    )
        )
        
        #return jsonify({
        #    'country': country,
        #    'information': analysis_data
        #})
        # Return the structured data directly
        #analysis_data = json.loads(response.text)
        return jsonify({
                #'country': country,
                "information": response.text,
                #"success": True
        })

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
