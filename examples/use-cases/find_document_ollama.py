import logging
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

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

local_model_name = 'deepseek-v2'

agent = Agent(
	task=task,
	llm=ChatOllama(model=local_model_name),
	browser=browser,
	sensitive_data={
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
