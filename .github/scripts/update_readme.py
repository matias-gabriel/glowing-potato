import os

# --- Configuration ---
README_PATH = "README.md"
# Updated to match your README file exactly
START_TAG = "<!---Exercise counting Start-->"
END_TAG = "<!---Exercise counting End-->"
EDUCATIVE_DIR = "educative_io"

# --- Logic ---
print("Starting README update script (non-regex method)...")

# 1. Count the exercises
leetcode_count = sum(
    1 for item in os.listdir(".") if os.path.isdir(item) and item[0].isdigit()
)
educative_count = 0
if os.path.isdir(EDUCATIVE_DIR):
    educative_count = sum(
        1 for item in os.listdir(EDUCATIVE_DIR) if item.endswith(".py")
    )

# 2. Read the existing README content
try:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"ERROR: {README_PATH} not found. Exiting.")
    exit(1)

# 3. Find the positions of our tags
try:
    start_index = content.index(START_TAG)
    end_index = content.index(END_TAG)
except ValueError:
    print(
        f"ERROR: Could not find start/end tags in {README_PATH}. Check for exact match including spaces. Exiting."
    )
    exit(1)

# 4. Build the new content block
new_stats_block = (
    f"\n* **LeetCode:** {leetcode_count}\n" f"* **Educative.io:** {educative_count}\n"
)

# 5. Build the final README content by combining the parts
updated_content = (
    content[: start_index + len(START_TAG)] + new_stats_block + content[end_index:]
)

# 6. Write the updated content back to the file
with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(updated_content)

print(
    f"Successfully updated README: LeetCode={leetcode_count}, Educative.io={educative_count}"
)
