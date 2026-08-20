# 🚀 LEAD RESEARCH, DEMO SITE PERSONALIZATION & OUTREACH WORKFLOW
### *Complete Master Guide & Operational Instructions (Read Me First)*

---

## 📌 1. Overview & System Architecture

This repository contains an end-to-end automated pipeline designed for **Lead Research**, **High-Converting Demo Website Personalization**, and **Cold Outreach Generation**.

The entire engine operates through a **3-Prompt Sequential Workflow** executed inside **Google Antigravity**:

```
[Google Maps URL]
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│ 🎯 PROMPT 1: Deep Research & Folder Creation                │
│ • Multi-source company & owner/employee research            │
│ • Mandatory email verification (Skip if no email)           │
│ • Duplicate check & Master Excel sheet update               │
│ • Copy mastertemplate/ ➔ coldemail/[CompanyNameNoSpaces]/   │
│ • Create structured companydetails.txt                      │
│ • Generate exact Vercel demo link                           │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 🎨 PROMPT 2: Demo Website Personalization                   │
│ • Detect business niche (1 of 5 categories)                 │
│ • Copy 17 category images from data/ to assets/images/      │
│ • Strict 17-Image Unique Use Rule (No repeats / No AI gen)  │
│ • Full content personalization of index.html                │
│ • Zero design damage (Layout, CSS & animations preserved)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ ✉️ PROMPT 3: Outreach Content Generation                    │
│ • Generate coldemail/[CompanyNameNoSpaces]/email.md         │
│ • Unique personalized cold emails for all verified emails   │
│ • Custom social DMs for Facebook, Instagram, LinkedIn, etc. │
│ • Embedded live Vercel link & CEO signature                 │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 🚀 GIT DEPLOYMENT (Required to make Vercel live)            │
│ • git add .                                                 │
│ • git commit -m "Add lead & demo for [CompanyName]"         │
│ • git push origin main                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 2. Repository Structure

```text
├── data/                               # Category Image Assets (17 images each)
│   ├── hvac/                           # hvac-01.jpg to hvac-17.jpg
│   ├── kitchen/                        # kitchen-01.jpg to kitchen-17.jpg
│   ├── plumbing/                       # 17 plumbing images (.avif / .jpg)
│   ├── roofing/                        # roofing-01.jpg to roofing-17.jpg
│   └── solar/                          # solar-01.jpg to solar-17.jpg
│
├── mastertemplate/                     # ⚠️ MASTER TEMPLATE (NEVER EDIT DIRECTLY)
│   ├── assets/                         # Icons, fonts, branding
│   ├── css/                            # Master stylesheets
│   ├── js/                             # Scripts & mock form handlers
│   └── index.html                      # Base conversion-focused demo page
│
├── coldemail/                          # 📂 Output Directory for Generated Leads
│   └── [CompanyNameWithoutSpaces]/    # Individual company working folder
│       ├── assets/images/              # 17 niche images copied here
│       ├── companydetails.txt          # Deep research file (Prompt 1)
│       ├── email.md                    # Outreach emails & social DMs (Prompt 3)
│       └── index.html                  # Personalized demo site (Prompt 2)
│
├── prompt1.md                          # PROMPT 1: Deep Research & Folder Creator
├── prompt2.md                          # PROMPT 2: Website Personalizer
├── prompt3.md                          # PROMPT 3: Outreach Content Generator
└── read me first.md                    # 📖 This Master Documentation File
```

---

## 🏷️ 3. The 5 Supported Business Niches

Every lead must belong to one of these 5 supported service categories:
1. **Plumbing** (`data/plumbing/`)
2. **Kitchen Cleaning** (`data/kitchen/`)
3. **Roofing Company** (`data/roofing/`)
4. **HVAC** (`data/hvac/`)
5. **Solar Panel Company** (`data/solar/`)

---

## 🛠️ 4. Complete Step-by-Step Workflow

### Step 0: Clone & Open the Workspace
1. Clone the repository to your local machine:
   ```bash
   git clone <REPO_URL>
   cd main
   ```
2. Open the project folder in **Antigravity**.

---

### Step 1: Execute PROMPT 1 (Lead Research & Company Folder Setup)

1. Open `prompt1.md`, copy its entire content, and paste it into Antigravity.
2. Antigravity will respond and ask:
   > *"Please provide the Google Maps / Google Business Profile link for the company."*
3. Go to [Google Maps](https://www.google.com/maps/).
4. In the search bar, search for one of the 5 niches + target city/state (e.g., `proroofing construction alabama usa` or `plumbing miami florida`).
5. Click on the company profile to open its Google Business Profile.
6. Copy the full URL from the browser address bar. It will look like this:
   ```text
   https://www.google.com/maps/place/Pro+Roofing+Solutions/@32.5000496,-88.8685669,7z/data=!4m10!1m2!2m1!1sproroofing+construction+alabama+usa!3m6!1s0x889bb1f3adfea763:0x6e6d7d1026ccb488!8m2!3d30.6097844!4d-88.2589984!15sCiNwcm9yb29maW5nIGNvbnN0cnVjdGlvbiBhbGFiYW1hIHVzYVolIiNwcm9yb29maW5nIGNvbnN0cnVjdGlvbiBhbGFiYW1hIHVzYZIBEnJvb2ZpbmdfY29udHJhY3RvcpoBJENoZERTVWhOTUc5blMwVkpRMEZuU1VRdGRUUTJTQzEzUlJBQuABAPoBBAgVEC4!16s%2Fg%2F11jz4m8t35?entry=ttu
   ```
7. Paste this GMB URL into Antigravity.
8. **What Antigravity executes automatically:**
   - Extracts GMB business details (Name, Phone, Address, Category, Website, Reviews, Rating).
   - Performs multi-source deep research (Website, BBB, Chamber, LinkedIn, Facebook, Instagram, State Licenses, Directories).
   - **MANDATORY EMAIL CHECK**: Searches for verified public business/owner/employee emails.
     - ⚠️ *If NO verified email exists*: The company is skipped, no folder or Excel row is created.
     - ✅ *If verified email exists*: Continues the process.
   - Performs duplicate check in the master Excel sheet.
   - Appends a new lead row to the master Excel sheet.
   - Copies `mastertemplate/` into `coldemail/[CompanyNameWithoutSpaces]/`.
   - Creates `companydetails.txt` containing full research data.
   - Generates the Vercel link:
     ```text
     https://master-five-theta.vercel.app/coldemail/[CompanyNameWithoutSpaces]/index.html
     ```

---

### Step 2: Execute PROMPT 2 (Website Personalization)

1. Once Prompt 1 finishes, open `prompt2.md`, copy its entire content, and paste it into Antigravity.
2. **What Antigravity executes automatically:**
   - Inspects `companydetails.txt` in the active company folder to detect the niche (1 of 5).
   - Copies **all 17 images** from the matching category folder in `data/` into `coldemail/[CompanyNameWithoutSpaces]/assets/images/`.
   - Reads the company facts from `companydetails.txt` and performs supplementary live research if needed.
   - Personalizes `index.html` inside the company folder:
     - **Title Tag & Header Contacts**: Business Name, Phone, Email, Address, Business Hours.
     - **Hero Section**: High-converting personalized heading & intro paragraph.
     - **Why Choose Us Section**: Real company statistics & facts (preserves exact character/word count).
     - **Instant Quote Form Section**: Service dropdowns, property types, and company-specific text.
     - **About Us / Hook Section**: Custom hook heading, company story, real Mission & Vision.
     - **Stats at a Glance**: Verified numerical statistics (Years in Business, Completed Projects, Clients, Team).
     - **Our Services Section**: Real services names, tailored descriptions, and 3 category images.
     - **Our Projects / Portfolio**: Tailored portfolio without false claims, and unique category images.
     - **Pricing Section**: Real package pricing (if public) or tailored quote-based structure.
     - **FAQ Section**: Real company FAQs & right-side category image.
     - **Footer Section**: Full verified contact details, office address, opening hours.
   - **Enforces Global Rules**:
     - 🚫 **Strict 17-Image Unique Use Rule**: Every image replaced uses only 1 of the 17 copied category images, with **zero repeats** and **no AI/external generation**.
     - 🚫 **Zero Design Change Rule**: No layout breakage, no CSS tampering, no animation disruption.

---

### Step 3: Execute PROMPT 3 (Outreach Content Generation)

1. Once Prompt 2 finishes, open `prompt3.md`, copy its entire content, and paste it into Antigravity.
2. **What Antigravity executes automatically:**
   - Reads `companydetails.txt` for all verified emails (Owner, CEO, Managers, Team, General inboxes).
   - Generates the file: `coldemail/[CompanyNameWithoutSpaces]/email.md`.
   - **For Every Email Address**: Creates a distinct, personalized email with:
     - Recipient Name & Position.
     - Unique, compelling Subject Line.
     - Conversion-focused body copy referencing their actual business services/history.
     - Active Vercel demo link (`https://master-five-theta.vercel.app/coldemail/[CompanyNameWithoutSpaces]/index.html`).
     - Professional signature with CEO contact details.
   - **For Every Social Profile (Facebook, Instagram, LinkedIn, etc.)**: Creates a concise, natural, platform-tailored DM with direct profile URL.

---

### Step 4: Git Commit & Push to Vercel (MANDATORY STEP)

> [!IMPORTANT]
> **Vercel will NOT display the new company folder until you push your changes to GitHub!**
> The generated Vercel URL will show `404 Not Found` until the repository is committed and pushed.

Open your terminal in the project root directory and run:

```bash
# 1. Stage all new company files, images, and research
git add .

# 2. Commit changes with a descriptive message
git commit -m "Add lead and personalized demo for [CompanyNameWithoutSpaces]"

# 3. Push changes to GitHub (triggers automated Vercel build)
git push origin main
```

---

### Step 5: Final Testing & Outreach Launch

1. **Test the Live Demo Website**:
   Open the generated Vercel URL in your browser:
   ```text
   https://master-five-theta.vercel.app/coldemail/[CompanyNameWithoutSpaces]/index.html
   ```
   - Verify that the company name, phone, email, and address are accurate.
   - Verify that images match the niche and all 17 images are unique.
   - Verify that the Instant Quote Form works and buttons function properly.

2. **Send Cold Outreach**:
   - Open `coldemail/[CompanyNameWithoutSpaces]/email.md`.
   - Copy the customized email for the primary contact and send it via your email client or outreach module.
   - Copy the social media messages and send direct messages on LinkedIn, Facebook, or Instagram.

3. **Repeat for the Next Lead**:
   - Start again at **Step 1** with a new Google Maps link!

---

## 🔒 5. Strict Operational Rules & Safeguards

| Rule | Description |
| :--- | :--- |
| **1. Master Template Safety** | **NEVER** edit, move, or rename `mastertemplate/` directly. Always make a copy into `coldemail/[CompanyNameWithoutSpaces]/`. |
| **2. Folder Naming Convention** | Company folders inside `coldemail/` **MUST NOT CONTAIN SPACES** (e.g. `ProRoofingSolutions` instead of `Pro Roofing Solutions`). |
| **3. Email Requirement** | If no publicly verifiable email address is found during deep research, **SKIP the company immediately**. Do not add to Excel, do not create a folder. |
| **4. 17-Image Unique Use Rule** | Only use the 17 category images copied from `data/[niche]/`. Each image can only be used **ONCE** on the page. No reuse, no AI generation, no external downloads. |
| **5. Zero Layout / CSS Tampering** | Do not change classes, CSS, layout grid, typography, colors, animations, or counters. Only replace text strings and image paths. |
| **6. Exact Vercel URL Format** | Must strictly follow: `https://master-five-theta.vercel.app/coldemail/[CompanyNameWithoutSpaces]/index.html`. |
| **7. Research File Naming** | The research file in the company folder must always be named exactly `companydetails.txt`. |

---

## ❓ 6. Troubleshooting & FAQs

### Q1: The Vercel link returns a "404: NOT_FOUND" error.
- **Fix**: You have not pushed your changes to GitHub yet. Run `git add .`, `git commit -m "Update"`, and `git push origin main`. Once GitHub pushes, Vercel updates in ~10 seconds.

### Q2: What if a company does not have an owner name listed?
- **Fix**: If the owner cannot be verified from public records (Secretary of State, LinkedIn, Website, BBB), use `NA` in Excel, and address outreach to `Hi [CompanyName] Team,`. Never fabricate names.

### Q3: What if a company has multiple emails?
- **Fix**: Add the primary email to the Excel row and list all additional verified emails in `companydetails.txt`. Prompt 3 will automatically generate separate custom emails for each address inside `email.md`.

### Q4: Can I run multiple companies in the same workspace?
- **Fix**: Yes! Every company gets its own separate folder inside `coldemail/` (e.g. `coldemail/CompanyA/`, `coldemail/CompanyB/`). They do not overwrite each other.

---
*Created for the automated Lead Generation, Personalization, and Outreach Workflow Engine.*
