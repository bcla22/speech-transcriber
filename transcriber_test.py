from unittest import TestCase, main
from unittest.mock import patch, MagicMock, PropertyMock, mock_open
from pathlib import Path
from transcriber import Transcriber


class TestTranscriber(TestCase):
    @patch("transcriber.available_models")
    @patch("transcriber.load_model")
    def test_init(self, mock_load_model, mock_available_models):
        mock_available_models.return_value = ["base.en"]
        t = Transcriber("base.en")
        self.assertEqual(t.model, mock_load_model.return_value)

    @patch("transcriber.available_models")
    @patch("transcriber.load_model")
    def test_init_invalid_model(self, mock_load_model, mock_available_models):
        mock_available_models.return_value = ["base.en"]
        with self.assertRaises(ValueError):
            t = Transcriber("invalid_model")

    @patch.object(Path, "is_file")
    @patch.object(Path, "suffix", new_callable=PropertyMock)
    @patch("transcriber.load_model")
    def test_voice_to_text(self, mock_load_model, mock_suffix, mock_is_file):
        mock_model = MagicMock()
        mock_load_model.return_value = mock_model
        mock_model.transcribe.return_value = {"text": "Hello, World!"}
        mock_is_file.return_value = True
        mock_suffix.return_value = ".wav"
        t = Transcriber("base.en")
        result = t.voice_to_text("path/to/audio/file", verbose=False)
        self.assertEqual(result, "Hello, World!")

    @patch("builtins.open", new_callable=mock_open())
    @patch("transcriber.load_model")
    @patch.object(Path, "is_file")
    @patch.object(Transcriber, "_add_number_to_filename")
    def test_write_output_to_disk(
        self, mock_add_number_to_filename, mock_is_file, mock_load_model, mock_open
    ):
        mock_is_file.return_value = True
        mock_add_number_to_filename.return_value = "path/to/output/file_1"

        t = Transcriber("base.en")
        t.write_output_to_disk("Hello, World!", "path/to/output/file")

        mock_open.assert_called_once_with("path/to/output/file_1", "w")
        handle = mock_open.return_value.__enter__.return_value
        handle.write.assert_called_once_with("Hello, World!")


if __name__ == "__main__":
    main()
