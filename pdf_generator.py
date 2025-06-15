"""PDF generation service for travel itineraries"""

from io import BytesIO
import textwrap
from utils import extract_cost, generate_packing_list

def create_professional_pdf(itinerary_json, num_people, city, start_date, end_date, total_cost):
    """Create a professional, beautifully formatted PDF itinerary"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.colors import HexColor, black, white
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
        from reportlab.lib.units import inch
        from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
        
        buffer = BytesIO()
        
        # Create document with margins
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=1*inch,
            bottomMargin=0.75*inch
        )
        
        # Define colors
        primary_color = HexColor('#1e293b')
        secondary_color = HexColor('#3b82f6')
        accent_color = HexColor('#8b5cf6')
        light_gray = HexColor('#f8fafc')
        dark_gray = HexColor('#64748b')
        
        # Get styles and create custom ones
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=primary_color,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=20,
            textColor=secondary_color,
            alignment=TA_CENTER,
            fontName='Helvetica'
        )
        
        section_header_style = ParagraphStyle(
            'SectionHeader',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=12,
            spaceBefore=20,
            textColor=primary_color,
            fontName='Helvetica-Bold'
        )
        
        day_header_style = ParagraphStyle(
            'DayHeader',
            parent=styles['Heading3'],
            fontSize=12,
            spaceAfter=8,
            spaceBefore=15,
            textColor=white,
            backColor=primary_color,
            fontName='Helvetica-Bold',
            leftIndent=10,
            rightIndent=10,
            borderPadding=8
        )
        
        activity_title_style = ParagraphStyle(
            'ActivityTitle',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=4,
            textColor=primary_color,
            fontName='Helvetica-Bold'
        )
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=9,
            spaceAfter=6,
            textColor=black,
            fontName='Helvetica',
            leftIndent=15
        )
        
        tip_style = ParagraphStyle(
            'TipStyle',
            parent=styles['Normal'],
            fontSize=9,
            spaceAfter=8,
            textColor=HexColor('#059669'),
            fontName='Helvetica-Oblique',
            leftIndent=15,
            backColor=HexColor('#f0fdf4'),
            borderColor=HexColor('#10b981'),
            borderWidth=1,
            borderPadding=6
        )
        
        # Build story (content)
        story = []
        
        # Title Page
        story.append(Paragraph(f"✈️ ELITE TRAVEL ITINERARY", title_style))
        story.append(Paragraph(f"{city.upper()}", subtitle_style))
        story.append(Spacer(1, 20))
        
        # Trip Overview Table
        overview_data = [
            ['Trip Details', ''],
            ['Destination', city],
            ['Duration', f"{start_date} to {end_date}"],
            ['Number of Travelers', str(num_people)],
            ['Total Cost', f"₹{total_cost:,}"],
            ['Cost per Person', f"₹{total_cost//num_people:,}"]
        ]
        
        overview_table = Table(overview_data, colWidths=[2*inch, 3*inch])
        overview_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (1, 0), primary_color),
            ('TEXTCOLOR', (0, 0), (1, 0), white),
            ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (1, 0), 12),
            ('BACKGROUND', (0, 1), (1, -1), light_gray),
            ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 1), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (1, -1), 10),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 1, dark_gray),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, light_gray])
        ]))
        
        story.append(overview_table)
        story.append(Spacer(1, 30))
        
        # Destination Info
        if "destination_info" in itinerary_json:
            dest_info = itinerary_json["destination_info"]
            story.append(Paragraph("🌍 DESTINATION INFORMATION", section_header_style))
            
            dest_data = [
                ['Best Time to Visit', dest_info.get('best_time_to_visit', 'N/A')],
                ['Local Currency', dest_info.get('local_currency', 'N/A')],
                ['Language', dest_info.get('language', 'N/A')]
            ]
            
            dest_table = Table(dest_data, colWidths=[2*inch, 3*inch])
            dest_table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (1, -1), 10),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('ROWBACKGROUNDS', (0, 0), (-1, -1), [white, light_gray]),
                ('GRID', (0, 0), (-1, -1), 0.5, dark_gray)
            ]))
            
            story.append(dest_table)
            story.append(Spacer(1, 20))
        
        story.append(PageBreak())
        
        # Daily Itinerary
        story.append(Paragraph("📅 DETAILED ITINERARY", section_header_style))
        story.append(Spacer(1, 15))
        
        for day_data in itinerary_json.get("days", []):
            # Day Header
            day_theme = day_data.get('theme', 'Exploration')
            story.append(Paragraph(f"DAY {day_data['day']}: {day_theme.upper()}", day_header_style))
            story.append(Spacer(1, 10))
            
            # Activities
            for i, activity in enumerate(day_data.get("activities", []), 1):
                # Activity title with time
                time_info = f"{activity.get('start_time', '')} - {activity.get('end_time', '')}"
                activity_header = f"{i}. {activity['title']} ({time_info})"
                story.append(Paragraph(activity_header, activity_title_style))
                
                # Description
                description = activity.get('description', 'N/A')
                if len(description) > 100:
                    description = textwrap.fill(description, width=80)
                story.append(Paragraph(f"<b>Description:</b> {description}", body_style))
                
                # Location
                location = activity.get('location', 'N/A')
                story.append(Paragraph(f"<b>Location:</b> {location}", body_style))
                
                # Cost
                cost = activity.get('cost', 'N/A')
                total_activity_cost = extract_cost(cost) * num_people if cost != 'N/A' else 'N/A'
                if total_activity_cost != 'N/A':
                    story.append(Paragraph(f"<b>Cost:</b> {cost} per person (₹{total_activity_cost:,} total)", body_style))
                else:
                    story.append(Paragraph(f"<b>Cost:</b> {cost}", body_style))
                
                # Insider tip
                tip = activity.get('insider_tip', '')
                if tip:
                    story.append(Paragraph(f"💡 <b>Insider Tip:</b> {tip}", tip_style))
                
                story.append(Spacer(1, 8))
            
            # Daily cost summary
            daily_total = extract_cost(day_data.get('daily_total', '₹0'))
            daily_per_person = daily_total // num_people if daily_total > 0 else 0
            
            daily_summary_data = [
                ['Daily Summary', ''],
                ['Total Cost', f"₹{daily_total:,}"],
                ['Cost per Person', f"₹{daily_per_person:,}"],
                ['Meals', day_data.get('meal_cost', 'N/A')],
                ['Transport', day_data.get('transport_cost', 'N/A')]
            ]
            
            daily_table = Table(daily_summary_data, colWidths=[1.5*inch, 2*inch])
            daily_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (1, 0), secondary_color),
                ('TEXTCOLOR', (0, 0), (1, 0), white),
                ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (1, 0), 10),
                ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (1, 1), (1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (1, -1), 9),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('GRID', (0, 0), (-1, -1), 0.5, dark_gray),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, light_gray])
            ]))
            
            story.append(daily_table)
            story.append(Spacer(1, 20))
        
        # Local Tips
        if "local_tips" in itinerary_json and itinerary_json["local_tips"]:
            story.append(PageBreak())
            story.append(Paragraph("💡 LOCAL TIPS & RECOMMENDATIONS", section_header_style))
            story.append(Spacer(1, 10))
            
            for i, tip in enumerate(itinerary_json["local_tips"], 1):
                story.append(Paragraph(f"{i}. {tip}", body_style))
                story.append(Spacer(1, 6))
        
        # Packing List
        story.append(PageBreak())
        story.append(Paragraph("🎒 PACKING CHECKLIST", section_header_style))
        story.append(Spacer(1, 15))
        
        # Generate packing list
        activities_list = []
        for day in itinerary_json.get("days", []):
            activities_list.extend([act.get('title', '') for act in day.get('activities', [])])
        
        packing_list = generate_packing_list(city, (end_date - start_date).days, activities_list)
        
        for category, items in packing_list.items():
            story.append(Paragraph(f"<b>{category}</b>", activity_title_style))
            for item in items:
                story.append(Paragraph(f"☐ {item}", body_style))
            story.append(Spacer(1, 10))
        
        # Footer info
        story.append(Spacer(1, 30))
        footer_style = ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=8,
            textColor=dark_gray,
            alignment=TA_CENTER,
            fontName='Helvetica-Oblique'
        )
        story.append(Paragraph("Generated by Elite Travel Planner | Safe travels and enjoy your adventure!", footer_style))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer
        
    except ImportError:
        # Fallback to simple PDF if reportlab components not available
        return create_simple_fallback_pdf(itinerary_json, num_people, city, start_date, end_date, total_cost)
    except Exception as e:
        raise RuntimeError(f"PDF generation error: {e}")

def create_simple_fallback_pdf(itinerary_json, num_people, city, start_date, end_date, total_cost):
    """Fallback PDF creation with basic reportlab"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.colors import HexColor
        
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4
        
        # Colors
        primary_color = HexColor('#1e293b')
        secondary_color = HexColor('#3b82f6')
        
        # Header with background
        pdf.setFillColor(primary_color)
        pdf.rect(0, height-80, width, 80, fill=1)
        
        # Title
        pdf.setFillColor(HexColor('#ffffff'))
        pdf.setFont("Helvetica-Bold", 24)
        pdf.drawCentredText(width/2, height-35, f"Elite Travel Itinerary")
        pdf.setFont("Helvetica", 16)
        pdf.drawCentredText(width/2, height-55, f"{city}")
        
        # Reset color
        pdf.setFillColor(HexColor('#000000'))
        
        # Trip details box
        y_pos = height - 120
        pdf.setFillColor(HexColor('#f8fafc'))
        pdf.rect(50, y_pos-60, width-100, 60, fill=1)
        
        pdf.setFillColor(HexColor('#000000'))
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(70, y_pos-20, "Trip Overview")
        
        pdf.setFont("Helvetica", 10)
        pdf.drawString(70, y_pos-35, f"Duration: {start_date} to {end_date}")
        pdf.drawString(70, y_pos-50, f"Travelers: {num_people} | Total Cost: ₹{total_cost:,}")
        
        y_pos -= 100
        
        # Daily itinerary
        for day in itinerary_json.get("days", []):
            if y_pos < 150:
                pdf.showPage()
                y_pos = height - 50
            
            # Day header with background
            pdf.setFillColor(secondary_color)
            pdf.rect(50, y_pos-25, width-100, 25, fill=1)
            
            pdf.setFillColor(HexColor('#ffffff'))
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(60, y_pos-18, f"Day {day['day']}: {day.get('theme', 'Exploration')}")
            
            pdf.setFillColor(HexColor('#000000'))
            y_pos -= 35
            
            for activity in day.get("activities", []):
                if y_pos < 100:
                    pdf.showPage()
                    y_pos = height - 50
                
                # Activity title
                pdf.setFont("Helvetica-Bold", 11)
                title = activity["title"][:70] + "..." if len(activity["title"]) > 70 else activity["title"]
                pdf.drawString(70, y_pos, title)
                y_pos -= 15
                
                # Details
                pdf.setFont("Helvetica", 9)
                
                # Description
                description = activity.get("description", "")[:90] + "..." if len(activity.get("description", "")) > 90 else activity.get("description", "")
                pdf.drawString(80, y_pos, f"Description: {description}")
                y_pos -= 12
                
                # Time and location
                time_info = f"{activity.get('start_time', '')} - {activity.get('end_time', '')}"
                pdf.drawString(80, y_pos, f"Time: {time_info} | Location: {activity.get('location', 'N/A')[:40]}")
                y_pos -= 12
                
                # Cost
                cost = activity.get("cost", "N/A")
                pdf.drawString(80, y_pos, f"Cost: {cost}")
                y_pos -= 20
            
            # Daily total
            daily_total = extract_cost(day.get('daily_total', '₹0'))
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(70, y_pos, f"Day {day['day']} Total: ₹{daily_total:,}")
            y_pos -= 30
        
        # Footer
        pdf.setFont("Helvetica-Oblique", 8)
        pdf.drawCentredText(width/2, 30, "Generated by Elite Travel Planner")
        
        pdf.save()
        buffer.seek(0)
        return buffer
        
    except Exception as e:
        raise RuntimeError(f"Fallback PDF generation error: {e}")
