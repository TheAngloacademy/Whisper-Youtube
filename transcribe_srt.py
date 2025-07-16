import os
import srt
import datetime
import subprocess
import tkinter as tk
from tkinter import filedialog, simpledialog
from faster_whisper import WhisperModel

# Set up model (GPU required)
model = WhisperModel("medium", device="cuda", compute_type="float16")

# Ask the user
use_youtube = input("Do you want to use a YouTube video? (y/n): ").strip().lower()
file_path = ""

if use_youtube == "y":
    # Ask for URL
    root = tk.Tk(); root.withdraw()
    url = simpledialog.askstring("YouTube URL", "Enter the YouTube video URL:")
    if not url:
        print("❌ No URL provided.")
        exit()

    print("📥 Downloading audio...")
    output_filename = "yt_audio.%(ext)s"
    subprocess.run([
        "yt-dlp", "-f", "bestaudio", "--extract-audio",
        "--audio-format", "mp3", "-o", output_filename, url
    ])

    # Find downloaded file
    for f in os.listdir():
        if f.startswith("yt_audio") and f.endswith(".mp3"):
            file_path = f
            break

    if not file_path:
        print("❌ Could not find downloaded audio.")
        exit()

else:
    # Select a local file
    root = tk.Tk(); root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an audio file", 
        filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.ogg")]
    )

    if not file_path:
        print("❌ No file selected.")
        exit()

print(f"🎙 Transcribing: {file_path}")

# Transcribe with GPU
segments, info = model.transcribe(file_path, beam_size=5)

# Build SRT (one-line subtitles)
subtitles = []
index = 1

for segment in segments:
    start = datetime.timedelta(seconds=segment.start)
    end = datetime.timedelta(seconds=segment.end)

    # Clean and shorten lines
    text_lines = segment.text.strip().split(". ")
    for line in text_lines:
        line = line.strip().replace("\n", " ")
        if not line:
            continue

        if len(line) > 80:
            words = line.split(" ")
            parts = []
            current = ""
            for word in words:
                if len(current + " " + word) > 80:
                    parts.append(current.strip())
                    current = word
                else:
                    current += " " + word
            parts.append(current.strip())
        else:
            parts = [line]

        for part in parts:
            subtitles.append(srt.Subtitle(index=index, start=start, end=end, content=part))
            index += 1

# Save subtitles
srt_path = os.path.splitext(file_path)[0] + ".srt"
with open(srt_path, "w", encoding="utf-8") as f:
    f.write(srt.compose(subtitles))

print(f"✅ Done! Subtitles saved as {srt_path}")
