import pyaudio
import pyttsx3
import speech_recognition as sr
import wave
import whisper

def load_model():
    model = whisper.load_model("base")
    return model

def config_speech():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('rate', 150) 
    engine.setProperty('volume',1.0)
    engine.setProperty('voice', voices[1].id)

    return engine

def record_audio(audio):
    temp_audio_file = "temp_audio.wav"
    with open(temp_audio_file, "wb") as f:
        f.write(audio.get_wav_data())

    return temp_audio_file

def microphone():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print('Speak the sentence:')
        audio = r.listen(mic)

    temp_audio_file = record_audio(audio)

    return temp_audio_file

def play_audio(audio_file):
    p = pyaudio.PyAudio()
    wf = wave.open(audio_file, 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

    chunk_size = 1024
    data = wf.readframes(chunk_size)

    while data:
        stream.write(data)
        data = wf.readframes(chunk_size)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

def speach_to_text(audio_file, model):
    my_audio = whisper.load_audio(audio_file)
    my_audio = whisper.pad_or_trim(my_audio)
    mel = whisper.log_mel_spectrogram(my_audio).to(model.device)
    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)
    return result.text

def user_interection(engine, model):
    initial = True
    while initial:
        navegation = True
        print('MENU:')
        print('1. REPEAT')
        print('2. SPEAK:')
        print('')
        print('Enter with a sentence:')
        sentence = input()

        while navegation:
            engine.say(sentence)
            engine.runAndWait()
            engine.stop()

            menu = input('MENU: ')

            if menu == '1':
                navegation = True
            elif menu == '2':
                speach_again = True

                while speach_again:
                    audio_file = microphone()
                    sub_navegation = True

                    while sub_navegation:
                        play_audio(audio_file)
                        text = speach_to_text(audio_file, model)
                        print('USER: ',text)
                        print('')
                        sub_menu = input('Press: \n 3) to listen again\n 4) to speach again \n 6) enter with other sentence: ')
                        
                        if sub_menu == '3':
                            sub_navegation = True
                        elif sub_menu == '4':
                            speach_again = True
                            sub_navegation = False
                        elif sub_menu == '6':
                            speach_again = False
                            navegation = False
                            sub_navegation = False
                            initial = True
                        else:
                            print('THE END')
                            speach_again = False
                            sub_navegation = False
                            navegation = False
                            initial = False

def main():
    model = load_model()
    engine = config_speech()
    user_interection(engine, model)

if __name__ == '__main__':
    main()