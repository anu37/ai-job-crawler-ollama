# 🔎 AI-Powered Job Crawler for Python Backend Roles

This project is a smart web crawler that automates the job-hunting process for **Python Backend Developer** roles. It scrapes company career pages, filters relevant job postings, and generates a **personalized cover letter** for each opportunity using a **local LLM via [Ollama](https://ollama.com)**.

---

## 🚀 Features

- 🌐 Crawl multiple company career pages
- 🔍 Find job openings based on keywords like `python`, `backend`, `API`, etc.
- 🔗 Extract and print direct URLs to relevant job listings
- ✍️ Generate tailored cover letters for each job using **local LLM models** (like `mistral`, `llama2`, `phi`)
- ⚡ Supports dynamic sites like **AshbyHQ**, **Workday**, and more via **Playwright**

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [Playwright](https://playwright.dev/python/) – For browser automation and JavaScript rendering
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – For parsing HTML
- [Ollama](https://ollama.com) – Run LLMs like `mistral`, `llama2`, etc. locally to generate cover letters

---

## 📦 Installation

```bash
# Install dependencies
pip install playwright beautifulsoup4 requests

# Install browser drivers for Playwright
playwright install

## 📄 Example Output 
🔍 Checking: https://jobs.ashbyhq.com/corti
✅ Found job: Backend Engineer – Python
🔗 URL: https://jobs.ashbyhq.com/corti/1234
✉️ Cover Letter:

Dear Hiring Manager,
As a Python backend engineer with experience in Django, FastAPI...
