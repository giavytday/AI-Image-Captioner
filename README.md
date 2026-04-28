# AI-Powered Image Captioning Suite
<img width="815" height="516" alt="Screenshot 2026-04-27 at 7 42 41 PM" src="https://github.com/user-attachments/assets/23dd0b83-122d-4a90-adaf-a3514d3974b3" />

An automated toolset leveraging Generative AI to convert visual content into descriptive text. This project addresses real-world challenges in web accessibility (Alt-text) and Search Engine Optimization (SEO) for high-volume digital publishers.

Project Overview
This suite transforms visual data into machine-readable language using state-of-the-art Image Captioning models. By implementing Salesforce's BLIP (Bootstrapping Language-Image Pre-training) architecture, the project provides automated solutions for:
- Accessibility: Improving digital inclusion for visually impaired users.
- SEO & Discovery: Enhancing image indexability for search engines.
- Operational Efficiency: Reducing manual overhead for high-volume content creators.

Technical Accomplishments
- Cloud-Native Deployment: Successfully containerized and deployed the application using IBM Cloud Code Engine, providing a public, scalable URL for global access.
- Model Integration: Implemented the Salesforce/blip-image-captioning-base model via the Hugging Face Transformers library.
- Resource Optimization: Engineered a memory-efficient build process by utilizing CPU-only PyTorch builds, significantly reducing the container image size and ensuring compatibility with cloud-based ephemeral storage.
- Interface Design: Developed a real-time web application using Gradio for seamless user interaction and model testing.
- Automated Pipelines: Built a web-scraped URL processing tool using BeautifulSoup to extract and caption images from live websites.

Core Features
- Interactive Web UI: A live interface for single-image uploads and real-time caption generation.
- Web Scraper & Captioner: Utilizes BeautifulSoup to extract and caption images from live URLs, generating structured descriptive reports.
- Containerized Environment: Fully defined Dockerfile and requirements.txt optimized for cloud deployment (IBM Code Engine/Docker).

Tech Stack
- AI/ML: Salesforce BLIP, Hugging Face Transformers, PyTorch (CPU-optimized)
- Web: Gradio, BeautifulSoup4, Requests
- Cloud: IBM Cloud Code Engine, IBM Cloud Container Registry
- Processing: PIL (Pillow), NumPy
- DevOps: Git, Docker

Installation and Usage
1. Local Setup
- pip install -r requirements.txt

2. Execution
- Web Application: python3 image_captioning_app.py
- URL Scraper: python3 automate_url_captioner.py

3. Cloud Deployment (IBM Code Engine)
- The project is configured for IBM Code Engine. To rebuild and redeploy:
- ibmcloud ce buildrun submit --name buildrun-v9 --build build-ai-captioner --source .
- ibmcloud ce application update --name ai-captioner-app

Repository & Live App
GitHub: https://github.com/giavytday/AI-Image-Captioner
Live URL: https://ai-captioner-app.297ozx12fq46.us-south.codeengine.appdomain.cloud
