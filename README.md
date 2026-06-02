# python-test-bot
Simple telegram bot that monitors server is on — if the bot is polling, server is alive.

## Aim
The bot for simple checking if your server is on
## How it works
- Bot runs continuensly
- Telegram connection acts as a heartbeat
- If process is alive → server is healthy
- No response → server or process is down
## Installation
**Clone repo**
```bash
git clone https://github.com/matgo1/python-test-bot.git
cd python-test-bot
```
**Install dependencies**
```bash
uv pip install -e .
```
## Configuration
```bash
touch .env
```
Inside enter your API as in `env.example .
## Run the Bot
You have two options
1. Option 1 (Recommended)
```bash
uv run app
```
2. Option 2 (Some kind of dev mode)
```bash
python -m python_test_mode.main
```
## Features
- lightweight health-check (Telegram-based)
- async python implementation 
- mirroring messages if on
- /start, /stop, /test
### Future features
- CPU/RAM monitoring
- Docker webhook implementation
- Integration in another planned project
## Tech Stack
- python 3.14
- aiogram
- uv
- pydantic
- asyncio
## Project Structure
```
src/
	python_test_bot/
		__init__.py
		main.py
		configure.py
		test_commands.py
		utils/
			__init__.py
			states.py
LICENSE
README.md
pyproject.toml
uv.lock
```
## License
MIT
