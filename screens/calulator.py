from screens.base import Base


class Calulator(Base):
    first_value_input = ('id', 'TextField1')
    second_value_input = ('id', 'TextField2')
    compute_sum_button = ('id', 'ComputeSumButton')
    sum_label = ('xpath', '//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]')
    show_alert_button = ('id', 'show alert')
    test_gesture_button = ('id', 'Test Gesture')

    def trigger_alert(self):
        self.click(self.show_alert_button)

    def open_map(self):
        self.click(self.test_gesture_button)
        self.click(self.alert_ok_button)

    def sum_numbers(self, first, second):
        self.send_keys(self.first_value_input, str(first))
        self.send_keys(self.second_value_input, str(second))
        self.click(self.compute_sum_button)
