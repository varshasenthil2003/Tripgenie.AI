"""Main application file for TripGenie.AI"""

import streamlit as st
import time
import json
from datetime import datetime

# Import modular components
from config import *
from styles import load_elite_css
from session_manager import initialize_session_state, store_itinerary
from components import (
    render_header, render_sidebar, render_welcome_screen,
    render_trip_overview, render_daily_itinerary, render_local_tips,
    render_packing_list, render_export_options
)
from ai_service import AITravelService
from utils import extract_cost

def main():
    """Main application function"""
    # Configure Streamlit
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Load styles and initialize session
    load_elite_css()
    initialize_session_state()
    
    # Render header
    render_header()
    
    # Render sidebar and get user inputs
    user_inputs = render_sidebar()
    
    # Handle itinerary generation
    if user_inputs['generate_btn'] and not st.session_state.itinerary_generated:
        if not user_inputs['city']:
            st.markdown("""
                <div style="display: flex; justify-content: center;">
                    <div style="background-color:#7f1d1d; padding:1rem; border-radius:8px; color:white; font-weight:600; text-align:center; width: fit-content; max-width: 90%;">
                        ⚠️ Please enter a destination city.
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.stop()
        
        generate_itinerary(user_inputs)
    
    # Display results or welcome screen
    if st.session_state.itinerary_generated and st.session_state.itinerary_data:
        display_itinerary_results(user_inputs)
    else:
        render_welcome_screen()

def generate_itinerary(user_inputs):
    """Generate itinerary using AI service"""
    # Progress tracking
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    with st.spinner("Crafting your luxury travel experience..."):
        try:
            # Simulate progress
            for i in range(100):
                progress_bar.progress(i + 1)
                if i < 25:
                    status_text.markdown("""
                        <div style="color:#1e293b; font-weight:600; font-size:0.95rem;">
                            🔍 Analyzing destination...
                        </div>
                    """, unsafe_allow_html=True)
                elif i < 50:
                    status_text.markdown("""
                        <div style="color:#1e293b; font-weight:600; font-size:0.95rem;">
                            🎯 Customizing preferences...
                        </div>
                    """, unsafe_allow_html=True)
                elif i < 75:
                    status_text.markdown("""
                        <div style="color:#1e293b; font-weight:600; font-size:0.95rem;">
                            🗺️ Planning routes...
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    status_text.markdown("""
                        <div style="color:#1e293b; font-weight:600; font-size:0.95rem;">
                            ✨ Finalizing itinerary...
                        </div>
                    """, unsafe_allow_html=True)
                time.sleep(0.02)
            
            # Prepare trip parameters
            interests = []
            for key, value in user_inputs['preferences'].items():
                if value:
                    interests.append(ACTIVITY_CATEGORIES[list(user_inputs['preferences'].keys()).index(key)])
            
            trip_params = {
                'city': user_inputs['city'],
                'days': user_inputs['days'],
                'num_people': user_inputs['num_people'],
                'group_type': user_inputs['group_type'],
                'budget': user_inputs['budget'],
                'travel_pace': user_inputs['travel_pace'],
                'accessibility': user_inputs['accessibility'],
                'food_preferences': user_inputs['food_preferences'],
                'interests': interests
            }
            
            # Generate itinerary using AI service
            ai_service = AITravelService()
            itinerary_json = ai_service.generate_itinerary(trip_params)
            
            # Calculate total cost
            total_cost = 0
            for day in itinerary_json.get("days", []):
                total_cost += extract_cost(day.get("daily_total", "₹0"))
            
            # Store in session state
            store_itinerary(itinerary_json, total_cost)
            
            # Clear progress
            progress_bar.empty()
            status_text.empty()
            
            st.rerun()
            
        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"Error generating itinerary: {e}")

def display_itinerary_results(user_inputs):
    """Display the generated itinerary results"""
    itinerary_json = st.session_state.itinerary_data
    total_cost = st.session_state.total_cost
    
    # Success message
    st.markdown("""
    <div class="success-banner">
        ✨ Your luxury travel itinerary has been crafted successfully!
    </div>
    """, unsafe_allow_html=True)
    
    # Trip Overview
    render_trip_overview(itinerary_json, user_inputs['days'], user_inputs['num_people'], total_cost)
    
    # Daily Itinerary
    render_daily_itinerary(itinerary_json, user_inputs['num_people'])
    
    # Local Tips
    render_local_tips(itinerary_json, user_inputs['city'])
    
    # Packing List
    render_packing_list(user_inputs['city'], user_inputs['days'], itinerary_json)
    
    # Export Options
    render_export_options(
        itinerary_json, 
        user_inputs['num_people'], 
        user_inputs['city'], 
        user_inputs['start_date'], 
        user_inputs['end_date'], 
        total_cost
    )

if __name__ == "__main__":
    main()
