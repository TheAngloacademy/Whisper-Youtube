# 🎙 YouTube or Local Audio to Subtitles (Whisper GPU Edition)

This project lets you transcribe **any audio or YouTube video** into clean `.srt` subtitles using OpenAI Whisper via `faster-whisper`, accelerated by your **GPU with CUDA + cuDNN**.

---

## ⚡ Features

* 🎧 Transcribe local audio files (MP3, WAV, M4A, OGG)
* 📥 Download and transcribe **YouTube** videos automatically
* 💨 Uses your **GPU (CUDA)** for fast transcription
* 🧹 Clean, short **one-line subtitles**
* 💬 Outputs standard `.srt` subtitle file

---

## 🧰 Requirements

* Windows with PowerShell
* Python 3.9 or 3.10 (64-bit)
* CUDA 12.1+ (tested with 12.9.1)
* cuDNN installed in your CUDA directory
* ffmpeg (auto-included by yt-dlp or install manually)

---

## 🔧 Installation

1. Clone or download the repository.
2. Create and activate your virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

---

## 🚀 Usage

```powershell
python transcribe_from_youtube_or_file.py
```

You'll be prompted:

* If you choose `y`, paste the YouTube URL and it will auto-download the audio.
* If you choose `n`, a file picker will appear for you to select a local audio file.

The resulting `.srt` file will be saved in the same folder as the input.

---

## 📝 Output Example

```srt
1
00:00:00,000 --> 00:00:04,500
Welcome to this video about AI and productivity.

2
00:00:04,500 --> 00:00:08,000
Let's explore how you can save time using Whisper.
```

---

## 👨‍💻 Based on

* [faster-whisper](https://github.com/guillaumekln/faster-whisper)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [OpenAI Whisper](https://github.com/openai/whisper)

---

## ✅ License

MIT – use freely for educational or commercial use.
