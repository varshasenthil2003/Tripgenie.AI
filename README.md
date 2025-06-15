# ✈️ TripGenie.AI – AI-Powered Travel Itinerary Generator 🌟

**TripGenie.AI** is a next-gen modular travel planning platform that uses powerful AI to generate personalized, luxury travel itineraries. Whether you want cultural insight, budget analytics, or an elite vacation plan — this app tailors your journey from start to finish with professional exports, smart design, and zero hassle.

---
## 🧭 Introduction

Planning the perfect trip is hard. **TripGenie.AI** makes it effortless.
Using AI-driven insights, interactive UI components, and detailed export options, TripGenie.AI creates custom travel itineraries designed to suit your **style, budget, and group preferences** — from solo adventurers to luxury family retreats.

---

## 🖥️ Example Screenshot

Here’s a quick preview of TripGenie.AI in action:

![TripGenie.AI Demo](assets/demo_screenshot.png)

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI API](https://img.shields.io/badge/OpenAI_API-10a37f?style=for-the-badge&logo=openai&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-API-007acc?style=for-the-badge)
![ReportLab](https://img.shields.io/badge/ReportLab-PDF-lightgrey?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)


---

## ⚙️ Features

### 🤖 1. Smart Itinerary Generation

* AI-based trip planning with **cultural insights and smart suggestions**
* Personalized for destination, budget, pace, group type, and more
* Custom itinerary prompts powered by **OpenRouter** LLMs

---

### 📊 2. Budget & Analytics

* Real-time cost estimations and budget classification
* Visual breakdown of expenses and travel patterns
* Auto-generated **smart packing lists** based on trip context

---

### 🎨 3. Professional Experience

* Sleek, responsive UI built with **custom CSS**
* Expandable day-by-day plans with embedded tips
* Export-ready layout with support for **PDF**, **ICS**, and **JSON**

---

### 🧰 4. Customization & Controls

* Accessibility settings and dietary considerations
* Session-based state management
* Detailed user preference configurations

---

### 📤 5. Export & Share

* 📄 Export professional itineraries as **PDF**
* 🗓️ Save travel plans directly to your **calendar (ICS)**
* 📦 Export raw data in **JSON** for integration or storage

---

## 🏗️ Directory Structure

```bash
Tripgenie.ai/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── styles.py              # CSS styling
├── components.py          # UI components
├── ai_service.py          # AI integration service
├── pdf_generator.py       # PDF generation utilities
├── utils.py               # Helper functions
├── session_manager.py     # Session state management
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

```

---

## 🚀 Quick Start

### 🔧 Method 1: Local Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/Tripgenie.AI.git
cd tripgenie-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your OpenRouter API key
# Edit config.py → API_KEY = "your-api-key"

# Launch the app
streamlit run main.py
```

---

## 📦 Modules Description

### Core Modules

| File                 | Description                            |
| -------------------- | -------------------------------------- |
| `main.py`            | Main entry point with tab routing      |
| `config.py`          | App configuration (API, styling, etc.) |
| `ai_service.py`      | AI integration using OpenRouter        |
| `session_manager.py` | Session state control logic            |
| `pdf_generator.py`   | Generates downloadable itineraries     |
| `utils.py`           | Reusable helper functions              |

---

### UI & Display Modules

| File                   | Feature                            |
| ---------------------- | ---------------------------------- |
| `styles.py`            | CSS styling for consistent UI      |
| `components.py`     | Reusable widgets and UI components |

---

## 🔧 Configuration

Edit `config.py` to personalize:

```python
API_KEY = 'your-api-key-here'
MODEL_NAME = "deepseek/deepseek-chat-v3-0324:free"
APP_TITLE = "TripGenie.AI"
BUDGET_RANGES = {
    "Budget": "₹2,000–4,000",
    "Mid-range": "₹4,000–8,000",
    "Luxury": "₹8,000–20,000"
}
```
---

## 🎨 Customization

| Module                 | Customization Options                 |
| ---------------------- | ------------------------------------- |
| `styles.py`            | Colors, fonts, layout, responsiveness |
| `ai_service.py`        | AI prompt logic, model control        |
| `pdf_generator.py`     | PDF layout and export templates       |

---

## 🔒 Security & Privacy

* 🔑 API Keys stored in `config.py` (never in logs)
* 🧼 Session data is cleared on browser close
* 🔐 Secure API calls only, no persistent user storage

---

## 🐞 Troubleshooting

### Common Fixes

| Error                   | Solution                                        |
| ----------------------- | ----------------------------------------------- |
| `Missing API Key`       | Add your OpenRouter key in `config.py`          |
| `PDF generation failed` | Install `reportlab` via `pip install reportlab` |
| `ModuleNotFoundError`   | Run `pip install -r requirements.txt`           |

---

## 📈 Performance Benchmarks

* ⏱️ Load time: < 3 sec
* ⚡ AI itinerary generation: 10–30 sec
* 🖨️ PDF export: < 5 sec
* 🧠 Memory usage: \~50MB

---

## 🙏 Acknowledgments

* 💡 OpenRouter API for enabling AI generation
* 🎨 Streamlit for rapid UI deployment
* 🖨️ ReportLab for elegant PDF exports
* 🤖 OpenAI (architectural inspiration)

---

**Made with ❤️ for travel lovers**

> *Transform your travel dreams into perfectly crafted journeys with AI-powered precision.*

