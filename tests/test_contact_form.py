from pages.contact_page import ContactPage
import time


def test_contact_form(driver):

    driver.get(
        "https://practicesoftwaretesting.com/contact"
    )

    contact_page = ContactPage(driver)

    print("\nTEST CASE : CONTACT FORM")

    # =========================
    # FIRST NAME
    # =========================

    contact_page.enter_first_name(
        "Mim"
    )

    print("First Name Entered")

    # =========================
    # LAST NAME
    # =========================

    contact_page.enter_last_name(
        "Rahman"
    )

    print("Last Name Entered")

    # =========================
    # EMAIL
    # =========================

    contact_page.enter_email(
        "rmim2906@gmail.com"
    )

    print("Email Entered")

    # =========================
    # SUBJECT
    # =========================

    contact_page.select_subject(
        "Customer service"
    )

    print("Subject Selected")

    # =========================
    # MESSAGE
    # =========================

    contact_page.enter_message(
        "This is Selenium automation testing project for practicing contact form validation and submission testing."
    )

    print("Message Entered")

    # =========================
    # FILE UPLOAD
    # =========================

    contact_page.upload_file(
        r"D:\Selenium-Project\test.txt"
    )

    print("File Uploaded")

    time.sleep(2)

    # =========================
    # SEND BUTTON
    # =========================

    contact_page.click_send()

    print("Send Button Clicked")

    time.sleep(3)

    # =========================
    # SUCCESS MESSAGE
    # =========================

    success_message = (
        contact_page.get_success_message()
    )

    print("\nSUCCESS MESSAGE:\n")

    print(success_message)

    assert (
        "Thanks for your message"
        in success_message
    )

    print(
        "\nCONTACT FORM TEST PASSED"
    )