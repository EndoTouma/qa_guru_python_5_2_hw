from selene import have, be, Browser
from selene.support.shared import browser, config


def test_successful_google_search(setup_browser):
	browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
	browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_successful_no_results(setup_browser):
	browser.element('[name="q"]').should(be.blank).type('wdf2345tge5466457').press_enter()
	browser.element('[id = "result-stats"]').should(have.text("Результатов: примерно 0"))
	print("Поиск по данному запросу не выдает результатов")
