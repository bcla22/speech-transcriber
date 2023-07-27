from whisper import available_models, load_model
from pathlib import Path

class Transcriber:
    def __init__(self, model: str):
        if model not in available_models():
            raise ValueError(f"Model {model} not available. Available models: {available_models()}")

        self.model = load_model(model)

    # for context manager
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.model = None

    def voice_to_text(self, audio_path: str, verbose: bool = False):
        assert self._is_file(audio_path), f"Input file not found: {audio_path}"
        assert self._is_audio_file(audio_path), f"Input file is not an audio format: {audio_path}"
        
        result = self.model.transcribe(audio_path, verbose=verbose, fp16=False)
        return result["text"]

    def write_output_to_disk(self, text: str, output_path: str):
        if self._is_file(output_path):
            output_path = self._add_number_to_filename(output_path)
        with open(output_path, "w") as f:
            f.write(text)
    
    def _is_file(self, path: str) -> bool:
        return Path(path).is_file()

    def _is_audio_file(self, path: str) -> bool:
        valid_ffmpeg_formats = ["mp3", "wav", "flac", "ogg", "m4a", "wma", "aac", "aiff", "opus"]
        return Path(path).suffix[1:] in valid_ffmpeg_formats
    
    def _add_number_to_filename(self, path: str) -> str:
        filename = Path(path).stem
        suffix = Path(path).suffix
        return f"{filename}_1{suffix}"