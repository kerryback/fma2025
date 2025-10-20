# Incorporating AI into Teaching

**Kerry Back, Rice University, FMA 2025**

---

## CNBC on JPMorgan, 9/30/2025

> [In 2023, JPMorgan] gave employees access to OpenAI's models through LLM Suite; it was essentially a corporate ChatGPT tool used to draft emails and summarize documents.

> About 250,000 JPMorgan employees have access to the platform today ... Half of them use it roughly every day.

> JPMorgan is now early in the next phase of its AI blueprint: It has begun deploying agentic AI to handle complex multistep tasks for employees, according to an internal road map provided by the bank.

---

## CNBC on JPMorgan, 9/30/2025

**Derek Waldron, Chief Analytics Officer:**

> (What we're working towards is that) every employee will have their own personalized AI assistant; every process is powered by AI agents, and every client experience has an AI concierge.

> You'll still have people at the top who are managing and have relationships with clients, but many, many of the processes underneath are now being done by AI systems.

> Workers would shift from being creators of reports or software updates, or "makers" ... to "checkers" or managers of AI agents doing that work.

---

## MIT/Media Labs State of AI in Business 2025

> Only 5% of AI pilots reach production.

> Workers from over 90% of the companies we surveyed reported regular use of personal AI tools for work tasks. In fact, almost every single person used an LLM in some form for their work.

---

## Life was the same for 40 years

- **VisiCalc** introduced for the Apple II in 1979
- **Lotus-123** introduced for the IBM PC in 1983
- **Microsoft Excel** introduced for Windows in 1987

---

## Now, with AI, we're all in the same boat

*[Image: Everyone learning together]*

---

## It's hard to keep up!

*[Image: Coyote struggling to keep up]*

---

## This is me (and you?)

*[Image: Coyote overwhelmed]*

---

## Plan

1. **A course on AI for finance**
2. Previous disruptive technologies
3. Updating existing courses for AI
4. Deep dive into Claude Code

---

## A course on AI for Finance: main themes

**Learn/practice chatting:**
- **Treat AI as a colleague:** Collaborate, evaluate, iterate
- **Coding:** LLMs are not trustworthy for arithmetic: Coding (Python) is essential

**Learn/practice building:**
- **Apps:** Encapsulate tested code in an app
- **Custom chatbots:** Chatbots can be customized through the system prompt, RAG, or fine tuning
- **Agents:** Agents are chatbots equipped with tools

---

## Teaching methods

- Case: Blazing New Trails: Responsible Generative AI and the Creative Adoption of a Large Language Model at Deloitte Canada (HBS, 2024)
- Financial analysis by vibe coding
- Build apps, custom chatbots, agents
- In-class demos, group projects

---

## Prompt Engineering

- Some students ask for instruction on how to prompt AI
- Special techniques aren't needed. Practice is.

**Ethan Mollick, Wharton, "Good Enough Prompting:"**

> Treat AI like an infinitely patient new coworker ... As it is a coworker, you want to work with it, not just give it orders, and you also want to learn what it is good or bad at ... Working with AI is a dialogue, not an order.

---

## Prompt Engineering

- When you learn what it is good and bad at, you can craft more precise prompts
- Save and re-use prompts
- Exercise (in class and assigned):
  - Chat with a chatbot about some financial analysis
  - Evaluate the chatbot output
  - Develop a prompt that will get what you want faster the next time you need a similar analysis

---

## AI Coding

**In March 2025, Y Combinator CEO Garry Tan and managing partner Jared Friedman stated:**

> For roughly a quarter of the startups in their Winter 2025 cohort, 95% of the codebase was written by AI.

---

## Aaron Linsky, CTO, AIA Labs at Bridgewater

> We've been developing capabilities powered by Claude since 2023 within AIA Labs.

> **Claude** powered the first versions of our Investment Analyst Assistant, which streamlined our analysts' workflow by generating **Python code**, creating **data visualizations**, and iterating through **complex financial analysis tasks** with the precision of a junior analyst.

---

## Tools for vibe coding

- Chatbots that code and execute: ChatGPT, Gemini, Claude, Julius.ai
- Python environments with AI assistance: Google Colab, VS Code, Cursor, Windsurf
- All-in-one vibe coder and host: Replit
- My current choice: Claude Desktop (python in cloud) and Claude Code (local python)

---

## Claude → Python → Excel

**Claude prompt:** Create an Excel file illustrating two-stage DCF valuation.

[Claude's Excel File example](https://iita2025.kerryback.com/claude-dcf-example.xlsx)

---

## Claude Demo

> Read the uploaded case. Ignore the valuation method described in the case. Do a two-stage DCF valuation. Project Sales, Assets (based on asset turnover projection), Depreciation (based on depreciation to assets), Cap Ex (based on asset and depreciation projections), Net Working Capital (based on net working capital to sales), EBITDA (based on EBITDA margin), Taxes, NOPAT, and Free Cash Flow. Create a PowerPoint deck and fully functioning and nicely formatted Excel workbook. Document your assumptions and your reasons for them. Put years in columns and items in rows throughout the Excel workbook and PowerPoint deck.

*Currently requires Claude Max subscription.*

---

## Microsoft Vibe Working (powered by Anthropic)

*[Video demonstration]*

---

## AI Plumbing

- Apps can use AI
- Chatbots are apps
- Agents are chatbots with tools

---

## Why teach the plumbing?

- May be useful to have some perspective on how things fit together
- May be valuable for students to be plumbers if they end up at small firms
- Examples provide another teaching opportunity for core financial analysis
- May check a box for recruiters

---

## Chatbot is an app consisting of

- User interface
- API connection to an LLM
- System prompt
- Possible retrieval of documents
- Possible use of tools

---

## System prompt is fundamental

> A system prompt is text that is sent to the LLM along with each user prompt.

> It contains information and instructions for the LLM.

[Anthropic's System Prompts](https://docs.claude.com/en/release-notes/system-prompts#august-5-2025)

---

## RAG (Retrieval Augmented Generation) chatbots

- Store documents
- Send chunks to LLM along with prompt and system prompt
- Choose most relevant chunks (vector similarity)
- Key element of many corporate AI implementations
- Google's Notebook LM (now in Canvas) uses RAG

---

## A vibe-coded chatbot

[chat.derivative-securities.org](https://chat.derivative-securities.org)

---

## Agent = Chatbot + Tools

- AI agent is a chatbot equipped with tools to do things
- Claude and ChatGPT are agents - they can send code to Python environments
- Database tools are very useful for chatbots

---

## Claude for Financial Services

**From Anthropic:**

Through data providers, Claude has real-time access to comprehensive financial information:

- Box, Daloopa, Databricks
- FactSet, Morningstar, Palantir
- PitchBook, S&P Global, Snowflake

---

## Why MBA students should learn about agents

**Fortune, 9-14-2025:**

> PromptQL, an enterprise AI platform created by San Francisco-based developer tooling company Hasura, is doling out **$900-per-hour** wages to its engineers tasked with building and deploying AI agents to analyze internal company data using large language models (LLMs).

> Tanmai Gopal, PromptQL's cofounder and CEO, said "**MBA types** ... are very strategic thinkers, and they're smart people, but they **don't have an intuition for what AI can do**."

---

## Chatbot structure

*[Diagram showing chatbot architecture]*

---

## Database agent passes prompt from user to LLM

*[Diagram: Step 1]*

May require chatting at this stage to clarify user's request

---

## Agent passes SQL from LLM to data warehouse

*[Diagram: Step 2]*

---

## Data Warehouse passes response to agent

*[Diagram: Step 3]*

- Response could be error message
- If so, agent should send to LLM for new SQL code

---

## Agent passes data from warehouse to user

*[Diagram: Step 4]*

- Could be more things connected
- E.g., send data to python engine
- Send python output to user

---

## A vibe-coded databot

[data-portal.rice-business.org](https://data-portal.rice-business.org)

---

## Claude code demo

On Windows: Open PowerShell, install Claude Code, type **claude** to run.

> Create a streamlit app that takes a user prompt and sends it to OpenAI GPT 4.1 using my OPENAI_API_KEY stored in C:\\users\\kerry\\Dropbox\\.ENV. In the system prompt, tell GPT to respond in Spanish. Run the app.

> Print the code in app.py to the screen and explain it.

> Use my NGROK_TOKEN in C:\\users\\kerry\\Dropbox\\.ENV to tunnel the app.

---

## No-code OpenAI Custom GPT

- **Configure:** Name, description, and system prompt
- **Add capabilities:** Web browsing, DALL-E, Code Interpreter
- **Upload knowledge:** Documents for RAG (PDFs, text files)
- **Add actions:** Connect to external APIs (optional)
- **Test & publish:** Private, link-only, or public to GPT Store

*Requires ChatGPT Plus subscription*

---

## Plan

1. A course on AI
2. **Previous disruptive technologies**
3. Updating existing courses for AI
4. Deep dive into Claude Code

---

## Handheld Calculators

- Much worry that students wouldn't learn addition, subtraction, ...
  - Studies haven't found an effect
  - But primary schools still provide practice and assessments in which calculators are not allowed
- Some hoped that schools could move beyond calculation and teach deeper math

---

## Handheld Calculators

- Much worry that students wouldn't learn addition, subtraction, ...
  - Studies haven't found an effect
  - But primary schools still provide practice and assessments in which calculators are not allowed
- Some hoped that schools could move beyond calculation and teach deeper math
  - **That didn't seem to happen either**

---

## Personal computers & spreadsheets

1. We added courses on how to use spreadsheets
2. We updated existing courses to use spreadsheets
3. We assess how well students can use spreadsheets (no pencil and paper valuation analyses)

> Teaching how to do finance in spreadsheets is a main goal.

---

## Why?

- Spreadsheets are used in business
- Spreadsheets are ideal for teaching the logic of some things (valuation/capital budgeting)
- Spreadsheets don't automatically do the things we were teaching before (financial calculators → spreadsheets)

---

## What about AI?

✓ AI is used in business

✓ AI is useful for teaching/tutoring

✗ AI can automatically do many things we were teaching before

> AI is more like calculators than spreadsheets. We worry that students won't learn skills that they need. Like primary schools and arithmetic, we will need to have practice and assessments in which AI is not allowed.

---

## Plan

1. A course on AI
2. Previous disruptive technologies
3. **Updating existing courses for AI**
4. Deep dive into Claude Code

---

## What should we teach?

- We generally teach concepts first with slides (or board)
- Then show in tools (usually Excel)
- Now, there is a next step: chatbots and agents

> Teach about implementation in Excel → students build Excel models.
>
> Teach about implementation in AI → students have chats or build apps

---

## Yeyati, Brookings, 2025

> As AI models begin to handle underwriting, compliance, and asset allocation, the traditional architecture of financial work is undergoing a fundamental shift.

> As job descriptions evolve, so does the definition of financial talent. **Excel is no longer a differentiator. Python is fast becoming the new Excel.**

> But technical skills alone will not cut it. The **most in demand profiles today are those that speak both AI and finance**.

---

## How can we assess?

- Out-of-class assignments should become "turn in your chat, its output, and your evaluation of the output" or "turn in your app."
- In-class **exams without AI** to ensure students understand concepts
- In-class **exams with AI** that are more ambitious than exams today. Cases can become exams with AI assistance.

---

## How should we teach?

- AI is a very effective tutor
- We should take advantage of it
- Asking students to **chat with chatbots can replace "Do the assigned reading."**
- Can be assigned before class or in class before slides

> Ask your chatbot to teach you about ... Be sure to tell it to ask you questions to ensure you are understanding.

---

## Controlling the sources

- Build RAG (Google's Notebook LM or Custom GPT or ...)
- If sources are copyrighted, first ask AI for a complete report on the subject, read and edit the AI report, and add to system prompt "Teach from this report ..."

> But this is probably unnecessary for most topics. The LLMs are much, much more reliable than they were a couple of years ago when everyone was concerned about hallucinations.

---

## Plan

1. A course on AI
2. Previous disruptive technologies
3. Updating existing courses for AI
4. **Deep dive into Claude Code**

---

## Claude Code

- Terminal based coding agent - also OpenAI Codex, Gemini CLI
- Can be used as a plug-in to VS Code, Cursor, Windsurf
- Uses standard Anthropic models, but seems to have a great system prompt

*Requires Claude Pro subscription.*

---

## Capabilities

- Create, edit, copy, move, delete files
- Write, edit, and run **Python** scripts and notebooks
- Write, edit, and compile **LaTeX** documents
- Create and edit **Word** docs, and **PowerPoint** decks
- Create GitHub repos and push and launch apps on hosts (Hugging Face Spaces, Streamlit Community Cloud, Koyeb, Render, ...)

---

## Claude Code Demo

VSCode with Python and Claude Code extensions:

> Create a Jupyter notebook for mean-variance optimization. Prompt the user for the number of assets, their means, standard deviations, and correlations and risk-free rate. Only ask for the minimum number of correlations required to compute the correlation matrix. Assume short sales are allowed. Compute and display the tangency portfolio.

---

## Adding tools to chatbots

- Anthropic created Model Context Protocol (MCP) for adding tools to chatbots. Recently simplified (mcpb files)
- Demo of Claude Code with Rice Business Stock Market Data Portal (vibe coded MCP server)

> Get tsla's roe by quarter on a trailing 4-quarters basis for Q1 2020 through Q3 2025 from the Rice stock database. Also, get tsla's adjusted closing price starting in Jan 1 2020. Filter to keep only end-of-quarter prices. Plot the roe and filtered price series in the same figure, with roe on the left y-axis and price on the right y-axis.

---

## Resources

[genai4finance.kerryback.com](https://genai4finance.kerryback.com)
