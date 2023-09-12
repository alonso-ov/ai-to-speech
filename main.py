from gtts import gTTS # needed to install brew 
import os
import openai
import speech_recognition as sr # Issues installing -> https://stackoverflow.com/questions/55984129/attributeerror-could-not-find-pyaudio-check-installation-cant-use-speech-re
from colorama import Fore, Style
from dotenv import load_dotenv # Needed to install python-dotenv


#load local environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []


while True:
    try:
        recon_obj = sr.Recognizer()

        # Get user audio input
        with sr.Microphone() as source:


            print(Fore.CYAN + "\nSay something!\n" + Style.RESET_ALL)

            audio = recon_obj.listen(source)
            user_input = recon_obj.recognize_google(audio)
        
        messages.append({ "role": "user", "content": user_input })

        # Print user input
        text = "\nYou: " + user_input
        text = text.replace("You", Fore.GREEN + "You" + Style.RESET_ALL)
        print(text)

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        reply = chat["choices"][0].message.content

        # Print reply
        text = "\nChatGPT: " + reply
        text = text.replace("ChatGPT", Fore.CYAN + "ChatGPT" + Style.RESET_ALL)
        print(text)

        # Create a gTTS object
        tts = gTTS(reply)

        # Save the audio as a file
        tts.save("output.mp3")

        # Play the audio (you may need a media player)
        os.system("afplay output.mp3")
    except KeyboardInterrupt:
        print("\nKeyboard Interruption\n")
        break
    except sr.UnknownValueError:
        print("\nCould not understand audio\n")
        break
    except sr.RequestError as e:
        print("\nCould not request results; {0}\n".format(e))
        break
    except FileNotFoundError:
        print("\nFileNotFoundError\n")
        break

# Remove file
os.remove("output.mp3")

print("\n ** Goodbye! ** \n")