# Figma Summer School: Designer to Builder — what's inside

A map of everything Figma developer advocate Riccardo Erra published for the **Designer to Builder** series (summer 2026): three one-hour live sessions that take one component from a Figma file to reviewed, merged code that is linked back to Figma with Code Connect. This page lists the materials and what each one teaches, so you can pick the right one instead of rewatching three hours.

Notes compiled by [Masha Sidorova](https://qua-design.com) from the recordings, the companion repository and the starter file. All materials belong to Figma and Riccardo Erra; this page only links to them and summarises them.

## The materials

| What | Where | Notes |
| --- | --- | --- |
| Series page | [fig-events.figma.com/designer-builder-series](https://fig-events.figma.com/designer-builder-series/) | Dates, session outlines, reading list for each session |
| Recordings | [figma.com/webinars/designer-to-builder-series](https://www.figma.com/webinars/designer-to-builder-series/) | Free, gated by a short form; ~65 min each, English auto-captions |
| Starter file | [Figma Community: Figma livestream: Designer → Builder](https://www.figma.com/community/file/1655994171720567013) | CC BY 4.0. Duplicate it to follow along |
| Companion repo | [github.com/riccardoerrafigma/designer-to-builder](https://github.com/riccardoerrafigma/designer-to-builder) | Final state after session 3: tokens, accordion, Code Connect files |
| Prompts and commands | [PROMPTS.md](https://github.com/riccardoerrafigma/designer-to-builder/blob/main/PROMPTS.md) | Every agent prompt and terminal command used in the series |
| Slide deck | Published in Figma Community (linked at the end of each session) | Includes the resource list |

## Session by session

### 1. Getting ready to build from Figma (22 July 2026)
[Recording](https://www.figma.com/webinars/getting-ready-to-build-from-figma/)

No AI on purpose: the foundations done by hand first.
- Git vs GitHub, what a repository is, clone vs fork, the terminal inside VS Code.
- The starter repo: plain HTML and CSS, no framework or build step, an empty `components` and `tokens` folder, and an `AGENTS.md` with rules for the coding agent.
- Variables → tokens. Each variable in the file has a **web code syntax** (`var(--…)`), so Dev Mode and the MCP show developers the code token name, not the designer's variable name. Tokens were exported with a plugin into `tokens.css`; for an always-in-sync setup, see the Variables REST API FigJam walkthrough.
- A light and a dark block on the preview page prove the theming works.
- Commit small and often: easier to review, easier to revert, a readable history.

### 2. Building your first component with AI (5 August 2026)
[Recording](https://www.figma.com/webinars/building-your-first-component-with-ai/)

- How the pieces connect: design context lives in Figma, code context lives in the repo (where the agent works), the **MCP** carries design context to the agent, **Code Connect** is the fixed bridge back.
- Prepare the file for AI: real components, auto layout, slots, meaningful layer names. The MCP panel in Dev Mode estimates how many tokens reading the selection will cost.
- **A good prompt has four parts**: the source (Figma node and repo), the outcome, the **constraints** (what the agent must not do) and the **proof** (how the agent checks its own work).
- Start in **plan mode**, and ask the plan to separate decisions from Figma, decisions from the repo, and what needs human judgement. Then implement.
- Run it locally and ask the agent to **compare** the code with the node without editing anything, and not to invent mismatches. Fix only verified mismatches.
- Use the agent to learn too: ask it to explain what it did and why.

### 3. Connecting, reviewing, and shipping your component (19 August 2026)
[Recording](https://www.figma.com/webinars/connecting-reviewing-and-shipping-your-component/)

- Work on a branch (`git switch -c …`), never straight on `main`.
- **Code Connect, parserless**: a `figma.config.json` plus an `Accordion.figma.ts` template. Here only the top-level Accordion is connected, and its `Slot` is mapped so the snippet stays flexible.
- Keep the personal access token in a git-ignored `.env`; never commit or share it.
- `figma connect preview` and `figma connect publish --dry-run` before anything goes live; if the preview fails, the agent fixes only the template or config.
- Commit, push, open a pull request. Someone else should review it: you can't see your own blind spots.
- After merge: `git switch main`, `git pull`, then `figma connect publish`. Anyone with a Full or Dev seat sees the snippet in Dev Mode, so in a team the design-system owners usually control publishing.
- The Q&A on the designer-engineer role: your taste stays the core skill; add front-end basics, Git and pull requests, and pair with developers.

## Inside the starter file

- **Primitives**: white and black opacity steps (10–100%); Grey, Brand, Orange, Red, Green ramps 100–800.
- **Semantic layer with Light and Dark modes**: Background (subtle, muted, strong, border, pop, action) and Foreground (secondary, primary).
- **Component tokens**: `--component-accordion-background`, `-background-active`, `-border`, `-border-active`, `-foreground`, `-foreground-active`, `-background-section`.
- **Type**: Google Sans Flex. Heading Large 24/110%, Heading 20/110%, Body and Body Strong 16/130%, Body Small and Small Strong 12/130%.
- **Spacing and effects**: padding 8 and 12, radius 8, border 0.5, a "Lift" shadow (0 2 4 at 10% black).
- **Accordion anatomy**: Accordion (one slot) → Accordion Item (Active = No/Yes) → Accordion Title (Closed/Open) + Accordion Body + Chevron, shown on a Light and a Dark page.

Small things worth a look if you rebuild it (good practice for the agent's "compare" step):
- In the file, the Body Strong style takes its line height from the heading variable (22) rather than 130%.
- The title variant property keeps the default name "Property 1".
- Two separate chevron components are both called "Chevron Up".

## Reuse it in Claude Code

The method is packaged as a Claude skill, `figma-create-component`: plan → implement on tokens → run and compare → fix → Code Connect → pull request → publish. It reuses the series' prompt shapes. The Figma side needs the [Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/); the Code Connect side needs `npm install --global @figma/code-connect@latest` (Node 18+).

## Reading list from the series

- [GitHub Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world) and [About Git](https://docs.github.com/en/get-started/using-git/about-git)
- [Figma MCP server: remote installation](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- [Syncing design systems using the Variables REST API](https://www.figma.com/community/file/1270821372236564565) (FigJam)
- [Guide to Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode)
- [Structure your Figma file for better code](https://developers.figma.com/docs/figma-mcp-server/structure-figma-file/)
- [Write effective prompts](https://developers.figma.com/docs/figma-mcp-server/write-effective-prompts/)
- [Code Connect quickstart](https://developers.figma.com/docs/code-connect/quickstart-guide/) and [template files](https://developers.figma.com/docs/code-connect/template-files/)
