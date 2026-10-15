# Amfion

Amfion is an AI front desk for service businesses that take appointments:
groomers, auto detailers, plumbing, HVAC and electrical companies, vet
clinics and law firms. It answers website chat, phone calls, texts and email
from the business's own services, prices, hours and policies, books
appointments, and hands a conversation to a person when it should.

This plugin lets you use it from Claude, ChatGPT and Codex:

- **Check the fit.** Ask whether Amfion can do what a business needs and
  what it costs. The answer says plainly what it does not do (for example,
  it does not write bookings into ServiceTitan or Jobber, and it is not
  built for health information).
- **Build a preview from a website.** Give it a business's website and it
  builds a working front desk from the services, prices, hours and policies
  it finds, in about a minute, before anyone signs up.
- **See what it learned and what it is unsure of.** Prices it did not find,
  appointment lengths it assumed, and the cases it sends to a person.
- **Test it the way a customer would.** Ask it the questions the business's
  customers ask, including a booking.
- **Add a live front desk to a website.** Get the exact code for a business
  already on Amfion, where to put it, and a checklist to confirm it works.

It creates no account and publishes nothing. To keep a preview, the business
owner opens its Keep link and signs up themselves.

Previews created through AI assistants are chat-only until the owner claims
them: they generate no phone greeting and accept no phone calls. Phone
features for claimed businesses are part of Amfion's live service, subject
to the business's plan.

## Use it

Install the plugin, then ask in your own words, for example:

- "Can an AI receptionist answer the phone for my grooming salon and book
  appointments?"
- "Build an AI front desk preview from harborpawsgrooming.com and tell me
  what it got wrong."
- "Give me the code to add our Amfion chat to the website, and add it."

The plugin connects to one MCP server, `https://api.amfionhq.com/v1/setup/mcp`,
which needs no sign-in. Help: <https://amfionhq.com/help/claude> (Claude) and
<https://amfionhq.com/help/chatgpt> (ChatGPT and Codex).

## Data

Depending on the tool you use, the plugin sends Amfion the business type and
needs you describe, the website address, the business's Amfion address,
connected domain or short name, preview and conversation identifiers, and
test messages. The MCP client may also send its name, version and session
identifier.

Amfion reads the public website to build the preview and records which
assistant app started it. Unclaimed previews and their conversations are
deleted 7 days after last use and no later than 30 days after creation;
measurement records without business names, websites or contact details
remain. Claimed business account data is retained until deleted under the
Privacy Policy. Deleted database data can remain in encrypted backups for
up to 12 weeks. Test conversations contact no customer and send no email.
Amfion's Privacy Policy: <https://amfionhq.com/privacy>.
Terms: <https://amfionhq.com/terms>.

## Limits

Previews built from AI assistants are limited per day across all users, and
each preview allows a limited number of test messages. Amfion is built for
businesses in the United States.
