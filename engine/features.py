from playsound import playsound
import eel

# Playing Assiatant Sound Function

@eel.expose
def playAssistentSound():
    music_dir = "www\\assets\\vendore\\texllate\\audio\\start_sound.mp3"
    playsound(music_dir)