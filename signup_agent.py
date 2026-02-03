from playwright.sync_api import sync_playwright
import os
import time

file_path = os.path.abspath("signup.html")

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        slow_mo=500   # slows down every action (ms)
    )

    page = browser.new_page()

    # Open page
    page.goto("file:///" + file_path)

    # Bring page to front (activate window)
    page.bring_to_front()

    page.wait_for_timeout(2000)  # wait 2 sec after page load

    # Fill fields with delay
    page.type("#firstName", "John", delay=150)
    time.sleep(1)

    page.type("#lastName", "Doe", delay=150)
    time.sleep(1)

    page.select_option("#day", "2")
    time.sleep(1)

    page.select_option("#month", "Feb")
    time.sleep(1)

    page.select_option("#year", "1995")
    time.sleep(1)

    page.check("input[value='Male']")
    time.sleep(1)

    page.type("#email", "john@test.com", delay=150)
    time.sleep(1)

    page.type("#password", "Test@123", delay=150)
    time.sleep(1)

    page.click("#submitBtn")

    page.wait_for_timeout(5000)
    browser.close()
