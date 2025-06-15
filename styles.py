"""CSS styles for TripGenie.AI"""

import streamlit as st

def load_elite_css():
    """Load the elite professional CSS styling"""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@400;500;600;700&display=swap');
    
    /* Global Reset & Base */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .main {
        background: transparent;
        padding: 0;
    }
    
    .block-container {
        padding: 0;
        max-width: none;
    }
    
    /* Hide Streamlit Elements */
    #MainMenu, footer, header, .stDeployButton {
        visibility: hidden;
        height: 0;
    }
    
    /* Custom Header */
    .elite-header {
        background: linear-gradient(135deg, #1e293b 0%, #334155 50%, #475569 100%);
        padding: 4rem 2rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .elite-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="0.5" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        opacity: 0.3;
    }
    
    .elite-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1rem;
        position: relative;
        z-index: 2;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .elite-subtitle {
        font-size: 1.25rem;
        color: #e2e8f0;
        font-weight: 400;
        position: relative;
        z-index: 2;
        opacity: 0.9;
    }
    
    /* Sidebar Redesign */
    .css-1d391kg {
        background: #ffffff;
        border-right: 1px solid #e2e8f0;
        box-shadow: 2px 0 10px rgba(0,0,0,0.05);
        padding: 2rem 1.5rem;
    }
    
    .sidebar-header {
        text-align: center;
        margin-bottom: 2rem;
        padding-bottom: 1.5rem;
        border-bottom: 2px solid #f1f5f9;
    }
    
    .sidebar-logo {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .sidebar-tagline {
        font-size: 0.875rem;
        color: #64748b;
        font-weight: 500;
    }
    
    .section-title {
        font-size: 0.875rem;
        font-weight: 700;
        color: white !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stDateInput > div > div > input {
        background: black;
        border: 2px solid #e2e8f0;
        border-radius: 8px;
        padding: 0.75rem;
        font-size: 0.875rem;
        font-weight: 500;
        color: white;
    }

    /* Focus styles */
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stDateInput > div > div > input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        outline: none;
    }

    /* Selectbox and Multiselect */
    .css-1wa3eu0-placeholder,
    .css-1uccc91-singleValue,
    .css-319lph-ValueContainer {
        color: white !important;
        background-color: black !important;
    }

    .css-1n7v3ny-option,
    .css-9gakcf-option {
        background-color: black !important;
        color: white !important;
    }

    .css-1n7v3ny-option:hover {
        background-color: #3b82f6 !important;
        color: white !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 1rem 2rem;
        font-weight: 600;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: all 0.3s ease;
        width: 100%;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.4);
    }
    
    /* Success Alert */
    .success-banner {
        background: linear-gradient(135deg, #d0e8ff 0%, #a8cfff 100%);
        color: black;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }
    
    /* Trip Overview Cards */
    .overview-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #f1f5f9;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .overview-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
    }
    
    .overview-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    
    .card-title {
        font-family: 'Playfair Display', serif;
        font-size: 0.875rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 1rem;
    }
    
    .card-content {
        font-family: 'Playfair Display', serif;
        font-size: 0.95rem;
        color: #374151;
        line-height: 1.6;
    }
    
    .cost-card {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        color: #ffffff;
        text-align: center;
    }
    
    .cost-amount {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        margin: 1rem 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .cost-label {
        font-size: 1rem;
        opacity: 0.9;
        font-weight: 500;
    }
    
    /* Section Headers */
    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 2.25rem;
        font-weight: 600;
        color: #1e293b;
        margin: 3rem 0 2rem 0;
        text-align: center;
        position: relative;
    }
    
    h2.section-header {
        color: #1e293b !important;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -0.5rem;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        border-radius: 2px;
    }
    
    /* Day Accordion */
    .day-accordion {
        background: #ffffff;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #f1f5f9;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .day-accordion:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    
    /* Activity Cards */
    .activity-container {
        padding: 2rem;
        background: #ffffff;
    }
    
    .activity-card {
        display: grid;
        grid-template-columns: 1fr auto;
        gap: 2rem;
        padding: 2rem;
        margin-bottom: 1.5rem;
        background: #f8fafc;
        border-radius: 12px;
        border-left: 4px solid #3b82f6;
        transition: all 0.3s ease;
    }
    
    .activity-card:hover {
        background: #f1f5f9;
        transform: translateX(4px);
    }
    
    .activity-info h5 {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    
    .activity-detail {
        font-size: 0.9rem;
        color: #4b5563;
        margin: 0.5rem 0;
        line-height: 1.6;
    }
    
    .activity-detail strong {
        color: #1e293b;
        font-weight: 600;
    }
    
    .activity-tip {
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
        border: 1px solid #a7f3d0;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
        font-size: 0.875rem;
        color: #065f46;
        font-style: italic;
    }
    
    .cost-display {
        text-align: center;
        min-width: 140px;
    }
    
    .cost-primary {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.25rem;
    }
    
    .cost-secondary {
        font-size: 0.875rem;
        color: #64748b;
        font-weight: 500;
    }
    
    /* Daily Summary */
    .daily-summary {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        color: #ffffff;
        padding: 1.5rem;
        text-align: center;
        font-size: 1.125rem;
        font-weight: 600;
        margin-top: 2rem;
        border-radius: 12px;
    }
    
    /* Tips Section */
    .tips-container {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        border-radius: 16px;
        padding: 2rem;
        margin: 3rem 0;
        border: 1px solid #fbbf24;
    }
    
    .tips-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: #1a1817;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    h3.tips-title {
        color: #1a1817 !important;
    }
    
    .tip-item {
        background: #ffffff;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 8px;
        border-left: 4px solid #f59e0b;
        font-size: 0.95rem;
        color: #374151;
        line-height: 1.6;
    }
    
    /* Packing List */
    .packing-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    .packing-card {
        background: #f1f5f9;
        border-radius: 16px;
        padding: 1.75rem;
        box-shadow: 0 8px 16px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
    }

    .packing-card:hover {
        transform: translateY(-6px);
    }

    .packing-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1.25rem;
        color: #0f172a;
        border-bottom: 2px solid #cbd5e1;
        padding-bottom: 0.6rem;
    }

    .packing-item {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-size: 1.125rem;
        color: #1e293b;
        margin-bottom: 0.75rem;
    }

    .packing-item::before {
        content: "🧳";
        font-size: 1.1rem;
    }
    
    /* Welcome Screen */
    .welcome-hero {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
        border-radius: 20px;
        margin-bottom: 3rem;
    }
    
    .welcome-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    
    h1.welcome-title {
        color: #1e293b !important;
    }
    
    .welcome-subtitle {
        font-size: 1.125rem;
        color: #64748b;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    .feature-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #f1f5f9;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    
    .feature-description {
        font-size: 0.95rem;
        color: #64748b;
        line-height: 1.6;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .elite-title {
            font-size: 2.5rem;
        }
        
        .activity-card {
            grid-template-columns: 1fr;
            gap: 1rem;
        }
        
        .cost-display {
            text-align: left;
            min-width: auto;
        }
    }
    </style>
    """, unsafe_allow_html=True)
