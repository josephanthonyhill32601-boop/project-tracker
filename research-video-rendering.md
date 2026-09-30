# Free Video Rendering Research — 2026-09-30

Researched for Joseph's film pipeline: AI-generated scenes + ffmpeg assembly + TTS + music, TikTok/YouTube output. Phone: moto g 2025 (4 GB RAM — not a render device). All limits below verified via web search of 2026 sources (multiple GitHub guides, Spheron 2026 comparison, Kaggle docs summaries, PyTorch/Lightning docs).

Key insight up front: **ffmpeg assembly is CPU work — it does not need a GPU at all.** The GPU only matters if you generate AI video scenes with local open-source models (LTX-Video, Wan, CogVideoX, etc.) on the cloud box. Joseph's current pipeline generates scenes through the built-in media pipeline, so Colab/Kaggle GPUs are headroom for future local-model work, not a requirement for assembly.

---

## 1. Google Colab (free tier) — the plan's default

| Item | Free tier (2026, verified) |
|---|---|
| GPU | NVIDIA T4 (~15–16 GB VRAM) — **not guaranteed**; peak hours can give CPU-only |
| Session cap | ~12 hours max, then forced disconnect |
| Idle timeout | ~90 min of inactivity = session killed |
| Quota | Dynamic, unpublished; in practice ~15–30 GPU hrs/week, and heavy users report throttling after ~3–4 GPU sessions/day |
| RAM / disk | ~12.7 GB RAM, ~78 GB disk — **wiped on disconnect** |
| Background run | **No** — browser tab must stay open |
| Cost/card | $0, no credit card |

**Pros**
- Fastest zero-setup free GPU in a browser tab; full pip/apt access.
- 2 vCPUs + T4 chew through 1-minute TikTok clips easily inside the 12 h window.
- Drive mounting gives free persistent storage (15 GB).

**Cons**
- GPU availability fluctuates; you may open a session and get no GPU.
- Everything local dies on disconnect — outputs MUST go to Google Drive (`from google.colab import drive; drive.mount('/content/drive')`).
- No background execution: closing the laptop/phone browser risks the run.
- Banned by ToS: crypto mining, SSH/remote-desktop into the VM, and limit-evasion tricks (e.g., rotating accounts to dodge quotas). Don't.

**When limits hit:** session is killed and the VM wiped. Reconnecting may give CPU-only for a while (throttle). Nothing is lost if you checkpointed to Drive.

## 2. Running ffmpeg film assembly on Colab — gotchas

1. **Install ffmpeg every session** (first cell): `!apt-get update -qq && apt-get install -y -qq ffmpeg`. Colab has shipped it pre-installed at times, but don't rely on it — the apt install takes ~1–2 min.
2. **Save outputs to Drive, not /content.** Anything in the VM disappears on timeout/disconnect.
3. **Use libx264 (CPU), not NVENC.** The stock apt ffmpeg lacks NVIDIA encoder support; building it wastes session time. T4's 2 vCPUs are slow but fine for short clips.
4. **Split long renders into checkpointed chunks.** If a session dies at hour 11 of a 12-hour batch, per-scene output files in Drive mean you resume instead of restarting.
5. **Uploading assets:** use Drive or `!wget` direct links; the browser upload widget is slow and capped. Keep the notebook's first cell as: mount Drive → apt install → pip install → verify `ffmpeg -version`.
6. **Don't run idle-keepalive scripts** to dodge the 90-min timeout — that's limit evasion and risks the account.

## 3. Free alternatives

### Kaggle Notebooks — best free GPU for batch work
- **Free:** 30 GPU-hours/week total (your choice per session: 2× T4 or 1× P100), plus 20 TPU-hours/week. No card; phone/SMS verification required for GPU access.
- **Sessions:** up to ~9–12 h; **background execution YES** — close the browser and the notebook keeps running. 20 GB persistent `/kaggle/working`.
- **Pros:** predictable weekly quota (vs Colab's dynamic throttling), background runs = start a batch render and walk away, dual T4s = 32 GB VRAM for bigger local video models.
- **Cons:** quota is weekly and hard-capped; notebooks are public by default on free tier (keep API keys in Kaggle Secrets); ML-oriented UI, slightly less flexible than Colab for general scripting.
- **Verdict:** the best complement to Colab — use Kaggle for unattended batch renders, Colab for interactive sessions.

### Lightning AI Studios — best free persistent dev box
- **Free:** 15 credits/month ≈ 22 T4 GPU-hours/month (fewer hours if you pick bigger GPUs like L4). No credit card. 1 studio at a time, free studios restart every 4 h.
- **Pros:** persistent storage, background execution, full Linux environment with VS Code/SSH integration — feels like a real dev machine, not a notebook.
- **Cons:** 4-hour restart cycle on free tier interrupts long runs; monthly credit pool is smaller than Kaggle's weekly one; GPU type availability varies.
- **Verdict:** good as a persistent project home (code + assets live there), less good for long single renders.

### Google Vids (already in the toolkit)
- **Free:** 6 AI video generations/month, 1080p output, via the `google-vids` workspace skill. Best free *true* video-generation path found.
- **Pros:** zero setup, 1080p, no GPU needed.
- **Cons:** only 6 clips/month — a supplement for quick scenes, not bulk generation.
- **Verdict:** use the 6 monthly clips for hero shots; bulk scene work stays on the media pipeline or local models.

## 4. What NOT to waste money on

- **Colab Pro/Pro+ ($10+/mo):** not needed until free-tier walls are hit *repeatedly*. Joseph's 1-minute clips fit comfortably in free sessions.
- **Paid video APIs (Veo, Kling, Runway, Luma):** free pipeline covers current volume; revisit only if a paid model wins a side-by-side quality test for a specific scene.
- **Pay-per-hour GPU rentals (RunPod, Vast.ai, Lambda):** only for deadline emergencies after all three free tiers are exhausted in the same week.
- **CapCut Pro / VN Pro:** already being canceled — the free tiers plus ffmpeg cover the edit.
- **Bigger phone storage/RAM for rendering:** the phone is the terminal, not the render farm. Never render on the moto g.

## Recommended setup

1. **Interactive/short work → Colab** (fastest to open, Drive-backed).
2. **Unattended batch renders → Kaggle** (background execution, 30 h/week).
3. **Persistent project home → Lightning AI Studio** (code + assets persist).
4. **Quick AI clips → Google Vids** (6 free 1080p generations/month).
5. All three free tiers are legitimate separate quotas — no ToS games needed, and combined they exceed anything one service gives free.

*Sources: Spheron "Google Colab Alternatives: 8 GPU Clouds Compared (2026)"; Google Colab FAQ; Kaggle efficient-GPU-usage docs (via 2026 community guides); PyTorch Lightning Studios install docs; free-llm-api-hub self-hosting-on-free-compute (verified 2026-07-12); film-factory workspace skill; google-vids workspace skill.*
