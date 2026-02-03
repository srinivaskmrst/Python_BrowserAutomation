from browser_agent import BrowserAgent

browser = BrowserAgent()
browser.start_browser()

browser.login("abc@gmail.com", "12345678")

browser.close_browser()
