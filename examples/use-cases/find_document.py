import logging
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent, Browser

logging.basicConfig(level=logging.DEBUG)
load_dotenv()

import asyncio

import os

user_name = os.getenv('USER_NAME')
user_password = os.getenv('USER_PASSWORD')

with open('examples/use-cases/find_document_task.md', 'r') as file:
    task = file.read()

browser = Browser()

agent = Agent(
	task=task,
	llm=ChatOpenAI(model='gpt-4o'),
	browser=browser,
	sensitive_data={
		'user_name': user_name,
		'user_password': user_password,
	},
	save_conversation_path='conversation_prompt_from_file.json',
	save_playwright_script_path='playwright_script_prompt_from_file.py',
)


async def main():
	await agent.run()
	input('Press Enter to close the browser...')
	await browser.close()


if __name__ == '__main__':
	asyncio.run(main())
