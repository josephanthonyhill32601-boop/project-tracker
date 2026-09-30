# Termux Power Tools — Research Report
**Device:** Motorola moto g 2025 (MediaTek Dimensity 6300, 4GB RAM, Android 15)
**Termux:** F-Droid build + Termux:API (F-Droid build)
**Researched:** 2026-09-30. Package availability and Android 15 restrictions verified via current web sources (see Sources at end).

## TL;DR
- `pkg install ffmpeg` gives you a full video studio on the phone, **including hardware-accelerated encoding** (`h264_mediacodec`) — 2–4x faster than CPU encoding, barely warms the phone.
- Termux:API turns your scripts into phone features: notifications, text-to-speech, camera, location, SMS, vibration, flashlight, clipboard, WiFi info.
- The two traps on Android 15: the **phantom process killer** (kills background scripts) and **battery optimization** (pauses Termux when the screen is off). Both have one-time fixes.
- 4GB RAM is fine for 720p/1080p work with hardware encoding; don't run two renders at once.

---

## 1. Power packages for your workflow

All install with `pkg install <name>`. These are all confirmed available in the Termux repository (aarch64):

| Package | What it does for you | Install |
|---|---|---|
| `ffmpeg` | Video/audio: concat clips, trim, compress, thumbnails, extract audio, convert formats. Includes `ffprobe`. | `pkg install ffmpeg` |
| `python-numpy`, `python-pillow` | Pre-built Python libs (no compiling on the phone). Pillow = thumbnails/contact sheets in Python. | `pkg install python-numpy python-pillow` |
| `yt-dlp` | Download reference clips/audio (via pip). | `pip install yt-dlp` |
| `imagemagick` | Batch image ops: resize art, strip metadata, convert formats, make contact sheets. | `pkg install imagemagick` |
| `tmux` | Keeps scripts running when you leave Termux; split terminal panes. | `pkg install tmux` |
| `openssh` | `sshd` server (access phone files from your computer over WiFi) + `scp`/`rsync` for backups. | `pkg install openssh` |
| `rsync` | Fast incremental backups of your project folder. | `pkg install rsync` |
| `jq` | Parse JSON in shell scripts (Termux:API outputs JSON). | `pkg install jq` |
| `termux-api` | The phone-control package (Section 2). | `pkg install termux-api` |
| `nodejs-lts` | Web dashboards/APIs on the phone (e.g. a local page showing your tracker). | `pkg install nodejs-lts` |
| `nano` | Simple text editor (friendlier than vi for quick edits). | `pkg install nano` |

**Python note:** Termux ships current Python 3.x. Prefer `pkg install python-<lib>` over `pip install` for heavy libs (numpy, pillow, opencv) — the Termux packages are pre-compiled for the phone; pip would try to compile from source and often fails. Pure-Python packages (yt-dlp, requests) are fine via pip.

**Pro:** everything above is free, offline-capable, and runs entirely on the phone — zero cloud minutes.
**Con:** heavy compiles (anything needing Rust/C++ toolchains via pip) usually fail; stick to Termux's packaged versions.

---

## 2. ffmpeg deep dive — your phone video studio

### Hardware encoding works (this is the big one)
Termux's ffmpeg build includes MediaTek-compatible hardware encoders exposed through Android's MediaCodec:
- `h264_mediacodec` — H.264 hardware encoder
- `hevc_mediacodec` — H.265/HEVC hardware encoder

Real-world benchmarks on phones show **~4x realtime for 1080p H.264 via MediaCodec vs ~1.9x on CPU** (`libx264`) — and the phone stays cool because the dedicated encoder chip does the work, not the CPU. Your Dimensity 6300 has hardware H.264/HEVC encoders, so this applies to you.

```bash
# Fast hardware transcode (phone stays usable)
ffmpeg -i input.mp4 -c:v h264_mediacodec -b:v 8M -c:a aac -movflags +faststart out.mp4

# If a hardware render ever looks corrupt, force the reliable CPU path:
ffmpeg -i input.mp4 -c:v libx264 -preset veryfast -crf 23 -c:a aac out.mp4
```

### What ffmpeg handles well on the phone
- **Concatenate clips** (same codec): the concat demuxer — instant, no re-encode
- **Trim/cut** scenes by timestamp
- **Extract thumbnails**: `ffmpeg -ss 00:00:05 -i clip.mp4 -vframes 1 thumb.jpg`
- **Compress for upload**: HEVC (`hevc_mediacodec`) cuts file size ~40–50% vs H.264
- **Extract/normalize audio** for your soundtrack work
- **Batch scripts**: loop over a folder of clips overnight

### Practical tips for 4GB RAM
- **One render at a time.** A second simultaneous encode will crawl or get killed.
- Run encodes at low priority so the phone stays responsive: `nice -n 15 ffmpeg ...`
- Use `termux-wake-lock` before a long encode so Android doesn't sleep mid-render; `termux-wake-unlock` after.
- 720p drafts on the phone, final 1080p/4K renders on Colab's free GPU — play to each machine's strength.

**Pro:** hardware encode is fast, cool, and battery-friendly; ffmpeg does in one command what takes 10 taps in an editor app.
**Con:** no GPU filters/AI upscaling on the phone (CPU-only, slow); complex filter chains on 4K will exhaust 4GB RAM — keep phone work to assembly, trims, and compression.

---

## 3. Termux:API — script your phone's hardware

> **Critical:** Termux and Termux:API must both come from **F-Droid** (which is your plan). Mixing sources (e.g. Termux from F-Droid + API from Play Store) causes signature mismatches and silent failures.

After `pkg install termux-api`, grant permissions in **Settings → Apps → Termux:API → Permissions** (or grant when prompted). Note: anything you grant to Termux:API is accessible to *every* script running in Termux — only grant what you'll use.

### Notifications & feedback
| Command | Does what |
|---|---|
| `termux-notification -t "Title" -c "Message"` | System notification (supports `--sound`, `--vibrate`, tap actions) |
| `termux-notification-remove --id <id>` | Clear it |
| `termux-toast "done"` | Brief popup |
| `termux-vibrate -d 500` | Vibrate (milliseconds) |
| `termux-torch on` / `off` | Flashlight |
| `termux-dialog text -i "Prompt"` | Interactive input dialog |

### Media & sensors
| Command | Does what |
|---|---|
| `termux-tts-speak "text"` | Speak aloud (no permission needed) |
| `termux-speech-to-text` | Voice input → text (needs microphone) |
| `termux-camera-photo -c 0 photo.jpg` | Back-camera photo (needs foreground + camera permission) |
| `termux-microphone-record -f rec.m4a` | Record audio (can run in background) |
| `termux-media-player play file.mp3` | Play audio |
| `termux-sensor -l` / `-s <name> -n 1` | Accelerometer, light, etc. |

### Communication (needs permissions — grant only if you want these)
| Command | Does what |
|---|---|
| `termux-sms-list -l 10` / `termux-sms-send -n <number> "msg"` | Read/send SMS |
| `termux-contact-list` | Contacts |
| `termux-call-log -l 10` | Call history |
| `termux-telephony-call <number>` | Place a call |

### Location, system, sharing
| Command | Does what |
|---|---|
| `termux-location -p network -r once` | GPS/network location (needs location permission) |
| `termux-battery-status` | Battery %, temp, charging state (JSON) |
| `termux-wifi-connectioninfo` | SSID, IP, signal |
| `termux-clipboard-get` / `-set` | Clipboard (Android 13+ notifies you when read) |
| `termux-volume`, `termux-brightness 150` | Volume / brightness control |
| `termux-wake-lock` / `termux-wake-unlock` | Keep phone awake during jobs |
| `termux-share -a send <file>` | Share a file to any app (TikTok, Drive…) |
| `termux-open-url <url>` | Open link in browser |
| `termux-job-scheduler` | Schedule persistent background jobs (survive reboots) |

**Pro:** your scripts can notify you, speak to you, and share finished videos straight to apps.
**Con:** SMS/call/contact permissions are powerful — a malicious script with those granted could read/send texts. Only grant permissions for commands you actually use, and never run scripts you haven't read.

---

## 4. Real limitations on your device (and the fixes)

### Android 15: phantom process killer
Android 12+ kills background child processes beyond a ~32-process limit. Symptom: Termux dies with `[Process completed (signal 9) - press Enter]`. **Your one-time fix:** Settings → (tap Build number 7x to unlock) Developer options → **"Disable child process restrictions"** → reboot. (The old ADB one-liners are increasingly locked down on Android 15; the GUI toggle is the reliable path.) System updates can reset it — reapply if signal 9 returns.

### Battery optimization
Android pauses apps when the screen is off. **Fix:** Settings → Apps → Termux → Battery → **Unrestricted** (do the same for Termux:API). Without this, overnight renders and scheduled jobs die when the phone sleeps. Pair with `termux-wake-lock` inside long scripts.

### 4GB RAM
- Fine for: 720p/1080p hardware encodes, Python tracker, tmux, ffmpeg batch jobs.
- Tight for: 4K CPU encodes with filters, multiple big apps + Termux at once. RAM Boost (storage-backed) helps marginally but is far slower than real RAM — don't count on it for encodes.
- Rule of thumb: one heavy job at a time, close camera-heavy apps during renders.

### Things Termux cannot do
- **No Docker/containers** — the kernel doesn't allow it without root.
- **No system settings changes** — Termux can't toggle Easy Mode, change launchers, or modify Android settings (apps are sandboxed). Those stay your manual taps.
- **Camera photos need Termux in the foreground.**
- `top`/`htop` are broken on Android (no `/proc/stat` access) — use `termux-battery-status` and common sense instead.
- Inbound network connections are restricted — your phone can *reach out* (push to GitHub) but the internet can't reach in.

---

## 5. Three starter uses (tied to your actual work)

### A. Overnight video prep for your films
A script that takes a folder of clips, concatenates them, compresses with hardware HEVC, and drops the result in Downloads with a notification when done:

```bash
#!/bin/bash
termux-wake-lock
cd ~/storage/shared/Movies/to_process
# join all clips (same codec) without re-encoding:
printf "file '%s'\n" *.mp4 > list.txt
ffmpeg -f concat -safe 0 -i list.txt -c copy joined.mp4
# hardware-compress for upload:
ffmpeg -i joined.mp4 -c:v hevc_mediacodec -b:v 6M -c:a aac final_upload.mp4
mv final_upload.mp4 ~/storage/downloads/
termux-wake-unlock
termux-notification -t "Video ready" -c "final_upload.mp4 is in Downloads" --sound
```

### B. Tracker reminders from the phone itself
A daily job that reads your `project_master.db` and notifies you of active projects:

```bash
#!/bin/bash
count=$(sqlite3 ~/storage/shared/Documents/project_master.db \
  "SELECT COUNT(*) FROM hybrid_projects WHERE status='Active';")
termux-notification -t "Project Tracker" -c "$count active projects — keep building" --sound
# schedule it daily:
termux-job-scheduler --job-id 1 --period-ms 86400000 --script ./daily_nudge.sh --persisted true
```

### C. One-command backup to your private GitHub repo
```bash
#!/bin/bash
cd ~/project-tracker
cp ~/storage/shared/Documents/project_master.db ./project_master.db
git add -A && git commit -m "backup $(date +%F)" && git push
termux-toast "Backup pushed"
```
Run it manually or via `termux-job-scheduler` nightly. (Keep the repo **private** per your attorney guidance.)

---

## Sources
- Termux ffmpeg + MediaCodec hardware encoding: [vedit](https://github.com/yashas-13/vedit), [jellyfin-termux-mediacodec-wrapper](https://github.com/citrustiara/jellyfin-termux-mediacodec-wrapper) (1080p benchmarks: 4.14x MediaCodec vs 1.87x libx264), [autoeditor Termux setup](https://github.com/codewithsiddique-04/autoeditor/blob/HEAD/docs/termux-android-setup.md)
- ffmpeg in Termux install: [video compression toolkit](https://github.com/omarali236/automated-video-compression-and-sorting-toolkit-using-ffmpeg)
- Termux:API command reference: [learn-skills.dev SKILL.md](https://github.com/neversight/learn-skills.dev/blob/HEAD/data/skills-md/4ier/agent-skills/termux-api/SKILL.md), [pepebot-space termux-api](https://github.com/pepebot-space/skills/blob/HEAD/termux-api/SKILL.md), [claude-code-android security model](https://github.com/ferrumclaudepilgrim/claude-code-android/blob/HEAD/docs/security-model.md) (permission exposure table; same-source signature requirement)
- Android 15 phantom process killer fix: [lenovo-dimensity8300-termux-desktop](https://github.com/ppsirius/lenovo-dimensity8300-termux-desktop) (Android 15/16 → Developer Options toggle), [linux-for-android troubleshooting](https://github.com/pdev-labs/linux-for-android/blob/HEAD/README.md), [kern android constraints](https://github.com/bentlybro/kern/blob/HEAD/docs/03-android-constraints.md)
- Termux package availability (numpy/pillow/opencv/yt-dlp/imagemagick/tmux/rsync): [FAVencoder Termux setup](https://github.com/minimaster4734/favencoder), [termux-ultimate](https://github.com/sachit1751-art/termux-ultimate/blob/HEAD/README.md)
