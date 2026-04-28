import os
import glob
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration 

# Load the pretrained processor and model (using Blip2 for this local example)
processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b")

# Specify the directory where your images are
image_dir = "/path/to/your/images"
image_exts = ["jpg", "jpeg", "png"] 

# Open a file to write the captions
with open("captions.txt", "w") as caption_file:
    # Iterate over each image file in the directory
    for image_ext in image_exts:
        # Search for files matching the extension in the specified directory
        for img_path in glob.glob(os.path.join(image_dir, f"*.{image_ext}")):
            # Load and convert image
            raw_image = Image.open(img_path).convert('RGB')
            
            # Process the image
            inputs = processor(raw_image, return_tensors="pt")
            
            # Generate caption
            out = model.generate(**inputs, max_new_tokens=50)
            caption = processor.decode(out[0], skip_special_tokens=True)
            
            # Write the filename and its caption to the text file
            caption_file.write(f"{os.path.basename(img_path)}: {caption}\n")