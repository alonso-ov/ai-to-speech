# ChatGPT Voice Assistant

This Python script utilizes the OpenAI GPT-3.5 Turbo model and Google Text-to-Speech (gTTS) to create a simple voice-based chat interface. The user can interact with the script by speaking, and the program generates responses using the ChatGPT model. Additionally, it converts the responses into speech and plays them back to the user.

## Prerequisites

Before running the script, make sure to install the required Python packages. You can install them using the following commands:

```bash
pip install gtts
pip install openai
pip install SpeechRecognition
pip install colorama
pip install python-dotenv
```

Please note that the script uses `afplay` as the audio player, which is a macOS-specific command. If you're using a different operating system, you may need to replace this command with a suitable alternative.

## Setup

1. Install the required packages using the commands mentioned above.
2. Set up a virtual environment if desired.
3. Obtain an OpenAI API key and set it as an environment variable. You can do this by creating a `.env` file in the project directory with the following content:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the script using the following command:

```bash
python script_name.py
```

Once the script is running, speak into the microphone when prompted, and the program will generate responses using ChatGPT and play them back as audio.

## Troubleshooting

If you encounter any issues with package installations or the speech recognition library, refer to the provided links in the comments for possible solutions.

## Disclaimer

This script is a basic example and might require additional adjustments based on your specific use case. Ensure compliance with OpenAI's usage policies when integrating the GPT-3.5 Turbo model into your projects.

Feel free to modify and enhance the script to suit your needs!
