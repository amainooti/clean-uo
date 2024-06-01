#!/bin/bash

# Define the target and destination directories
target_dir="$HOME/Downloads"

#specify your own directory in my case it's
destination_dir="$HOME/Documents/books/computer-science"

# Define the extensions to be moved
extensions=(".pdf" ".epub" ".docx")

# Create the destination directory if it does not exist
mkdir -p "$destination_dir"

# Loop through each extension and move matching files
for ext in "${extensions[@]}"; do
    # Find files with the current extension in the target directory and move them to the destination directory
    find "$target_dir" -type f -name "*$ext" -exec mv {} "$destination_dir" \;
done

echo "Files moved successfully!"

cd "$destination_dir" && open .



# you can further make this an executable by using chmod -x filename_for_script
# if you want to take it to the next level set a cron job using crontab -e and \
# specify when you want it to execute