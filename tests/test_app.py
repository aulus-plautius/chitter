from playwright.sync_api import Page, expect

# Tests for your routes go here
def test_show_latest_peeps(page: Page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    page.goto(f"http://{test_web_address}/")

    peep_title_elements = page.locator(".peep_title")

    expect(peep_title_elements).to_have_text(
        [
            '4:00pm 22/08/2024: @sarah_d - Sarah Davis',
            '3:30pm 22/08/2024: @sarah_d - Sarah Davis',
            '12:30pm 22/08/2024: @jane_smith - Jane Smith',
            '10:15am 22/08/2024: @david_w - David Wilson',
            '8:00am 22/08/2024: @john_doe - John Doe',
            '7:00pm 21/08/2024: @mike_j - Mike Johnson',
            '9:45am 21/08/2024: @emily_b - Emily Brown',
            '6:30pm 20/08/2024: @john_doe - John Doe'
        ]
    )

    peep_body_elements = page.locator(".peep_body")

    expect(peep_body_elements).to_have_text(
        [
            "Had a great time exploring the city.",
            "Just baked some fresh cookies.",
            "Loving this sunny weather.",
            "Excited for the weekend ahead.",
            "Just finished a great workout!",
            "Reading a fantastic book right now.",
            "Coffee always makes the day better.",
            "Trying out a new recipe tonight."
        ]    
    )

    peep_tags_elements = page.locator(".peep_tags")

    expect(peep_tags_elements).to_have_text(
        [
            "Tagged: @john_doe, @mike_j",
            "Tagged: @jane_smith, @sarah_d",
            "Tagged: @mike_j",
            "Tagged: @john_doe, @sarah_d",
            "Tagged: @mike_j, @sarah_d",
            "Tagged: @john_doe",
            "Tagged: @mike_j",
            "Tagged: @jane_smith"
        ]
    )

def test_user_is_signed_out(page: Page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    page.goto(f"http://{test_web_address}/")

    user_status_element = page.locator(".user")
    expect(user_status_element).to_have_text("You are signed out, please sign in.")

def test_user_signs_in(page: Page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    page.goto(f"http://{test_web_address}/")
    page.locator('#signin').click()
    page.fill("input[name='email']", 'john.doe@example.com')
    page.fill("input[name='password']", 'Pass1234!')
    page.locator('#signin').click()
    user_status_element = page.locator(".user")
    expect(user_status_element).to_have_text("Hello @john_doe")

def test_user_signs_in_then_out(page: Page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    page.goto(f"http://{test_web_address}/")
    page.locator('#signin').click()
    page.fill("input[name='email']", 'john.doe@example.com')
    page.fill("input[name='password']", 'Pass1234!')
    page.locator('#signin').click()
    user_status_element = page.locator(".user")
    expect(user_status_element).to_have_text("Hello @john_doe")
    page.locator('#signout').click()
    user_status_element = page.locator(".user")
    expect(user_status_element).to_have_text("You are signed out, please sign in.")

def test_user_creates_peep(page: Page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    page.goto(f"http://{test_web_address}/")
    page.locator('#signin').click()
    page.fill("input[name='email']", 'john.doe@example.com')
    page.fill("input[name='password']", 'Pass1234!')
    page.locator('#signin').click()
    page.locator('#addpeep').click()
    expect(page.locator(".title")).to_have_text("Add Peep")
    page.fill("input[name='content']", 'This is a new peep.')
    page.select_option("#tags", ["@jane_smith", "@mike_j"])
    page.locator('#addpeep').click()
    peep_body_elements = page.locator("h2")
    peep_body_elements = page.locator(".peep_body")

    expect(peep_body_elements).to_have_text(
        [   
            'This is a new peep.',
            "Had a great time exploring the city.",
            "Just baked some fresh cookies.",
            "Loving this sunny weather.",
            "Excited for the weekend ahead.",
            "Just finished a great workout!",
            "Reading a fantastic book right now.",
            "Coffee always makes the day better.",
            "Trying out a new recipe tonight."
        ]    
    )
    peep_tags_elements = page.locator(".peep_tags")

    expect(peep_tags_elements).to_have_text(
        [
            "Tagged: @jane_smith, @mike_j",
            "Tagged: @john_doe, @mike_j",
            "Tagged: @jane_smith, @sarah_d",
            "Tagged: @mike_j",
            "Tagged: @john_doe, @sarah_d",
            "Tagged: @mike_j, @sarah_d",
            "Tagged: @john_doe",
            "Tagged: @mike_j",
            "Tagged: @jane_smith"
        ]
    )

def test_create_new_user(page: Page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    page.goto(f"http://{test_web_address}/")
    page.locator('#createaccount').click()
    page.fill("input[name='email']", 'test@dummy.com')
    page.fill("input[name='password']", '@TestPassword123')
    page.fill("input[name='name']", 'Test Dummy')
    page.fill("input[name='handle']", '@test_dummy')
    page.locator('#createaccount').click()
    user_status_element = page.locator(".user")
    expect(user_status_element).to_have_text("Hello @test_dummy")

def test_create_new_user_with_invalid_password(page: Page, test_web_address, db_connection):
    db_connection.seed('seeds/peeps_users.sql')
    page.goto(f"http://{test_web_address}/")
    page.locator('#createaccount').click()
    page.fill("input[name='email']", 'test@dummy.com')
    page.fill("input[name='password']", '123')
    page.fill("input[name='name']", 'Test Dummy')
    page.fill("input[name='handle']", '@test_dummy')
    page.locator('#createaccount').click()
    password_message = page.locator(".passwordmessage")
    expect(password_message).to_have_text("Invalid Password")















