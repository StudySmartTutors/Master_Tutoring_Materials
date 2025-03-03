#!/usr/bin/env python
# coding: utf-8

# In[25]:


import os
import re

# Set the test directory path
test_dir = "/Users/juanescobar/Documents/Curriculum/test_guided_practice"

# Function to convert spaces and special characters to underscores, ensuring grade numbers are kept
def format_underscores(grade, standard):
    # Replace spaces and '&' with underscores
    standard = standard.replace(" ", "_").replace("&", "_")
    
    # Extract multiple standards and ensure grade number is prefixed to each
    standards = re.findall(r"[A-Za-z]*\.?\d+[A-Za-z0-9.]*", standard)

    # Debugging: Print extracted standards
    print(f"📌 Extracted from '{standard}': {standards}")

    formatted_standards = "_".join([f"{grade}.{s}" for s in standards])
    
    return formatted_standards

# Define renaming patterns for Phase 1 (underscore conversion)
rename_patterns = {
    # Math Student Version
    r"^Generic\.(\d+)\.(.+)\.GL\.tex$": lambda m: f"GuidedLesson_Grade{m.group(1)}_Math_{m.group(1)}.{m.group(2)}.tex",

    # Math Instructor Version
    r"^Generic\.(\d+)\.(.+)\.GL\.Instructor Version\.tex$": lambda m: f"GuidedLesson_Grade{m.group(1)}_Math_{m.group(1)}.{m.group(2)}_Instr.tex",

    # ELA Student Version (fixing multiple standards issue, ensuring proper '&' detection)
    r"^GP (\d+)\.([A-Za-z0-9\s&.]+)\.tex$": lambda m: f"GuidedLesson_Grade{m.group(1)}_ELA_{format_underscores(m.group(1), m.group(2))}.tex",

    # ELA Instructor Version (ensuring correct standard format, fixing standard parsing)
    r"^(\d+)([A-Za-z0-9\s&.]+) key\.tex$": lambda m: f"GuidedLesson_Grade{m.group(1)}_ELA_{format_underscores(m.group(1), m.group(2))}_Instr.tex"
}

# Function to rename files (Phase 1 - Underscore conversion only)
def rename_guided_practice():
    for file in os.listdir(test_dir):
        old_path = os.path.join(test_dir, file)
        new_filename = None

        # Apply renaming rules
        for pattern, replacement in rename_patterns.items():
            match = re.match(pattern, file)
            if match:
                new_filename = replacement(match)
                break

        # Debugging: Print before renaming
        if new_filename:
            print(f"🔄 Attempting to rename: {file} → {new_filename}")

        # If a new name was generated, rename the file
        if new_filename and new_filename != file:
            new_path = os.path.join(test_dir, new_filename)
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {file} → {new_filename}")

# Run the renaming function for Phase 1
rename_guided_practice()

print("✅ Phase 1: Underscore Conversion Complete!")



# In[21]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




