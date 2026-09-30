# ============================
# Video2Text.py
# Robust batch transcription with Whisper (Windows, no admin)
# ============================

import os
import sys
import shutil
import whisper

# ---------- CONFIG ----------
FFMPEG_BIN = r"C:\Users\klavassa\ffmpeg\ffmpeg-8.0.1-essentials_build\bin\ffmpeg.exe"
MODEL_NAME = "base"   # tiny | base | small
# ----------------------------

# ---------- VERIFY FFMPEG ----------
if not os.path.isfile(FFMPEG_BIN):
    print("❌ ffmpeg.exe NOT FOUND at:")
    print(FFMPEG_BIN)
    sys.exit(1)

# Force ffmpeg visibility for this process
os.environ["PATH"] = os.path.dirname(FFMPEG_BIN) + os.pathsep + os.environ.get("PATH", "")

# Double-check ffmpeg is callable
if shutil.which("ffmpeg") is None:
    print("❌ ffmpeg is still not visible to Python.")
    sys.exit(1)

print("✅ ffmpeg detected")

# ---------- LOAD MODEL ----------
model = whisper.load_model(MODEL_NAME)

# ---------- FIND VIDEOS ----------
current_dir = os.getcwd()
mp4_files = [f for f in os.listdir(current_dir) if f.lower().endswith(".mp4")]

if not mp4_files:
    print("❌ No MP4 files found in this folder.")
    sys.exit(1)

print(f"\n🎬 Found {len(mp4_files)} video(s)\n")

# ---------- TRANSCRIBE ----------
for mp4 in mp4_files:
    video_path = os.path.join(current_dir, mp4)
    print(f"📝 Transcribing: {mp4}")

    try:
        result = model.transcribe(video_path)

        output_name = os.path.splitext(mp4)[0] + "_Transcribed.txt"
        output_path = os.path.join(current_dir, output_name)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"✅ Saved: {output_name}\n")

    except Exception as e:
        print(f"❌ Failed on {mp4}")
        print(type(e).__name__, e, "\n")

print("🎉 All transcriptions completed.")
