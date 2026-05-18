import re, pytest

from playwright.sync_api import Page, expect

def test_title_is_present_on_page(live_server , page: Page):
    page.goto(f"{live_server.url()}/duties")
    expect(page).to_have_title(re.compile(r"Duties"))
    
def test_user_can_add_a_new_duty(live_server, page: Page):
    page.goto(f"{live_server.url()}/duties")
    expect(page).to_have_title(re.compile(r"Duties"))
    expect(page.get_by_role('link', name='Add Duty')).to_be_visible()
    page.get_by_role('link', name='Add Duty').click()
    expect(page.get_by_label("Name:")).to_be_visible()
    expect(page.get_by_label("Description:")).to_be_visible()
    expect(page.get_by_role("button", name="Create")).to_be_enabled()
    page.get_by_label("Name:").fill("D1")
    page.get_by_label("Description:").fill("Desc 1")
    page.get_by_role("button", name="Create").click()

    expect(page).to_have_title(re.compile(r"Duties"))
    expect(page.get_by_text("D1")).to_be_visible()
    expect(page.get_by_text("Desc 1")).to_be_visible()

def test_user_can_navigate_to_all_pages(live_server, page: Page):
    page.goto(f"{live_server.url()}/")
    expect(page.get_by_text("hello there")).to_be_visible()
    expect(page.get_by_role("link", name="Duties")).to_be_visible()
    page.get_by_role("link", name="Duties").click()

    expect(page).to_have_url(f"{live_server.url()}/duties")
    expect(page).to_have_title(re.compile(r"Duties"))
    expect(page.get_by_role('link', name='Add Duty')).to_be_visible()
    page.get_by_role('link', name='Add Duty').click()
    
    expect(page).to_have_url(f"{live_server.url()}/duties/new")
    expect(page.get_by_label("Name:")).to_be_visible()
    expect(page.get_by_label("Description:")).to_be_visible()
    expect(page.get_by_role("link", name="Cancel")).to_be_enabled()
    page.get_by_role("link", name="Cancel").click()

    expect(page).to_have_title("Duties")

def test_user_sees_error_message_on_duplicate_duty(live_server, page: Page):
    page.goto(f"{live_server.url()}/duties")
    expect(page).to_have_title(re.compile(r"Duties"))
    expect(page.get_by_role('link', name='Add Duty')).to_be_visible()
    page.get_by_role('link', name='Add Duty').click()
    expect(page.get_by_label("Name:")).to_be_visible()
    expect(page.get_by_label("Description:")).to_be_visible()
    expect(page.get_by_role("button", name="Create")).to_be_enabled()
    page.get_by_label("Name:").fill("D1")
    page.get_by_label("Description:").fill("Desc 1")
    page.get_by_role("button", name="Create").click()

    expect(page).to_have_title(re.compile(r"Duties"))
    expect(page.get_by_text("D1")).to_be_visible()
    expect(page.get_by_text("Desc 1")).to_be_visible()

    page.get_by_role('link', name='Add Duty').click()
    expect(page.get_by_label("Name:")).to_be_visible()
    expect(page.get_by_label("Description:")).to_be_visible()
    expect(page.get_by_role("button", name="Create")).to_be_enabled()
    page.get_by_label("Name:").fill("D1")
    page.get_by_label("Description:").fill("Desc 1")
    page.get_by_role("button", name="Create").click()

    expect(page).to_have_title(re.compile(r"Duties"))
    expect(page.get_by_text("A duty with this name already exists")).to_be_visible()
    


