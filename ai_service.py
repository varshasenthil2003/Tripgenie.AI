"""AI service for generating travel itineraries"""

import json
import re
from openai import OpenAI
from config import API_KEY, API_BASE_URL, MODEL_NAME

class AITravelService:
    def __init__(self):
        if not API_KEY:
            raise ValueError("API Key is missing. Please configure your OpenRouter API key.")
        
        self.client = OpenAI(
            base_url=API_BASE_URL,
            api_key=API_KEY,
        )
    
    def generate_itinerary(self, trip_params):
        """Generate travel itinerary using AI"""
        prompt = self._build_prompt(trip_params)
        
        try:
            completion = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=4000
            )
            
            response_text = completion.choices[0].message.content.strip()
            response_text = re.sub(r'```json\s*|\s*```', '', response_text)
            
            itinerary_json = json.loads(response_text)
            return itinerary_json
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing AI response: {e}")
        except Exception as e:
            raise RuntimeError(f"Error generating itinerary: {e}")
    
    def _build_prompt(self, params):
        """Build the AI prompt for itinerary generation"""
        city = params['city']
        days = params['days']
        num_people = params['num_people']
        group_type = params['group_type']
        budget = params['budget']
        travel_pace = params['travel_pace']
        accessibility = params['accessibility']
        food_pref = params['food_preferences']
        interests = params['interests']
        
        return f"""
        You are an expert travel planning assistant specializing in personalized, culturally rich, and practical itineraries.

        Generate a **day-by-day travel itinerary** for a trip to **{city}**, lasting **{days} days**, for **{num_people}** traveler(s).

        ---

        ### 🧭 TRIP OVERVIEW
        - **Destination**: {city}
        - **Duration**: {days} days
        - **Number of Travelers**: {num_people}
        - **Group Type**: {group_type}
        - **Budget Level**: {budget}
        - **Travel Pace**: {travel_pace} (Relaxed / Medium / Packed)
        - **Accessibility Needs**: {"Yes" if accessibility != "None" else "None"}

        ---

        ### 🎯 TRAVEL PREFERENCES
        - **Food Preferences**: {', '.join(food_pref) if food_pref else 'No specific preferences'}
        - **Interest Areas**: {', '.join(interests) if interests else 'General exploration and sightseeing'}

        ---

        ### 💰 BUDGET GUIDELINES (Per Person Per Day)
        - Budget: ₹2,000–4,000
        - Mid-range: ₹4,000–8,000
        - Luxury: ₹8,000–20,000

        ---

        ### 📝 ITINERARY OBJECTIVE
        Build a complete **daily itinerary** with the following:
        - A unique **theme for each day** (e.g. "Cultural Immersion", "Nature Escape", "Urban Adventure")
        - **3–5 curated activities per day**, blending popular sights with local gems
        - For every activity, include:
        - `title`
        - `description` (short, vivid, engaging)
        - `location`
        - `start_time` and `end_time`
        - `cost` (in ₹)
        - `category` (e.g. sightseeing, culinary, adventure, shopping)
        - `insider_tip` (local advice, hack, or recommendation)
        - Add estimated **meal_cost**, **transport_cost**, and **daily_total**

        Ensure the plan:
        - Is logistically practical and well-paced
        - Reflects group type, travel pace, budget, and preferences
        - Offers a mix of free, budget, and premium options

        ---

        ### 🧾 OUTPUT FORMAT (STRICTLY JSON ONLY)
        Return only valid, clean JSON in this structure:

        ```json
        {{
        "destination_info": {{
            "city": "{city}",
            "best_time_to_visit": "e.g. October to March for pleasant weather",
            "local_currency": "e.g. Indian Rupee (INR)",
            "language": "e.g. Hindi, English widely spoken"
        }},
        "days": [
            {{
            "day": 1,
            "theme": "Theme of the day",
            "activities": [
                {{
                "title": "Activity Name",
                "description": "Short vivid description including what to expect",
                "location": "Specific place / landmark",
                "start_time": "9:30 AM",
                "end_time": "11:30 AM",
                "cost": "₹1200",
                "category": "e.g. culture, food, adventure, shopping",
                "insider_tip": "Local advice or tip"
                }}
            ],
            "meal_cost": "₹1500",
            "transport_cost": "₹800",
            "daily_total": "₹5200"
            }}
        ],
        "local_tips": [
            "Cultural etiquette to follow",
            "Transport or safety advice",
            "Budget-saving tip or booking hack"
        ]
        }}
        Respond only with the formatted JSON. Do not include commentary or text outside the JSON object. Keep it engaging, informative, and highly relevant."""
