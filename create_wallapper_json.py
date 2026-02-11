import os
import json

def generate_wallpaper_json():
    # The list that will hold our category objects
    wallpaper_data = []
    
    # Path where your folders are located (current directory)
    root_dir = "."
    
    # Extension types we want to include
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')

    # Get all directories in the current path
    # We skip hidden folders like .git
    categories = [d for d in os.listdir(root_dir) if os.path.isdir(d) and not d.startswith('.')]

    for category in categories:
        category_path = os.path.join(root_dir, category)
        image_list = []

        # Get all images in this folder
        for filename in os.listdir(category_path):
            if filename.lower().endswith(valid_extensions):
                # Matching your requested JSON format: { "name": "filename.jpg" }
                image_list.append({
                    "name": filename
                })

        # Only add categories that actually contain images
        if image_list:
            wallpaper_data.append({
                "category": category,
                "images": image_list
            })

    # Save to a file called wallpapers.json
    with open('wallpapers.json', 'w', encoding='utf-8') as f:
        json.dump(wallpaper_data, f, indent=4)

    print(f"Successfully generated wallpapers.json with {len(wallpaper_data)} categories!")

if __name__ == "__main__":
    generate_wallpaper_json()