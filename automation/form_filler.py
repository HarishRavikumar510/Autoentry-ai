import sys
import asyncio

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from playwright.sync_api import sync_playwright


def fill_google_form(form_url, row_data):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(form_url, timeout=60000)

        page.wait_for_timeout(3000)

        # Get all text input fields
        text_inputs = page.locator("input[type='text']")

        input_count = text_inputs.count()

        values = list(row_data.values())

        # Fill fields one by one
        for i in range(min(input_count, len(values))):

            text_inputs.nth(i).fill(str(values[i]))

            page.wait_for_timeout(500)

        # Click submit button
        submit_button = page.get_by_role("button", name="Submit")
        submit_button.click()

        page.wait_for_timeout(5000)

        browser.close()

    return True