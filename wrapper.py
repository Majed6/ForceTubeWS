from ctypes import *
import json
import os
import time

class ForceTubeVRChannel:
    all = 0
    rifle = 1
    rifleButt = 2
    rifleBolt = 3
    pistol1 = 4
    pistol2 = 5
    other = 6
    vest = 7

class Wrapper:
    def __init__(self):
        cwd = os.getcwd()
        self.ForceTubeVR_API_x64 = CDLL(cwd + "/ForceTubeVR_API_x64.dll")
        self.InitPistol = self.ForceTubeVR_API_x64['InitPistol']
        self.InitRifle = self.ForceTubeVR_API_x64['InitRifle']
        self.SetActiveResearch = self.ForceTubeVR_API_x64['SetActive']
        self.Kick = self.ForceTubeVR_API_x64['KickChannel']
        self.Rumble = self.ForceTubeVR_API_x64['RumbleChannel']
        self.Shot = self.ForceTubeVR_API_x64['ShotChannel']
        self.TempoToKickPower = self.ForceTubeVR_API_x64['TempoToKickPower']
        self.GetBatteryLevel = self.ForceTubeVR_API_x64['GetBatteryLevel']
        self.ListConnectedForceTube = self.ForceTubeVR_API_x64['ListConnectedForceTube']
        self.ListConnectedForceTube.restype = c_char_p
        self.ListChannels = self.ForceTubeVR_API_x64['ListChannels']
        self.ListChannels.restype = c_char_p
        self.InitChannels = self.ForceTubeVR_API_x64['InitChannels']
        self.AddToChannel = self.ForceTubeVR_API_x64['AddToChannel']
        self.RemoveFromChannel = self.ForceTubeVR_API_x64['RemoveFromChannel']
        self.ClearChannel = self.ForceTubeVR_API_x64['ClearChannel']
        # self.ClearAllChannel = self.ForceTubeVR_API_x64['ClearAllChannel']

        self.InitPistol()
        self.InitRifle()

    def demo(func):
        def waitForConnection(self):
            now = time.time()
            connectedList = {'Connected': []}
            while len(connectedList['Connected']) == 0 and time.time() - now < 30:
                connectedList = json.loads(self.ListConnectedForceTube())
                time.sleep(5)
            if len(connectedList['Connected']):
                print("Device connected")
                func(self)
        return waitForConnection

    @demo
    def Sniper(self):
        self.Shot(255,0,0,ForceTubeVRChannel.all)


    @demo
    def P90(self):
        for i in range(10):
            self.Shot(82,0,0,ForceTubeVRChannel.all)
            time.sleep(0.062)
    @demo
    def M16(self):
        for i in range(3):
            self.Shot(105,0,0,ForceTubeVRChannel.all)
            time.sleep(0.071)
    @demo
    def PKM(self):
        for i in range(20):
            self.Shot(156,0,0,ForceTubeVRChannel.all)
            time.sleep(0.091)
    @demo
    def LaserGun(self):
        for i in range(80):
            time.sleep(0.020)
            rumblePower = (255/80)*float(i+1)
            self.Shot(0,int(rumblePower),0,ForceTubeVRChannel.all)
        time.sleep(2)
        self.Shot(255,0,0,ForceTubeVRChannel.all)

        