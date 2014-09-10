import pytest
import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@pytest.fixture()
def driver_setup(request):
    capabilities = {
        'platformName':     'iOS',
        'deviceName':       'iPhone Simulator',
        'app':              PATH('app/TestApp.app.zip'),
    }
    url = 'http://localhost:4723/wd/hub'
    request.instance.driver = webdriver.Remote(url, capabilities)

    def teardown():
        request.instance.driver.quit()
    request.addfinalizer(teardown)
