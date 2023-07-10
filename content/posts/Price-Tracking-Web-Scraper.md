---
title: Price-Tracking-Web-Scraper
date: 2023-07-10T12:17:54+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1687593883595-6b678fc5c413?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODg5NjI2NDJ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1687593883595-6b678fc5c413?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODg5NjI2NDJ8&ixlib=rb-4.0.3
---

# [techwithtim/Price-Tracking-Web-Scraper](https://github.com/techwithtim/Price-Tracking-Web-Scraper)

# Project Information

This project provides a user interface to interact with an automated price tracking web scraper. Currently the tracker scrapes amazon.ca, but could be configured to scrape multiple sources.

## Libraries/Frameworks/Modules

This project uses:

- React
- Flask
- Playwright
- Bright Data (Web Scraping Browser)

## Using the Scraper

Install all dependencies, create the `auth.json` file, start the flask backend, run the react frontend and interact with the tool.

### auth.json

Fill in your [Bright Data Scraping Browser](https://brightdata.com/products/scraping-browser) credentials in a `backend/scraper/auth.json` file (see `auth_example.json`).

### Python Flask Backend

- `cd backend`
- `pip install -r requirements.txt`
- `playwright install`
- `python app.py` or `python3 app.py`

### Running the React Frontend

- `cd frontend`
- `npm i`
- `npm run start`

## Setting Up Automation

To automate the collection of prices from this software simply run the `scheduler/main.py` file at your desired increment while the python flask backend is running.

### Windows

I have created a simple `.bat` script called `run.bat` that you can schedule to execute using the Windows Task Scheduler that will automatically run the backend api and send the appropriate request to it.
