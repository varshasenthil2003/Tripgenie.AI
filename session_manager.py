"""Session state management for TripGenie.AI"""

import streamlit as st

def initialize_session_state():
    """Initialize session state variables"""
    if 'itinerary_generated' not in st.session_state:
        st.session_state.itinerary_generated = False
    if 'itinerary_data' not in st.session_state:
        st.session_state.itinerary_data = None
    if 'total_cost' not in st.session_state:
        st.session_state.total_cost = 0
    if 'expanded_days' not in st.session_state:
        st.session_state.expanded_days = set()

def reset_session():
    """Reset session state for new journey"""
    st.session_state.itinerary_generated = False
    st.session_state.itinerary_data = None
    st.session_state.total_cost = 0
    st.session_state.expanded_days = set()

def store_itinerary(itinerary_data, total_cost):
    """Store itinerary data in session state"""
    st.session_state.itinerary_data = itinerary_data
    st.session_state.total_cost = total_cost
    st.session_state.itinerary_generated = True
