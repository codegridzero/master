# Standalone Hostinger SMTP Email Module

A production-ready, reusable Python module for sending plain text and HTML emails via **Hostinger SMTP** (SSL/TLS on port 465). 

This module is designed to be **completely standalone**—it has zero coupling to external databases, CRMs, or web apps, allowing you to drop it directly into any Python project.

---

## 📁 Project Structure

```text
smtp_module/
├── smtp_sender.py       # Core reusable module containing the send_email() function
├── .env                 # Environment file holding your SMTP credentials
├── .gitignore           # Git ignore file protecting .env, caches, and virtual envs
├── requirements.txt     # Minimal dependencies (python-dotenv)
├── test_smtp.py         # Standalone interactive test script
└── README.md            # Complete documentation & integration guide
```

---

## ⚙️ Where Values Are Stored & How to Change Them

All configuration values can be customized either globally via the [`.env`](file:///home/veyren/Desktop/email_sender_module_riss/smtp_module/.env) file or dynamically per function call in Python.

### 1. Configuration in `.env`
Open [`.env`](file:///home/veyren/Desktop/email_sender_module_riss/smtp_module/.env) to edit global default settings:

| Variable in `.env` | Current / Default Value | Purpose / How to Change |
| :--- | :--- | :--- |
| `SMTP_HOST` | `smtp.hostinger.com` | The SMTP server address. Change if using another mail provider. |
| `SMTP_PORT` | `465` | SSL/TLS port (typically `465`). |
| `SMTP_USERNAME` | `info@theriss.net` | The mailbox username / email address used for authentication. |
| `SMTP_PASSWORD` | *(Your mailbox password)* | The password for your Hostinger email account. |

```ini
# Example .env format
SMTP_HOST=smtp.hostinger.com
SMTP_PORT=465
SMTP_USERNAME=info@theriss.net
SMTP_PASSWORD=your_mailbox_password
```

### 2. Parameters in `send_email()`
You can also override any configuration directly inside your Python code when calling `send_email()`:

```python
send_email(
    to="recipient@example.com",     # (Required) Single email or list of emails
    subject="Email Subject",        # (Required) Subject line
    body="Message body text",       # (Required) Plain text or HTML body
    from_email="info@theriss.net",  # (Optional) Defaults to SMTP_USERNAME
    is_html=False,                  # (Optional) Set to True for rich HTML emails
    host=None,                      # (Optional) Override SMTP host
    port=None,                      # (Optional) Override SMTP port
    username=None,                  # (Optional) Override SMTP username
    password=None,                  # (Optional) Override SMTP password
    timeout=30                      # (Optional) Connection timeout in seconds
)
```

---

## 🚀 How to Implement in Any Python Project

### Approach A: Copy into your new project
1. Copy [`smtp_sender.py`](file:///home/veyren/Desktop/email_sender_module_riss/smtp_module/smtp_sender.py) and [`.env`](file:///home/veyren/Desktop/email_sender_module_riss/smtp_module/.env) into your new project directory.
2. Install dependencies in your project environment:
   ```bash
   pip install python-dotenv
   ```
3. Import and call the function in your code:
   ```python
   from smtp_sender import send_email

   send_email(
       to="user@example.com",
       subject="Hello from my new project",
       body="This email was sent using the reusable SMTP module."
   )
   ```

---

### Approach B: Import without copying files (Python Path)
If you want to keep `smtp_module` in its own folder and call it from another directory on your PC:

```python
import sys
# Add path to the smtp_module folder
sys.path.append("/home/veyren/Desktop/email_sender_module_riss/smtp_module")

from smtp_sender import send_email

send_email(
    to="client@example.com",
    subject="Automated Notification",
    body="System notification details here..."
)
```

---

### Approach C: Pass credentials in code (No `.env` file needed)
If your target project manages credentials differently (e.g. from a database or cloud vault):

```python
from smtp_sender import send_email

send_email(
    to="client@example.com",
    subject="Direct Credentials Test",
    body="Sending email without using .env",
    username="info@theriss.net",
    password="your_password_here"
)
```

---

## 💻 Code Examples

### 1. Basic Text Email
```python
from smtp_sender import send_email

result = send_email(
    to="recipient@example.com",
    subject="Quick Update",
    body="Hello,\n\nHere is the update you requested."
)

print(result["message"])
```

### 2. Sending to Multiple Recipients
```python
from smtp_sender import send_email

recipients = ["john@example.com", "sarah@example.com", "team@example.com"]

send_email(
    to=recipients,
    subject="Team Announcement",
    body="Hi Team,\n\nPlease see the weekly update attached."
)
```

### 3. Sending an HTML Email
```python
from smtp_sender import send_email

html_template = """
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: Arial, sans-serif; }
    .card { padding: 20px; background-color: #f4f6f8; border-radius: 8px; }
    .btn { background-color: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px; }
  </style>
</head>
<body>
  <div class="card">
    <h2>Welcome to Our Service!</h2>
    <p>Thank you for choosing us. Click below to verify your account:</p>
    <a class="btn" href="https://example.com/verify">Verify Account</a>
  </div>
</body>
</html>
"""

send_email(
    to="client@example.com",
    subject="Welcome to Our Service!",
    body=html_template,
    is_html=True
)
```

### 4. Production Error Handling Pattern
```python
from smtp_sender import (
    send_email,
    SMTPConfigError,
    SMTPAuthenticationFailedError,
    SMTPSendingError,
)

try:
    send_email(
        to="user@example.com",
        subject="Monthly Invoice",
        body="Please find your invoice details."
    )
    print("Email sent successfully!")
except SMTPConfigError as e:
    # Triggered if password or recipient is missing
    print(f"[Configuration Error] {e}")
except SMTPAuthenticationFailedError as e:
    # Triggered if username/password is rejected by Hostinger
    print(f"[Auth Error] {e}")
except SMTPSendingError as e:
    # Triggered if network/server connection fails
    print(f"[Delivery Error] {e}")
```

---

## 🧪 Testing the Module

To run an interactive test at any time:

1. Navigate to the module directory:
   ```bash
   cd /home/veyren/Desktop/email_sender_module_riss/smtp_module
   ```
2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
3. Run the test script:
   ```bash
   python3 test_smtp.py
   ```

---

## 🔒 Security Best Practices

1. **Keep `.env` Protected**: The `.gitignore` file prevents `.env` from ever being pushed to public or private Git repositories.
2. **Never Hardcode Secrets**: Keep mailbox passwords exclusively in `.env` or inject them via environment variables in production.
3. **Encrypted in Transit**: Communication is enforced via SSL/TLS on port 465, ensuring full encryption between your application and Hostinger's mail servers.
