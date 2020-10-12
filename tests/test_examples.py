import pytest
import logging
from selenium import webdriver
from selenium.webdriver.support.select import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
logger = logging.getLogger(__name__)

def test_python_dot_org():
    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        desired_capabilities=DesiredCapabilities.CHROME,
    )

    driver.get("http://www.python.org")
    assert "Python" in driver.title
    logger.info(f"the driver title is: {driver.title}")
    elem = driver.find_element(by=By().NAME, value="q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()