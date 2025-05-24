🌟 MindMap Magic Generator 🌟
Welcome to the MindMap Magic Generator, the coolest tool to transform your boring PDFs and PowerPoint slides into snappy summaries and awesome ASCII mind maps! 🚀 Upload your notes, watch the OCR wizardry extract text, let AI sprinkle some summarization fairy dust, and poof—a neat mind map appears in glorious ASCII art! Ready to declutter your brain? Let’s dive in! 😎
🎉 What’s This All About?
This is a Python-powered web app built with Flask that:

Extracts text from PDFs (via Tesseract OCR) or PPTX files (via python-pptx).
Summarizes the content using the open-source facebook/bart-large-cnn model from Hugging Face.
Generates a slick ASCII mind map to highlight key points, perfect for quick reviews or showing off your notes in style!

Whether you're a student, a professional, or just someone with a pile of slides, this tool makes your notes pop into a visual masterpiece. 🎨
🚀 Getting Started
Ready to unleash the magic? Follow these steps to get your mind map generator up and running on your macOS (or any) machine!
🛠️ Requirements
To make the magic happen, you’ll need:

Python 3.9+ (3.9.20 works like a charm!)
Python Packages:
flask - For the snazzy web interface.
pytesseract - For OCR text extraction from PDFs.
pdf2image - Converts PDFs to images for OCR.
python-pptx - Extracts text from PowerPoint files.
transformers - Powers AI summarization with Hugging Face’s BART model.


System Dependencies:
Tesseract OCR: For reading text from PDFs.
Poppler: Helps pdf2image do its thing.



Install them like this:
pip install flask pytesseract pdf2image python-pptx transformers

For macOS:
brew install tesseract
brew install poppler

🧙‍♂️ Installation

Clone the Repo (or just grab mindmap.py and templates/index.html):
git clone https://github.com/your-username/mindmap-generator.git
cd mindmap-generator


Set Up a Virtual Environment:
python -m venv mindmap-env
source mindmap-env/bin/activate


Install Python Dependencies:
pip install flask pytesseract pdf2image python-pptx transformers


Ensure Tesseract and Poppler are Installed:

Verify Tesseract: tesseract --version
Verify Poppler: pdftoppm --version
If missing, install them with Homebrew (see Requirements above).


Create Templates Folder:

Create a templates folder in your project directory.
Place index.html (from the provided code) in templates/index.html.


Launch the Magic:
python -u mindmap.py


Open your browser and head to http://localhost:5000. Voilà! 🎉


🎮 How to Use It

Upload Your File:

On the homepage, select a .pdf or .pptx file (your notes, slides, or secret plans).
Click "Generate Mind Map" and let the magic unfold!


Watch the Magic:

The app extracts text (OCR for PDFs, direct extraction for PPTX).
AI summarizes the content into a concise blurb.
An ASCII mind map is generated, showcasing up to 5 key points in a tree-like structure.


Admire the Result:

Your mind map appears in a neat <pre> block, ready to copy, share, or just marvel at!



Pro Tip: Clear, typed text in PDFs works best for OCR. Handwritten notes might make Tesseract a bit grumpy. 😅
🐛 Troubleshooting

ModuleNotFoundError: No module named 'pptx'?
Install the correct package: pip install python-pptx.


ValueError: too many values to unpack?
Ensure extract_text_from_pdf in mindmap.py returns exactly two values (text, err). Use the provided mindmap.py version to fix this.


TemplateNotFound: index.html?
Ensure index.html is in a templates folder in your project directory.


Tesseract or Poppler missing?
Install them with brew install tesseract poppler on macOS.


Torchvision warnings?
These are harmless. The provided mindmap.py silences them with torchvision.disable_beta_transforms_warning().


Other errors? Check your Python version (python --version) and ensure you’re in the right virtual environment.

Still stuck? Ping the community or raise an issue on GitHub! We’re here to help. 😊
🌈 Why This Rocks

Fast: Upload, process, and get your mind map in seconds.
Free & Open-Source: Powered by open-source tools like Tesseract and Hugging Face.
Fun: ASCII art makes everything better, right? 🎨
Lightweight: Runs on your local machine, no cloud nonsense.

🤝 Contributing
Got ideas to make this even cooler? Add colors to the ASCII map? Support more file types? Dive in!

Fork the repo, make your changes, and submit a pull request.
Share feedback or report bugs via GitHub Issues.

📜 License
This project is licensed under the MIT License—free to use, modify, and share! 🚀
😎 Final Words
Turn your notes into a masterpiece with the MindMap Magic Generator! Upload, summarize, and map your ideas like a pro. Got questions? Want to add sparkles to the UI? Let us know! Now go make some mind-blowing mind maps! 💥
