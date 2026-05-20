# 🚀 AutoEntry AI

## Intelligent Document Processing & Workflow Automation System

AutoEntry AI is an AI-powered workflow automation platform that extracts structured data from PDFs, resumes, invoices, spreadsheets, and documents, then automatically fills and submits online forms using browser automation.

The system combines OCR-ready document intelligence, smart field matching, analytics dashboards, reporting systems, and browser automation into one unified platform.

---

# 📌 Project Overview

This project was developed to automate repetitive data entry workflows using AI-assisted extraction and browser automation.

The platform can:

- Upload CSV or Excel files
- Upload PDF resumes/invoices/documents
- Extract structured information automatically
- Match extracted fields intelligently
- Auto-fill Google Forms
- Track submission history
- Generate analytics dashboards
- Export reports

This project simulates real-world enterprise workflow automation systems used in HR, finance, insurance, operations, and document processing industries.

---

# ✨ Features

## 📄 Document Intelligence
- PDF text extraction
- Resume information extraction
- Invoice data extraction
- OCR-ready architecture
- Structured field detection

## 🤖 Browser Automation
- Google Form auto-fill
- Automatic form submission
- Multi-record processing
- Smart dynamic field matching
- Browser control using Playwright

## 📊 Dashboard & Analytics
- Submission analytics dashboard
- Success/failure tracking
- Submission history
- Progress monitoring
- Downloadable reports

## 🗄️ Database Persistence
- SQLite integration
- Permanent submission history
- Error logging
- Automation audit tracking

## 🎨 Professional UI
- Multi-page dashboard
- Sidebar navigation
- Dark modern interface
- Configurable settings page

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core backend logic |
| Streamlit | Frontend dashboard |
| Playwright | Browser automation |
| SQLite | Database persistence |
| Pandas | Data processing |
| PyMuPDF (fitz) | PDF text extraction |
| Regex | Smart field extraction |
| VS Code | Development environment |

---

# 🏗️ Project Architecture

```text
PDF / CSV / Excel Upload
            ↓
Document Extraction Engine
            ↓
Smart Field Detection
            ↓
Structured Data Processing
            ↓
Browser Automation Engine
            ↓
Google Form Submission
            ↓
SQLite Database Storage
            ↓
Analytics Dashboard & Reports
```

---

# 🔄 Workflow

## CSV Workflow

```text
CSV Upload
→ Smart Column Mapping
→ Data Preview
→ Automated Form Submission
→ Submission Tracking
→ Report Export
```

## PDF Workflow

```text
PDF Upload
→ Text Extraction
→ Name/Email/Phone Detection
→ Structured Data Generation
→ Form Auto-fill
→ Automated Submission
```

---

# 📸 Screenshots

## Dashboard
(Add Screenshot Here)

## PDF Extraction
(Add Screenshot Here)

## Analytics Dashboard
(Add Screenshot Here)

## Submission History
(Add Screenshot Here)

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/autoentry-ai.git
```

## 2. Open Project

```bash
cd autoentry-ai
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
python -m streamlit run app.py
```

---

# 📁 Project Structure

```text
ai-data-entry-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── submission_history.db
│
├── automation/
│   └── form_filler.py
│
├── database/
│   └── db.py
│
├── utils/
│   └── document_extractor.py
│
├── assets/
├── screenshots/
└── sample_files/
```

---

# 📈 Usage

## CSV Automation
1. Upload CSV/Excel file
2. Paste Google Form URL
3. Preview mapped fields
4. Start automation
5. Download submission report

## PDF Automation
1. Upload PDF resume/invoice
2. Extract document information
3. Paste Google Form URL
4. Auto-submit extracted data

---

# 🔮 Future Enhancements

- OCR support for scanned images
- Handwriting recognition
- AI confidence scoring
- Duplicate detection
- Retry failed submissions
- Authentication system
- Cloud deployment
- AI-based resume ranking
- ERP integration
- REST API integration

---

# 🎯 Industry Use Cases

- HR Resume Automation
- Invoice Processing
- Insurance Form Automation
- Banking KYC Systems
- Student Registration Automation
- Enterprise Workflow Automation
- Intelligent Document Processing

---

# 👨‍💻 Developer

Harish Ravikumar

Electronics and Communication Engineering Student  
AI • Automation • IoT • Intelligent Systems

---

# ⭐ Conclusion

AutoEntry AI demonstrates the integration of AI-powered document processing, workflow automation, browser control, database persistence, and analytics dashboards into one intelligent automation platform.

This project represents a real-world implementation of Intelligent Document Processing (IDP) and Robotic Process Automation (RPA) concepts.