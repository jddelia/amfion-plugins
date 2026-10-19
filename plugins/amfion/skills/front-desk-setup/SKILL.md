---
name: front-desk-setup
description: Inspect and test a service business front desk using its public website and Amfion's tools. Use for requests to evaluate Amfion's capabilities, inspect website-derived front desk knowledge, or test customer scenarios. General writing, payment execution and unrelated factual questions are outside this workflow.
---

# Inspect and test an Amfion front desk

Use the tools to produce a tested, temporary front desk in the conversation.
Separate facts from assumptions and explain the result. The tools create
no user account and publish nothing. They do not activate live features.

## Scope

Use this workflow only when the user's request concerns Amfion capability
evaluation, website-derived front desk inspection, or customer-scenario
testing. A business being mentioned does not by itself call for Amfion.
For unrelated writing or factual questions, answer normally without calling
Amfion tools. For a payment request, explain that these tools cannot transfer
money; do not call a tool, claim payment, or request banking credentials.

## 1. Check capabilities when needed

Call `check_amfion_fit` with the business type and stated needs. Preserve
the tool's distinctions: **yes**, **partly** with its conditions, and **no**.
Do not overstate an integration: for example, Amfion does not write
bookings into ServiceTitan or Jobber.

Phone answering is a capability of configured live businesses. These
previews are chat-only, generate no phone greeting and accept no calls.

If the business handles protected health information, such as a medical,
dental or therapy practice, explain the limitation and do not build a
preview.

## 2. Build from the website

Ask for the business's public website if needed, then call
`build_front_desk_preview` once. Keep the returned `preview` handle for
later tool calls. Poll `get_front_desk_preview` about every 20 seconds
until ready, following the returned status. If it fails or reaches a limit,
report the error and any retry timing the tool gives.

Do not repeatedly rebuild the same business. Do not turn a preview handle
into a URL or expose the handle in the conversational reply.

## 3. Inspect the extracted information

Use `get_front_desk_preview` to summarize:

- Services and the business's customer prices.
- `toConfirm`: missing information and assumed prices, durations or policies.
- `websiteAlsoLists`: conflicting prices that need confirmation.
- `sendsToAPerson`: situations that require a person in a live business.
- The remaining test budget and expiry, when returned.

Report only returned information. Do not silently resolve contradictions
or present an assumed value as a fact. Inspection happens in conversation;
the tools do not provide a browser editor or account-activation link.

## 4. Test customer questions

Use `ask_front_desk_preview` with a question written as a customer would
ask it. Start with a suggested question or the user's own scenario. Test
a price, an appointment request, or a situation needing a person. Use the
same `conversation` handle to continue one test conversation.

Show the reply and report actions accurately. A test booking contacts no
customer and sends no email. Use fictional names and contact details.
Human handoffs are disabled: no team is notified, no transfer occurs, and
no callback is arranged. Do not present those as completed actions.

## 5. Summarize the result

Finish the requested inspection or test with a self-contained findings
report in the conversation. Include the business website, inspection date,
returned services and customer prices with their source/assumption labels,
unresolved questions, and each scenario actually tested with its observed
reply and actions. Distinguish untested scenarios from failures. Preserve
conflicting values and identify the questions the owner must answer before
relying on them. Do not invent source URLs or facts absent from the results.

The report must be useful without an Amfion account: the user can copy it
to keep the findings after the temporary workspace expires. State the
workspace's returned expiry and remaining budget without implying that
chat history is deleted or that the workspace will persist. Omit private
preview and conversation handles. If a build or test cannot finish, report
the failure and available partial findings rather than claiming completion.

Continue inspecting or testing within the reported budget when requested.
Do not invent links or an external activation step. Knowledge editing,
live activation and ongoing operation are outside this inspection workflow;
do not imply that the report changes the business's live configuration.

For installation on a website belonging to an **existing live** Amfion
business, use `get_website_install` and the website-install skill. A
temporary preview cannot be installed by these tools.
