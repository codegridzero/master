"""
Standalone Reusable Hostinger SMTP Email Sender Module with HTML Template Support.

This module provides a clean, robust, and reusable interface to send emails
via Hostinger SMTP using SSL/TLS encryption (port 465 by default).
Supports plain text, rich responsive HTML templates (MIME multipart),
and cold pitch email campaigns for RISS.
"""

import os
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path
from typing import Dict, List, Optional, Union
from dotenv import load_dotenv

# Import email templates
try:
    from email_templates import render_cold_pitch_email
except ImportError:
    from .email_templates import render_cold_pitch_email

# Automatically load environment variables from .env in the same directory or project root
_ENV_PATH = Path(__file__).resolve().parent / ".env"
if _ENV_PATH.exists():
    load_dotenv(dotenv_path=_ENV_PATH)
else:
    load_dotenv()


class SMTPError(Exception):
    """Base exception for SMTP module errors."""
    pass


class SMTPConfigError(SMTPError):
    """Raised when required SMTP configuration/credentials are missing."""
    pass


class SMTPAuthenticationFailedError(SMTPError):
    """Raised when SMTP authentication fails."""
    pass


class SMTPSendingError(SMTPError):
    """Raised when connecting or sending an email fails."""
    pass


def send_email(
    to: Union[str, List[str]],
    subject: str,
    body: Optional[str] = None,
    text_body: Optional[str] = None,
    html_body: Optional[str] = None,
    from_email: Optional[str] = None,
    is_html: bool = False,
    host: Optional[str] = None,
    port: Optional[int] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    timeout: int = 30,
) -> Dict[str, Union[bool, str]]:
    """
    Send an email via Hostinger SMTP (SSL/TLS on port 465 by default).
    Supports plain text, pure HTML, or multipart MIME (plain text fallback + rich HTML).

    Args:
        to: Recipient email address (single string, comma-separated string, or list).
        subject: Subject line of the email.
        body: Main body content (plain text if is_html=False, or HTML if is_html=True).
        text_body: Explicit plain text body (for multipart MIME).
        html_body: Explicit HTML body (for multipart MIME).
        from_email: Sender email address (defaults to configured SMTP_USERNAME).
        is_html: If True and only 'body' is provided, treats body as HTML.
        host: SMTP host (defaults to SMTP_HOST from .env or smtp.hostinger.com).
        port: SMTP port (defaults to SMTP_PORT from .env or 465).
        username: SMTP username (defaults to SMTP_USERNAME from .env).
        password: SMTP password (defaults to SMTP_PASSWORD from .env).
        timeout: Socket connection timeout in seconds (default: 30).

    Returns:
        Dict with keys:
            'success' (bool): True if sent successfully.
            'message' (str): Descriptive result message.

    Raises:
        SMTPConfigError: If credentials or mandatory fields are missing.
        SMTPAuthenticationFailedError: If username or password authentication fails.
        SMTPSendingError: If connection, TLS, or sending fails.
    """
    # Resolve configuration values
    smtp_host = host or os.getenv("SMTP_HOST", "smtp.hostinger.com")
    env_port = os.getenv("SMTP_PORT", "465")
    try:
        smtp_port = port if port is not None else int(env_port)
    except ValueError:
        raise SMTPConfigError(f"Invalid SMTP_PORT value: '{env_port}'. Must be an integer.")

    smtp_user = username or os.getenv("SMTP_USERNAME", "info@theriss.net")
    smtp_pass = password if password is not None else os.getenv("SMTP_PASSWORD", "")
    sender_addr = from_email or smtp_user or "info@theriss.net"

    # Validation
    if not smtp_pass or not smtp_pass.strip():
        raise SMTPConfigError(
            "SMTP password is not set. Please enter your mailbox password in .env (SMTP_PASSWORD=...) "
            "or pass it via the 'password' parameter."
        )

    if not to:
        raise SMTPConfigError("Recipient email address ('to') is required.")

    # Normalize recipient list
    if isinstance(to, str):
        recipient_list = [addr.strip() for addr in to.split(",") if addr.strip()]
        to_header = ", ".join(recipient_list)
    elif isinstance(to, (list, tuple)):
        recipient_list = [str(addr).strip() for addr in to if str(addr).strip()]
        to_header = ", ".join(recipient_list)
    else:
        raise SMTPConfigError("Parameter 'to' must be a string or list of email strings.")

    if not recipient_list:
        raise SMTPConfigError("No valid recipient email address provided.")

    # Determine body contents
    final_text = text_body
    final_html = html_body

    if not final_text and not final_html:
        if is_html:
            final_html = body or ""
            final_text = "Please view this message in an HTML-compatible email client."
        else:
            final_text = body or ""

    # Build EmailMessage (MIME standard)
    msg = EmailMessage()
    msg["Subject"] = subject or ""
    msg["From"] = sender_addr
    msg["To"] = to_header

    if final_text:
        msg.set_content(final_text)
        if final_html:
            msg.add_alternative(final_html, subtype="html")
    elif final_html:
        msg.set_content(final_html, subtype="html")
    else:
        msg.set_content("")

    # Create SSL Context
    ssl_context = ssl.create_default_context()

    # Send email over SSL
    try:
        with smtplib.SMTP_SSL(smtp_host, smtp_port, context=ssl_context, timeout=timeout) as server:
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        raise SMTPAuthenticationFailedError(
            f"SMTP Authentication failed for user '{smtp_user}'. "
            "Please check your credentials in .env or Hostinger mailbox settings."
        ) from None
    except (smtplib.SMTPConnectError, ConnectionRefusedError, TimeoutError, OSError) as conn_err:
        raise SMTPSendingError(
            f"Failed to connect to SMTP server '{smtp_host}:{smtp_port}': {conn_err}"
        ) from None
    except smtplib.SMTPException as smtp_err:
        raise SMTPSendingError(f"SMTP error occurred while sending email: {smtp_err}") from None
    except Exception as exc:
        raise SMTPSendingError(f"Unexpected error while sending email: {exc}") from None

    return {
        "success": True,
        "message": f"Email successfully sent to {to_header}."
    }


def send_cold_pitch_email(
    to: Union[str, List[str]],
    recipient_name: str,
    company_name: str,
    preview_url: str,
    subject: Optional[str] = None,
    sender_name: str = "Abdul Rehman",
    sender_title: str = "CEO",
    sender_company: str = "RISS - Remote IT Services & Solutions",
    sender_phone: str = "+92 347 1663003",
    sender_email: str = "Abdulrehman226721skp@gmail.com",
    company_website: str = "https://theriss.net",
    company_logo_url: str = "https://theriss.net/images/Logo.png",
    from_email: Optional[str] = None,
    **smtp_kwargs,
) -> Dict[str, Union[bool, str]]:
    """
    High-level convenience function to render and send a professional cold outreach email.

    Args:
        to: Prospect email address or list of emails.
        recipient_name: Prospect receiver's name (e.g. 'John').
        company_name: Prospect's business name (e.g. 'Mechanical Plumbing Systems, Inc.').
        preview_url: URL to the website demo preview.
        subject: Optional custom subject line. Defaults to: 'Quick website preview for {company_name}'.
        sender_name: Sender's name (default: 'Abdul Rehman').
        sender_title: Sender's title (default: 'CEO').
        sender_company: Sender's company name.
        sender_phone: Sender's WhatsApp / Phone number.
        sender_email: Sender's contact email.
        company_website: Company website URL.
        company_logo_url: Company logo URL.
        from_email: Optional sender address override.
        **smtp_kwargs: Optional extra arguments passed to send_email (host, port, username, password, timeout).

    Returns:
        Dict with keys: 'success' (bool), 'message' (str).
    """
    rendered = render_cold_pitch_email(
        recipient_name=recipient_name,
        company_name=company_name,
        preview_url=preview_url,
        sender_name=sender_name,
        sender_title=sender_title,
        sender_company=sender_company,
        sender_phone=sender_phone,
        sender_email=sender_email,
        company_website=company_website,
        company_logo_url=company_logo_url,
        custom_subject=subject,
    )

    return send_email(
        to=to,
        subject=rendered["subject"],
        text_body=rendered["text"],
        html_body=rendered["html"],
        from_email=from_email,
        **smtp_kwargs,
    )


if __name__ == "__main__":
    print("smtp_sender module loaded successfully.")
    print("Available functions:")
    print("  - send_email(to, subject, body/html_body/text_body, ...)")
    print("  - send_cold_pitch_email(to, recipient_name, company_name, preview_url, ...)")
