import denonavr
import rumps

zone2 = {"Zone2": "Office"}
d = denonavr.DenonAVR("192.168.1.212", add_zones=zone2)
d.update()


class AvrApp(object):
    def __init__(self):
        self.app = rumps.App("AVR", "🎛️")

    print(d.volume, d.zones["Zone2"].volume)

    @rumps.clicked("Volume +")
    def volume_up(self):
        d.zones["Zone2"].volume_up()
        d.zones["Zone2"].update()
        print("Up volume is: ", d.zones["Zone2"].volume)

    @rumps.clicked("Volume -")
    def volume_up(self):
        d.zones["Zone2"].volume_down()
        d.zones["Zone2"].update()
        print("Down volume is: ", d.zones["Zone2"].volume)

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = AvrApp()
    app.run()
