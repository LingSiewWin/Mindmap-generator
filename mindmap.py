from flask import Flask, request, render_template
import pytesseract
from pdf2image import convert_from_bytes
from pptx import Presentation
from transformers import pipeline
import torchvision
torchvision.disable_beta_transforms_warning()  # Silence torchvision warnings
import io
import re

app = Flask(__name__)

# Initialize summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_text_from_pdf(file):
    try:
        images = convert_from_bytes(file.read())
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image) + "\n"
        return text, None
    except Exception as e:
        return None, str(e)

def extract_text_from_pptx(file):
    try:
        prs = Presentation(file)
        text = ""
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text += shape.text + "\n"
        return text, None
    except Exception as e:
        return None, str(e)

def summarize_text(text):
    text = re.sub(r'\s+', ' ', text).strip()
    max_input_length = 1024
    text = text[:max_input_length]
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def generate_ascii_mind_map(summary):
    sentences = re.split(r'[.!?]\s+', summary)
    key_points = [s.strip() for s in sentences if s.strip()]
    mind_map = "Mind Map\n"
    mind_map += "└── Main Topic\n"
    for i, point in enumerate(key_points[:5], 1):
        mind_map += f"    ├── {point}\n"
    return mind_map

@app.route("/", methods=["GET", "POST"])
def index():
    mind_map = None
    error = None
    
    if request.method == "POST":
        if 'file' not in request.files:
            error = "No file uploaded"
        else:
            file = request.files['file']
            if file.filename.endswith('.pdf'):
                text, err = extract_text_from_pdf(file)
            elif file.filename.endswith('.pptx'):
                text, err = extract_text_from_pptx(file)
            else:
                error = "Unsupported file type. Use PDF or PPTX."
                text = None
            
            if text:
                try:
                    summary = summarize_text(text)
                    mind_map = generate_ascii_mind_map(summary)
                except Exception as e:
                    error = f"Error processing file: {str(e)}"
            else:
                error = err or "Failed to extract text from file."
    
    return render_template('index.html', mind_map=mind_map, error=error)

if __name__ == "__main__":
    app.run(debug=True)