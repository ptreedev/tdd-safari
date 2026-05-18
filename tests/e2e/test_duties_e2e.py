import re

from playwright.sync_api import Page, expect

duties_regex = re.compile(r"Duties")

def add_duty(page: Page, name="D1", description="Desc 1"):
    page.goto("/duties/new")
    page.get_by_label("Name:").fill(name)
    page.get_by_label("Description:").fill(description)
    page.get_by_role("button", name="Create").click()

def test_title_is_present_on_page(live_server , page: Page):
    page.goto("/duties")
    expect(page).to_have_title(duties_regex)
    
def test_user_can_add_a_new_duty(live_server, page: Page):
    add_duty(page)

    expect(page).to_have_title(duties_regex)
    expect(page.get_by_text("D1")).to_be_visible()
    expect(page.get_by_text("Desc 1")).to_be_visible()

def test_user_can_navigate_to_all_pages(live_server, page: Page):
    page.goto("/")
    expect(page.get_by_text("hello there")).to_be_visible()
    expect(page.get_by_role("link", name="Duties")).to_be_visible()
    page.get_by_role("link", name="Duties").click()

    expect(page).to_have_url(f"{live_server.url()}/duties")
    expect(page).to_have_title(duties_regex)
    expect(page.get_by_role('link', name='Add Duty')).to_be_visible()
    page.get_by_role('link', name='Add Duty').click()
    
    expect(page).to_have_url(f"{live_server.url()}/duties/new")
    expect(page.get_by_label("Name:")).to_be_visible()
    expect(page.get_by_label("Description:")).to_be_visible()
    expect(page.get_by_role("link", name="Cancel")).to_be_enabled()
    page.get_by_role("link", name="Cancel").click()

    expect(page).to_have_title("Duties")

def test_user_sees_error_message_on_duplicate_duty(live_server, page: Page):
    add_duty(page)

    expect(page).to_have_title(duties_regex)
    expect(page.get_by_text("D1")).to_be_visible()
    expect(page.get_by_text("Desc 1")).to_be_visible()

    add_duty(page)

    expect(page).to_have_title(duties_regex)
    expect(page.get_by_text("A duty with this name already exists")).to_be_visible()
    


