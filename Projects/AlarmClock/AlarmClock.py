from playsound import playsound
import time


def alarm(sec):
    time_alapsed = 0

    while time_alapsed < 5:
        time.sleep(1)
        time_alapsed += 1
        if time_alapsed == 5:
            playsound("./ringtone.mp3")


alarm(5)
