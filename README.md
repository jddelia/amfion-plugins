# Amfion plugins

Plugins that let Claude, ChatGPT and Codex work with
[Amfion](https://amfionhq.com), an AI front desk for service businesses that
take appointments.

| Plugin | What it does |
|---|---|
| [`amfion`](plugins/amfion) | Check whether Amfion fits a business, build and test a preview front desk from the business's website, and add a live Amfion front desk to a website. |

## Install

**Claude Code**

```bash
claude plugin marketplace add jddelia/amfion-plugins
claude plugin install amfion@amfion
```

Or connect only the MCP server:

```bash
claude mcp add --transport http amfion https://api.amfionhq.com/v1/setup/mcp
```

**claude.ai and Claude Desktop:** Customize → Plugins → Add → Add marketplace,
then enter `jddelia/amfion-plugins`. Or add the server alone under Customize →
Connectors → Add custom connector with the URL
`https://api.amfionhq.com/v1/setup/mcp`.

**ChatGPT:** open Plugins, choose Add custom MCP server, and enter
`https://api.amfionhq.com/v1/setup/mcp`.

**Codex:** add to `~/.codex/config.toml`:

```toml
[mcp_servers.amfion]
url = "https://api.amfionhq.com/v1/setup/mcp"
```

Full instructions: <https://amfionhq.com/help/claude> and
<https://amfionhq.com/help/chatgpt>.

## About this repository

Each plugin folder carries manifests for both ecosystems: `.claude-plugin/plugin.json`
and `.mcp.json` for Claude, and `plugin.json` and `mcp.json` (the Agent
Plugins format, with OpenAI settings under `extensions.com.openai`) for
ChatGPT and Codex. The skills under `skills/` are shared. There is no code to
run: the plugin is instructions and a link to Amfion's MCP server.

The source of truth lives in Amfion's main repository (`integrations/ai-plugins`)
and is published here; open issues at <mailto:admin@amfionhq.com>.

MIT licensed.
