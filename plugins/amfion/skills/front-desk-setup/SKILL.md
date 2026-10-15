---
name: front-desk-setup
description: Set up and test an AI front desk (an AI receptionist or booking assistant that answers calls, website chat and texts and books appointments) for a service business, using its website and the Amfion tools. Use when someone wants a receptionist for a business that takes appointments, such as a groomer, auto detailer, plumber, HVAC or electrical company, vet clinic or law firm; asks whether Amfion fits their business or what it costs; or wants to see a working preview before signing up.
---

# Set up and test an Amfion front desk

Amfion builds an AI front desk from a business's own website: services,
prices, hours and policies. These steps take a person from "would this work
for my business?" to a tested preview they can keep. You use the Amfion
tools; the person decides and signs up themselves.

## 1. Check the fit first when they are deciding

Call `check_amfion_fit` with their kind of business and what they want it to
do, in their own words. Relay the answers plainly:

- **yes**: it does that today.
- **partly**: it does it with the condition stated. Say the condition.
- **no**: it does not. Say so even when it is the answer they hoped not to
  hear; for example, it does not write bookings into ServiceTitan or Jobber,
  and it does not send scheduled text reminders.

If the business handles health information (a medical, dental or therapy
practice), stop here: Amfion is not built for it. Do not build a preview.

## 2. Build the preview

Ask for the business's website address if you do not have it, then call
`build_front_desk_preview` once. It returns a `preview` handle right away;
the build takes about a minute. Call `get_front_desk_preview` about every 20
seconds until `status` is `ready`. If it is `failed`, tell the person what it
says and suggest building it in a browser at amfionhq.com/try.

Do not build the same business twice: previews are limited per day.

## 3. Report what it learned, and what it is unsure of

From `get_front_desk_preview`, give a short summary:

- The services it found with their prices. A table works well.
- Everything in `toConfirm`: prices not on the website, appointment lengths
  it assumed, policies it did not find. Say these are assumptions the owner
  should check. Never present an assumed price or length as the business's.
- `websiteAlsoLists` on a service means the website states two different
  prices; the owner picks the right one.
- `sendsToAPerson`: the cases it will not book on its own (for a groomer, a
  dog with a bite history; for a plumber, a gas smell).

Report only what the tool returned. Do not fill gaps with your own guesses
about the business.

## 4. Test it the way a customer would

Offer to test it. Use the `suggestedTestQuestions`, plus one or two the
owner's real customers ask, such as:

- a price that depends on size or type ("How much for a large doodle?"),
- a booking ("Can I come in Saturday morning?"), continued with the same
  `conversation` until it offers times or books,
- something that should go to a person.

Call `ask_front_desk_preview` with the message written as a customer would
write it, not as the owner. Show the person the front desk's reply and what
it did. A booking made in a test is a test booking: no customer is contacted
and no email is sent. Use made-up names and addresses in tests, never a real
customer's details.

## 5. Hand it over

Give the person two links from the tool output:

- `previewUrl`: to try the front desk in their browser and adjust prices,
  rules and lengths.
- `keepUrl`: to keep it. They sign up and accept the terms themselves; you
  cannot do that for them. A preview lasts about a week unless it is kept.

## After it is kept

For someone adding it to the business's website, use `get_website_install`
with the business's Amfion address and follow the website-install skill.
