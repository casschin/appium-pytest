import pytest
from screens.calulator import Calulator
from screens.map import Map


@pytest.mark.usefixtures('driver_setup')
class TestSomething:
    def test_sum(self):
        calculator = Calulator(self.driver)
        calculator.sum_numbers(3, 4)
        assert calculator.get_element(calculator.sum_label).text == '7'

    def test_alert(self):
        calculator = Calulator(self.driver)
        calculator.trigger_alert()
        assert calculator.is_visible(calculator.alert)

    def test_pan_map(self):
        calculator = Calulator(self.driver)
        calculator.open_map()
        map_element = Map(self.driver)
        map_element.pan_map_area()
        map_element.pan_map_area()
        assert not map_element.is_visible(map_element.current_location)
