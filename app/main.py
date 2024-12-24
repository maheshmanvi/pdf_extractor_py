import pytesseract
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from pathlib import Path
from typing import Optional
import shutil
import os
from services.pdf_extractor import extract_pdf_data, extract_tables_from_pdf, extract_toc
from models.response_model import ExtractedDataResponse
from logger import log_error, generate_unique_id
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration from .env file
TESSERACT_PATH = os.getenv("TESSERACT_PATH", r"C:\Program Files\Tesseract-OCR\tesseract.exe")

# Set up Tesseract path if required
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

# Get the paths from the .env file
TEMP_DIR = os.getenv("TEMP_DIR", ".temp")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", os.path.join(TEMP_DIR, "uploads"))
EXTRACTED_DIR = os.getenv("EXTRACTED_DIR", os.path.join(TEMP_DIR, "extracted"))

app = FastAPI()

@app.post("/extract-pdf", response_model=ExtractedDataResponse)
async def extract_pdf(
    file: UploadFile = File(...),
    pages: Optional[str] = Form(None),
    headings: Optional[str] = Form(None),
    chapters: Optional[str] = Form(None),
    language: Optional[str] = Form("eng"),
    index_page: Optional[int] = Form(None)
):
    # Generate a unique ID for this request
    request_id = generate_unique_id()

    # Clear previous uploads and extractions
    if os.path.exists(UPLOAD_DIR):
        shutil.rmtree(UPLOAD_DIR)
    if os.path.exists(EXTRACTED_DIR):
        shutil.rmtree(EXTRACTED_DIR)

    # Ensure directories exist
    Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
    Path(EXTRACTED_DIR).mkdir(parents=True, exist_ok=True)

    # Save the uploaded PDF file to the .temp/uploads folder
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Parse optional form parameters
    page_numbers = [int(p.strip()) for p in pages.split(",") if p.strip().isdigit()] if pages else None
    chapter_headings = [h.strip() for h in headings.split(",")] if headings else None
    chapter_names = [c.strip() for c in chapters.split(",")] if chapters else None

    toc = extract_toc(file_path)
    if toc:
        for entry in toc:
            print(f"Level: {entry['level']}, Title: {entry['title']}, Page: {entry['page']}")
    else:
        print("No Table of Contents found.")

    try:
        # Extract data from the PDF
        extracted_data = extract_pdf_data(
            file_path,
            EXTRACTED_DIR,
            pages=page_numbers,
            headings=chapter_headings,
            chapters=chapter_names,
            ocr_languages=language,
            request_id=request_id,
            index_page=index_page
        )

        # Extract tables if needed (using Camelot)
        tables = ""  # For now, keeping it empty as your example doesn't extract tables

        # Return the extracted data along with a success message
        return {
            "text": extracted_data["text"],
            "images": extracted_data["images"],
            "metadata": extracted_data["metadata"],
            "tables": tables,
            "notes": f"Extraction completed successfully. Request ID: {request_id}. Check the logs for any errors."
        }

    except Exception as e:
        log_error(f"Error during PDF extraction for request {request_id}: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred during extraction (Request ID: {request_id}).")
