"""
RISS Email Templates Module.

Provides responsive, high-converting HTML/CSS email templates with
corresponding plain-text fallbacks for cold outreach, website redesign
proposals, and client notifications.
"""

import html
from typing import Dict, Optional


def render_cold_pitch_email(
    recipient_name: str = "there",
    company_name: str = "your company",
    preview_url: str = "https://theriss.net",
    sender_name: str = "Abdul Rehman",
    sender_title: str = "CEO",
    sender_company: str = "RISS - Remote IT Services & Solutions",
    sender_phone: str = "+92 347 1663003",
    sender_email: str = "Abdulrehman226721skp@gmail.com",
    company_website: str = "https://theriss.net",
    company_logo_url: str = "https://theriss.net/images/Logo.png",
    custom_subject: Optional[str] = None,
) -> Dict[str, str]:
    """
    Renders a modern, responsive cold pitch email for website redesigns/previews.

    Args:
        recipient_name: Name of the prospect / receiver (e.g. 'John').
        company_name: Name of the prospect's business (e.g. 'Mechanical Plumbing Systems, Inc.').
        preview_url: URL to the custom website prototype / preview demo.
        sender_name: Sender's full name (default: 'Abdul Rehman').
        sender_title: Sender's job title (default: 'CEO').
        sender_company: Sender's company name (default: 'RISS - Remote IT Services & Solutions').
        sender_phone: Sender's phone / WhatsApp (default: '+92 347 1663003').
        sender_email: Sender's email (default: 'Abdulrehman226721skp@gmail.com').
        company_website: Company website URL (default: 'https://theriss.net').
        company_logo_url: URL to company logo (default: 'https://theriss.net/images/Logo.png').
        custom_subject: Optional custom subject line override.

    Returns:
        Dict with keys:
            'subject' (str): Recommended / custom email subject line.
            'html' (str): Full responsive HTML email code with inlined CSS.
            'text' (str): Plain-text fallback for spam filter resilience.
    """
    # Clean and escape inputs for HTML safety
    safe_recip = html.escape(recipient_name.strip() if recipient_name else "there")
    safe_company = html.escape(company_name.strip() if company_name else "your company")
    safe_preview = preview_url.strip() if preview_url else "https://theriss.net"
    safe_sender = html.escape(sender_name)
    safe_title = html.escape(sender_title)
    safe_sender_comp = html.escape(sender_company)
    safe_phone = html.escape(sender_phone)
    safe_email = html.escape(sender_email)
    safe_website = company_website.strip()
    safe_logo = company_logo_url.strip()

    # Format WhatsApp URL (clean numbers only for wa.me)
    wa_digits = "".join(ch for ch in sender_phone if ch.isdigit())
    wa_url = f"https://wa.me/{wa_digits}" if wa_digits else f"https://wa.me/923471663003"

    # Default Subject
    subject = custom_subject or f"Quick website preview for {company_name}"

    # Plain text version
    text_content = f"""Hi {recipient_name},

I came across {company_name} and put together a quick preview of what your website could look like:
{safe_preview}

Key improvements focused in this preview:
- Cleaner UI with stronger calls-to-action to make it effortless for visitors to take action.
- Mobile-first features like a sticky call bar and direct WhatsApp/text contact options.
- Conversion-focused elements to reduce hesitation and turn more website visitors into calls and quote requests.
- Engaging, fast layout that makes your brand stand out and easy to navigate.

No obligation — just wanted to show you what's possible for {company_name}. Let me know what you think!

Best regards,

{sender_name} ({sender_title})
WhatsApp: {sender_phone} ({wa_url})
Email: {sender_email}
Company: {sender_company}
Website: {company_website}

---
If you do not wish to receive future emails, simply reply with 'unsubscribe' and we will remove you immediately.
"""

    # Rich responsive HTML with table-based structure + modern CSS
    html_content = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="x-apple-disable-message-reformatting" />
  <title>{html.escape(subject)}</title>
  <!--[if mso]>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <![endif]-->
  <style type="text/css">
    body, table, td, a {{ -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }}
    table, td {{ mso-table-lspace: 0pt; mso-table-rspace: 0pt; }}
    img {{ -ms-interpolation-mode: bicubic; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; }}
    table {{ border-collapse: collapse !important; }}
    body {{ height: 100% !important; margin: 0 !important; padding: 0 !important; width: 100% !important; background-color: #0f172a; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    a {{ color: #38bdf8; text-decoration: none; }}
    
    @media screen and (max-width: 600px) {{
      .mobile-full-width {{ width: 100% !important; max-width: 100% !important; }}
      .mobile-padding {{ padding-left: 18px !important; padding-right: 18px !important; }}
      .feature-card {{ display: block !important; width: 100% !important; box-sizing: border-box !important; margin-bottom: 12px !important; }}
      .cta-btn {{ display: block !important; width: 100% !important; text-align: center !important; box-sizing: border-box !important; }}
    }}
  </style>
</head>
<body style="margin: 0; padding: 0; background-color: #0b0f19; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #334155;">

  <!-- Preheader Text (Visible in email preview) -->
  <div style="display: none; font-size: 1px; color: #0b0f19; line-height: 1px; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">
    I put together a live interactive website preview for {safe_company}. Take a look inside. &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
  </div>

  <!-- Main Background Container -->
  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #0b0f19; table-layout: fixed;">
    <tr>
      <td align="center" style="padding: 30px 12px 40px 12px;">
        
        <!-- Main Card Wrapper (600px Max) -->
        <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mobile-full-width" style="max-width: 600px; background-color: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4); border: 1px solid #1e293b;">
          
          <!-- BRAND HEADER -->
          <tr>
            <td style="background: linear-gradient(135deg, #090d16 0%, #111827 50%, #1e293b 100%); padding: 26px 32px; border-bottom: 2px solid #0284c7;" class="mobile-padding">
              <table border="0" cellpadding="0" cellspacing="0" width="100%">
                <tr>
                  <td align="left" valign="middle">
                    <a href="{safe_website}" target="_blank" style="display: inline-block; text-decoration: none;">
                      <img src="{safe_logo}" alt="RISS Logo" width="125" style="display: block; max-width: 125px; height: auto; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.4));" />
                    </a>
                  </td>
                  <td align="right" valign="middle">
                    <span style="display: inline-block; background-color: rgba(2, 132, 199, 0.18); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-size: 11px; font-weight: 700; letter-spacing: 0.8px; text-transform: uppercase; padding: 6px 14px; border-radius: 20px;">
                      Web Design &amp; IT Solutions
                    </span>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- EMAIL BODY CONTENT -->
          <tr>
            <td style="padding: 36px 32px 28px 32px;" class="mobile-padding">
              
              <!-- Greeting -->
              <p style="margin: 0 0 16px 0; font-size: 17px; font-weight: 600; color: #0f172a; line-height: 24px;">
                Hi {safe_recip},
              </p>

              <!-- Intro Statement -->
              <p style="margin: 0 0 24px 0; font-size: 15px; color: #475569; line-height: 25px;">
                I came across <strong style="color: #0f172a;">{safe_company}</strong> and put together a quick preview of what your website could look like with a modern, high-converting design:
              </p>

              <!-- INTERACTIVE PREVIEW CTA BOX -->
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border: 1px solid #bae6fd; border-radius: 12px; margin-bottom: 28px; overflow: hidden;">
                <tr>
                  <td style="padding: 24px 20px; text-align: center;">
                    <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #0284c7; margin-bottom: 6px;">
                      🎯 Live Interactive Prototype
                    </div>
                    <div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 16px;">
                      {safe_company} Concept Redesign
                    </div>
                    
                    <!-- Call To Action Button -->
                    <table border="0" cellpadding="0" cellspacing="0" align="center" style="margin: 0 auto;">
                      <tr>
                        <td align="center" style="border-radius: 8px; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); box-shadow: 0 6px 16px rgba(2, 132, 199, 0.35);">
                          <a href="{safe_preview}" target="_blank" class="cta-btn" style="font-size: 15px; font-weight: 700; color: #ffffff; text-decoration: none; padding: 14px 28px; display: inline-block; border-radius: 8px; letter-spacing: 0.3px;">
                            👉 View Live Website Preview &rarr;
                          </a>
                        </td>
                      </tr>
                    </table>
                    
                    <div style="margin-top: 14px; font-size: 12px; color: #64748b;">
                      Direct Link: <a href="{safe_preview}" target="_blank" style="color: #0284c7; word-break: break-all; text-decoration: underline;">{safe_preview}</a>
                    </div>
                  </td>
                </tr>
              </table>

              <!-- HIGHLIGHTS / VALUE PROPOSITION SECTION -->
              <p style="margin: 0 0 14px 0; font-size: 15px; font-weight: 700; color: #0f172a; letter-spacing: -0.2px;">
                Key features focused in this demo:
              </p>

              <!-- Feature Grid 2x2 / Stack -->
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-bottom: 24px;">
                <tr>
                  <td width="50%" valign="top" class="feature-card" style="padding: 0 6px 12px 0;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; height: 100%;">
                      <tr>
                        <td style="padding: 14px 16px;">
                          <div style="font-size: 14px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">
                            🚀 High-Converting UI
                          </div>
                          <div style="font-size: 13px; color: #64748b; line-height: 19px;">
                            Cleaner layout &amp; stronger calls-to-action that make it effortless for visitors to take action.
                          </div>
                        </td>
                      </tr>
                    </table>
                  </td>
                  <td width="50%" valign="top" class="feature-card" style="padding: 0 0 12px 6px;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; height: 100%;">
                      <tr>
                        <td style="padding: 14px 16px;">
                          <div style="font-size: 14px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">
                            📱 Mobile-First Features
                          </div>
                          <div style="font-size: 13px; color: #64748b; line-height: 19px;">
                            Sticky call bar &amp; instant WhatsApp/text contact options for mobile users on the go.
                          </div>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <tr>
                  <td width="50%" valign="top" class="feature-card" style="padding: 0 6px 0 0;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; height: 100%;">
                      <tr>
                        <td style="padding: 14px 16px;">
                          <div style="font-size: 14px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">
                            ⚡ Frictionless Quotes
                          </div>
                          <div style="font-size: 13px; color: #64748b; line-height: 19px;">
                            Conversion-focused quote requests designed to turn traffic into phone calls and booked jobs.
                          </div>
                        </td>
                      </tr>
                    </table>
                  </td>
                  <td width="50%" valign="top" class="feature-card" style="padding: 0 0 0 6px;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; height: 100%;">
                      <tr>
                        <td style="padding: 14px 16px;">
                          <div style="font-size: 14px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">
                            ✨ Engaging UX
                          </div>
                          <div style="font-size: 13px; color: #64748b; line-height: 19px;">
                            Ultra-fast navigation that makes your business look established and trusted.
                          </div>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>

              <!-- Low Friction Reassurance -->
              <p style="margin: 0 0 0 0; font-size: 14px; color: #475569; line-height: 22px; background-color: #faf5ff; border-left: 3px solid #a855f7; padding: 14px 18px; border-radius: 0 8px 8px 0;">
                <strong style="color: #6b21a8;">No obligation at all</strong> — just wanted to share what is possible for your digital presence. Let me know if you would like to explore this further or make adjustments!
              </p>

              <!-- SPACER & DIVIDER -->
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top: 28px; margin-bottom: 24px;">
                <tr>
                  <td style="border-top: 1px solid #e2e8f0; height: 1px; line-height: 1px; font-size: 1px;">&nbsp;</td>
                </tr>
              </table>

              <!-- EXECUTIVE SIGNATURE CARD -->
              <table border="0" cellpadding="0" cellspacing="0" width="100%">
                <tr>
                  <td valign="middle">
                    <div style="font-size: 17px; font-weight: 700; color: #0f172a; letter-spacing: -0.2px; line-height: 22px;">
                      {safe_sender}
                    </div>
                    <div style="font-size: 13px; font-weight: 600; color: #475569; margin-top: 3px; margin-bottom: 12px;">
                      {safe_title} &bull; {safe_sender_comp}
                    </div>
                    
                    <table border="0" cellpadding="0" cellspacing="0">
                      <tr>
                        <td style="font-size: 13px; color: #0f172a; line-height: 24px;">
                          <span style="font-weight: 600; color: #0f172a;">WhatsApp:</span> 
                          <a href="{wa_url}" target="_blank" style="color: #0f172a; text-decoration: none; font-weight: 500;">{safe_phone}</a>
                          &nbsp;&nbsp;|&nbsp;&nbsp;
                          <span style="font-weight: 600; color: #0f172a;">Email:</span> 
                          <a href="mailto:{safe_email}" style="color: #0f172a; text-decoration: none; font-weight: 500;">{safe_email}</a>
                          <br />
                          <span style="font-weight: 600; color: #0f172a;">Website:</span> 
                          <a href="{safe_website}" target="_blank" style="color: #0f172a; text-decoration: none; font-weight: 500;">theriss.net</a>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>

            </td>
          </tr>

          <!-- COMPLIANCE & BRAND FOOTER -->
          <tr>
            <td style="background-color: #0f172a; padding: 22px 32px; text-align: center; border-top: 1px solid #1e293b;" class="mobile-padding">
              <p style="margin: 0 0 8px 0; font-size: 12px; color: #94a3b8; line-height: 18px;">
                <strong>RISS (Remote IT Services &amp; Solutions)</strong> &bull; Crafting high-impact web &amp; digital solutions.
              </p>
              <p style="margin: 0; font-size: 11px; color: #64748b; line-height: 16px;">
                You received this personalized message because we researched {safe_company}. If you do not wish to receive further communications, simply reply with "unsubscribe" and you will be immediately removed.
              </p>
            </td>
          </tr>

        </table>
        <!-- End Main Card -->

      </td>
    </tr>
  </table>

</body>
</html>
"""

    return {
        "subject": subject,
        "html": html_content,
        "text": text_content,
    }


if __name__ == "__main__":
    # Quick self-test rendering
    sample = render_cold_pitch_email(
        recipient_name="John Doe",
        company_name="Mechanical Plumbing Systems, Inc.",
        preview_url="https://masterplumber.vercel.app/Mechanical%20Plumbing%20Systems/"
    )
    print("Subject:", sample["subject"])
    print("HTML Length:", len(sample["html"]))
    print("Text Length:", len(sample["text"]))
