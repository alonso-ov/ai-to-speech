from gtts import gTTS
import os
import openai
from dotenv import load_dotenv

#load local environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

chat = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "What is your name?"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

reply = chat["choices"][0].message.content

print(reply)

# Create a gTTS object
tts = gTTS(reply)

# Save the audio as a file
tts.save("output.mp3")

# Play the audio (you may need a media player)
os.system("afplay output.mp3")
os.remove("output.mp3")
