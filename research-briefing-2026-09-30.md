# Free-Resources Research Briefing — 2026-09-30

All three tracks researched with current 2026 sources. Full reports live in this
folder: `research-video-rendering.md`, `research-termux-tools.md`,
`research-cloud-ide-storage.md`. This is the short version.

## 1. Video rendering (your films)

**Key insight: ffmpeg assembly is CPU work — it needs no GPU at all.** GPUs only
matter if you generate AI scenes with local open-source models. Your current
pipeline (media pipeline + ffmpeg) doesn't need cloud GPUs for assembly.

| Option | Free deal | Best for |
|---|---|---|
| Google Colab | T4 GPU (not guaranteed), ~12h sessions, ~90-min idle kill, tab must stay open | Interactive/short work |
| Kaggle Notebooks | **30 GPU-hrs/week**, background execution (close browser, it keeps running) | Unattended batch renders |
| Lightning AI Studios | ~22 T4-hrs/month, persistent storage, restarts every 4h | Persistent project home |
| Google Vids | 6 free 1080p AI clips/month | Hero shots |

**Rules:** save everything to Drive (Colab wipes VMs on disconnect), never render
on the phone, never pay for Colab Pro / Veo / Kling / Runway at your volume.

## 2. Termux power tools (OneLove)

- `pkg install ffmpeg` gives hardware-accelerated encoding (`h264_mediacodec`) —
  roughly **4x realtime 1080p**, phone stays cool. One command joins, trims,
  compresses, thumbnails.
- Termux:API scripts your phone: notifications, text-to-speech, camera,
  `termux-share` sends finished videos straight to TikTok/Drive.
- **Two one-time Android 15 fixes or background jobs die:** Developer Options →
  "Disable child process restrictions" → reboot; and set Termux + Termux:API
  battery to **Unrestricted**.
- **Critical:** Termux AND Termux:API must both come from F-Droid — mixed sources
  fail silently.
- 4GB RAM is fine for 720p/1080p hardware encodes and the tracker. One heavy job
  at a time; `termux-wake-lock` during long encodes.
- Starter scripts in the full report: overnight video assembly with completion
  notification, daily tracker nudge from your database, one-command git backup to
  your private repo.

## 3. Cloud IDE + storage

- **Codespaces: 120 core-hours = 60 real hours/month free, 15 GB storage.**
  Gotcha: **stopped codespaces still eat storage quota — delete them at
  github.com/codespaces when done.** No card on file = no surprise charges.
- **github.dev** (press `.` on any repo): completely free, unlimited, works on
  private repos — use for quick edits instead of burning Codespace hours.
- **Firebase Studio**: best free backup IDE (3 workspaces free, 10 with free
  Google Developer membership).
- **Skip** StackBlitz free (public-only — clashes with keeping work unpublished)
  and Replit free (credits burn fast).
- **Storage:** you're at ~6.7 of 15 free Google GB — no need to pay. Add MEGA's
  free 20 GB (encrypted) as overflow for sensitive/legal files. Reclaim space
  with Photos "Free up space" only after backup confirms 100%.

## Bottom line

- Code: Codespaces (real work) → github.dev (quick edits) → Firebase Studio (backup). $0.
- Renders: Kaggle (batch) → Colab (interactive) → Google Vids (hero clips). $0.
- Phone: Termux + ffmpeg hardware encoding + Termux:API. $0.
- Storage: Google 15 GB + MEGA 20 GB encrypted. $0.
- Your Colab minutes and Codespace hours stay banked until you actually need them.
