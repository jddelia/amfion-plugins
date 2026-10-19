# Amfion for ChatGPT and Codex

Inspect and test a service business's front desk in conversation. This
plugin uses five Amfion tools to check capabilities and limitations, build
a temporary front desk from a public website, show what it learned and
what needs confirmation, test customer questions, and obtain website
installation code for a business already live on Amfion.

Customer prices belong to the business being inspected. The tools do not
display Amfion subscription plans or provide an account-activation flow.
They create no user account and publish nothing. Previews remain inside
the tool workflow; there is no browser handover.

## Use it

Install the plugin, then ask in your own words:

- "Can Amfion answer calls for my plumbing company and put jobs in ServiceTitan?"
- "Build a front desk from harbor-paws.amfionhq.com and show what needs confirming."
- "Test that front desk: how much is a full groom for a large dog?"
- "Give me the code to add my existing Amfion chat to my website."

The MCP endpoint is
`https://api.amfionhq.com/v1/setup/openai/mcp`. It requires no sign-in.
The same five tools are available to every caller of this endpoint.
For help, contact <mailto:admin@amfionhq.com>.

## What a test can do

The front desk answers from the business's services, customer prices,
hours and policies. Assumed prices, appointment lengths and missing
policies are labeled for review. Test conversations can propose appointment
times or create a test booking. They contact no customer and send no email.

Assistant-created previews are chat-only: they generate no phone greeting
and accept no phone calls. They cannot notify a team, transfer to a person
or arrange a callback. Existing live businesses have their own configured
features; a preview does not activate them.

An inspection finishes with an in-chat findings report: extracted facts,
labeled assumptions, unresolved questions and observed customer-test
results. Copy and keep that report independently of an Amfion account;
the temporary workspace itself remains subject to the limits below.

## Data and limits

Depending on the tool, the plugin sends Amfion the business type and needs
you describe, the public website address, an existing business's Amfion
address, connected domain or short name, preview and conversation handles,
and test messages. The MCP client may also send its name, version and
session identifier. Treat preview and conversation handles as private.

Amfion reads the public website to build the preview and records which
assistant app started it. Follow the tool's returned expiry time: previews
normally expire seven days after qualifying activity, capped at 30 days
after creation. Test messages extend activity; reading the report alone
does not. Expired previews become unavailable and are deleted by scheduled
cleanup.
Measurement records without business names, websites or contact details
remain. Deleted database data can remain in encrypted backups for up to
12 weeks. Use fictional customer details in tests.

Builds are limited per day across assistant users. Each preview also has
conversation and message limits; the tools report the remaining budget.
Amfion is built for United States service businesses and is not intended
for businesses handling protected health information.

Privacy: <https://amfionhq.com/privacy>.
Terms: <https://amfionhq.com/terms>.
