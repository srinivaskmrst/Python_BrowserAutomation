from playwright.sync_api import sync_playwright
import pandas as pd

class BrowserAgent:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None


    def fileread(filepath):
        data = pd.read_excel(filepath)
        return data
    
    def start_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False, slow_mo=500)
        self.page = self.browser.new_page()
        self.page.set_viewport_size({"width": 1280, "height": 800})

    def login(self, username, password):
        print("Opening login page...")

        # Open login page
        self.page.goto("https://www.facebook.com")

        # Wait for input fields
        self.page.wait_for_selector("input[placeholder='Email address or phone number']")

        # Fill username and password
        self.page.get_by_placeholder("Email address or phone number").fill(username)
        self.page.get_by_placeholder("Password").fill(password)

        # Click Login button
        self.page.get_by_role("button", name="Log in").click()

        self.page.wait_for_timeout(3000)
        print("Login attempted")

    def close_browser(self):
        self.browser.close()
        self.playwright.stop()
        print("Browser closed")
