#!/bin/bash

# Define the path to the Math Guided Lessons
MATH_PATH="/Users/juanescobar/Documents/Curriculum/Master Tutoring Curriculum Mar 2025"

# Loop through each Math Guided Lesson folder (Grades 3-8)
for folder in "$MATH_PATH"/Grade*Guided*Lesson/; do
    # Extract grade level from folder name
    GRADE=$(basename "$folder" | grep -o '[0-9]')

    # Loop through all .tex files in the folder
    for file in "$folder"/*.tex; do
        # Extract filename without the path
        filename=$(basename "$file")

        # Identify if it's an Instructor Version
        if [[ "$filename" == *"Instructor Version"* ]]; then
            INSTRUCTOR="_Instr"
        else
            INSTRUCTOR=""
        fi

        # Extract standard(s) from filename
        STANDARD=$(echo "$filename" | grep -oE '[0-9]\.[A-Z]+\.[A-Z]+\.[0-9]+(, [0-9]\.[A-Z]+\.[A-Z]+\.[0-9]+)*')

        # If a standard is found, apply the new naming format
        if [[ -n "$STANDARD" ]]; then
            # Replace commas with underscores for multiple standards
            STANDARD_FORMATTED=$(echo "$STANDARD" | sed 's/, /)_(/g')

            # Construct the new filename
            NEW_NAME="GuidedLesson_Grade${GRADE}_Math_(${STANDARD_FORMATTED})${INSTRUCTOR}.tex"

            # Rename the file
            mv "$file" "$folder/$NEW_NAME"

            echo "Renamed: $filename → $NEW_NAME"
        else
            echo "Skipping (no standard found): $filename"
        fi
    done
done

echo "✅ Math Guided Lesson renaming complete!"



