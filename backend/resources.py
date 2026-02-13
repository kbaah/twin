from pypdf import PdfReader
import json

# Read Profile PDF (Primary)
try:
    reader = PdfReader("./data/Kwabena Baah-Boakye Profile.pdf")
    profile = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            profile += text
except FileNotFoundError:
    profile = "Profile not available"

# Read Resume PDF
try:
    reader = PdfReader("./data/Kwabena Baah-Boakye - Resume.pdf")
    resume = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume += text
except FileNotFoundError:
    resume = "Resume not available"

# Read LinkedIn PDF
try:
    reader = PdfReader("./data/linkedin.pdf")
    linkedin = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            linkedin += text
except FileNotFoundError:
    linkedin = "LinkedIn profile not available"

# Read other data files
with open("./data/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

with open("./data/style.txt", "r", encoding="utf-8") as f:
    style = f.read()

with open("./data/facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)