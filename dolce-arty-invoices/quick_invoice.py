#!/usr/bin/env python3
"""
Quick Invoice Generator - CLI Tool
Usage: python quick_invoice.py "Client Name" hours invoice_number
Example: python quick_invoice.py "Maria Lopez" 2 140
"""

import sys
import os
sys.path.insert(0, '/home/claude/dolce-arty-invoices')
from invoice_generator import create_invoice
from datetime import datetime

def main():
    if len(sys.argv) < 4:
        print("Usage: python quick_invoice.py 'Client Name' hours invoice_number")
        print("Example: python quick_invoice.py 'Maria Lopez' 2 140")
        sys.exit(1)
    
    client_name = sys.argv[1]
    hours = float(sys.argv[2])
    invoice_number = sys.argv[3]
    
    # Calculate amount
    amount = int(hours * 350)
    
    # Generate filename
    filename = f"invoice_{client_name.replace(' ', '')}_{invoice_number}.pdf"
    output_path = f"/mnt/user-data/outputs/{filename}"
    
    # Create invoice
    create_invoice(
        output_path=output_path,
        client_name=client_name,
        invoice_number=invoice_number,
        description=f"{hours} hr{'s' if hours != 1 else ''}. Class, 1 person.",
        amount=str(amount)
    )
    
    print(f"\n✅ Invoice #{invoice_number} created!")
    print(f"   Client: {client_name}")
    print(f"   Hours: {hours}")
    print(f"   Amount: {amount}.00 DHS")
    print(f"   Date: {datetime.now().strftime('%B %d, %Y')}")
    print(f"   File: {filename}")

if __name__ == "__main__":
    main()
