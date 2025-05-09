import logging
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from browser_use import Agent, Browser

logging.basicConfig(level=logging.DEBUG)
load_dotenv()

import asyncio

import os

site_url = os.getenv('SITE_URL')
user_name = os.getenv('USER_NAME')
user_password = os.getenv('USER_PASSWORD')

task = """
   ### Prompt for finding a document in a web application

**Objective:**
Visit [Web application](<secret>site_url</secret>), login and find a document.

### Step 1: Navigate to the Website
- Open [Web application](<secret>site_url</secret>).
- If you are not logged in, you will be redirected to the login page.
- Enter the following credentials to log in:
  - **Username:** <secret>user_name</secret>
  - **Password:** <secret>user_password</secret>

---

### Step 2: Load Doccenter
- Click on the "Doccenter" tab in the left navigation bar.

#### Search the content:
- **Content name:** 24 slides static pptx

#### Step 3: Open the content
- Click on the content named "24 slides static pptx" from the search result.
- Wait for the content to load.
"""

browser = Browser()

local_model_name = 'phi4'

agent = Agent(
	task=task,
	llm=ChatOllama(model=local_model_name),
	browser=browser,
	sensitive_data={
		'site_url': site_url,
		'user_name': user_name,
		'user_password': user_password,
	},
	save_conversation_path=f'conversation_updated_prompt_ollama_{local_model_name}.json',
	save_playwright_script_path=f'playwright_script_updated_prompt_ollama_{local_model_name}.py',
)


async def main():
	await agent.run()
	input('Press Enter to close the browser...')
	await browser.close()


if __name__ == '__main__':
	asyncio.run(main())
