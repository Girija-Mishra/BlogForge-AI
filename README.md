# BlogForge AI 🤖

**BlogForge AI** is a multi-agent AI system that helps generate structured blog articles using multiple specialized AI agents.

Instead of asking a single AI model to generate the complete blog, BlogForge divides the process into multiple stages such as research, planning, SEO optimization, writing, reviewing, editing, and finalization.

## 🚀 Live Demo

https://blogforge-ai-nfjyfuvgjcwnw7tvbktrdo.streamlit.app/

## 📌 Features

* Generate blogs from a given topic
* Multi-agent workflow for different writing tasks
* Research-based content generation
* Blog planning and structure generation
* SEO-focused optimization
* AI-generated blog content
* Content review and revision
* Final blog formatting
* Image prompt generation
* Interactive Streamlit interface

## 🧠 Agent Workflow

The system follows a sequential multi-agent workflow:

```text
User Topic
    ↓
Research Agent
    ↓
Planner Agent
    ↓
SEO Agent
    ↓
Writer Agent
    ↓
Reviewer Agent
    ↓
   ┌───────────────┐
   │ Needs Revision?│
   └───────┬───────┘
       Yes ↓     No
      Editor       ↓
         ↓      Finalizer
         └────────→ ↓
                 Final Blog
```

### Agents

**1. Research Agent**
Collects and organizes relevant information for the selected topic.

**2. Planner Agent**
Creates the structure and outline of the blog.

**3. SEO Agent**
Suggests SEO-related elements such as keywords, headings, and optimization points.

**4. Writer Agent**
Generates the main blog content using the research, plan, and SEO information.

**5. Reviewer Agent**
Checks the generated content for issues such as missing information, structure, clarity, and quality.

**6. Editor Agent**
Revises the blog when the reviewer identifies issues that need correction.

**7. Finalizer Agent**
Produces the final formatted blog after the required stages are completed.

**8. Image Prompt Agent**
Generates prompts that can be used to create suitable images for the blog.

## 🛠️ Tech Stack

* **Python** – Main programming language
* **LangChain** – AI application and agent workflow development
* **Gemini API** – Large language model
* **OpenRouter** – Model/API access
* **Streamlit** – Web interface

## 📂 Project Structure

```text
BlogForge-AI/
│
├── app.py
├── agents/
│   ├── research_agent.py
│   ├── planner_agent.py
│   ├── seo_agent.py
│   ├── writer_agent.py
│   ├── reviewer_agent.py
│   ├── editor_agent.py
│   ├── finalizer_agent.py
│   └── image_prompt_agent.py
│
├── prompts/
├── requirements.txt
├── .env
└── README.md
```

> The exact file structure may vary depending on the current version of the project.

## ⚙️ How It Works

1. The user enters a topic through the Streamlit interface.
2. The Research Agent prepares relevant information.
3. The Planner Agent creates the blog structure.
4. The SEO Agent identifies optimization requirements.
5. The Writer Agent generates the blog.
6. The Reviewer Agent evaluates the generated content.
7. If changes are required, the Editor Agent revises the content.
8. The Finalizer Agent prepares the final version.
9. The Image Prompt Agent can generate prompts for relevant blog images.

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Girija-Mishra/BlogForge-AI.git
cd BlogForge-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file and add the required API keys:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

Do not upload your `.env` file or API keys to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 Why Multi-Agent Architecture?

A single AI call can generate a complete blog, but BlogForge separates the process into specialized tasks.

Each agent has a specific responsibility. This makes the workflow easier to organize and allows different stages such as planning, SEO checking, writing, and reviewing to be handled separately.

The reviewer and editor are also separated so that the generated content can be checked before being revised.

## 📊 Example Workflow

For a topic such as:

```text
"The Future of Electric Vehicles"
```

BlogForge can process it through:

```text
Research
   ↓
Blog Outline
   ↓
SEO Optimization
   ↓
Content Generation
   ↓
Review
   ↓
Revision (if required)
   ↓
Final Blog
```

## 🌱 Future Improvements

* Add more specialized agents
* Improve factual verification
* Add better source tracking
* Support additional LLM providers
* Add more customization options for blog tone and length
* Improve image generation integration
* Add persistent storage for generated blogs

## 👩‍💻 Author

**Girija Kumari Mishra**

B.Tech – Computer Science Engineering
GITAM

GitHub: [Girija-Mishra](https://github.com/Girija-Mishra)

## 📄 License

This project is intended for educational and learning purposes.
