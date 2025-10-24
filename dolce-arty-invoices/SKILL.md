---
name: dolce-arty-invoices
description: Generate professional PDF invoices for Dolce Arty (Art by Inga Dubai Art Academy) private art lessons. Use when the user needs to create invoices, billing documents, or payment requests for art classes. Handles private lessons, group sessions, and balance payments with automatic formatting in the established brand style.
---

# Dolce Arty Invoice Generator

Generate professional, branded PDF invoices for Dolce Arty art teaching services that match the established visual identity.

## When to Use This Skill

Use this skill whenever the user needs to:
- Create an invoice for a client
- Generate billing documents for art lessons
- Issue payment requests for private or group classes
- Create balance payment invoices

## Company Information

**Business Name:** Art by Inga  
**Service Brand:** Dolce Arty  
**Location:** Dubai Art Academy  
**Social Media:** @dolcearty (Instagram)

**Banking Details:**
- Bank: ADIB (Abu Dhabi Islamic Bank)
- Account Holder: Inga Chalaia
- Account Number: 29109510
- IBAN: AE630500000000029109510
- SWIFT Code: ABDIAEADXXX

**Payment Terms:** 100% ONCE DELIVERED

## Invoice Generation Process

### Step 1: Gather Required Information

Ask the user for the following details if not provided:

**Client Information:**
- Client name (e.g., "Elizaveta")
- Invoice date (default to today if not specified)

**Service Details:**
- Service type (e.g., "PRIVATE LESSON", "GROUP CLASS", "BALANCE PAYMENT")
- Description (e.g., "1 hrs. Class, 1 person.")
- Amount in DHS (e.g., 350)
- Quantity (typically 1)

**Invoice Number:**
- If not provided, ask the user for the next invoice number (format: 048, 049, etc.)

### Step 2: Read the PDF Skill

Before creating the invoice, ALWAYS read the PDF skill documentation to understand proper PDF generation techniques:

```bash
view /mnt/skills/public/pdf/SKILL.md
```

### Step 3: Generate the PDF Invoice

Create a professional PDF invoice using the exact design specifications below.

**IMPORTANT:** This skill includes the following assets that MUST be used:
- `assets/dolce_arty_logo.png` - Official Dolce Arty logo (extracted from original invoice)
- `assets/footer_pattern.png` - Decorative footer with artistic doodle pattern
- `assets/generate_invoice.py` - Complete Python script ready to use

You can either:
1. **Use the included script:** Run `assets/generate_invoice.py` directly (modify parameters as needed)
2. **Generate custom code:** Follow the design specifications below and use the logo/footer images

## Design Specifications

### Color Palette
- **Background:** Warm beige/cream (#F5EBE0 or similar)
- **Text Primary:** Dark brown (#3D2817)
- **Text Secondary:** Medium brown (#6B4423)
- **Accent:** Warm brown matching the logo

### Layout Structure

**Header Section:**
- Logo "dolce ARTY" in top right corner (brown script font for "dolce", bold caps for "ARTY")
- "invoice" in large serif font, left-aligned

**Client & Business Info Section (Two columns):**
- Left column: Client name in bold
- Left column: Date and Invoice number below client name
- Right column: "Art by Inga" / "Dubai" / "Art Academy" right-aligned

**Line Items Table:**
- Three columns: QUANTITY | DESCRIPTION | SUBTOTAL
- First row: Main service (e.g., "PRIVATE LESSON") with amount
- Additional rows as needed (e.g., description details, balance payments)
- All caps for section headers
- Clear visual separation with horizontal lines

**Totals Section:**
- "TOTAL" label right-aligned
- "TOTAL PAYMENT" with large amount (e.g., "$350.00 DHS")

**Payment Information Section:**
- "Payment Terms: 100% ONCE DELIVERED"
- "Bank Details are as follows:"
- Table format:
  - Row 1: Bank | Name | SWIFT CODE
  - Row 2: Account Number | IBAN Number

**Footer:**
- Decorative border with artistic doodle pattern (optional - can use simple line)
- Instagram handle "@dolcearty" in bottom right

### Typography Guidelines
- Main title "invoice": Large serif font (36-48pt)
- Client name: Bold sans-serif (18-20pt)
- Section headers (QUANTITY, DESCRIPTION, etc.): Bold caps, smaller (10-12pt)
- Service titles (PRIVATE LESSON): Bold (14-16pt)
- Body text: Regular sans-serif (10-12pt)
- Total amount: Large bold (24-28pt)

## Example Invoice Data

**Example 1: Private Lesson**
```
Client: Elizaveta
Date: September 11, 2024
Invoice Nº: 048

Service: PRIVATE LESSON
Description: 1 hrs. Class, 1 person.
Additional: Balance Payment
Amount: $350 DHS
```

**Example 2: Multiple Sessions Package**
```
Client: Ahmed
Date: October 22, 2025
Invoice Nº: 052

Service: PRIVATE LESSON PACKAGE
Description: 4 hrs. Classes, 1 person.
Amount: $1,200 DHS
```

## Implementation Instructions

1. Read the PDF skill first (CRITICAL)
2. Gather all required information from the user
3. Use reportlab or similar PDF library to generate the invoice
4. Match the design specifications exactly:
   - Warm beige background
   - Brown color scheme
   - Clean, professional layout
   - All required sections included
5. Save the PDF with a descriptive filename: `invoice_[ClientName]_[InvoiceNumber]_[Date].pdf`
6. Place the completed invoice in `/mnt/user-data/outputs/`
7. Provide a download link to the user

## Quality Checklist

Before delivering the invoice, verify:
- [ ] Client name is correct
- [ ] Date is properly formatted
- [ ] Invoice number is unique
- [ ] Service description is clear
- [ ] Amount is correct and formatted as "$XXX DHS" or "$XXX.00 DHS"
- [ ] All banking details are accurate
- [ ] PDF matches the brand visual style
- [ ] File is saved in outputs directory
- [ ] Download link is provided to user

## Common Pricing Reference

Based on the Dubai market analysis, typical Dolce Arty pricing:
- Private lesson (1 hour): AED 150-200
- Private lesson (1.5 hours): AED 200-250
- Package of 4 sessions: AED 600-800
- Package of 8 sessions: AED 1,200-1,500
- Travel fee (if applicable): AED 30-50

Note: Always confirm the actual amount with the user - these are reference ranges only.
