# AI-Powered Image Captioning Suite
<img width="815" height="516" alt="Screenshot 2026-04-27 at 7 42 41 PM" src="https://github.com/user-attachments/assets/23dd0b83-122d-4a90-adaf-a3514d3974b3" />

An automated toolset leveraging Generative AI to convert visual content into descriptive text. This project addresses real-world challenges in web accessibility (Alt-text) and Search Engine Optimization (SEO) for high-volume digital publishers.

Project Overview
This suite transforms visual data into machine-readable language using state-of-the-art Image Captioning models. By implementing Salesforce's BLIP architecture, the project provides automated solutions for:
- Accessibility: Improving digital inclusion for visually impaired users.
- SEO & Discovery: Enhancing image indexability for search engines and internal databases.
- Operational Efficiency: Reducing manual overhead for high-volume content creators.

Technical Accomplishments
- Model Integration: Implemented BLIP and BLIP-2 models via the Hugging Face Transformers library.
- Interface Design: Developed a real-time web application using Gradio for seamless user interaction.
- Data Engineering: Built custom pipelines for both web-scraped URL processing and local batch image processing.

Core Features
- Web Scraper & Captioner: Utilizes BeautifulSoup to extract and caption images from live URLs, generating structured reports.
- Batch Processor: Automates the captioning of local image directories using high-performance BLIP-2 models.
- Interactive Web UI: Provides an intuitive interface for single-image uploads and real-time caption generation.

Tech Stack
- AI/ML: Salesforce BLIP & BLIP-2, Hugging Face Transformers, PyTorch
- Web: Gradio, BeautifulSoup4, Requests
- Processing: PIL (Pillow), NumPy

Installation and Usage
1. Install Dependencies
pip install transformers pillow gradio beautifulsoup4 requests torch
2. Execution
- Web Application: python3 image_captioning_app.py
- URL Scraper: Configure automate_url_captioner.py and run.
- Local Batch: python3 blip2_image_cap_local.py
