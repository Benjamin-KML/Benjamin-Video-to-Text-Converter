# Video2Text

Video2Text is a simple Python program that converts every MP4 video in a folder into a text transcript. It uses OpenAI's Whisper speech-recognition model and creates a separate `.txt` file for each video.

## What it does

- Finds all `.mp4` files in the current folder
- Transcribes each video with the Whisper `base` model
- Saves each transcript as `<video name>_Transcribed.txt`
- Continues processing if one video fails
- Runs locally on your computer; no API key is required

## Requirements

- Windows
- Python 3.9 or newer
- FFmpeg
- Enough free storage for Whisper's model files

## Installation

1. Download and install Python from [python.org](https://www.python.org/downloads/).
2. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and extract it to a folder on your computer.
3. Download this repository and open Command Prompt in its folder.
4. Install the Python dependency:

   ```bash
   pip install -r requirements.txt
   ```

5. Open `Video2Text.py` and change `FFMPEG_BIN` so it points to your own `ffmpeg.exe` file. For example:

   ```python
   FFMPEG_BIN = r"C:\Users\YourName\ffmpeg\bin\ffmpeg.exe"
   ```

## Usage

1. Put `Video2Text.py` in the folder containing the MP4 videos you want to transcribe.
2. Open Command Prompt in that folder.
3. Run:

   ```bash
   python Video2Text.py
   ```

4. The program will create transcript files in the same folder. For example:

   ```text
   lecture.mp4
   lecture_Transcribed.txt
   ```

## Selecting a Whisper model

The program uses the `base` model by default. You can change this line in `Video2Text.py`:

```python
MODEL_NAME = "base"
```

Common choices are:

| Model | Speed | Accuracy |
| --- | --- | --- |
| `tiny` | Fastest | Lower |
| `base` | Fast | Good |
| `small` | Slower | Better |

Larger models generally produce better transcripts but require more memory and processing time.

## Notes

- The first run may take longer because Whisper downloads the selected model.
- Processing time depends on the video length and your computer's speed.
- Keep personal or confidential videos out of a public GitHub repository.

## License

No license has been specified. Add a license before allowing others to reuse or distribute the software.
