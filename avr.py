import rumps


class AvrApp(object):
    def __init__(self):
        self.app = rumps.App("AVR", "💿")

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = AvrApp()
    app.run()
