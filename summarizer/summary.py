# import os

# def get_summaries():
#     # Directory where the summaries are stored
#     summary_dir = "summarizer"
    
#     # List all files in the summary folder
#     summary_files = [f for f in os.listdir(summary_dir) if f.endswith(".txt")]
    
#     summaries = {}
#     for summary_file in summary_files:
#         summary_path = os.path.join(summary_dir, summary_file)
        
#         # Read the content of each summary file
#         with open(summary_path, 'r', encoding='utf-8') as file:
#             summaries[summary_file] = file.read()

#     return summaries

import os

def get_txt_files(folder_path=None):
    # Default to the 'summarizer/summaries' folder if no folder path is provided
    if folder_path is None:
        folder_path = os.path.join(os.path.dirname(__file__), 'summaries')
    return [f for f in os.listdir(folder_path) if f.endswith('.txt')]



def read_file_content(filename, folder_path=None):
    if folder_path is None:
        folder_path = os.path.join(os.path.dirname(__file__), 'summaries')
    file_path = os.path.join(folder_path, filename)

    try:
        # First try utf-8
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # Fallback to cp1252 for Windows-encoded files
        with open(file_path, 'r', encoding='cp1252') as f:
            return f.read()
