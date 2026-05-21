# AI File Summarizer

A Python-based application that reads files and generates structured summaries using AI.

---

## Features

* Read `.txt` files
* Read `.pdf` files
* AI-powered summarization
* Handles long documents using chunking
* Basic error handling (missing files, empty files)
* Command-line interface (CLI)

---

## Tech Stack

* Python
* OpenAI API
* PyPDF2 / pdfplumber (PDF reading)
* python-dotenv

---

## Project Structure

ai-file-summarizer/
│
├── files/                # Sample input files
├── main.py               # Main application logic
├── requirements.txt      # Dependencies
├── .env                  # API key (not committed)
├── .gitignore
└── README.md

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/evamaina/ai-file-summarizer.git
cd ai-file-summarizer

### 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add OpenAI API key

Create a `.env` file:

OPENAI_API_KEY=your_api_key_here

---

## How to Run

python main.py

Then enter the file path when prompted:

files/sample.txt
or
files/sample.pdf

---

## Example Output

AI Summary:

Short Summary:
...

Key Points:

* ...
* ...

Main Takeaway:
...

---

## What I Learned

* How to integrate AI into real applications
* How to safely manage API keys
* Handling different file formats (TXT, PDF)
* Working with large inputs using chunking
* Structuring a project for GitHub and version control

---

## Future Improvements

* Combine chunk summaries into one final summary
* Add support for scanned PDFs (OCR)
* Build a web interface
* Add file upload support
