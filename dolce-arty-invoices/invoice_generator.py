#!/usr/bin/env python3
"""
Dolce Arty Invoice Generator - Final Version
Reusable module for generating invoices
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from datetime import datetime

def create_invoice(output_path, client_name, invoice_number, description, amount, 
                   date=None, service_type="PRIVATE LESSON", quantity=1, balance_payment=True):
    """
    Generate a Dolce Arty branded invoice
    
    Args:
        output_path: Path where PDF will be saved
        client_name: Client's name
        invoice_number: Invoice number (e.g., "138")
        date: Date string (e.g., "October 22, 2025") - defaults to today if None
        service_type: Type of service (default: "PRIVATE LESSON")
        description: Service description (e.g., "2 hrs. Class, 1 person.")
        amount: Amount in DHS (as string, e.g., "700")
        quantity: Quantity (default 1)
        balance_payment: Show balance payment line (default True)
    """
    
    # Use current date if not provided
    if date is None:
        date = datetime.now().strftime("%B %d, %Y")
    
    # Define colors - using exact logo brown
    bg_color = HexColor('#F5EBE0')
    text_primary = HexColor('#582c00')
    text_secondary = HexColor('#8B5A00')
    
    # Create canvas
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    # Draw background color
    c.setFillColor(bg_color)
    c.rect(0, 0, width, height, fill=True, stroke=False)
    
    # ===== HEADER SECTION =====
    c.setFillColor(text_primary)
    c.setFont("Helvetica-Bold", 48)
    c.drawString(100, height - 150, "Invoice")
    
    # Logo image (right side)
    logo_path = "/home/claude/dolce-arty-invoices/assets/dolce_arty_logo.png"
    logo_width = 1.6 * inch
    logo_height = 1.16 * inch
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
    y_pos = height - 340
    
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
    y_pos -= 35
    c.setFillColor(text_primary)
    c.setFont("Helvetica", 12)
    c.drawString(110, y_pos, str(quantity))
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(250, y_pos, service_type)
    
    c.setFont("Helvetica-Bold", 14)
    c.drawRightString(width - 100, y_pos, f"{amount} DHS")
    
    # Description line
    y_pos -= 25
    c.setFont("Helvetica", 11)
    c.drawString(250, y_pos, description)
    
    # Balance Payment line (if applicable)
    if balance_payment:
        y_pos -= 35
        c.setFont("Helvetica-Bold", 12)
        c.drawString(250, y_pos, "Balance Payment")
        c.drawRightString(width - 100, y_pos, f"{amount} DHS")
    
    # ===== TOTAL SECTION =====
    y_pos -= 45
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(text_secondary)
    c.drawRightString(width - 250, y_pos, "TOTAL")
    
    c.setStrokeColor(text_secondary)
    c.setLineWidth(0.5)
    c.line(100, y_pos - 5, width - 100, y_pos - 5)
    
    # Total payment
    y_pos -= 32
    c.setFillColor(text_primary)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y_pos, "TOTAL PAYMENT")
    
    c.setFont("Helvetica-Bold", 20)
    c.drawRightString(width - 100, y_pos, f"{amount}.00 DHS")
    
    # ===== PAYMENT INFORMATION SECTION =====
    y_pos -= 45
    c.setStrokeColor(text_secondary)
    c.setLineWidth(1)
    c.line(100, y_pos, width - 100, y_pos)
    
    y_pos -= 18
    c.setFillColor(text_primary)
    c.setFont("Helvetica", 10)
    c.drawString(100, y_pos, "Payment Terms:")
    y_pos -= 13
    c.drawString(100, y_pos, "100% ONCE DELIVERED")
    
    y_pos -= 18
    c.drawString(100, y_pos, "Bank Details are as follows:")
    
    # Bank details table
    y_pos -= 18
    c.setFont("Helvetica-Bold", 9)
    c.drawString(100, y_pos, "Bank")
    c.drawString(250, y_pos, "Name")
    c.drawString(420, y_pos, "SWIFT CODE")
    
    y_pos -= 13
    c.setFont("Helvetica", 9)
    c.drawString(100, y_pos, "ADIB")
    c.drawString(250, y_pos, "Inga Chalaia")
    c.drawString(420, y_pos, "ABDIAEADXXX")
    
    y_pos -= 18
    c.setFont("Helvetica-Bold", 9)
    c.drawString(100, y_pos, "Account Number")
    c.drawString(250, y_pos, "IBAN Number")
    
    y_pos -= 13
    c.setFont("Helvetica", 9)
    c.drawString(100, y_pos, "29109510")
    c.drawString(250, y_pos, "AE630500000000029109510")
    
    # ===== INSTAGRAM LOGO IN BOTTOM RIGHT =====
    instagram_path = "/home/claude/dolce-arty-invoices/assets/instagram_logo.png"
    ig_width = 1.5 * inch
    ig_height = ig_width / 4.22
    
    c.drawImage(instagram_path, width - 100 - ig_width, 30, 
                width=ig_width, height=ig_height, mask='auto', preserveAspectRatio=True)
    
    c.save()
    return output_path

if __name__ == "__main__":
    # Test
    create_invoice(
        output_path="/tmp/test_invoice.pdf",
        client_name="Test Client",
        invoice_number="999",
        date=datetime.now().strftime("%B %d, %Y"),
        service_type="PRIVATE LESSON",
        description="1 hr. Class, 1 person.",
        amount="350",
        quantity=1,
        balance_payment=True
    )
    print("✅ Test invoice created")
