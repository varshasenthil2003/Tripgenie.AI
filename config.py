"""Configuration settings for TripGenie.AI"""

import os
from datetime import datetime, timedelta

# API Configuration
API_KEY = 'add your open ai api key here'
API_BASE_URL = "https://openrouter.ai/api/v1"
MODEL_NAME = "add the model you want to use " #deepseek/deepseek-chat-v3-0324:free is the model used by me

# App Configuration
APP_TITLE = "TripGenie.AI"
APP_ICON = "✈️"
PAGE_TITLE = "TripGenie.AI"
TAGLINE = "AI-Powered Travel Experience Generator"

# Budget Guidelines (Per Person Per Day in INR)
BUDGET_RANGES = {
    "Budget": {"min": 2000, "max": 4000},
    "Mid-range": {"min": 4000, "max": 8000},
    "Luxury": {"min": 8000, "max": 20000}
}

# Default Values
DEFAULT_DAYS = 3
DEFAULT_PEOPLE = 2
MAX_TRIP_DAYS = 30
MAX_PEOPLE = 20

# Travel Options
BUDGET_OPTIONS = ["Budget", "Mid-range", "Luxury"]
PACE_OPTIONS = ["Relaxed", "Medium", "Packed"]
GROUP_OPTIONS = ["Solo", "Couple", "Family", "Friends"]
ACCESSIBILITY_OPTIONS = ["None", "Wheelchair Access", "Visual Assistance", "Hearing Assistance"]
FOOD_PREFERENCES = ["Vegetarian", "Vegan", "Local Cuisine", "Street Food", "Fine Dining"]

# Activity Categories
ACTIVITY_CATEGORIES = [
    "Art & Culture", "Museums", "Outdoor Activities", "Indoor Activities",
    "Kid-Friendly", "Trendy Spots", "Nightlife", "Shopping"
]
