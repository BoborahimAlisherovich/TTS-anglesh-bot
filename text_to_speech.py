from gtts import gTTS 



import os
def tts(mytext):
   
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    
    myobj.save(f"{mytext}.mp3") 
        

    os.system(f"{mytext}.mp3")

