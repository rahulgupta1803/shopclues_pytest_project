import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(browser):
    if browser=="chrome":
        print("launching chrome")
        driver = webdriver.Chrome()

    elif browser=='firefox':
        print('launching firefox')
        driver = webdriver.Firefox()

    elif browser=="edge":
        print("launching edge")
        driver = webdriver.Edge()

    else:
        print("headless")
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get("https://www.shopclues.com/")
    return driver

def pytest_metadata(metadata):
    metadata["class"] = "Credence"
    metadata["Batch"] = 'CT-15'
    metadata ["url"] = "https://www.shopclues.com/"
    metadata.pop("Python",None)


