from threading import Thread


class SendEmailWithThreading(Thread):
    def __init__(self, email_obj):
        super().__init__()
        self.email_obj = email_obj

    def run(self):
        self.email_obj.send()