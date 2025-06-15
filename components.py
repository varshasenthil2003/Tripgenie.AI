"""UI components for TripGenie.AI"""

import streamlit as st
from datetime import datetime, timedelta
from config import *
from utils import extract_cost

def render_header():
    """Render the application header"""
    st.markdown(f"""
    <div class="elite-header">
        <h1 class="elite-title">{APP_TITLE}</h1>
        <p class="elite-subtitle">{TAGLINE}</p>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Render the sidebar with trip configuration"""
    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-header">
            <div class="sidebar-logo">{APP_ICON} TripGenie</div>
            <div class="sidebar-tagline">Crafting Perfect Journeys</div>
        </div>
        """, unsafe_allow_html=True)

        # Trip Basics
        st.markdown('<div class="section-title">🌍 Trip Basics</div>', unsafe_allow_html=True)
        city = st.text_input("Destination City", placeholder="e.g., Paris, Tokyo, New York")
        
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date", value=datetime.today())
        with col2:
            max_end_date = start_date + timedelta(days=MAX_TRIP_DAYS)
            end_date = st.date_input("End Date", 
                                   value=start_date + timedelta(days=DEFAULT_DAYS), 
                                   min_value=start_date, 
                                   max_value=max_end_date)
        
        days = (end_date - start_date).days
        num_people = st.number_input("Number of Travelers", 
                                   min_value=1, 
                                   max_value=MAX_PEOPLE, 
                                   value=DEFAULT_PEOPLE, 
                                   step=1)
        
        # Travel Preferences
        st.markdown('<div class="section-title">🎯 Preferences</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        preferences = {}
        with col1:
            preferences['art'] = st.checkbox("Art & Culture")
            preferences['museums'] = st.checkbox("Museums")
            preferences['outdoor'] = st.checkbox("Outdoor Activities")
            preferences['indoor'] = st.checkbox("Indoor Activities")
        with col2:
            preferences['kids_friendly'] = st.checkbox("Kid-Friendly")
            preferences['young_people'] = st.checkbox("Trendy Spots")
            preferences['nightlife'] = st.checkbox("Nightlife")
            preferences['shopping'] = st.checkbox("Shopping")
        
        # Advanced Settings
        st.markdown('<div class="section-title">⚙️ Advanced Settings</div>', unsafe_allow_html=True)
        budget = st.selectbox("Budget Level", BUDGET_OPTIONS)
        travel_pace = st.selectbox("Travel Pace", PACE_OPTIONS)
        group_type = st.selectbox("Group Type", GROUP_OPTIONS)
        accessibility = st.selectbox("Accessibility", ACCESSIBILITY_OPTIONS)
        food_pref = st.multiselect("Food Preferences", FOOD_PREFERENCES)
        
        # Generate button
        generate_btn = st.button("Generate Elite Itinerary")
        
        # New journey button
        if st.session_state.get('itinerary_generated', False):
            if st.button("Create New Journey"):
                st.session_state.itinerary_generated = False
                st.session_state.itinerary_data = None
                st.session_state.expanded_days = set()
                st.rerun()
    
    return {
        'city': city,
        'start_date': start_date,
        'end_date': end_date,
        'days': days,
        'num_people': num_people,
        'preferences': preferences,
        'budget': budget,
        'travel_pace': travel_pace,
        'group_type': group_type,
        'accessibility': accessibility,
        'food_preferences': food_pref,
        'generate_btn': generate_btn
    }

def render_welcome_screen():
    """Render the welcome screen"""
    st.markdown("""
    <div class="welcome-hero">
        <h1 class="welcome-title">Welcome to Modern Travel Planning</h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI-Powered Intelligence</div>
            <div class="feature-description">Advanced AI algorithms analyze your preferences to create perfectly tailored travel experiences that match your unique style and budget.</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Comprehensive Analytics</div>
            <div class="feature-description">Detailed cost breakdowns, interactive charts, smart packing lists, and professional export options for complete trip management.</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">✨</div>
            <div class="feature-title">Luxury Experience</div>
            <div class="feature-description">Curated recommendations, insider tips, and premium experiences designed to create unforgettable memories and seamless travel.</div>
        </div>
        """, unsafe_allow_html=True)

def render_trip_overview(itinerary_json, days, num_people, total_cost):
    """Render trip overview cards"""
    if "destination_info" in itinerary_json:
        dest_info = itinerary_json["destination_info"]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="overview-card">
                <div class="card-title">Destination Information</div>
                <div class="card-content">
                    <p><strong>Best Time to Visit:</strong><br>{dest_info.get('best_time_to_visit', 'N/A')}</p>
                    <p><strong>Language:</strong><br>{dest_info.get('language', 'N/A')}</p>
                    <p><strong>Currency:</strong><br>{dest_info.get('local_currency', 'N/A')}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="overview-card">
                <div class="card-title">Trip Summary</div>
                <div class="card-content">
                    <p><strong>Duration:</strong><br>{days} days</p>
                    <p><strong>Travelers:</strong><br>{num_people} people</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="overview-card cost-card">
                <div class="card-title">Total Investment</div>
                <div class="cost-amount">₹{total_cost:,}</div>
                <div class="cost-label">₹{total_cost//num_people:,} per person</div>
            </div>
            """, unsafe_allow_html=True)

def render_daily_itinerary(itinerary_json, num_people):
    """Render the daily itinerary with expandable days"""
    st.markdown('<h2 class="section-header">Your Journey</h2>', unsafe_allow_html=True)
    
    for day_data in itinerary_json.get("days", []):
        day_num = day_data['day']
        is_expanded = day_num in st.session_state.get('expanded_days', set())
        
        # Day Header (Clickable)
        if st.button(f"Day {day_num}: {day_data.get('theme', 'Exploration')}", 
                    key=f"day-{day_num}", 
                    help="Click to expand/collapse"):
            if 'expanded_days' not in st.session_state:
                st.session_state.expanded_days = set()
            
            if day_num in st.session_state.expanded_days:
                st.session_state.expanded_days.remove(day_num)
            else:
                st.session_state.expanded_days.add(day_num)
            st.rerun()
        
        # Day Content (Conditionally shown)
        if is_expanded:
            st.markdown('<div class="activity-container">', unsafe_allow_html=True)
            
            # Activities
            for activity in day_data.get("activities", []):
                cost_per_person = extract_cost(activity.get('cost', '₹0'))
                total_activity_cost = cost_per_person * num_people
                
                st.markdown(f"""
                <div class="activity-card">
                    <div class="activity-info">
                        <h5>{activity['title']}</h5>
                        <p class="activity-detail"><strong>Description:</strong> {activity.get('description', 'N/A')}</p>
                        <p class="activity-detail"><strong>Location:</strong> {activity.get('location', 'N/A')}</p>
                        <p class="activity-detail"><strong>Time:</strong> {activity.get('start_time', 'N/A')} - {activity.get('end_time', 'N/A')}</p>
                        <div class="activity-tip"><strong>Insider Tip:</strong> {activity.get('insider_tip', 'Enjoy the experience!')}</div>
                    </div>
                    <div class="cost-display">
                        <div class="cost-primary">₹{cost_per_person:,}</div>
                        <div class="cost-secondary">per person</div>
                        <div class="cost-secondary">₹{total_activity_cost:,} total</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Daily Summary
            daily_total = extract_cost(day_data.get('daily_total', '₹0'))
            st.markdown(f"""
            <div class="daily-summary">
                Day {day_data['day']} Total: ₹{daily_total:,} (₹{daily_total//num_people:,} per person)
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

def render_local_tips(itinerary_json, city):
    """Render local tips section"""
    if "local_tips" in itinerary_json:
        st.markdown('<h2 class="section-header">Local Insights</h2>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="tips-container">
            <h3 class="tips-title">Essential Tips for {city}</h3>
        """, unsafe_allow_html=True)
        
        for tip in itinerary_json["local_tips"]:
            st.markdown(f'<div class="tip-item">{tip}</div>', unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

def render_packing_list(city, days, itinerary_json):
    """Render packing list section"""
    from utils import generate_packing_list
    
    st.markdown('<h2 class="section-header">Packing Essentials</h2>', unsafe_allow_html=True)
    
    activities_list = []
    for day in itinerary_json.get("days", []):
        activities_list.extend([act.get('title', '') for act in day.get('activities', [])])
    
    packing_list = generate_packing_list(city, days, activities_list)
    
    st.markdown('<div class="packing-grid">', unsafe_allow_html=True)
    for category, items in packing_list.items():
        st.markdown(f"""
        <div class="packing-card">
            <div class="packing-title">{category}</div>
        """, unsafe_allow_html=True)
        for item in items:
            st.markdown(f"""
            <div class="packing-item">{item}</div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_export_options(itinerary_json, num_people, city, start_date, end_date, total_cost):
    """Render export options"""
    import json
    from pdf_generator import create_professional_pdf
    from utils import create_calendar_file
    
    st.markdown('<h2 class="section-header">Export Your Journey</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # PDF Export
        try:
            pdf_buffer = create_professional_pdf(itinerary_json, num_people, city, start_date, end_date, total_cost)
            if pdf_buffer:
                st.download_button(
                    "📄 Download PDF",
                    data=pdf_buffer,
                    file_name=f"{city}_elite_itinerary_{start_date}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        except Exception as e:
            st.error(f"PDF generation failed: {e}")
    
    with col2:
        # Calendar Export
        cal_content = create_calendar_file(itinerary_json, start_date)
        st.download_button(
            "📅 Download Calendar",
            data=cal_content,
            file_name=f"{city}_itinerary.ics",
            mime="text/calendar",
            use_container_width=True
        )
    
    with col3:
        # JSON Export
        json_content = json.dumps(itinerary_json, indent=2)
        st.download_button(
            "📋 Download Data",
            data=json_content,
            file_name=f"{city}_itinerary.json",
            mime="application/json",
            use_container_width=True
        )
