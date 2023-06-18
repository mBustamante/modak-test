
class NotificationThrottleException(Exception):
    def __init__(self, message='Notification limit exceeded'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class NotificationAlreadySentException(Exception):
    def __init__(self, message='Notification already sent'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
