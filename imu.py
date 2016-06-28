from Phidgets.Devices.Spatial import Spatial

class IMU(object):

    device = None

    def __init__(self):
        self.spatial = Spatial()
        self.spatial.setOnSpatialDataHandler(self.getDataHandler)
        self.spatial.setOnAttachHandler(self.attachDeviceHandler)
        self.spatial.openPhidget()
        self.spatial.waitForAttach(10000)
        self.spatial.setDataRate(16)

    def attachDeviceHandler(self, e):
        self.device = e.device

    def getDataHandler(self,e):
        for data in e.spatialData:
            if len(data.Acceleration) > 0:
                print "Acc",
                print data.Acceleration[0],
                print data.Acceleration[1],
                print data.Acceleration[2],
            if len(data.AngularRate) > 0:
                print "Gyr",
                print data.AngularRate[0],
                print data.AngularRate[1],
                print data.AngularRate[2],
            if len(data.MagneticField) > 0:
                print "Mag",
                print data.MagneticField[0],
                print data.MagneticField[1],
                print data.MagneticField[2]
 
