class Solution:
    def trafficSignal(self, timer: int) -> str:
        signals = {0: "Green", 30: "Orange"}

        if timer in signals:
            return signals[timer]

        if 30 < timer <= 90:
            return "Red"

        return "Invalid"
