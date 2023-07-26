import argparse
import whisper


class Transcriber:
    def __init__(self, model: str):
        if model not in whisper.available_models():
            raise ValueError(
                f"Model {model} not available. Available models: {whisper.available_models()}"
            )

        self.model = whisper.load_model(model)

    # for context manager
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.model = None

    def voice_to_text(self, audio_path: str, verbose: bool = False):
        result = self.model.transcribe(audio_path, verbose=verbose, fp16=False)
        return result["text"]

    def write_output_to_disk(self, text: str, output_path: str):
        with open(output_path, "w") as f:
            f.write(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="speech-transcriber",
        description="Speech-to-text using OpenAI's Whisper model",
    )
    parser.add_argument("-v", "--verbose", action="store_true", default=True)
    parser.add_argument("-i", "--input", type=str, required=True)
    parser.add_argument("-o", "--output", type=str, default="output.txt")
    parser.add_argument("-m", "--model", type=str, default="base.en", choices=whisper.available_models())
    args = parser.parse_args()

    with Transcriber(model=args.model) as transcriber:
        text = transcriber.voice_to_text(audio_path=args.input, verbose=args.verbose)
        transcriber.write_output_to_disk(text, args.output)
