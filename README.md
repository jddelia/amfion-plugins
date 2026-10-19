# Amfion OpenAI distribution

This is the source for Amfion's separate ChatGPT and Codex package. Its
package identity is `amfion-front-desk`, with version `1.0.3`, for the
separate OpenAI submission. Its directory display name remains Amfion.
The portal does not allow changing an existing plugin’s MCP URL: use a
new plugin draft for this endpoint, not a reupload onto the general-endpoint
1.0.2 draft. The package calls the fixed OpenAI profile at
`https://api.amfionhq.com/v1/setup/openai/mcp`; the server selects this
profile by route, not by a client-supplied name or a reviewer identity.

The package under [`plugins/amfion`](plugins/amfion) has five tools for
capability checks, website-based front desk inspection and testing, and
website installation for an existing live business. It omits Amfion plan
offers and browser preview or account-activation links. Customer prices
extracted from the business's website remain part of the useful output.

`../ai-plugins` is the existing Claude distribution. Do not change its
manifest, marketplace, skills or endpoint as part of an OpenAI release.

## Test locally

From the monorepo root:

```bash
pnpm --filter @amfion/api exec vitest run src/services/setup-mcp.openai-plugin.test.ts src/services/setup-mcp.plugin.test.ts
```

Run the endpoint's route and service tests with the runtime change as
well. Package tests check the endpoint contract, five positive and three
negative review cases, supported tool references, asset paths and the
archive boundary. They do not prove that ChatGPT invoked a packaged skill
or that a directory accepted the submission.

## Build a review archive

Create a local draft while the fresh recording is pending:

```bash
python3 integrations/openai-plugins/package.py --output /absolute/private/path/amfion-front-desk-1.0.3-draft.zip
```

The ZIP has `plugin.json` at its root and contains only the eight
distributable files listed in the packaging script. It excludes source
tests, credentials, private evidence and the Claude package. ZIP metadata
is fixed so the same source produces the same SHA-256.

For a submission archive, first record and verify the five positive and
three negative cases against the deployed OpenAI endpoint in ChatGPT.
Use fictional demo data. Confirm that the recording shows this profile,
not the earlier general endpoint. Add the accessible recording URL to
`extensions.com.openai.review.demo_recording_url` in the source manifest,
then run:

```bash
python3 integrations/openai-plugins/package.py --review --output /absolute/private/path/amfion-front-desk-1.0.3-review.zip
```

`--review` refuses a missing recording URL and the superseded 1.0.2 movie.
It does not certify that a new URL is accessible or that its contents show
the correct release; those checks remain part of the release evidence.
The current source includes the October 19 recording URL. It is an edited
walkthrough of the custom MCP connection; native packaged skills were tested
separately in Codex. Waiting/navigation were removed and result captures
held for readability. It is not evidence of native packaged-skill execution
in ChatGPT. Do not submit a draft archive.

## Publish without changing Claude's submission

After reviewing and committing the source, export only
`integrations/openai-plugins` from that exact source commit to a dedicated
`openai` branch in `jddelia/amfion-plugins`. Verify its tree and use a normal
push. Keep the public `main` branch and existing Claude review tag at their
reviewed commits. Do not force-update either branch or reuse a review tag.

After the new recording passes visual review, choose its stable release
asset URL under the new immutable tag `review-openai-2026-10-19`. Put that
URL in the source manifest before the final source commit and export.
Publish the `openai` branch, create that tag on the exact exported commit,
and upload the reviewed recording as a prerelease asset. Verify anonymous
access and the media hash before building the submission archive. Record
the source, export, archive and media hashes, then re-upload that exact ZIP
to the separate OpenAI draft and repeat its checks. Do not reuse the old
movie or its release tag.

The exported branch contains this packaging script beside `plugins/`, so
it can also be packaged from a clean checkout of that exact public commit
with `python3 package.py --review --output /absolute/private/path/review.zip`.

This separation preserves Claude's submitted source. It does not imply
OpenAI approval: the guidelines' treatment of a temporary-preview workflow
still needs an honest description and review. The wider product roadmap
is tracked separately in `docs/openai-directory-roadmap.md` in the source
monorepo.
