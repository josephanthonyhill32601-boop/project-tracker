# Free Cloud IDEs & Storage — Research Report
Researched 2026-09-30. All free-tier limits verified against current sources (see links at bottom).

## 1. GitHub Codespaces (your main cloud IDE) — free tier, exact numbers

Official GitHub docs for a free personal account:

- **Compute: 120 core-hours/month** = **60 real hours/month** on the default 2-core machine. (A 4-core machine burns it twice as fast — stick to 2-core.)
- **Storage: 15 GB-months/month.** This is the gotcha: **stopped codespaces still eat storage quota.** Delete codespaces you're not using within a week or two.
- **Billing cycle resets on the 1st of each month**, not on your signup anniversary.
- **No payment method on file = no charges possible.** GitHub blocks usage instead of charging. (Safe by default for you.)
- **Idle timeout:** default 30 minutes, adjustable in Settings → Codespaces. Set retention to 7 days so forgotten codespaces auto-delete.
- **Bonus freebies on the same account:** 2,000 GitHub Actions minutes/month, 500 MB package storage, GitHub Pages on public repos.

**Pros:** Full Linux + VS Code in the browser, works with your private repos (important while your work stays unpublished), generous 60 hrs/mo for your pace.
**Cons:** Not always-on (sleeps when idle); storage quota silently drains if you leave stopped machines around.
**Verdict:** This is your primary cloud IDE. Nothing to change.

## 2. Free alternative cloud IDEs

### A. github.dev — instant browser editor (FREE, unlimited)
Press `.` on any GitHub repo page (or change `github.com` → `github.dev` in the URL). A lightweight VS Code opens right in the browser — browse, edit, commit.

- **Pros:** Completely free, zero quota usage, works on private repos, nothing to install, great on your phone's browser for quick fixes.
- **Cons:** No terminal, no running code — editing only. Uncommitted work lives in browser storage, so commit often.
- **Verdict:** Your quick-edit tool. Use it instead of spinning up a Codespace for small changes — saves your 60 hours.

### B. Firebase Studio (formerly Project IDX) — Google's free cloud IDE
- **Free tier:** 3 cloud workspaces, no cost. Join the free Google Developer Program → **10 workspaces**. (Premium ~$24.99/mo → 30 workspaces — you don't need this.)
- **Pros:** VS Code-like editor in browser, Gemini AI built in, GitHub integration, one-click deploy to Firebase. Good fit since you already use Gemini.
- **Cons:** Only 3 free workspaces (fine — delete/rotate); Flutter/React Native mobile workspaces capped at 2 total on free.
- **Verdict:** Best free backup IDE for web/app prototyping. Worth having alongside Codespaces.

### C. StackBlitz (free "Personal" plan) — use with caution
- **Free:** unlimited **public** projects, open/edit public GitHub repos, Node.js runs in the browser (no server needed). 1 MB file-upload limit per project.
- **Pros:** Instant, nothing installs, great for quick frontend experiments.
- **Cons:** **Free = public projects only.** Private repos need Pro ($18/mo annual). That clashes with your rule to keep work unpublished until your attorney approves.
- **Verdict:** Skip for real work. Only use for throwaway public experiments, if ever.

### D. Replit (free "Starter" plan) — weakest option
- **Free:** daily AI Agent credits (reset roughly every 5 hours), built-in database, publish 1 project.
- **Pros:** AI agent builds apps from prompts; built-in hosting + database in one place.
- **Cons:** Multiple 2026 reviews call the free plan weak — credits can burn through in a single session. Paid plans start at $20/mo and costs are usage-based and unpredictable.
- **Verdict:** Skip. Codespaces + Firebase Studio cover everything better, for free.

**Ranking for you:** 1) Codespaces (main) → 2) github.dev (quick edits, saves quota) → 3) Firebase Studio (backup/prototyping) → skip StackBlitz & Replit.

## 3. Free cloud storage — extend what you have

Your Google storage: ~6.74 GB used of 15 GB free. You're fine — no need to pay for anything.

| Service | Free space | Notes |
|---|---|---|
| Google Drive (what you use) | **15 GB** (shared with Gmail + Photos) | Best everyday option, you're at <50% |
| MEGA | **20 GB** | End-to-end encrypted — good overflow for sensitive/legal files |
| pCloud | up to 10 GB | Fine, but MEGA gives more free |
| OneDrive | 5 GB | Only useful if you lived in Microsoft apps |
| iCloud | 5 GB | Apple-only world, not yours |
| Dropbox | 2 GB | Too small to matter |

**Simple storage-management practices (no apps to buy):**
1. **Google Photos → "Free up space"** — but ONLY after the app confirms backup is 100% complete. This is usually the biggest single reclaim.
2. **Drive → Storage view** (drive.google.com, click Storage) — sort by size, delete or move the big forgotten files.
3. **Gmail search:** `has:attachment larger:10M` — finds the emails hogging space; delete the ones you don't need.
4. **Phone:** keep photos/videos on a microSD card (your phone supports up to 1 TB) instead of internal storage.
5. **MEGA as overflow:** put encrypted copies of important/legal documents there — 20 GB free, and the encryption means even MEGA can't read them.

## 4. What NOT to pay for

- **Google One paid plans** (100 GB $1.99/mo+) — you're under half your free 15 GB. Revisit only if you cross ~13 GB.
- **GitHub Pro for extra Codespaces hours** (180 vs 120 core-hours) — your pace won't burn 60 real hours/month. Free is plenty.
- **Replit Core ($20/mo) or Pro ($100/mo)** — usage-based billing is unpredictable; the free plan is weak by design.
- **StackBlitz Pro ($18/mo)** — only buys private projects, which Codespaces already gives you free.
- **pCloud lifetime / MEGA paid** — you don't need paid storage yet.
- **TeraBox "free 1 TB"** — technically the biggest free tier, but monetized with ads and heavy download throttling; not trustworthy as your primary storage. Avoid.

## Bottom line for your setup

- **Code:** Codespaces (60 hrs/mo free) for real work, github.dev for quick edits, Firebase Studio as the free backup. Total extra cost: $0.
- **Storage:** Stay on Google's free 15 GB (you're at ~6.7 GB), add MEGA's free 20 GB encrypted as overflow. Total extra cost: $0.
- **The one habit that saves your quota:** delete stopped Codespaces at github.com/codespaces when you're done — stopped machines still eat your 15 GB storage allowance.

---
*Sources: [GitHub plans/docs](https://docs.github.com/en/get-started/learning-about-github/githubs-plans) · [Codespaces billing discussion](https://github.com/orgs/community/discussions/181042) · [github.dev docs](https://docs.github.com/en/enterprise-cloud@latest/codespaces/the-githubdev-web-based-editor) · [Firebase Studio pricing](https://firebase.google.com/docs/studio/pricing) · [StackBlitz pricing 2026](https://www.eesel.ai/blog/stackblitz-pricing) · [Replit pricing Sept 2026](https://www.appypie.com/blog/replit-alternatives) · [Cloud storage comparison July 2026](https://www.cloudslinker.com/projects/cloud-storage-pricing-comparison/) · [TechRadar free storage](https://www.techradar.com/best/best-free-cloud-storage-service)*
