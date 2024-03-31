#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/29 11:42
# @Author  : 晚秋
# @File    : tools.py
# @Description : 文件作用注释
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


def create_pdf_with_image(output_path, image_path, items_list, financial_summary, invoice_info, bill_to_info):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter  # Get the width and height of the page

    # Load and place the image
    logo = ImageReader(image_path)
    logo_width, logo_height = logo.getSize()
    max_height = 50
    if logo_height > max_height:
        scale_factor = max_height / float(logo_height)
        logo_width *= scale_factor
        logo_height = max_height
    c.drawImage(logo, 50, height - 50 - logo_height, width=logo_width, height=logo_height)

    # Invoice information
    text_start_height = height - 50 - logo_height - 20
    c.setFont("Helvetica", 10)
    c.drawString(50, text_start_height - 20, f"Invoice No: {invoice_info['Invoice No']}")
    c.drawString(50, text_start_height - 35, f"Customer ID: {invoice_info['Customer ID']}")
    c.drawString(300, text_start_height - 20, f"Invoice Date: {invoice_info['Invoice Date']}")
    c.drawString(300, text_start_height - 35, f"Payment Terms: {invoice_info['Payment Terms']}")
    c.drawString(300, text_start_height - 50, f"Currency: {invoice_info['Currency']}")

    # Bill To:
    bill_to_height = text_start_height - 80
    c.drawString(50, bill_to_height, "Bill To:")
    for i, line in enumerate(bill_to_info, start=1):
        c.drawString(50, bill_to_height - 15 * i, line)

    # Dynamic position for items table based on bill to section
    table_header_height = bill_to_height - 15 * len(bill_to_info) - 25

    # Drawing table headers
    c.drawString(50, table_header_height, "Line")
    c.drawString(80, table_header_height, "Description")
    c.drawString(350, table_header_height, "Quantity")
    c.drawString(400, table_header_height, "Unit Price")
    c.drawString(470, table_header_height, "Amount")
    c.drawString(540, table_header_height, "Tax Code")

    # Drawing items from the list
    item_height = table_header_height - 20
    line_number = 1
    for item in items_list:
        c.drawString(50, item_height, str(line_number))
        c.drawString(80, item_height, item["Description"])
        c.drawString(350, item_height, str(item["Quantity"]))
        c.drawString(400, item_height, "{:.2f}".format(item["Unit Price"]))
        c.drawString(470, item_height, "{:.2f}".format(item["Amount"]))
        c.drawString(540, item_height, item["Tax Code"])
        item_height -= 20  # Move to the next line
        line_number += 1

    # Totals (using the financial_summary dictionary)
    totals_height = item_height - 90
    c.drawString(420, totals_height, "Basic:")
    c.drawString(470, totals_height, financial_summary["basic"])
    c.drawString(420, totals_height - 15, "Other Taxes:")
    c.drawString(500, totals_height - 15, financial_summary["Other Taxes"])
    c.drawString(420, totals_height - 30, "AMOUNT DUE:")
    c.drawString(500, totals_height - 30, financial_summary["Amount Due"])

    # Footer with payment information
    # Footer with detailed payment information
    payment_details = """
        Payment Options:
        Wire Payments/EFT: Please include Invoice Number with payment and 
        send an email confirmation when sending funds
        Account Name: Queen's University at Kingston
        Bank: Bank of Montreal, 297 King St. East, Kingston, ON K7L 3B3
        Bank: 001 Transit: 00162 Account: 0000-085 
        Swift/BIC: BOFMCAM2 IBAN: 001001620000085
        banking@queensu.ca

        Cheques: Please include Invoice Number with Payment
        Please make cheques payable to Queen's University at Kingston and remit to:
        Queen's University, Financial Services
        355 King Street West, Kingston, ON, K7L 3N6

        Payment Instructions:
        Please include the invoice number as payment reference AND email remittance 
        MUST be sent to banking@queensu.ca
        The amount paid must be the same amount and currency shown on the invoice, 
        net of any bank fees.

        THANK YOU FOR YOUR BUSINESS
        """

    # Draw the payment details text
    text_object = c.beginText(50, 200)
    text_object.setFont("Helvetica", 7)
    for line in payment_details.split('\n'):
        text_object.textLine(line.strip())
    c.drawText(text_object)
    c.save()