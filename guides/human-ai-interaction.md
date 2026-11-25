# Human-AI interaction and agent UX: a reading list

Evidence-backed reading on how people work with AI and how to design agents they can trust. Sources: Nielsen Norman Group (original usability studies), the Interaction Design Foundation (definitions, checklists, vocabulary) and O'Reilly (architecture, trust and where human judgment sits). Each entry has a link, authors, date and a short summary in my own words. Read the originals for detail and visuals.

Compiled by [Masha Sidorova](https://qua-design.com), November 2026. Part of the [Reference Hub](../README.md).

## 1. Designing agent experiences

### [Designing AI Agents: 4 Lessons from China's Qwen Agent](https://www.nngroup.com/articles/designing-ai-agents/)
Feifei Liu, Maria Rosala, NN/g, 8 May 2026. Remote usability study, 6 participants.
1. Discoverability: give more than one way in, typed requests and browsable menus. For a broad request, ask a clarifying question.
2. Familiar patterns: borrow layouts people know, and show how many results exist so a carousel does not hide options.
3. Personal data: ask for active consent, explain why a detail appears, show only what the current step needs.
4. Autonomy: disclose all costs before the commit step and surface the details a decision depends on.

### [Crafting AI Explanations for Every Role in Your Enterprise](https://www.nngroup.com/articles/crafting-ai-explanations/)
Katie Schmidt, Jessa Anderson, Hayley Mortin, NN/g, 3 Jul 2026. One AI output needs different explanations for different readers: audit trails and compliance summaries for governance; output-specific explanations and actionable errors for builders; plain language, visual highlights and familiar precedents for domain experts.

### [Agent Harness: Definition](https://www.nngroup.com/articles/agent-harness/)
Caleb Sponheim, NN/g, 6 Nov 2026. The harness is the software around the model that runs the loop: it executes tool requests, assembles context, enforces permissions and limits time, cost and steps. Designers should decide with engineers which actions need approval, and test whole tasks, not single outputs.

### [Initial Impressions of ChatGPT's Agent: Successful, Shaky, and Slow](https://www.nngroup.com/articles/impressions-chatgpt-agent/)
Evan Sunwall, NN/g, 8 Aug 2025. The agent booked a restaurant, but took about 11 minutes for a form a person fills in about 2, and asked no clarifying questions. Human-in-the-loop checkpoints protect the person but reduce the value of delegating.

### [Context Architecture](https://www.nngroup.com/articles/context-architecture/)
Paz Perez, NN/g, 12 Jun 2026. Information architecture applied to what an agent reads: instructions, retrieved knowledge, skills, tools, memory and the prompt. Label concepts in users' words, rank source trust, and define what the system remembers, forgets or never does.

### [How Service Design Will Evolve with AI Agents](https://www.nngroup.com/articles/service-design-evolve-ai-agents/)
Sarah Gibbons, Pablo Fernández Vallejo, NN/g, 14 Feb 2025. Agents become actors in a service. People state an outcome and the agent does the steps; success metrics widen to task success, data quality and trust.

## 2. The agent as a new kind of user

- [AI Agents as Users](https://www.nngroup.com/articles/ai-agents-as-users/), Sarah Gibbons, Kate Moran, NN/g, 10 Apr 2026. Agents read interfaces through screenshots, the accessibility tree or APIs. Descriptive labels, consistent patterns and semantic structure serve people and agents alike.
- [Experience Design: Dropping the "User" from "User Experience"](https://www.nngroup.com/articles/ux-vs-experience-design/), Raluca Budiu, NN/g, 30 Oct 2026. The field now covers people using products, agents using systems for people, and people and agents working together.

## 3. How people actually talk to AI

- [The 6 Types of Conversations with Generative AI](https://www.nngroup.com/articles/AI-conversation-types/), Budiu, Liu, Cionca, Zhang, NN/g, 10 Nov 2023. A diary study of 425 conversations: search query, funneling, exploring, chiseling, expanding, pinpointing. Detect the type early and respond differently; length says nothing about success.
- [Less Chat, More Answer: Site AI Chatbots Need to Get to the Point](https://www.nngroup.com/articles/less-chat-more-answer/), Rosala, Kenderova, Kohler, NN/g, 17 Apr 2026. Answer first, state limits upfront, keep it short and specific, offer follow-up prompts.
- [GenAI for Complex Questions, Search for Critical Facts](https://www.nngroup.com/articles/ai-search-infoseeking/), Maria Rosala, Josh Brown, NN/g, 27 Feb 2026. People use AI for vague, many-constraint questions and search for facts and high-stakes checks. Make every claim easy to verify.
- [Accordion Editing and Apple Picking](https://www.nngroup.com/articles/accordion-editing-apple-picking/), Gibbons, Mugunthan, Nielsen, NN/g, 24 Sep 2023. Let people edit part of a response, edit text directly and point at the piece they mean.

## 4. Big picture

- [State of UX 2026: Design Deeper to Differentiate](https://www.nngroup.com/articles/state-of-ux-2026/), Moran, Budiu, Gibbons, NN/g, 16 Jan 2026. AI fatigue makes trust the central design problem; confidence comes back through visible system behaviour, control, consistency and recovery.

## 5. More from NN/g

- Explainability and trust: [Explainable AI in Chat Interfaces](https://www.nngroup.com/articles/explainable-ai/), [The 5 Qualities of Site-Specific AI Chatbots](https://www.nngroup.com/articles/dimensions-of-ai-chatbots/), [Handmade Designs: The New Trust Signal](https://www.nngroup.com/articles/handmade-designs/)
- Chat interfaces: [AI Chat Is Not (Always) the Answer](https://www.nngroup.com/articles/ai-chat-not-the-answer/), [10 Guidelines for Designing Your Site's AI Chatbots](https://www.nngroup.com/articles/ai-chatbots-design-guidelines/), [What Is Your Site's AI Chatbot for? Users Can't Tell](https://www.nngroup.com/articles/site-ai-chatbot/)
- Prompt help and generated UI: [GenUI: Buttons and Checkboxes](https://www.nngroup.com/articles/genui-buttons-and-checkboxes/), [Prompt Controls in GenAI Chatbots](https://www.nngroup.com/articles/prompt-controls-genai/), [Prompt Suggestions](https://www.nngroup.com/articles/prompt-suggestions/), [Designing Use-Case Prompt Suggestions](https://www.nngroup.com/articles/designing-use-case-prompt-suggestions/), [The Articulation Barrier and Hybrid Interfaces](https://www.nngroup.com/articles/ai-articulation-barrier/), [Generative UI and Outcome-Oriented Design](https://www.nngroup.com/articles/generative-ui/)
- Output: [Product-Specific GenAI Needs to Write for the Web](https://www.nngroup.com/articles/genai-write-for-the-web/), [AI Summaries of Reviews](https://www.nngroup.com/articles/ai-reviews/)
- Hubs: [Designing AI Products and Features: Study Guide](https://www.nngroup.com/articles/designing-ai-study-guide/), [How AI Works and How Users Think About It](https://www.nngroup.com/articles/ai-functionality-study-guide/), [NN/g AI topic](https://www.nngroup.com/topic/ai/)

## 6. Interaction Design Foundation

Topic pages (free): [Human-AI Interaction](https://ixdf.org/literature/topics/human-ai-interaction), [Human-Centered AI](https://ixdf.org/literature/topics/human-centered-ai), [Artificial Intelligence](https://ixdf.org/literature/topics/ai), [Generative AI](https://ixdf.org/literature/topics/generative-ai), [Chatbots](https://ixdf.org/literature/topics/chatbots), [Prompt Engineering](https://ixdf.org/literature/topics/prompt-engineering), [AI Prompts](https://ixdf.org/literature/topics/ai-prompts), [No-UI Design](https://ixdf.org/literature/topics/no-ui-design), [Bias in UX/UI Design](https://ixdf.org/literature/topics/bias).

Articles:
- [AI Challenges and How You Can Overcome Them: How to Design for Trust](https://ixdf.org/literature/article/ai-challenges-and-how-you-can-overcome-them-how-to-design-for-trust), Feb 2026. Transparency is the main lever: say where data comes from, how the system learns and how often it is wrong. Built on NIST's characteristics of trustworthy AI. The most useful IxDF piece.
- [Are AI-Generated Synthetic Users Replacing Personas?](https://ixdf.org/literature/article/ai-vs-researched-personas), Aug 2026. Synthetic personas are fast but shallow and agreeable; keep real users at the centre.
- [No-UI: How to Build Transparent Interaction](https://ixdf.org/literature/article/no-ui-how-to-build-transparent-interaction)
- [Your Practical Prompt Playbook](https://ixdf.org/literature/article/how-to-craft-effective-text-prompts-for-design), Feb 2026
- [How to Supercharge Your Design Workflow with AI](https://ixdf.org/literature/article/how-to-supercharge-your-design-workflow-with-ai), Feb 2026
- [Shneiderman's Eight Golden Rules](https://ixdf.org/literature/article/shneiderman-s-eight-golden-rules-will-help-you-design-better-interfaces): not about AI, but internal locus of control, easy reversal and informative feedback apply directly to agents.

Paid, for deeper study: the [AI for Designers](https://ixdf.org/courses/ai-for-designers) course and [master classes](https://ixdf.org/master-classes), including Vitaly Friedman's [design patterns for AI UX](https://ixdf.org/master-classes/design-patterns-for-ai-ux).

## 7. O'Reilly

O'Reilly looks at agents from the builder's side: architecture, trust boundaries and where human judgment sits. Radar articles are free; the books need an O'Reilly subscription (most have a free trial).

Radar articles:
- [Interfaces That Build Themselves](https://www.oreilly.com/radar/interfaces-that-build-themselves/). The most UX-focused piece: chat is fine for simple tasks but exhausting for nuanced, ongoing work, and the hard part is making the AI's reasoning visible enough for people to stay in the loop.
- [The Architect's Dilemma](https://www.oreilly.com/radar/the-architects-dilemma/). Start from who the consumer is: a machine needs vending-machine predictability, a person or agent needs a concierge that guides. Explains why some tasks should never be a conversation.
- [The Agentic Commerce Revolution](https://www.oreilly.com/radar/the-agentic-commerce-revolution/). What breaks when an agent pays for you: authorisation, authenticity and consumer trust, and two answers to them, a conversational checkout and a verified "final click".
- [From Capabilities to Responsibilities](https://www.oreilly.com/radar/from-capabilities-to-responsibilities/). For high-stakes agents that change real data, approval queues become a bottleneck; "human over the loop" puts people in charge of the rules and the exceptions instead.
- [Human Judgment Doesn't Leave the Software Factory, It Relocates](https://www.oreilly.com/radar/human-judgment-doesnt-leave-the-software-factory-it-relocates/). Constraints tighten or relax as the system earns or loses trust, and the agent has to show evidence that its work is right.
- [Building Organizational Intelligence](https://www.oreilly.com/radar/building-organizational-intelligence/). An internal AI research assistant that people did not trust until there was a way to review, challenge and refine what it surfaced.
- [The Agent Stack Bet](https://www.oreilly.com/radar/the-agent-stack-bet/). Argues for built-in human-in-the-loop primitives, so an agent pauses and asks before doing something new.
- [Intent, Not Identity](https://www.oreilly.com/radar/intent-not-identity/). When a person and an agent share one browser session, knowing who is acting matters less than knowing what they intend.

Books and chapters:
- [Designing AI Interfaces](https://www.oreilly.com/library/view/designing-ai-interfaces/9798341639812/), Louise Macfadyen, O'Reilly, March 2026. A design-first guide to interfaces for LLMs and autonomous systems, including outputs, canvases and designing for errors.
- [User Experience Design for Agentic Systems](https://www.oreilly.com/library/view/building-applications-with/9781098176495/ch03.html), chapter 3 of Building Applications with AI Agents, Michael Albada, O'Reilly, September 2025.
- [UX for Agentic AI](https://www.oreilly.com/library/view/ux-for-ai/9781394345922/c15.xhtml), chapter 15 of UX for AI, Greg Nudelman and Daria Kempka, Wiley, May 2025, read on O'Reilly. The same book has a chapter on SaaS copilot design.

## Principles across all of it

1. Keep the person in control at commit points: approval before irreversible or costly actions, costs and key details visible first.
2. Show the work: sources, what the agent looked at, why it recommends something, in the reader's language.
3. Ask before assuming: a clarifying question beats a silent guess.
4. Chat plus GUI, not chat alone: menus, presets, buttons and editable results.
5. Answer first, then detail, with limits stated upfront.
6. Minimise and explain personal data use, with active consent.
7. Reuse familiar patterns so people can predict what the agent will do.
8. Measure whole tasks: success, time, trust and recovery.
9. Structure interfaces and context for agents too: semantic, accessible, consistently labelled.
10. Use trust's named parts as a checklist: validity, safety, accountability, explainability, privacy, fairness.
11. Every automated action needs feedback and a manual fallback.
12. Augment, don't replace: keep the human in the loop where judgement matters.
