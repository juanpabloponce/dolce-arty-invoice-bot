#!/usr/bin/env python3
"""
Dolce Arty Invoice Generator - Exact Replica
Generates professional branded invoices matching the established design exactly
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from datetime import datetime

def create_invoice(output_path, client_name, invoice_number, date, service_type, 
                   description, amount, quantity=1, balance_payment=True):
    """Generate a Dolce Arty branded invoice matching the exact original design"""
    
    # Define colors - matching the original
    bg_color = HexColor('#F5EBE0')
    text_primary = HexColor('#2B1810')  # Darker brown for main text
    text_secondary = HexColor('#6B4423')  # Medium brown
    
    # Create canvas
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    # Draw background color
    c.setFillColor(bg_color)
    c.rect(0, 0, width, height, fill=True, stroke=False)
    
    # Draw background pattern over the beige color
    c.saveState()
    pattern_path = "/home/claude/dolce-arty-invoices/assets/fondo_patron.png"
    # Draw pattern covering the full page with low opacity
    c.setFillAlpha(0.25)  # 25% opacity for subtle pattern effect
    c.drawImage(pattern_path, 0, 0, 
                width=width, height=height, preserveAspectRatio=False)
    c.restoreState()
    
    # ===== HEADER SECTION =====
    # "invoice" title (left side) - using sans-serif lowercase with spacing
    c.setFillColor(text_primary)
    c.setFont("Helvetica", 48)
    c.drawString(100, height - 150, "invoice")
    
    # Logo image (right side) - maintaining correct aspect ratio (1.38:1)
    logo_path = "/home/claude/dolce-arty-invoices/assets/dolce_arty_logo.png"
    logo_width = 1.6 * inch
    logo_height = 1.16 * inch  # Maintains 1.38:1 ratio
    c.drawImage(logo_path, width - 100 - logo_width, height - 120, 
                width=logo_width, height=logo_height, mask='auto', preserveAspectRatio=True)
    
    # ===== CLIENT & BUSINESS INFO SECTION =====
    y_pos = height - 230
    
    # Left column - Client info
    c.setFillColor(text_primary)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, y_pos, client_name)
    
    c.setFont("Helvetica", 11)
    c.drawString(100, y_pos - 25, f"Date: {date}")
    c.drawString(100, y_pos - 42, f"Invoice Nº: {invoice_number}")
    
    # Right column - Business info
    c.setFont("Helvetica-Bold", 14)
    c.drawRightString(width - 100, y_pos, "Art by Inga")
    c.setFont("Helvetica", 12)
    c.drawRightString(width - 100, y_pos - 18, "Dubai")
    c.setFont("Helvetica-Bold", 12)
    c.drawRightString(width - 100, y_pos - 36, "Art Academy")
    
    # ===== LINE ITEMS TABLE =====
    y_pos = height - 350
    
    # Table headers
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(text_secondary)
    c.drawString(100, y_pos, "QUANTITY")
    c.drawString(250, y_pos, "DESCRIPTION")
    c.drawRightString(width - 100, y_pos, "SUBTOTAL")
    
    # Header line
    c.setStrokeColor(text_secondary)
    c.setLineWidth(1)
    c.line(100, y_pos - 5, width - 100, y_pos - 5)
    
    # Service line
    y_pos -= 40
    c.setFillColor(text_primary)
    c.setFont("Helvetica", 12)
    c.drawString(110, y_pos, str(quantity))
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(250, y_pos, service_type)
    
    c.setFont("Helvetica-Bold", 14)
    c.drawRightString(width - 100, y_pos, f"${amount} DHS")
    
    # Description line
    y_pos -= 28
    c.setFont("Helvetica", 11)
    c.drawString(250, y_pos, description)
    
    # Balance Payment line (if applicable)
    if balance_payment:
        y_pos -= 40
        c.setFont("Helvetica-Bold", 12)
        c.drawString(250, y_pos, "Balance Payment")
        c.drawRightString(width - 100, y_pos, f"${amount} DHS")
    
    # ===== TOTAL SECTION =====
    y_pos -= 70
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(text_secondary)
    c.drawRightString(width - 250, y_pos, "TOTAL")
    
    c.setStrokeColor(text_secondary)
    c.setLineWidth(0.5)
    c.line(100, y_pos - 5, width - 100, y_pos - 5)
    
    # Total payment
    y_pos -= 35
    c.setFillColor(text_primary)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y_pos, "TOTAL PAYMENT")
    
    c.setFont("Helvetica-Bold", 28)
    c.drawRightString(width - 100, y_pos, f"${amount}.00 DHS")
    
    # ===== PAYMENT INFORMATION SECTION =====
    y_pos -= 70
    c.setStrokeColor(text_secondary)
    c.setLineWidth(1)
    c.line(100, y_pos, width - 100, y_pos)
    
    y_pos -= 30
    c.setFillColor(text_primary)
    c.setFont("Helvetica", 11)
    c.drawString(100, y_pos, "Payment Terms:")
    y_pos -= 18
    c.drawString(100, y_pos, "100% ONCE DELIVERED")
    
    y_pos -= 30
    c.drawString(100, y_pos, "Bank Details are as follows:")
    
    # Bank details table
    y_pos -= 30
    c.setFont("Helvetica-Bold", 11)
    c.drawString(100, y_pos, "Bank")
    c.drawString(280, y_pos, "Name")
    c.drawString(470, y_pos, "SWIFT CODE")
    
    y_pos -= 18
    c.setFont("Helvetica", 11)
    c.drawString(100, y_pos, "ADIB")
    c.drawString(280, y_pos, "Inga Chalaia")
    c.drawString(470, y_pos, "ABDIAEADXXX")
    
    y_pos -= 28
    c.setFont("Helvetica-Bold", 11)
    c.drawString(100, y_pos, "Account Number")
    c.drawString(280, y_pos, "IBAN Number")
    
    y_pos -= 18
    c.setFont("Helvetica", 11)
    c.drawString(100, y_pos, "29109510")
    c.drawString(280, y_pos, "AE630500000000029109510")
    
    # ===== FOOTER =====
    # Decorative footer pattern
    footer_path = "/home/claude/dolce-arty-invoices/assets/footer_pattern.png"
    footer_height = 1.5 * inch
    c.drawImage(footer_path, 0, 0, 
                width=width, height=footer_height, preserveAspectRatio=True, mask='auto')
    
    # Instagram handle overlay on footer
    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor('#FFFFFF'))  # White text on the footer
    c.drawRightString(width - 100, 0.3 * inch, "@dolcearty")
    
    # Save the PDF
    c.save()
    print(f"✅ Invoice created successfully: {output_path}")

if __name__ == "__main__":
    # Test invoice
    create_invoice(
        output_path="/mnt/user-data/outputs/invoice_MariaGonzalez_055_Oct22_2025.pdf",
        client_name="María González",
        invoice_number="055",
        date="October 22, 2025",
        service_type="PRIVATE LESSON",
        description="1.5 hrs. Class, 1 person.",
        amount="200",
        quantity=1,
        balance_payment=True
    )
