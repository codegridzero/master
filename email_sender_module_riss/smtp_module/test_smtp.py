#!/usr/bin/env python3
"""
Interactive Standalone Test Script for Hostinger SMTP Module.

Prompts for recipient details and sends a test email to verify credentials
and connectivity without exposing sensitive information.
"""

import sys
from smtp_sender import (
    send_email,
    SMTPConfigError,
    SMTPAuthenticationFailedError,
    SMTPSendingError,
    SMTPError,
)


def run_test():
    print("=" * 60)
    print(" Hostinger SMTP Interactive Test")
    print("=" * 60)
    print("Note: Ensure your SMTP password is set in .env before running.")
    print()

    # Recipient Input
    try:
        recipient = input("Recipient email: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nTest cancelled.")
        sys.exit(0)

    if not recipient:
        print("ERROR: Recipient email address cannot be empty.")
        sys.exit(1)

    # Subject Input (with default)
    try:
        subject_input = input("Subject [Hostinger SMTP Test]: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nTest cancelled.")
        sys.exit(0)
    subject = subject_input if subject_input else "Hostinger SMTP Test"

    # Message Input (with default)
    try:
        body_input = input("Message [This is a test email.]: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nTest cancelled.")
        sys.exit(0)
    body = body_input if body_input else "This is a test email."

    print("\nSending...")
    try:
        result = send_email(
            to=recipient,
            subject=subject,
            body=body
        )
        print("\nSUCCESS: Email sent successfully.")
        print(f"Details: {result.get('message', 'Delivered to SMTP server.')}")
    except SMTPConfigError as cfg_err:
        print(f"\nCONFIGURATION ERROR: {cfg_err}")
    except SMTPAuthenticationFailedError as auth_err:
        print(f"\nAUTHENTICATION ERROR: {auth_err}")
    except SMTPSendingError as send_err:
        print(f"\nSENDING ERROR: {send_err}")
    except SMTPError as smtp_err:
        print(f"\nSMTP ERROR: {smtp_err}")
    except Exception as exc:
        print(f"\nUNEXPECTED ERROR: {exc}")


if __name__ == "__main__":
    run_test()
