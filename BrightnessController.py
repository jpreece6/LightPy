import ConfigReader
import Astro
import time
import datetime

class BrightnessController:

    def CalculateBrightness(self):
        now = datetime.datetime.utcnow()
        early_bound = self.astro.Sunset - datetime.timedelta(hours=1)
        peak_late = self.astro.Sunset + datetime.timedelta(minutes=30)
        late_bound = self.astro.Sunset + datetime.timedelta(hours=1) 

        # N| -> |SS
        if now.time() > early_bound.time() and now.time() < self.astro.Sunset.time():
            diff = self.astro.Sunset - now
            return self.FlipScale(self.Scale(60, diff.seconds / 60))
        
        # SS| -> |EP
        elif now.time() > self.astro.Sunset.time() and now.time() < peak_late.time():
            return self.max_brightness
        
        # EP| -> |LB
        elif now.time() > peak_late.time() and now.time() < late_bound.time():
            corrected = (late_bound - datetime.timedelta(days=1)) # Correct as our value is based on sunset of tomorrow
            diff = corrected - now
            return self.Scale(60, diff.seconds / 60)
        
        # LB| -> |MN
        elif now.time() > late_bound.time():
            return self.night_brightness
        else:
            return 0

    def FlipScale(self, value):
        return ((value - self.max_brightness) +1) *-1 # Scale and flip

    def Scale(self, oldRange, minutes):
        newRange = self.max_brightness - self.night_brightness
        val = ((minutes * newRange) / oldRange) + self.night_brightness
        if (val > self.max_brightness):
            val = self.max_brightness
        elif val < self.night_brightness:
            val = self.night_brightness
        return val

    def UpdateBrightness(self):
        return self.CalculateBrightness()
        #self.cfg['strip']['brightness'] = self.CalculateBrightness()
        #ConfigReader.Dump(self.cfg)

    def __init__(self, cfg):
        self.cfg = cfg #ConfigReader.GetConfig()
        self.astro = Astro.AstroCalculator()
        self.midnight = datetime.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
        self.max_brightness = self.cfg['strip']['max_brightness']
        self.night_brightness = self.cfg['strip']['night_brightness']