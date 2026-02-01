<p align="center">
  <img src="https://skillicons.dev/icons?i=bot&theme=dark" width="100" />
</p>

<h1 align="center">🚀 Career Launcher: AI-Job Agent</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/DeepSeek-AI-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/github/license/YOUR_USERNAME/Career-Launcher-AI-Agent?style=for-the-badge" />
</p>

---

### 🎯 The Mission
As a **Software Developer** transitioning into the high-stakes world of **SLAM and Sensor Fusion**, I built this agent to automate the path to my next R&D role. This isn't just a scraper; it's a strategic intelligence tool that identifies exactly what my CV is missing for every specific robotics role in Germany.

---

### 🛠️ Tech Stack & Skills
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,cpp,ros,githubactions,linux,git&theme=dark" />
  </a>
</p>

* **Logic:** Python (Pandas, OpenPyXL)
* **Intelligence:** DeepSeek AI (LLM-based Gap Analysis)
* **Extraction:** JobSpy (LinkedIn, Indeed, Glassdoor)
* **Automation:** GitHub Actions (Daily 08:00 AM Cron Jobs)

---

### ✨ Key Features
* **🔍 Precision Search:** Targets `SLAM`, `Sensor Fusion`, and `Autonomous Systems` roles across Germany.
* **🧠 CV Gap Analysis:** Compares the job description against my current profile and lists **3 specific keywords** I need to address.
* **✍️ Tailored Narrative:** Generates a cover letter draft focusing on my **MSc Digital Engineering Thesis** and **C++** industrial experience.
* **📊 Excel Auto-Tracker:** Maintains a live `Job_Hunt_Tracker.xlsx` file in this repo with match scores and status.

---

### 📂 Project Architecture


```text
├── .github/workflows/
│   └── run_agent.yml      # The Automation Engine
├── src/
│   ├── agent.py           # Core Logic & AI Integration
│   └── resume.txt         # Source material for AI analysis
├── Job_Hunt_Tracker.xlsx  # Live database of opportunities
└── requirements.txt       # Dependencies