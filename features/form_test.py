from playwright.async_api import async_playwright
import utils.secrets as secrets

### debugging mode
import os
os.environ['PWDEBUG'] = '1'

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()

        # Navigate to the page
        await page.goto("https://app.mightyfields.com/")

        # Fill-in login credentials
        await page.fill('input[placeholder="Email"]', secrets.username)
        await page.fill('input[placeholder="Password"]', secrets.password)
        await page.get_by_role("button", name="Submit").click()
        
        # Create a new case by clicking Start a new case from the navigation tab
        await page.get_by_role("link", name="Start new case").click()

        # Select "test" category
        await page.get_by_role("heading", name="test", exact=True).click()
        # Select "SimpleTestForm" procedure
        await page.get_by_role("heading", name="SimpleTestForm").click()
        # Create a new case
        await page.get_by_role("button", name="Create").click()

        # Input client information
        await page.locator("#procedureForm input[type=\"text\"]").click()
        await page.locator("#procedureForm input[type=\"text\"]").fill("Miha")
        await page.locator("input[type=\"tel\"]").click()
        await page.locator("input[type=\"tel\"]").fill("36")
        await page.get_by_label("SlovenijaItalijaAustrijaHrvaš").select_option("5e3d0319cddfd91e006f78d6")

        # Toggle Language switch
        await page.locator("label").filter(has_text="English").locator("div").nth(1).click()
        await page.get_by_label("UltraMega").select_option("624eb8ec15f93801004f59c5")

        # Dismiss cookie message
        await page.get_by_label("dismiss cookie message").click()
        
        # Click "Finish" tab and push the form to cloud
        await page.locator("a").filter(has_text="Finish").click()
        await page.get_by_role("button", name="Close case").click()
        await page.get_by_role("button", name="Yes").click()
        await page.get_by_role("button", name="OK").click()
       
        ### CLOSE BROWSER ###
        await browser.close()