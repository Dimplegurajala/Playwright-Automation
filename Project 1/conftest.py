import pytest
from playwright.sync_api import sync_playwright
from datetime import datetime
import os

# --- FIXTURE: BROWSER SETUP & TRACING ---
@pytest.fixture(scope="function")
def page_context():
    with sync_playwright() as p:
        # 1. Launch Browser (Headless=False to see it)
        browser = p.chromium.launch(headless=False, slow_mo=500)
        
        # 2. Create Context (Incognito mode)
        context = browser.new_context()
        
        # 3. Start Visual Tracing (Screenshots/Network Logs)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        page = context.new_page()
        
        # 4. Global Pop-up Handler (Auto-accept alerts)
        page.on("dialog", lambda dialog: dialog.accept())
        
        yield page # Test runs here!
        
        # 5. Teardown
        context.tracing.stop()
        context.close()
        browser.close()

# --- HOOK: SAVE ARTIFACTS ON FAILURE ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if "page_context" in item.funcargs:
            page = item.funcargs["page_context"]
            
            # Create reports folder if missing
            os.makedirs("reports", exist_ok=True)
            timestamp = datetime.now().strftime("%H-%M-%S")
            
            # Save Trace.zip
            trace_path = f"reports/trace_{item.name}_{timestamp}.zip"
            page.context.tracing.stop(path=trace_path)
            
            # Save Screenshot
            page.screenshot(path=f"reports/screen_{item.name}_{timestamp}.png")