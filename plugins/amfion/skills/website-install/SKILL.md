---
name: website-install
description: Add an Amfion front desk (the chat bubble, an in-page chat or the request form) to a website and check that it works. Use when someone building or editing a website for a business that is live on Amfion asks to add the Amfion chat, booking assistant or request form, or mentions embed.js or an Amfion address such as harbor-paws.amfionhq.com.
---

# Add an Amfion front desk to a website

## 1. Get the exact code

Ask for the business's Amfion address (the owner finds it in Amfion under
Channels, Website chat & booking page; it looks like
`harbor-paws.amfionhq.com`) if you do not
have it, then call `get_website_install` with it. Use the code it returns
exactly. Never change `data-tenant` to another business, and never write the
snippet from memory.

If the tool says the business is a preview, the owner has to keep it first.

## 2. Choose what to add

- **Chat bubble** (`chatBubble`): the usual choice. Add it once, site-wide,
  so every page shows it.
- **In-page chat** (`inPageChat`): for a contact or booking page. It renders
  inside the `div` in the snippet; put that `div` where it should appear.
- **Request form** (`requestForm`): for a quote or contact page, only when
  the business uses Amfion's request form (law firms do not have one).

Add each script once. Loading it twice shows two bubbles.

## 3. Put it in the site

Find where the site's shared layout ends (the element every page uses) and
put the bubble's script just before `</body>`:

- **Plain HTML or a static site generator:** the shared footer or base
  layout template.
- **Next.js (App Router):** in `app/layout.tsx`, use
  `import Script from 'next/script'` and render
  `<Script src="…/embed.js" data-tenant="…" strategy="afterInteractive" />`
  with the same `data-*` attributes as the snippet. Do the same in
  `pages/_app.tsx` for the Pages Router.
- **React single-page app (Vite, Create React App):** add the script tag to
  `index.html`, not inside a component, so it loads once.
- **Website builders (WordPress, Squarespace, Wix, Webflow, Shopify):** use
  the builder's site-wide custom code setting for the footer or end of
  `<body>` (for WordPress, the theme footer or a header-and-footer code
  plugin; for Shopify, `theme.liquid`). Some builders allow custom code only
  on paid plans. Menu names change; follow the builder's own help if they
  differ.

If the site sends a Content-Security-Policy header, add the business's
Amfion address (the tool's `contentSecurityPolicy` values) to `script-src`
and `frame-src`.

## 4. Check that it works

Run or open the site and go through the tool's `verify` list:

1. The bubble appears and opens a chat for the right business.
2. A question the business answers on its site (hours, a price) gets the
   right answer.
3. Asking to book offers real times or asks for details first.
4. The browser console shows no `[Amfion]` error and no Content-Security-
   Policy violation.

If you can drive a browser, check these yourself and report what you saw.
Use made-up details in any test conversation.

## 5. Tell the owner

Tell them what you added and where. Ask them to make sure the website in
their Amfion business profile is this site's address: Amfion only counts the
website as connected when the two match.
