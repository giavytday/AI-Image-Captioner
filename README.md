# AI-Powered Image Captioning Suite

An automated toolset that leverages Generative AI to bridge the gap between visual content and text. This project was developed to solve real-world challenges in accessibility (Alt-text) and SEO for high-volume digital publishers.

## 🌟 Core Philosophy
In a digital-first world, images without text are "invisible" to search engines and screen readers. This suite provides a "voice" to images by using **BLIP (Bootstrapping Language-Image Pre-training)** models to generate human-like descriptions automatically.

## 🛠 Features
- **URL Scraper & Captioner:** Uses `BeautifulSoup` to find images on any webpage (like Wikipedia) and generates a `captions.txt` report.
- **Local Batch Processor:** Scans local directories using `glob` to process large libraries of images using the powerful **BLIP-2** model.
- **Interactive Web App:** A user-friendly `Gradio` interface that allows users to upload images and get instant captions.

## 🚀 Tech Stack
- **AI Models:** Salesforce BLIP & BLIP-2 (via Hugging Face Transformers)
- **Frontend:** Gradio
- **Web Scraping:** BeautifulSoup4 & Requests
- **Image Processing:** PIL (Pillow) & NumPy

## 📖 How to Use
1. **Install Dependencies:**
   ```bash
   pip install transformers pillow gradio beautifulsoup4 requests torch

2. Run the Web App:
    python3 image_captioning_app.py

3. Process a Website:
    Edit the URL in automate_url_captioner.py and run:
    python3 automate_url_captioner.py