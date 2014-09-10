# Appium with py.test

Example of how I'm currently using py.test with tests written with [Appium](http://appium.io/) modeled closely to how [Mozilla's WebQA framework](https://github.com/mozilla/mozwebqa-test-templates).

You can clone this repo and run the example tests provided -- test iOS app is provided by the [Appium Python Client](https://github.com/appium/python-client) project. You'll need to make sure that you set up your enironment properly using the [Appium documentation](http://appium.io/slate/en/master/?python#setting-up-appium).

## File overview

`conftest.py` holds the Appium driver setup/teardown using py.test fixtures

`/app`:

* `TestApp.app.zip` is a test iOS app

`/screens`:

* `screen.py` contains custom helpers for Appium that can apply to any Appium project
* `base.py` extends `screen.py` and includes general locators that aren't specific to any screen in your app
* `calculator.py` and `map.py` represent individual screens in the app that extends `base.py`. These files include the locators and specific functions that apply to each

`/tests`:

* `test_something.py` contains the tests and is marked to use the `driver_setup` fixture defined in `conftest.py`
