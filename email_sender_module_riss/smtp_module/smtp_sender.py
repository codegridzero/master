"""
Standalone Reusable Hostinger SMTP Email Sender Module.

This module provides a clean and reusable interface to send emails
via Hostinger SMTP using SSL/TLS encryption.
Credentials can be loaded automatically from a .env file or passed directly.
"""

import os
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path
from typing import Dict, List, Optional, Union
from dotenv import load_dotenv

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
    body: str,
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

    Args:
        to: Recipient email address (single string or list of strings).
        subject: Subject line of the email.
        body: Plain text or HTML content of the email.
        from_email: Sender email address (defaults to configured SMTP_USERNAME).
        is_html: If True, sends body as HTML content; otherwise plain text.
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

    # Build EmailMessage
    msg = EmailMessage()
    msg["Subject"] = subject or ""
    msg["From"] = sender_addr
    msg["To"] = to_header

    if is_html:
        msg.set_content(body or "")
        msg.add_alternative(body or "", subtype="html")
    else:
        msg.set_content(body or "")

    # Create SSL Context
    ssl_context = ssl.create_default_context()

    # Send email over SSL
    try:
        with smtplib.SMTP_SSL(smtp_host, smtp_port, context=ssl_context, timeout=timeout) as server:
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
    except smtplib.SMTPAuthenticationError as auth_err:
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


if __name__ == "__main__":
    print("smtp_sender module loaded. Import this module using: from smtp_sender import send_email")
