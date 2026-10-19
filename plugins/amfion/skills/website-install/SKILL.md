---
name: website-install
description: Add the Amfion chat bubble, in-page chat or request form to a website for an existing live Amfion business, then verify it. Use when a user requests installation or mentions embed.js or their business address such as harbor-paws.amfionhq.com.
---

# Install an existing live Amfion front desk

## 1. Get the exact code

Ask for the existing business's Amfion address if needed, then call
`get_website_install`. Use its snippets exactly. Never substitute another
business's `data-tenant` or write a snippet from memory.

If the address identifies a preview or is not an active business, report
the tool's limitation. Installation requires an existing live business;
this plugin does not activate one.

## 2. Choose the placement

- **Chat bubble** (`chatBubble`): add once to the site's shared layout.
- **In-page chat** (`inPageChat`): place the returned container where the
  chat should appear on a contact or booking page.
- **Request form** (`requestForm`): use only when returned for that
  business. Law firms do not have a request form.

Do not add the same script twice.

For plain HTML, put the bubble before `</body>` in the shared layout. In
Next.js, use `next/script` with `strategy="afterInteractive"` and the exact
returned attributes. In a React single-page app, use the host HTML so the
script loads once. In a website builder, use its supported site-wide
custom-code setting; consult the builder's documentation when needed.

Use the returned `contentSecurityPolicy` values for `script-src` and
`frame-src` when the site sets a Content-Security-Policy header.

## 3. Verify and report

Follow the tool's `verify` list. Check the correct business appears, a
question about its services or hours is answered, appointment requests
work as described, and no script or Content-Security-Policy error appears.
Use fictional customer details and do not contact customers during testing.

Report the code placement and what you actually verified. If browser
testing was unavailable, say which checks remain. Ask the owner to confirm
the website in their existing Amfion business profile matches this site
so the installation can be recognized.
