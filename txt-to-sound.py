from PIL import Image
import  pytesseract  
import vlc
import gtts


text="hello"
tts=gtts.gTTS(text,lang='en',slow='false')
tts.save('voice.mp3')
instance = vlc.Instance('--aout=alsa')
p = instance.media_player_new()
m = instance.media_new('voice.mp3') 
p.set_media(m)
p.play() 
p.pause() 
vlc.libvlc_audio_set_volume(p, 200)
