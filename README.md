# 100 Days of Code — Python Projects & Daily Challenges

A hands-on collection of **50+ mini-projects and daily challenges** built during my #100DaysOfCode journey. Each project is self-contained, practical, and demonstrates core software engineering skills: automation, web scraping, data processing, API integration, Web Development and clean code.

## What You'll Find Here

- **Daily challenge folders** — progressive Python projects organized by day
- **Real-world automation** — weather alerts, stock monitoring, browser automation, habit tracking
- **Data & scraping** — web scraping, structured data parsing, API integration
- **Games & UI projects** — small projects demonstrating logic and event handling
- **Web Development** - Flask, DataBases(SQLite, SQLAlchemy),CSS (Framework: BootStrap), Authentication , deployment, Version Control , VC from terminal.  

## Tech Stack

**Language:** Python 
**Libraries & Tools:** requests, BeautifulSoup, Selenium, pandas, smtplib, gspread (Google Sheets API), datetime, json, csv  
**Best Practices:** Virtual environments, requirements.txt, modular scripts, project-level documentation

## IDE 
**NANO (LINUX BUILT IN TEXT EDITOR)** 

## Machine ## **Linux, Distro-Debian**

## Quick Start

```bash
# Clone the repo
git clone https://github.com/HarshitPant-999/100_days_of_code.git
cd 100_days_of_code

# Create & activate a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or: .\venv\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install -r requirements.txt

# Run a project
python path/to/script.py
```

## API Keys Setup

Some projects require external API credentials. Set them as environment variables before running:

### Weather & SMS Projects
**day-35-rain-alert** requires:
- `OWM_API_KEY` — Get from [OpenWeatherMap](https://openweathermap.org/api)
- `TWILIO_ACCOUNT_SID` — Get from [Twilio Console](https://www.twilio.com/console)
- `TWILIO_AUTH_TOKEN` — Get from [Twilio Console](https://www.twilio.com/console)

### Stock News Monitoring
**day-36-Stock_news_monitoring_project** requires:
- `AVS_API_KEY` — Get from [Alpha Vantage](https://www.alphavantage.co/)
- `NA_API_KEY` — Get from [NewsAPI](https://newsapi.org/)
- `TWILIO_ACCOUNT_SID` & `TWILIO_AUTH_TOKEN` — Get from [Twilio Console](https://www.twilio.com/console)

### Workout Tracking
**day-38-Workout Tracking Using Google Sheets** requires:
- `App_ID` — Get from [Nutritionix API](https://www.nutritionix.com/api)
- `API_key` — Get from [Nutritionix API](https://www.nutritionix.com/api)
- Sheety API token for Google Sheets integration

### Flight Deals Finder
**day-39-Flight Dealer Finder** requires:
- `SerpApi_key` — Get from [SerpAPI](https://serpapi.com/)
- Sheety API token for Google Sheets integration
- `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `twilio_number`, `phone_number` for SMS notifications

### Habit Tracker
**habit-tracker** requires:
- `PIXELA_TOKEN` — Register at [Pixela](https://pixe.la/) and generate a token

**Setting environment variables:**
```bash
# macOS/Linux
export OWM_API_KEY="your_key_here"
export TWILIO_ACCOUNT_SID="your_sid_here"
export TWILIO_AUTH_TOKEN="your_token_here"
# ... and so on

# Windows (PowerShell)
$env:OWM_API_KEY="your_key_here"
$env:TWILIO_ACCOUNT_SID="your_sid_here"
# ... and so on
```

Or create a `.env` file in the project directory and load it (make sure to add `.env` to `.gitignore`).

**Note:** Some projects require additional setup like browser drivers for Selenium or credentials for Google Sheets. Check individual project READMEs for detailed instructions.
