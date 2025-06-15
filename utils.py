"""Utility functions for TripGenie.AI"""

import re
from datetime import datetime, timedelta

def extract_cost(cost_text):
    """Extract numeric cost from formatted price string"""
    if not cost_text or cost_text == "N/A":
        return 0
    cost_text = str(cost_text).replace(",", "").replace("₹", "").lower()
    match = re.search(r"(\d+(\.\d+)?)(k?)", cost_text)
    if match:
        value = float(match.group(1))
        if match.group(3) == "k":
            value *= 1000
        return int(value)
    return 0

def analyze_budget_breakdown(itinerary_json, num_people):
    """Analyze budget breakdown by categories"""
    categories = {"Activities": 0, "Meals": 0, "Transport": 0}
    
    for day in itinerary_json.get("days", []):
        for activity in day.get("activities", []):
            cost = extract_cost(activity.get("cost", "₹0")) * num_people
            categories["Activities"] += cost
        
        categories["Meals"] += extract_cost(day.get("meal_cost", "₹0")) * num_people
        categories["Transport"] += extract_cost(day.get("transport_cost", "₹0")) * num_people
    
    return categories

def generate_packing_list(destination, days, activities):
    """Generate smart packing list based on destination and activities"""
    packing_list = {
        "Travel Documents": ["Passport/ID", "Travel insurance", "Booking confirmations", "Emergency contacts"],
        "Electronics": ["Phone charger", "Power bank", "Camera", "Travel adapter", "Headphones"],
        "Clothing": ["Weather-appropriate clothing", "Comfortable walking shoes", "Sleepwear", "Undergarments"],
        "Personal Care": ["Toiletries", "Medications", "Sunscreen", "Hand sanitizer", "First aid kit"]
    }
    
    activity_text = " ".join(activities).lower()
    if "outdoor" in activity_text or "hiking" in activity_text:
        packing_list["Outdoor Equipment"] = ["Sunglasses", "Hat", "Water bottle", "Backpack", "Weather protection"]
    
    if "swim" in activity_text or "beach" in activity_text:
        packing_list["Beach/Pool Items"] = ["Swimwear", "Beach towel", "Flip-flops", "Waterproof bag"]
    
    return packing_list

def create_calendar_file(itinerary_json, start_date):
    """Create ICS calendar file content"""
    calendar_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Travel Planner//EN\n"
    
    base_date = datetime.combine(start_date, datetime.min.time())
    
    for day_data in itinerary_json.get("days", []):
        event_time = base_date + timedelta(days=day_data["day"] - 1, hours=10)
        
        for activity in day_data.get("activities", []):
            start_time = event_time.strftime("%Y%m%dT%H%M%S")
            end_time = (event_time + timedelta(hours=2)).strftime("%Y%m%dT%H%M%S")
            
            calendar_content += f"""BEGIN:VEVENT
DTSTART:{start_time}
DTEND:{end_time}
SUMMARY:{activity['title']}
DESCRIPTION:{activity.get('description', '')}
LOCATION:{activity.get('location', '')}
END:VEVENT
"""
            event_time += timedelta(hours=2.5)
    
    calendar_content += "END:VCALENDAR"
    return calendar_content

def toggle_day_expansion(day_num, expanded_days):
    """Toggle day expansion state"""
    if day_num in expanded_days:
        expanded_days.remove(day_num)
    else:
        expanded_days.add(day_num)
    return expanded_days
