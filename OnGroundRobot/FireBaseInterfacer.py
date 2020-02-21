import pyrebase

class FireBaseUpdater():
    firebase = None
    info = None
    db = None

    firebase = None;
    def __init__(self, config):
        self.firebase = pyrebase.initialize_app(config)
        self.db = self.firebase.database()

    def get_information(self):
        self.info = self.db.child("OnGroundRobot").child("Receive").get().val()
        return self.info

    def write_information(self, ControllerLy: float, ControllerRx: float, light_on: bool):
        data = {'ControllerLy_Rx':[ControllerLy, ControllerRx], 'LightOne': True}
        self.db.child("OnGroundRobot").child("Send").set(data)

def main():
    config = {
        "apiKey": "AIzaSyBBFze3rkgjPBwEkno8ZFOuHZLCWhbXstk",
        "authDomain": "synopsys2020-1.firebaseapp.com",
        "databaseURL": "https://synopsys2020-1.firebaseio.com/",
        "storageBucket": "synopsys2020-1.appspot.com"
    }
    db = FireBaseUpdater(config)

    print(db.get_information())
    db.write_information(.2, .2, True)

if __name__ == "__main__":
    main()