import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import requests

# Keywords to match relevant jobs
KEYWORDS = ['python', 'api', 'django', 'fastapi', 'devops']

# List of career pages to check
# Step to dynamically load career pages from companies.txt
def load_company_career_pages(file_path):
    """Load company career page URLs from a text file."""
    urls = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("http"):
                urls.append(line)
    return urls

# Load URLs from companies.txt
COMPANY_CAREER_PAGES = load_company_career_pages("companies.txt")

# Step 1: Use Playwright to load dynamic pages
async def fetch_html_with_playwright(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=60000)
            content = await page.content()
        except Exception as e:
            print(f"Error loading {url}: {e}")
            content = ""
        await browser.close()
        return content

# Step 2: Find relevant job postings based on keyword
def extract_matching_job_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        text = a.get_text().lower()
        if any(keyword in text for keyword in KEYWORDS):
            full_url = a['href']
            if not full_url.startswith('http'):
                full_url = base_url.rstrip('/') + '/' + full_url.lstrip('/')
            links.append((a.get_text().strip(), full_url))
    return links

# Step 3: Generate cover letter using local Ollama model
def generate_cover_letter(job_title, job_url):
    prompt = f"""
    Write a professional and concise cover letter for the following job:
    
    Job Title: {job_title}
    Job URL: {job_url}

    I am a Python backend developer with experience in Django, FastAPI, and DevOps. Mention relevant skills, enthusiasm for the role, and adaptability.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",  # or llama2, phi, etc.
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json().get("response", "No response from Ollama.")

# Step 4: Main logic to go through each company
async def main():
    for url in COMPANY_CAREER_PAGES:
        print(f"\n🔍 Checking: {url}")
        html = await fetch_html_with_playwright(url)
        if not html:
            continue
        job_links = extract_matching_job_links(html, url)
        if job_links:
            for title, link in job_links:
                print(f"\n✅ Found job: {title}")
                print(f"🔗 URL: {link}")
                print("📄 Generating Cover Letter...")
                cover_letter = generate_cover_letter(title, link)
                print("✉️ Cover Letter:\n")
                print(cover_letter)
                print("-" * 80)
        else:
            print("❌ No Python Backend jobs found.")

# Run the script
asyncio.run(main())
