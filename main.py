from argparse import ArgumentParser
from whisper import available_models
from transcriber import Transcriber

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="speech-transcriber",
        description="Speech-to-text using OpenAI's Whisper model",
    )
    parser.add_argument("-v", "--verbose", action="store_true", default=True)
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", default="output.txt")
    parser.add_argument("-m", "--model", default="base.en", choices=available_models())
    args = parser.parse_args()

    with Transcriber(model=args.model) as transcriber:
        text = transcriber.voice_to_text(audio_path=args.input, verbose=args.verbose)
        transcriber.write_output_to_disk(text, args.output)
