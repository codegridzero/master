#!/usr/bin/env python3
"""
Interactive Standalone Test Script for Hostinger SMTP Module.

Allows testing plain text emails, HTML emails, and the professional
RISS Cold Pitch Template with custom prospect details and live website demo URLs.
"""

import sys
from pathlib import Path
from smtp_sender import (
    send_email,
    send_cold_pitch_email,
    SMTPConfigError,
    SMTPAuthenticationFailedError,
    SMTPSendingError,
    SMTPError,
)
from email_templates import render_cold_pitch_email


def prompt_input(label: str, default: str = "") -> str:
    """Helper to prompt user input with a default fallback."""
    suffix = f" [{default}]" if default else ""
    try:
        val = input(f"{label}{suffix}: ").strip()
        return val if val else default
    except (KeyboardInterrupt, EOFError):
        print("\nOperation cancelled.")
        sys.exit(0)


def test_cold_pitch():
    """Interactively sends a high-converting Cold Pitch HTML email."""
    print("\n--- [Option 1] Send Professional Cold Pitch Email ---")
    recipient = prompt_input("Recipient Email Address (e.g. client@example.com)")
    if not recipient:
        print("ERROR: Recipient email address cannot be empty.")
        return

    recipient_name = prompt_input("Prospect / Contact Name", "John")
    company_name = prompt_input("Prospect Company Name", "Mechanical Plumbing Systems, Inc.")
    preview_url = prompt_input(
        "Website Demo Preview Link",
        "https://masterplumber.vercel.app/Mechanical%20Plumbing%20Systems/"
    )
    subject = prompt_input("Subject Line", f"Quick website preview for {company_name}")

    print("\nPreparing email with RISS branding, logo & responsive design...")
    print(f"To: {recipient}")
    print(f"Company: {company_name}")
    print(f"Demo Link: {preview_url}")
    print("\nSending via Hostinger SMTP...")

    try:
        result = send_cold_pitch_email(
            to=recipient,
            recipient_name=recipient_name,
            company_name=company_name,
            preview_url=preview_url,
            subject=subject,
        )
        print("\n✅ SUCCESS: Cold pitch email successfully sent!")
        print(f"Details: {result.get('message')}")
    except SMTPConfigError as cfg_err:
        print(f"\n❌ CONFIGURATION ERROR: {cfg_err}")
    except SMTPAuthenticationFailedError as auth_err:
        print(f"\n❌ AUTHENTICATION ERROR: {auth_err}")
    except SMTPSendingError as send_err:
        print(f"\n❌ SENDING ERROR: {send_err}")
    except SMTPError as smtp_err:
        print(f"\n❌ SMTP ERROR: {smtp_err}")
    except Exception as exc:
        print(f"\n❌ UNEXPECTED ERROR: {exc}")


def test_plain_email():
    """Interactively sends a basic plain-text test email."""
    print("\n--- [Option 2] Send Simple Test Email ---")
    recipient = prompt_input("Recipient Email Address")
    if not recipient:
        print("ERROR: Recipient email address cannot be empty.")
        return

    subject = prompt_input("Subject", "Hostinger SMTP Test")
    body = prompt_input("Message Body", "This is a test email from RISS SMTP module.")

    print("\nSending...")
    try:
        result = send_email(to=recipient, subject=subject, body=body)
        print("\n✅ SUCCESS: Email sent successfully.")
        print(f"Details: {result.get('message')}")
    except SMTPConfigError as cfg_err:
        print(f"\n❌ CONFIGURATION ERROR: {cfg_err}")
    except SMTPAuthenticationFailedError as auth_err:
        print(f"\n❌ AUTHENTICATION ERROR: {auth_err}")
    except SMTPSendingError as send_err:
        print(f"\n❌ SENDING ERROR: {send_err}")
    except Exception as exc:
        print(f"\n❌ UNEXPECTED ERROR: {exc}")


def export_preview():
    """Exports a local preview_template.html for browser preview."""
    print("\n--- [Option 3] Export Local HTML Preview ---")
    recipient_name = prompt_input("Prospect Name", "John")
    company_name = prompt_input("Company Name", "Mechanical Plumbing Systems, Inc.")
    preview_url = prompt_input(
        "Website Demo Preview Link",
        "https://masterplumber.vercel.app/Mechanical%20Plumbing%20Systems/"
    )

    rendered = render_cold_pitch_email(
        recipient_name=recipient_name,
        company_name=company_name,
        preview_url=preview_url
    )

    out_file = Path(__file__).resolve().parent / "preview_template.html"
    out_file.write_text(rendered["html"], encoding="utf-8")
    print(f"\n✅ Preview file generated: {out_file}")
    print("You can open this HTML file directly in any web browser to view the design.")


def main():
    print("=" * 65)
    print(" RISS SMTP & Cold Email Interactive Tester")
    print("=" * 65)
    print("1. Send Professional Cold Pitch Email (HTML + Logo + Demo Link)")
    print("2. Send Simple Plain-Text Test Email")
    print("3. Export/Update Local HTML Preview (preview_template.html)")
    print("4. Exit")
    print("-" * 65)

    choice = prompt_input("Select an option (1-4)", "1")

    if choice == "1":
        test_cold_pitch()
    elif choice == "2":
        test_plain_email()
    elif choice == "3":
        export_preview()
    elif choice == "4":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Invalid selection. Exiting.")


if __name__ == "__main__":
    main()
