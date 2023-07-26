# speech-transcriber 

A useful little script for quickly transcribing English speech-to-text using OpenAI's Whisper models.

## Setting Up 

You'll need:

- Python 3.9+ (3.11.x recommended)
- 3 minutes of your time

To get started:

- Install pip dependencies into a new virtualenv
  ```sh 
  python -m venv env && source env/bin/activate && pip install -r requirements
  ```
- Run main.py with the input/output files you want to transcribe:
  ```sh
  python -m main -i myrecording.mp3 -o output.txt
  ```
- Check `output.txt` to see the result.  You can also change the Whisper model with:
  ```sh
  python -m main -i myrecording.mp3 -o output.txt -m medium.en
  ```

  Valid Whisper models are:
    - tiny.en
    - base.en
    - small.en
    - medium.en
    - large-v1
    - large-v2
    - large