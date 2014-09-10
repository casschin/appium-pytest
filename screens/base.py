from screens.screen import Screen


class Base(Screen):

    # Alerts
    alert = ('class_name', 'UIAAlert')
    alert_title = ('id', 'Cool title')
    alert_text = ('id', 'this alert is so cool.')
    alert_cancel_button = ('id', 'Cancel')
    alert_ok_button = ('id', 'OK')
