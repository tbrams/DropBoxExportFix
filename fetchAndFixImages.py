import os
import re
import requests

def process_markdown_files(directory):
    # Get a list of all markdown files in the current directory
    for root, dirs, files in os.walk(directory):
        markdown_files = [f for f in files if f.endswith('.md') and not f.startswith('._')]
        
        for file in markdown_files:
            file_path = os.path.join(root, file)
            
            # Create 'images' directory if it doesn't exist
            images_dir = os.path.join(root, 'images')
            if not os.path.exists(images_dir):
                os.makedirs(images_dir)

            # Open the markdown file and read its content
            with open(file_path, 'r') as f:
                content = f.read()

            # Find all dropbox image links in the content
            image_links = re.findall(r'https://paper-attachments.dropbox.com[^\s\)]+', content)

            # Download each image and save it to the 'images' directory
            for link in image_links:
                filename = link.split('/')[-1]
                file_path = f'{images_dir}/{filename}'
                if not os.path.exists(file_path):
                    response = requests.get(link)
                    if response.status_code == 200:
                        with open(file_path, 'wb') as f:
                            f.write(response.content)
                        print(f'Downloaded {filename}')
                    else:
                        print(f'Failed to download {link}')
                else:
                    print(f'{filename} already exists, skipping download')

            # Replace the links in the content with the local path to the images
            new_content = re.sub(r'https://paper-attachments.dropbox.com[^\s\)]+', lambda x: f'images/{x.group(0).split("/")[-1]}', content)

            # Save the modified content to a new file with '_new' suffix
            new_file = file.replace('.md', '_new.md')
            new_file_path = os.path.join(root, new_file)
            with open(new_file_path, 'w') as f:
                f.write(new_content)
            print(f'Saved modified content to {new_file_path}')

print('Process started')
process_markdown_files('.')
print('Process completed')