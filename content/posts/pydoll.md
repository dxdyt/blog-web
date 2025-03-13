---
title: pydoll
date: 2025-03-13T12:22:26+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1739715640692-22ef6a326271?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDE4Mzk2NTB8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1739715640692-22ef6a326271?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDE4Mzk2NTB8&ixlib=rb-4.0.3
---

# [thalissonvs/pydoll](https://github.com/thalissonvs/pydoll)

<p align="center">
    <h1>🚀 Pydoll: Async Web Automation in Python!</h1>
</p>
<br>
<p align="center">
    <img src="https://github.com/user-attachments/assets/c4615101-d932-4e79-8a08-f50fbc686e3b" alt="Alt text" /> <br><br>
</p>

<p align="center">
    <img src="https://codecov.io/github/thalissonvs/pydoll/graph/badge.svg?token=40I938OGM9"/> 
    <img src="https://github.com/thalissonvs/pydoll/actions/workflows/tests.yml/badge.svg" alt="Tests">
    <img src="https://github.com/thalissonvs/pydoll/actions/workflows/ruff-ci.yml/badge.svg" alt="Ruff CI">
    <img src="https://github.com/thalissonvs/pydoll/actions/workflows/release.yml/badge.svg" alt="Release">
    <img src="https://tokei.rs/b1/github/thalissonvs/pydoll" alt="Total lines">
    <img src="https://tokei.rs/b1/github/thalissonvs/pydoll?category=files" alt="Files">
    <img src="https://tokei.rs/b1/github/thalissonvs/pydoll?category=comments" alt="Comments">
    <img src="https://img.shields.io/github/issues/thalissonvs/pydoll?label=Issues" alt="GitHub issues">
    <img src="https://img.shields.io/github/issues-closed/thalissonvs/pydoll?label=Closed issues" alt="GitHub closed issues">
    <img src="https://img.shields.io/github/issues/thalissonvs/pydoll/bug?label=Bugs&color=red" alt="GitHub bug issues">
    <img src="https://img.shields.io/github/issues/thalissonvs/pydoll/enhancement?label=Enhancements&color=purple" alt="GitHub enhancement issues">
</p>
<p align="center">
    <a href="https://trendshift.io/repositories/13125" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13125" alt="thalissonvs%2Fpydoll | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

Pydoll is an innovative Python library that's redefining Chromium browser automation! Unlike other solutions, Pydoll **completely eliminates the need for webdrivers**, providing a much more fluid and reliable automation experience.



## ⭐ Extraordinary Features

- **Zero Webdrivers!** Say goodbye to webdriver compatibility and configuration headaches
- **Native Captcha Bypass!** Naturally passes through Cloudflare Turnstile and reCAPTCHA v3 *
- **Performance** thanks to native asynchronous programming
- **Realistic Interactions** that simulate human behavior
- **Advanced Event System** for complex and reactive automations

> Note: for cloudflare captcha, you have to perform a click in the checkbox. Just find a div containing the iframe and use the `.click()` method. Automatic detection and click coming soon! 
  
## Table of Contents

- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Core Components](#-core-components)
  - [Browser Interface](#browser-interface)
  - [Page Interface](#page-interface)
  - [WebElement Interface](#webelement-interface)
- [Advanced Features](#-advanced-features)
  - [Event System](#event-system)
  - [Concurrent Scraping](#concurrent-scraping)
- [Best Practices](#-best-practices)
- [Contributing](#-contributing)

## 🔥 Installation

```bash
pip install pydoll-python
```

## ⚡ Quick Start

See how simple it is to get started - no webdriver configuration needed!

```python
import asyncio
from pydoll.browser.chrome import Chrome
from pydoll.constants import By

async def main():
    # Start the browser with no additional webdriver configuration!
    async with Chrome() as browser:
        await browser.start()
        page = await browser.get_page()
        
        # Navigate through captcha-protected sites without worry
        await page.go_to('https://example-with-cloudflare.com')
        button = await page.find_element(By.CSS_SELECTOR, 'button')
        await button.click()

asyncio.run(main())
```

If you need to configure the browser, you can do it like this:

```python
from pydoll.browser.chrome import Chrome
from pydoll.browser.options import Options

options = Options()
# Public or private proxy, you choose!
options.add_argument('--proxy-server=username:password@ip:port')
# Needs to change the default browser location? No worries!
options.binary_location = '/path/to/your/browser'
async with Chrome(options=options) as browser:
    await browser.start()
```

Here you can find all the options available: [Chromium Command Line Switches](https://peter.sh/experiments/chromium-command-line-switches/)

## 🎯 Core Components

### Browser Interface

The Browser domain provides direct control over the browser itself, offering global methods to manage the entire browser instance. Unlike page-specific operations, these methods affect the browser as a whole, allowing you to control multiple pages, handle window properties, manage cookies across all domains, and monitor events throughout the entire browsing session.

Here's an example of how to use the Browser domain:

```python
async def browser_examples():
    async with Chrome() as browser:
        await browser.start()
        # Control multiple pages with incredible ease
        pages = [await browser.get_page() for _ in range(3)]
        
        # Advanced settings with a simple command
        await browser.set_window_maximized()
```

#### Browser Management

Now, let's dive into the methods of the Browser domain.

##### `async start() -> None`
Fires up your browser and gets everything ready for automation magic!

```python
async with Chrome() as browser:
    await browser.start()  # Starts the browser
```

##### `async stop() -> None`
Gracefully shuts down the browser when you're done.

```python
await browser.stop()  # Manually stops the browser
```

##### `async get_page() -> Page`
Grabs an existing page or creates a fresh one if needed - super convenient!

```python
# Gets an existing page or creates a new one
page = await browser.get_page()
await page.go_to("https://www.example.com")
```

##### `async new_page(url: str = '') -> str`
Opens a brand new page and returns its ID for future reference.
Always prefer using the `get_page` method to get a page instance.

```python
# Creates a new page and navigates directly to a URL
page_id = await browser.new_page("https://www.example.com")
```

##### `async get_page_by_id(page_id: str) -> Page`
Lets you access any specific page using its ID - perfect for multi-tab automation!

```python
# Gets a specific page by ID
page = await browser.get_page_by_id(page_id)
```

##### `async get_targets() -> list`
Shows you all open pages in the browser - great for keeping track of everything.

```python
# Lists all open pages in the browser
targets = await browser.get_targets()
for target in targets:
    print(f"Page: {target.get('title')} - URL: {target.get('url')}")
```

Want to switch between tabs or pages? It's super easy! First, get all your targets:

```python
targets = await browser.get_targets()
```

You'll get something like this:

```python
[{'targetId': 'F4729A95E0E4F9456BB6A853643518AF', 'type': 'page', 'title': 'New Tab', 'url': 'chrome://newtab/', 'attached': False, 'canAccessOpener': False, 'browserContextId': 'C76015D1F1C690B7BC295E1D81C8935F'}, {'targetId': '1C44D55BEEE43F44C52D69D8FC5C3685', 'type': 'iframe', 'title': 'chrome-untrusted://new-tab-page/one-google-bar?paramsencoded=', 'url': 'chrome-untrusted://new-tab-page/one-google-bar?paramsencoded=', 'attached': False, 'canAccessOpener': False, 'browserContextId': 'C76015D1F1C690B7BC295E1D81C8935F'}]
```

Then just pick the page you want:

```python
target = next(target for target in targets if target['title'] == 'New Tab')
```

And switch to it:

```python
new_tab_page = await browser.get_page_by_id(target['targetId'])
```

Now you can control this page as if it were the only one open! Switch between tabs effortlessly by keeping references to each page.

##### `async set_window_bounds(bounds: dict) -> None`
Position and size your browser window exactly how you want it!

```python
# Sets the size and position of the window
await browser.set_window_bounds({
    'left': 100, 
    'top': 100, 
    'width': 1024, 
    'height': 768
})
```

##### `async set_window_maximized() -> None`
Make your browser take up the full screen with one simple command.

```python
# Maximizes the browser window
await browser.set_window_maximized()
```

##### `async set_window_minimized() -> None`
Hide the browser window when you don't need to see it.

```python
# Minimizes the browser window
await browser.set_window_minimized()
```

##### `async get_cookies() -> list[dict]`
Peek into all cookies stored by the browser - great for debugging or session management!

```python
# Gets all cookies
cookies = await browser.get_cookies()
for cookie in cookies:
    print(f"Name: {cookie['name']}, Value: {cookie['value']}")
```

##### `async set_cookies(cookies: list[dict]) -> None`
Set up custom cookies for authentication or testing scenarios.

```python
# Sets cookies in the browser
await browser.set_cookies([
    {
        'name': 'session_id',
        'value': '12345',
        'domain': 'example.com',
        'path': '/',
        'expires': -1,  # Session
        'secure': True
    }
])
```

##### `async delete_all_cookies() -> None`
Wipe all cookies clean - perfect for testing from a fresh state!

```python
# Clears all cookies
await browser.delete_all_cookies()
```

##### `async set_download_path(path: str) -> None`
Tell your browser exactly where to save downloaded files.

```python
# Sets the directory to save downloads
await browser.set_download_path("/path/to/downloads")
```

##### `async on(event_name: str, callback: callable, temporary: bool = False) -> int`
Registers a callback for a specific event. You can read more about the events in the [Event Monitoring](#event-monitoring) section.


### Page Interface

The Page Interface is the heart of your automation! 🌟 This domain provides precise control over individual pages, representing a single tab in the browser and enabling interactions with web content, event handling, screenshots, and much more. This is where the real magic happens!

Here's how to use the Page interface:

```python
async def page_examples():
    # Smooth navigation, even on protected sites
    await page.go_to('https://example.com')
    
    # Retrieve information about the page
    current_url = await page.current_url
    content = await page.page_source
    
    # Capture perfect screenshots
    await page.get_screenshot('/screenshots/evidence.png')
    
    # Handle cookies with ease
    cookies = await page.get_cookies()
    await page.set_cookies([{'name': 'session', 'value': 'xyz123'}])
    
    # Execute JavaScript on the page
    await page.execute_script('return document.title')
```

#### Page Management

Let's explore the awesome ways to control your pages:

##### `async go_to(url: str, timeout=300) -> None`
Navigate to any URL with smart loading detection - works beautifully with protected sites!

```python
# Navigate to a URL with custom timeout
await page.go_to("https://www.example.com", timeout=60)
```

##### `async refresh() -> None`
Refresh your page with a single command - perfect for testing state changes.

```python
# Refresh the page when needed
await page.refresh()
```

##### `async close() -> None`
Close the current tab while keeping your browser session alive.

```python
# Close the page when done
await page.close()
```

##### `async current_url -> str`
Instantly know exactly where you are in your automation journey.

```python
# Check the current URL
url = await page.current_url
print(f"We are at: {url}")
```

##### `async page_source -> str`
Get the complete HTML source with one command - perfect for scraping or debugging.

```python
# Capture the complete HTML of the page
html = await page.page_source
```

##### `async get_cookies() -> list[dict]`
See all cookies for the current page - great for debugging authentication issues!

```python
# Get all cookies
cookies = await page.get_cookies()
for cookie in cookies:
    print(f"Name: {cookie['name']}, Value: {cookie['value']}")
```

##### `async set_cookies(cookies: list[dict]) -> None`
Set up exactly the cookies you need for testing logged-in states or specific scenarios.

```python
# Set custom cookies
await page.set_cookies([
    {
        'name': 'session_id',
        'value': '12345',
        'domain': 'example.com',
        'path': '/',
        'expires': -1,  # Session
        'secure': True
    }
])
```

##### `async delete_all_cookies() -> None`
Start fresh with a clean cookie state - perfect for testing login flows!

```python
# Clear all cookies to start fresh
await page.delete_all_cookies()
```

##### `async get_screenshot(path: str) -> None`
Capture visual evidence of your automation in action!

```python
# Capture a screenshot of the entire page
await page.get_screenshot("/path/to/screenshot.png")
```

##### `async print_to_pdf(path: str) -> None`
Generate beautiful PDF reports directly from your pages.

```python
# Convert the page to PDF
await page.print_to_pdf("/path/to/document.pdf")
```

##### `async get_pdf_base64() -> str`
Get PDF data ready for processing or sending in API requests.

```python
# Get PDF in base64 format for processing
pdf_base64 = await page.get_pdf_base64()
```

##### `async has_dialog() -> bool`
Never be surprised by unexpected alerts or confirmations again!

```python
# Check if there's an alert or confirmation
if await page.has_dialog():
    # Handle the dialog
```

##### `async get_dialog_message() -> str`
Read what those pesky dialogs are trying to tell you.

```python
# Read the dialog message
if await page.has_dialog():
    message = await page.get_dialog_message()
    print(f"Dialog says: {message}")
```

##### `async accept_dialog() -> None`
Automatically dismiss dialogs to keep your automation flowing smoothly.

```python
# Automatically accept any dialog
if await page.has_dialog():
    await page.accept_dialog()
```


##### `async set_download_path(path: str) -> None`
Control exactly where your files go - per page or globally!

```python
# Configure custom download folder
await page.set_download_path("/my_downloads")
```

##### `async get_network_logs(matches: list[str] = []) -> list`
See exactly what requests your page is making - filter for just what you need!

```python
# Capture requests to specific APIs
await page.enable_network_events() # this is obligatory!
await page.go_to('https://example.com')
logs = await page.get_network_logs(['/example-api', '/another-api'])
```

This will give you detailed insights like:

```python
{
  "method": "Network.requestWillBeSent",
  "params": {
    "requestId": "764F3179D5C6D0A1A3F67E7C0ECD88DB",
    "loaderId": "764F3179D5C6D0A1A3F67E7C0ECD88DB",
    "documentURL": "https://google.com/",
    "request": {
      "url": "https://google.com/",
      "method": "GET",
      "headers": {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\""
      },
      "mixedContentType": "none",
      "initialPriority": "VeryHigh",
      "referrerPolicy": "strict-origin-when-cross-origin",
      "isSameSite": true
    },
    "timestamp": 152714.232433,
    "wallTime": 1741737850.444337,
    "initiator": {
      "type": "other"
    },
    "redirectHasExtraInfo": false,
    "type": "Document",
    "frameId": "2EC0B50381EB2D8CF48BE3CF1D933B59",
    "hasUserGesture": false
  }
}
```

##### `async get_network_response_bodies(matches: list[str] = []) -> list`
Capture the actual response data from your API calls - perfect for validation!

```python
# Get responses from API requests
responses = await page.get_network_response_bodies(['google.com'])
```

You'll get something like this:

```python
[
    {
        'body': '...',
        'base64Encoded': False
    }
]
```

##### `async get_network_response_body(request_id: str) -> tuple`
Target specific requests for detailed analysis.

```python
# Retrieve a specific response body
logs = await page.get_network_logs(['api/products'])
body, encoded = await page.get_network_response_body(logs[0]['params']['requestId'])
```

##### `async on(event_name: str, callback: callable, temporary: bool = False) -> int`
Make your automation reactive by responding to page events in real-time! Check out the [Event System](#event-system) section for more details.

##### `async execute_script(script: str, element: WebElement = None)`
Unleash the full power of JavaScript directly from your Python code!

```python
# Execute JavaScript on the page
title = await page.execute_script('return document.title')

# Execute JavaScript on a specific element
button = await page.find_element(By.CSS_SELECTOR, 'button')
await page.execute_script('arguments[0].click()', button)
```

### WebElement Interface

A WebElement represents a DOM element in the browser, allowing you to interact with it in ways that simulate real human behavior. This section explores the most useful methods for interacting with web elements.


##### `value -> str`
Get the current value of the element - perfect for checking form fields.

```python
# Check the value of an input field
input_element = await page.find_element(By.CSS_SELECTOR, 'input')
print(f"Current value: {input_element.value}")
```

##### `class_name -> str`
Access the element's CSS classes - useful for style verification.

```python
# Check CSS classes
button = await page.find_element(By.CSS_SELECTOR, 'button')
print(f"Classes: {button.class_name}")
```

##### `id -> str`
Retrieve the element's ID - perfect for unique identification.

```python
# Get the element's ID
element = await page.find_element(By.CSS_SELECTOR, 'div')
print(f"ID: {element.id}")
```

##### `is_enabled -> bool`
Quickly check if the element is enabled for interaction.

```python
# Check if a button is enabled before clicking
button = await page.find_element(By.CSS_SELECTOR, 'button')
if button.is_enabled:
    await button.click()
```

##### `async bounds -> list`
Get the exact coordinates of the element's bounding box.

```python
# Get the element's coordinates
element = await page.find_element(By.CSS_SELECTOR, 'div')
bounds = await element.bounds
print(f"Coordinates: {bounds}")
```

##### `async inner_html -> str`
Retrieve the element's inner HTML - perfect for scraping!

```python
# Get the inner HTML of a container
container = await page.find_element(By.CSS_SELECTOR, '.container')
html = await container.inner_html
print(f"Inner HTML: {html}")
```

##### `async get_element_text() -> str`
Get the text contained in the element - clean and ready to use.

```python
# Get the element's text
element = await page.find_element(By.CSS_SELECTOR, 'p')
text = await element.get_element_text()
print(f"Text: {text}")
```

##### `get_attribute(name: str) -> str`
Access any attribute of the element directly.

```python
# Get a custom attribute value
link = await page.find_element(By.CSS_SELECTOR, 'a')
href = link.get_attribute('href')
data_id = link.get_attribute('data-id')
```

##### `async scroll_into_view()`
Ensure the element is visible before interacting with it.

```python
# Make sure the element is visible
button = await page.find_element(By.CSS_SELECTOR, 'button.footer')
await button.scroll_into_view()
await button.click()
```

##### `async click(x_offset: int = 0, y_offset: int = 0)`
Click elements with amazing precision - even with offsets.

```python
# Click with custom offset
slider = await page.find_element(By.CSS_SELECTOR, '.slider')
# Click 10px to the right of the element's center
await slider.click(x_offset=10, y_offset=0)
```

##### `async click_using_js()`
Click problematic elements that might be obscured or dynamic.

```python
# Use JavaScript to click difficult elements
overlay_button = await page.find_element(By.CSS_SELECTOR, '.overlay-button')
await overlay_button.click_using_js()
```

##### `async send_keys(text: str)`
Send text to form fields quickly.

```python
# Fill a text field
input_field = await page.find_element(By.CSS_SELECTOR, 'input[name="username"]')
await input_field.send_keys("user123")
```

##### `async type_keys(text: str)`
Type realistically, key by key, simulating human input.

```python
# Type like a real human - with pauses between each key
password_field = await page.find_element(By.CSS_SELECTOR, 'input[type="password"]')
await password_field.type_keys("secure_password123")  # Realistic typing!
```

##### `async get_screenshot(path: str)`
Capture an image of just the element - perfect for testing or evidence.

```python
# Capture screenshots of specific elements
error_message = await page.find_element(By.CSS_SELECTOR, '.error-message')
await error_message.get_screenshot('/screenshots/error.png')
```

The WebElement interface also inherits element finding capabilities from FindElementsMixin, allowing you to find child elements:

##### `async find_element(by: By, value: str, raise_exc: bool = True)`
Find a child element within this element.

```python
# Find an element within another
container = await page.find_element(By.CSS_SELECTOR, '.container')
button = await container.find_element(By.CSS_SELECTOR, 'button')
await button.click()
```

##### `async find_elements(by: By, value: str, raise_exc: bool = True)`
Find all matching child elements within this element.

```python
# Find all items in a list
list_container = await page.find_element(By.CSS_SELECTOR, 'ul.items')
list_items = await list_container.find_elements(By.CSS_SELECTOR, 'li')
# Iterate through found items
for item in list_items:
    text = await item.get_element_text()
    print(f"Item: {text}")
```

##### `async wait_element(by: By, value: str, timeout: int = 10, raise_exc: bool = True)`
Wait until a child element appears within this element.

```python
# Wait for an element to appear within another
modal = await page.find_element(By.CSS_SELECTOR, '.modal')
# Wait up to 5 seconds for confirm button to appear in the modal
confirm_button = await modal.wait_element(By.CSS_SELECTOR, '.confirm', timeout=5)
await confirm_button.click()
```

## 🚀 Advanced Features

### Event System

Pydoll's event system is where the magic really happens! Monitor and react to browser events in real-time for incredibly dynamic automation.

##### `async on(event_name: str, callback: callable, temporary: bool = False) -> int`
Register custom callbacks for any browser event. First, enable the events you want to track. Keep in mind that you can use the global or local event listener.
If you want to use the local listener, enable the events on the page instance.
It's really useful, don't you think?

```python
from pydoll.events.page import PageEvents
# Monitors all navigation events on any page
async def on_page_loaded(event):
    print(f"🌐 Navigating to: {event['params'].get('url')}")

await browser.enable_page_events()  # Activates page events
await browser.on(PageEvents.PAGE_LOADED, on_page_loaded) # Global listener!
# Needs to be locally? Use the page.on method!
await page.on(PageEvents.PAGE_LOADED, on_page_loaded)
```

Need to pass extra parameters to your callback? No problem!

```python
from functools import partial

async def on_page_loaded(page, event):
    print(f"📄 Page loaded: {await page.current_url}")

await browser.on(PageEvents.PAGE_LOADED, partial(on_page_loaded, page))
```

##### `async enable_page_events() -> None`
Track everything happening on your pages - loading states, navigation, DOM changes, and more! This works globally or locally. Just use the browser or the page instance to enable the events.

```python
# Enables page event monitoring
await browser.enable_page_events() # global
```


##### `async enable_network_events() -> None`
See all network activity in real-time - perfect for debugging or monitoring specific API calls!

```python
from pydoll.events.network import NetworkEvents

async def on_request(event):
    print(f"🔄 Request to: {event['params']['request']['url']} will be sent")

await browser.enable_network_events()
await browser.on(NetworkEvents.REQUEST_WILL_BE_SENT, on_request)

await page.go_to('https://www.google.com') # This will trigger the on_request callback
```

##### `async enable_dom_events() -> None`
Watch the page structure change in real-time and react accordingly!

```python
from pydoll.events.dom import DomEvents

async def on_dom_event(event):
    print(f"🔄 The DOM has been updated!")

await browser.enable_dom_events()
await browser.on(DomEvents.DOCUMENT_UPDATED, on_dom_event)
```

##### `async enable_fetch_events(handle_auth_requests: bool = False, resource_type: str = '') -> None`
The ultimate power tool - intercept and modify network requests before they're even sent!

```python
# Intercepts all network requests
from pydoll.events.fetch import FetchEvents
from pydoll.commands.fetch import FetchCommands
from functools import partial

async def interceptor(page, event):
    request_id = event['params']['requestId']
    request_url = event['params']['request']['url']
    print(f"🕵️ Intercepting request to: {request_url}")
    
    # Customize the request however you want!
    await page._execute_command(
        FetchCommands.continue_request(
            request_id=request_id,
            method='GET', # change the HTTP method
            headers={'X-Custom-Header': 'CustomValue'}, # add your own headers
            post_data='Hello World', # modify the request body
            url='https://www.google.com', # even change the destination URL!
            intercept_response=True # and intercept the response too
        )
    )

await browser.enable_fetch_events(resource_type='xhr') # only intercept XHR requests
await browser.on(FetchEvents.REQUEST_PAUSED, partial(interceptor, page))
```

With this power, you can transform your automation into something truly intelligent!

##### `async disable_fetch_events() -> None`
Turn off request interception when you're done.

```python
# Disables request interception
await browser.disable_fetch_events()
```

### Concurrent Scraping

Scrape multiple pages simultaneously with extraordinary performance:

```python
async def concurrent_example():
    pages = [await browser.get_page() for _ in range(10)]
    # Parallel scraping with intelligent resource management
    results = await asyncio.gather(
        *(scrape_page(page) for page in pages)
    )
    # Just declare the scrape_page method and see the magic happens!
```

## 🌟 Best Practices

Get the most out of Pydoll with these tips:

- Use asynchronous patterns throughout your code for maximum performance
- Prefer specific selectors (IDs, data attributes) over generic ones
- Add proper error handling for robust automation
- Use the event system for reactive scenarios rather than constant polling
- Close browser instances when done to avoid memory leaks

## 🤝 Contributing

We'd love your help making Pydoll even better! Check out our contribution guidelines to get started. Whether it's fixing bugs, adding features, or improving documentation - all contributions are welcome!
