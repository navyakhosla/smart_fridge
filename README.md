# Smart Fridge Recipe Assistant 🍳

A Python-based web application that uses Google's Gemini 2.5 Flash API to analyze fridge images and suggest recipes based on available ingredients and the user's preferred cooking time.

## Features

- **Image Upload:** Upload a fridge image in JPG, JPEG, or PNG format.
- **AI-Powered Recipe Suggestions:** Uses Gemini 2.5 Flash to identify items in the image and generate three recipe suggestions.
- **Structured Recipe Data:** Parses AI-generated JSON containing recipe names, cooking times, difficulty levels, and step-by-step instructions.
- **Time-Based Filtering:** Displays recipes that can be prepared within the user's specified maximum cooking time.
- **Interactive Interface:** Built with Streamlit, with image previews, cooking-time input, recipe details, and feedback when no recipes match the selected time.

## Technologies Used

- **Python** — Application logic and data processing
- **Streamlit** — Interactive web interface
- **Google Gemini 2.5 Flash API** — Image analysis and recipe generation
- **Pillow (PIL)** — Image loading and processing
- **JSON** — Parsing structured recipe responses

## How It Works

1. The user uploads an image of their fridge.
2. The application sends the image and a recipe-generation prompt to Gemini 2.5 Flash.
3. Gemini identifies items in the image and returns three recipe suggestions in JSON format.
4. The application parses the response into Python data structures.
5. The user selects a maximum cooking time.
6. The application displays matching recipes, including their cooking times, difficulty levels, and preparation steps.

## Installation and Setup

### Prerequisites

- Python 3.9 or later
- A Google Gemini API key

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Install Dependencies

```bash
pip install streamlit google-genai pillow
```

### 3. Configure the API Key

Create a file named `.streamlit/secrets.toml` in the project directory:

```toml
GOOGLE_API_KEY = "your-api-key-here"
```

Replace the placeholder with your own API key. Do not commit this file to GitHub.

### 4. Run the Application

```bash
streamlit run app.py
```

Replace `app.py` with your actual Python filename if it is different.

## Future Improvements

- Improve handling of invalid or unexpected AI responses.
- Add dietary preferences and ingredient-based filtering.
- Allow users to save favorite recipes.
- Improve ingredient recognition and recipe relevance.
- Add estimated ingredient quantities and nutritional information.

## Security

Store API credentials using Streamlit secrets or environment variables. Keep API keys and secret configuration files out of version control.
