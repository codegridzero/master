# Standalone Hostinger SMTP & Cold Email Module

A production-ready, reusable Python module for sending plain text and **high-converting, responsive HTML emails** via **Hostinger SMTP** (SSL/TLS on port 465) with built-in branding and cold outreach templates for **RISS (Remote IT Services & Solutions)**.

This module is designed to be **completely standalone**—drop it directly into any Python scraper, lead-generation workflow, automation pipeline, or CRM.

---

## 📁 Project Structure

```text
smtp_module/
├── email_templates.py   # High-converting responsive HTML & text email templates
├── smtp_sender.py       # Core module with send_email() and send_cold_pitch_email()
├── preview_template.html# Standalone HTML preview for browser inspection
├── .env                 # Environment file holding SMTP credentials
├── .gitignore           # Git ignore file protecting .env, caches, and venv
├── requirements.txt     # Dependencies (python-dotenv)
├── test_smtp.py         # Interactive CLI tester with menu options
└── README.md            # Complete documentation & usage guide
```

---

## 🌟 Key Features

1. **Brand-Aligned Cold Pitch Template**:
   - Official RISS Logo (`https://theriss.net/images/Logo.png`)
   - Clean dark-navy brand banner and modern card styling
   - Personalized prospect name & company name
   - High-contrast Call-To-Action (CTA) button leading directly to the live website preview
   - 4 visual feature highlight cards (Conversion UI, Mobile sticky bar & WhatsApp chat, frictionless quote form, engaging UX)
   - Low-friction reassurance statement
   - Executive CEO signature card (Abdul Rehman, WhatsApp 1-click link, email, website)
   - Professional CAN-SPAM compliant opt-out footer
2. **Multipart MIME Deliverability**:
   - Automatically sends both HTML and plain-text fallback so spam filters remain happy and every email client renders perfectly.
3. **Cross-Client Compatibility**:
   - Handcrafted responsive layout tested for Gmail, Apple Mail, Outlook, Yahoo, and Mobile browsers.

---

## ⚙️ Configuration & Credentials

Credentials can be loaded automatically from [`.env`](file:///home/veyren/Desktop/main/email_sender_module_riss/smtp_module/.env) or passed directly via function arguments.

### `.env` File Example:
```ini
SMTP_HOST=smtp.hostinger.com
SMTP_PORT=465
SMTP_USERNAME=info@theriss.net
SMTP_PASSWORD=your_mailbox_password
```

---

## 🚀 Quick Usage Examples

### 1. Send Cold Pitch Email (Recommended)

To send a cold pitch email where only client details and demo preview link change:

```python
from smtp_sender import send_cold_pitch_email

result = send_cold_pitch_email(
    to="client@example.com",
    recipient_name="John",
    company_name="Mechanical Plumbing Systems, Inc.",
    preview_url="https://masterplumber.vercel.app/Mechanical%20Plumbing%20Systems/"
)

print(result["message"])
```

### 2. Customizing Sender Information or Subject

```python
from smtp_sender import send_cold_pitch_email

send_cold_pitch_email(
    to="prospect@example.com",
    recipient_name="Sarah",
    company_name="Apex Electric Solutions",
    preview_url="https://masterplumber.vercel.app/Apex%20Electric/",
    subject="New website design concept for Apex Electric Solutions",
    sender_name="Abdul Rehman",
    sender_title="CEO",
    sender_phone="+92 347 1663003",
    sender_email="Abdulrehman226721skp@gmail.com",
    company_website="https://theriss.net"
)
```

### 3. Rendering HTML & Plain Text Without Sending Immediately

If you want to preview or store the generated HTML/Text:

```python
from email_templates import render_cold_pitch_email

rendered = render_cold_pitch_email(
    recipient_name="David",
    company_name="Skyline Roofing LLC",
    preview_url="https://masterplumber.vercel.app/Skyline%20Roofing/"
)

print("Subject:", rendered["subject"])
print("Plain Text Body:\n", rendered["text"])
# Save or inspect HTML
with open("skyline_pitch.html", "w", encoding="utf-8") as f:
    f.write(rendered["html"])
```

### 4. Basic General Purpose Email

```python
from smtp_sender import send_email

send_email(
    to="user@example.com",
    subject="Standard Notification",
    body="Hello, this is a plain text notification."
)
```

---

## 🧪 Testing

Run the interactive test script:

```bash
cd /home/veyren/Desktop/main/email_sender_module_riss/smtp_module
source .venv/bin/activate
python3 test_smtp.py
```

The interactive menu provides 3 options:
1. **Send Professional Cold Pitch Email** (Prompts for recipient, company name, demo link).
2. **Send Simple Plain-Text Test Email**.
3. **Export/Update Local HTML Preview** (`preview_template.html`).

---

## 🌐 Visual Preview

You can open [`preview_template.html`](file:///home/veyren/Desktop/main/email_sender_module_riss/smtp_module/preview_template.html) in Google Chrome, Firefox, or any browser to see the exact email design.
