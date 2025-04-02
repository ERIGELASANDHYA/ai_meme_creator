import sys
from PIL import Image, ImageDraw, ImageFont

# Ensure correct virtual environment usage
venv_path = "/Users/sandhyaerigela/Desktop/ai_meme_creator/backend/venv/lib/python3.13/site-packages"
if venv_path not in sys.path:
    sys.path.insert(0, venv_path)

# Load the uploaded image
image_path = "img-1.png"  # Path to uploaded image
img = Image.open(image_path)

# User preference: Change this to "overlay" or "under"
text_position_type = "under"  # Change to "overlay" for text on the image

# Define text
text = "Your custom text goes here!"

# Load a font (use Arial or fallback)
try:
    font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 40)  # Adjust size
except IOError:
    font = ImageFont.load_default()

# Initialize drawing context
draw = ImageDraw.Draw(img)
text_color = "white"  # Change color if needed

if text_position_type == "overlay":
    # Overlay text on image (top center)
    text_position = (img.width // 4, 50)  # Adjust for better visibility
    draw.text(text_position, text, fill=text_color, font=font)

else:  # "under" - Add text below the image
    padding = 100  # Space for text
    new_height = img.height + padding  # Extend image height
    
    # Create new image with extra space
    new_img = Image.new("RGB", (img.width, new_height), "white")
    new_img.paste(img, (0, 0))

    # Draw text in the new area
    draw = ImageDraw.Draw(new_img)
    text_position = (50, img.height + 20)  # Adjust below the image
    draw.text(text_position, text, fill="black", font=font)

    img = new_img  # Update image reference

# Show and save the final image
img.show()
img.save("output_img_1.png")

print("Image processed successfully! Saved as 'output_img_1.png'.")
