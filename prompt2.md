PROMPT 2 — COMPANY DEMO WEBSITE PERSONALIZATION
================================================

START FROM HERE.

You are working inside the company folder inside `coldemail/` that was created by the previous lead-research/cold-email automation process (Prompt 1).

If you are continuing the current lead workflow, operate on the active company folder just created. If multiple company folders exist in `coldemail/` and context is unclear, target the most recently created folder inside `coldemail/` or verify with the user.

Your job now is ONLY to personalize the existing website inside that company folder according to the exact rules below.


DO NOT skip any instruction.
DO NOT change, remove, add, reinterpret, simplify, or replace any requirement.
DO NOT modify the website structure, layout, UI, branding, styling, animations, responsiveness, component structure, or visual design unless an instruction below explicitly asks you to replace TEXT or an IMAGE PATH.

================================================
1. FIRST: IDENTIFY THE BUSINESS CATEGORY
================================================

Before changing anything, inspect the company folder and its companydetails.txt file.

Determine which one of these five categories the business belongs to:

1. Plumbing
2. Kitchen Cleaning
3. Roofing Company
4. HVAC
5. Solar Panel Company

The category must be determined from the company information and research.

You MUST use the matching category image folder from the following data directory:

data/
├── hvac/
│   ├── hvac-01.jpg
│   ├── hvac-02.jpg
│   ├── hvac-03.jpg
│   ├── hvac-04.jpg
│   ├── hvac-05.jpg
│   ├── hvac-06.jpg
│   ├── hvac-07.jpg
│   ├── hvac-08.jpg
│   ├── hvac-09.jpg
│   ├── hvac-10.jpg
│   ├── hvac-11.jpg
│   ├── hvac-12.jpg
│   ├── hvac-13.jpg
│   ├── hvac-14.jpg
│   ├── hvac-15.jpg
│   ├── hvac-16.jpg
│   └── hvac-17.jpg
├── kitchen/
│   ├── kitchen-01.jpg
│   ├── kitchen-02.jpg
│   ├── kitchen-03.jpg
│   ├── kitchen-04.jpg
│   ├── kitchen-05.jpg
│   ├── kitchen-06.jpg
│   ├── kitchen-07.jpg
│   ├── kitchen-08.jpg
│   ├── kitchen-09.jpg
│   ├── kitchen-10.jpg
│   ├── kitchen-11.jpg
│   ├── kitchen-12.jpg
│   ├── kitchen-13.jpg
│   ├── kitchen-14.jpg
│   ├── kitchen-15.jpg
│   ├── kitchen-16.jpg
│   └── kitchen-17.jpg
├── plumbing/
│   ├── 13430.avif
│   ├── 2148095762.avif
│   ├── 2150721551.avif
│   ├── 2150721567.avif
│   ├── 2150721573.avif
│   ├── 2150746309.avif
│   ├── 2150746310.avif
│   ├── 2150990725.avif
│   ├── 46945.avif
│   ├── 55756.avif
│   ├── 58251.avif
│   ├── 7790.avif
│   ├── article-plumbing-tips.jpg
│   ├── article-water-heater.jpg
│   ├── drain-cleaning-service.jpg
│   ├── project-repiping.jpg
│   └── vinicius-wiesehofer-UOavP_Z38lE-unsplash.avif
├── roofing/
│   ├── roofing-01.jpg
│   ├── roofing-02.jpg
│   ├── roofing-03.jpg
│   ├── roofing-04.jpg
│   ├── roofing-05.jpg
│   ├── roofing-06.jpg
│   ├── roofing-07.jpg
│   ├── roofing-08.jpg
│   ├── roofing-09.jpg
│   ├── roofing-10.jpg
│   ├── roofing-11.jpg
│   ├── roofing-12.jpg
│   ├── roofing-13.jpg
│   ├── roofing-14.jpg
│   ├── roofing-15.jpg
│   ├── roofing-16.jpg
│   └── roofing-17.jpg
└── solar/
    ├── solar-01.jpg
    ├── solar-02.jpg
    ├── solar-03.jpg
    ├── solar-04.jpg
    ├── solar-05.jpg
    ├── solar-06.jpg
    ├── solar-07.jpg
    ├── solar-08.jpg
    ├── solar-09.jpg
    ├── solar-10.jpg
    ├── solar-11.jpg
    ├── solar-12.jpg
    ├── solar-13.jpg
    ├── solar-14.jpg
    ├── solar-15.jpg
    ├── solar-16.jpg
    └── solar-17.jpg

Once the category is identified, copy ALL 17 images from ONLY that category folder into:

[CURRENT COMPANY FOLDER]/assets/images/

Do NOT copy images from any other category.

For example:

If the company is Plumbing:
copy all 17 files from data/plumbing/

If the company is HVAC:
copy all 17 files from data/hvac/

If the company is Roofing:
copy all 17 files from data/roofing/

If the company is Kitchen Cleaning:
copy all 17 files from data/kitchen/

If the company is Solar:
copy all 17 files from data/solar/

The company folder must therefore contain the complete 17-image set for its category inside:

assets/images/

================================================
2. COMPANY RESEARCH SOURCE
================================================

The company folder contains:

companydetails.txt

This file contains the detailed research already performed for the company.

You MUST study companydetails.txt before editing index.html.

Use the information in companydetails.txt as the primary source.

You may also perform your own current web research when necessary to verify, clarify, or supplement information.

Use real information whenever it is available.

Do NOT invent company facts when reliable information can be found.

If a fact cannot be verified anywhere, do not falsely present it as verified.

================================================
3. GLOBAL WEBSITE EDITING RULE
================================================

The existing index.html is a completed website template.

The current text and images are dummy/template content.

Your task is to replace ONLY the requested text and image paths described below.

DO NOT redesign the website.

DO NOT change:

- HTML structure
- CSS
- classes
- IDs
- layout
- spacing
- typography
- colors
- branding
- responsive behavior
- animations
- counters functionality
- JavaScript functionality
- section order
- component structure
- image dimensions
- image containers
- visual styling

The ONLY permitted content modifications are:

1. Text replacements specifically requested below.
2. Image path replacements specifically requested below.
3. Copying the required 17 category images into assets/images/.

When replacing content, preserve the existing HTML structure.

Do not remove elements.

Do not add unnecessary elements.

Do not change the design to accommodate content.

================================================
4. IMAGE RULE — GLOBAL RULE FOR THE ENTIRE PAGE
================================================

THIS RULE APPLIES TO EVERY IMAGE REPLACEMENT IN THIS ENTIRE WEBSITE.

Only the 17 category-specific images copied into:

assets/images/

may be used.

You are NOT allowed to generate new images.

You are NOT allowed to download additional images.

You are NOT allowed to use images from another category.

You are NOT allowed to reuse the same image twice on the page.

EVERY IMAGE USED AS A REPLACEMENT MUST BE UNIQUE.

Each of the 17 copied images may be used only ONCE.

Therefore, maintain an internal list of the 17 images and mark each image as USED immediately after assigning it to an image element.

Never assign a USED image again.

This rule applies globally across the entire page, including every section listed below and any future image replacement requested later.

If a later instruction simply says:

"change this image"

you MUST continue following this same global image rule automatically.

The image rule does NOT reset between sections.

Use all 17 images only as needed for the requested image replacements.

Do not generate additional images just because an image seems unsuitable.

If there are fewer than 17 image replacement locations, unused images must simply remain unused.

If there are more image replacement locations than available unused images, STOP and ask me before proceeding.

IMPORTANT:

If anything about an image replacement is unclear, DO NOT guess.

Ask me directly and wait for confirmation before proceeding.

Do not skip the image instruction.

================================================
5. INDEX.HTML TEXT AND IMAGE REPLACEMENTS
================================================

After copying the correct 17 images into assets/images/, edit the existing index.html.

Follow every line/section instruction below.

------------------------------------------------
1. LINE 7 — PAGE TITLE
------------------------------------------------

Line 7 contains the page title.

Replace the title with the exact business name.

------------------------------------------------
2. LINE 62 — PHONE
------------------------------------------------

Line 62 currently contains:

<p class="_14px-text">+923347200660</p>

Replace the phone number with the business phone number.

------------------------------------------------
3. LINE 70 — EMAIL
------------------------------------------------

Line 70 currently contains:

<p class="_14px-text break">info@theriss.net</p>

Replace it with the business email.

------------------------------------------------
4. LINE 78 — BUSINESS HOURS
------------------------------------------------

Line 78 currently contains:

<p class="_14px-text">Mon to Fri: 08:00 - 19:00</p>

Replace this with the business's actual operating hours if those hours are available or publicly listed.

If business hours cannot be verified, leave the existing text exactly as it is.

------------------------------------------------
5. LINE 163 — EMAIL
------------------------------------------------

Line 163 contains:

<p class="_15px-400">info@theriss.net</p>

Replace it with the business email.

------------------------------------------------
6. LINE 170 — PHONE
------------------------------------------------

Line 170 contains:

<p class="_15px-400">+923347200660</p>

Replace the number with the business contact number.

------------------------------------------------
7. LINE 177 — ADDRESS
------------------------------------------------

Line 177 contains:

<p class="_15px-400">9261 Candice Trail,  <br />North Carolina, United States</p>

Replace this address with the actual business address.

------------------------------------------------
8. LINE 516 — HERO HEADING
------------------------------------------------

Line 516 contains:

<h1 class="hero-title">Expert Plumbing Solutions for Every Home</h1>

Replace the heading with a strong heading relevant to the actual business.

The heading must be personalized to the company.

------------------------------------------------
9. LINES 517–518 — HERO PARAGRAPH
------------------------------------------------

Replace the existing dummy hero paragraph:

<p class="hero-paragraph">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                            varius enim in eros elementum tristique. Duis cursus, mi quis viverra ornare.</p>

with a personalized paragraph relevant to the actual company and its services.

------------------------------------------------
10. LINES 535–570 — WHY CHOOSE US SECTION
------------------------------------------------

This is the Why Choose Us section.

Replace the dummy text throughout this entire section with real, company-specific information discovered during research.

Every factual statement must relate to the business.

Keep the word count/content length approximately the same as the existing dummy content so the visual layout does not become distorted.

Do not change the structure or styling.

------------------------------------------------
11. LINES 986–1174 — GET A QUOTE SECTION
------------------------------------------------

Personalize the entire Get A Quote section.

Every text element in this section must be changed to information relevant to the business.

Every heading, paragraph, label, supporting text, CTA text, and other text in this section must be relevant to the company.

Do not change the form structure, layout, styling, fields, classes, or functionality.

Only personalize the text.

------------------------------------------------
12. LINE 1185 — IMAGE
------------------------------------------------

Line 1185 currently contains:

rc="./assets/images/2150721551.avif"

Replace this image path with ONE UNUSED image from the 17 copied category images.

Use each image only once.

------------------------------------------------
13. LINE 1196 — COMPANY HOOK HEADING
------------------------------------------------

Line 1196 contains:

<h2 class="heading">Committed to Delivering Quality and Innovation</h2>

Replace this with a strong company-specific heading.

This heading should act as a hook for the business and should be about the actual company.

------------------------------------------------
14. LINES 1198–1199 — COMPANY DESCRIPTION
------------------------------------------------

Replace:

<p class="margin-bottom-40px">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do
                            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>

with company-specific content based on real research.

------------------------------------------------
15. LINES 1202–1204 AND 1210–1213 — MISSION AND VISION
------------------------------------------------

Replace the Mission text with the company's real mission when publicly available.

Replace the Vision text with the company's real vision when publicly available.

If the company does not publicly state an official mission or vision, create concise text that accurately reflects the company's documented business values and operations.

Do not falsely label invented statements as official company statements.

------------------------------------------------
16. LINE 1266–1269 — STATS SECTION
------------------------------------------------

Line 1266 contains:

<h2 class="white-heading">Our Stats at a Glance</h2>

Replace the heading with company-specific text.

Line 1269 contains:

<p class="secondary-pargraph">Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                    Suspendisse varius enim in eros elementum tristique.</p>

Replace this paragraph with company-specific text.

The four statistics in this section must ALSO be replaced with real company-related values.

The four statistics are:

Years of Experience
Completed Projects
Total Clients
Team Members

Replace all four labels and all four numerical values with real, verified company information wherever available.

Do not leave placeholder values.

Do not break the counter animation or JavaScript functionality.

Only change the displayed text/numbers.

Do not change the counter implementation.

If an exact statistic cannot be verified, use the most defensible publicly supported value or ask me if an exact value is essential.

------------------------------------------------
17. LINES 1281–1308 — THREE IMAGES
------------------------------------------------

There are three images in this block.

Replace each of the three images with UNUSED images from the 17 copied category images.

Each image must be unique.

No image may already have been used elsewhere on the page.

Follow the global 17-image rule.

Do not change the image containers, dimensions, layout, classes, or styling.

------------------------------------------------
18. LINES 1441–1559 — OUR SERVICES SECTION
------------------------------------------------

This entire section must be personalized.

Replace EVERY text element in this section.

This includes:

- headings
- service names
- descriptions
- labels
- supporting text
- CTA text
- every other text element

All content must be based on the actual services of the business.

Use real services found in companydetails.txt and current research.

Do not use generic services unrelated to the company.

Then replace the three images in this section with three UNUSED images from the 17 copied category images.

Follow the global image rule.

Each image must be unique.

------------------------------------------------
19. LINES 1560–1729 — OUR PROJECT SECTION
------------------------------------------------

Completely personalize this section.

Replace EVERY text element with company-specific content.

Replace EVERY image in this section with UNUSED images from the 17 copied category images.

Every text and image must relate to the actual business.

The purpose is to make the portfolio/project section feel like the company's own real work.

IMPORTANT:

Do not fabricate specific completed projects as verified projects unless research actually supports them.

Where individual projects are not publicly documented, use accurately supported project/service descriptions without falsely claiming specific projects were completed.

Follow the global image rule.

Never reuse an image already used elsewhere on the page.

------------------------------------------------
20. LINES 1889–2190 — PRICING SECTION
------------------------------------------------

Personalize EVERY text element in the pricing section.

Do not leave generic placeholder text. Also text in pricing secyion will be change to real text of the company all text within the 3 cards of pricing should be the text of the 3 services of the company which the company wants to show in pricing section.

Use real company information and real pricing information whenever publicly available.

If the company's current website publicly lists actual pricing/packages, research it and use those real values.

If actual company pricing is not publicly available, DO NOT invent prices and present them as real company pricing. but if you didnt find text to put in any card, then make something up based on the services of the company. but this is for text only not for pricing 

In that situation, personalize the section using accurate service/package descriptions and clearly appropriate quote-based language without fabricating pricing facts.

Do NOT change:

- section structure
- layout
- UI
- branding
- styling
- number of cards
- CSS
- HTML structure

Only change the content/text required to personalize the section.

------------------------------------------------
21. LINES 2722–2968 — FAQ SECTION
------------------------------------------------

Personalize the entire FAQ section.

Replace EVERY text element with information relevant to the actual business.

Questions and answers must be based on real company information, services, policies, service areas, emergency availability, hours, pricing approach, and other verified facts where available.

Do not invent unsupported company policies.

There is also one image in this section.

Replace that image with an UNUSED image from the 17 copied category images.

Follow the global image rule.

Do not reuse an image already used elsewhere.

------------------------------------------------
22. LINE 3095 ONWARD — FOOTER
------------------------------------------------

The footer section begins around line 3095.

Replace ALL possible text in the footer with real information about the business.

Replace every applicable:

- business name
- phone
- email
- address
- hours
- service information
- location information
- CTA/supporting text
- other business-related text

Use verified company information.

Do not alter footer structure, styling, layout, branding, or functionality.

================================================
6. CONTENT RULES
================================================

These rules apply to ALL generated/replaced text.

RULE 1 — CONTENT LENGTH

Do NOT increase content length unnecessarily.

If the existing dummy text has approximately 7 words, the replacement should remain approximately the same length.

Preserve the visual size and layout of the existing website.

Do not create long paragraphs where the original paragraph was short.

RULE 2 — LANGUAGE

All generated content must be in English.

All content must be relevant to the actual business.

RULE 3 — NO SYMBOLS OR ICONS IN GENERATED TEXT

Do not add unnecessary symbols, icons, decorative characters, emojis, or special characters to generated text.

Use normal English text.

Existing required punctuation in the HTML should not be destroyed.

RULE 4 — TRUTH FIRST

Always research first.

Use companydetails.txt first.

Then perform current web research when necessary.

Prefer:

- official company website
- official company pages
- verified business listings
- BBB
- chambers
- government/licensing records
- credible directories
- other reliable public sources

Use real facts whenever available.

Only when a suitable factual statement cannot be found may you create reasonable business-related wording.

Generated wording must remain realistic and consistent with the company.

Never fabricate:

- licenses
- awards
- ratings
- project counts
- client counts
- employee counts
- years of experience
- pricing
- certifications
- locations
- official mission statements
- official company claims

================================================
7. IMAGE RULE REPEATED — ABSOLUTE
================================================

For the avoidance of doubt:

ONLY the 17 images copied from the correct category folder may be used for image replacements.

NO NEW IMAGES.

NO EXTERNAL IMAGES.

NO IMAGES FROM OTHER CATEGORIES.

NO IMAGE REPEATS.

ONE IMAGE = ONE USE ONLY.

This rule applies to the entire page.

Maintain a used-image tracking list while editing.

Example:

USED:
image-01
image-02
image-03

AVAILABLE:
all remaining unused images

Before every image replacement, check the list.

Never accidentally reuse an image.

================================================
8. FUTURE IMAGE REPLACEMENT RULE
================================================

This image rule is permanent.

If I later tell you:

"change the image at line XXXX"

you must automatically understand that:

- use only one of the original 17 copied category images
- use an UNUSED image
- never reuse an image
- do not generate a new image
- do not download another image
- do not change layout
- do not change UI
- do not change styling

You do not need me to repeat the image rules every time.

================================================
9. GLOBAL NO-DESIGN-CHANGE RULE
================================================

This is a strict global rule.

Whenever you replace text or images:

DO NOT change the:

- layout
- UI
- visual design
- branding
- colors
- typography
- spacing
- dimensions
- responsiveness
- animations
- transitions
- counters
- JavaScript behavior
- HTML structure
- CSS
- classes
- IDs
- section structure
- page structure

ONLY replace the requested text and image paths.

The existing website must visually remain the same template.

The goal is:

SAME WEBSITE DESIGN
+
REAL COMPANY CONTENT
+
REAL COMPANY INFORMATION
+
CATEGORY-SPECIFIC IMAGES

NOT a redesign.

================================================
10. FINAL VALIDATION BEFORE FINISHING
================================================

Before declaring the task complete, verify all of the following:

1. Correct business category identified.
2. Correct category's 17 images copied into assets/images/.
3. No images from another category were copied.
4. No new images were generated/downloaded.
5. No replacement image is repeated anywhere on the page.
6. All requested image locations were updated.
7. All requested text sections were personalized.
8. Business name is correct.
9. Phone number is correct.
10. Email is correct.
11. Address is correct.
12. Business hours were updated only if verified; otherwise original hours remain.
13. Mission and vision are appropriately personalized.
14. Stats use real/defensible company information.
15. Services section uses actual company services.
16. Project section is personalized without falsely claiming unsupported projects.
17. Pricing section uses real pricing where publicly available and does not fabricate prices. Also text in pricing secyion will be change to real text of the company all text within the 3 cards of pricing should be the text of the 3 services of the company which the company wants to show in pricing section.
18. FAQ section is personalized using accurate company information.
19. Footer contains real company information.
20. All generated content is in English.
21. Content length has not been unnecessarily increased.
22. No unnecessary symbols/icons/emojis were added.
23. HTML structure remains intact.
24. CSS remains unchanged.
25. Layout remains unchanged.
26. UI remains unchanged.
27. Branding remains unchanged.
28. Animations remain functional.
29. Counter functionality remains functional.
30. Responsive behavior remains intact.
31. No unrelated code was modified.
32. companydetails.txt remains intact.
33. No requested section was skipped.

If you discover an ambiguity that could cause an image rule violation, code damage, or incorrect company information, STOP and ask me before making that change.

DO NOT GUESS when the instruction specifically requires a real company fact.

================================================
FINAL OBJECTIVE
================================================

Take the existing company folder created by the previous process.

Identify its business category.

Copy exactly the 17 images belonging to that category into assets/images/.

Then personalize the existing index.html using:

- companydetails.txt
- reliable current research
- the exact text replacement locations specified above
- the exact image replacement rules specified above

The finished page must look like the ORIGINAL TEMPLATE in terms of:

LAYOUT
UI
BRANDING
STRUCTURE
STYLING
RESPONSIVENESS
ANIMATIONS

but its content must be personalized for the actual company.

DO NOT redesign it.

DO NOT simplify the task.

DO NOT skip any section.

DO NOT change any of the rules above.

START THE WORK NOW.