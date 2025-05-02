# import ollama
# from parsers.parse_docs import parse_policy_folder
# import os




# def summarize_with_llama(content):
#     # prompt = f"""Summarize the following document content into bullet-point key ideas. Be concise and ignore filler content. /
#     # Only include the most important insights and facts.
    
#     prompt = f"""
#     Summarize the following parsed text with high fidelity, ensuring no minor details or specific information are omitted.
#     Maintain accuracy and completeness while condensing the content. Output should be concise but fully representative of all critical and
#     nuanced elements in the original text.

#     Content:
#     \"\"\"
#     {content}
#     \"\"\"

#     Summary:"""

#     # Now, produce a comprehensive yet concise summary that fully represents all specific content from the original text, without altering meaning or omitting any detail."""

#     response = ollama.chat(
#         model='llama3.2', 
#         messages=[{'role': 'user', 'content': prompt}]
#     )

#     return response['message']['content']


# if __name__ == "__main__":
#     # Parse PDFs from the 'policy' folder
#     parsed_docs = parse_policy_folder("data/policies")



#     for doc in parsed_docs:
#         print(f"\n--- Summary for {doc['filename']} ---")
#         summary = summarize_with_llama(doc["content"])
#         print(summary)
#         print("\n" + "-"*80 + "\n")

import ollama
import os
from parsers.parse_docs import parse_policy_folder

def summarize_with_llama(content):
    # The original prompt remains unchanged
    prompt = f"""
    Summarize the following parsed text with high fidelity, ensuring no minor details or specific information are omitted.
    Maintain accuracy and completeness while condensing the content. Output should be concise but fully representative of all critical and
    nuanced elements in the original text.

    Content:
    \"\"\"
    {content}
    \"\"\"

    Summary:"""

    # Requesting summary from the Llama model
    response = ollama.chat(
        model='llama3.2', 
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['message']['content']


       
def save_summary_to_file(summary, filename):
    # Ensure the 'summarizer/summaries' directory exists
    summaries_dir = 'summarizer/summaries'
    os.makedirs(summaries_dir, exist_ok=True)  # Create 'summaries' folder if it doesn't exist

    # Save the summary in a text file with the same name as the policy file
    summary_filename = os.path.join(summaries_dir, f"{filename}.txt")
    with open(summary_filename, 'w') as f:
        f.write(summary)


if __name__ == "__main__":
    # Define the folder path for internal policies
    policy_folder_path = 'data/policies'

    # Parse PDFs from the 'all_internal_policy' folder
    parsed_docs = parse_policy_folder(policy_folder_path)

    # For each parsed document, generate a summary and save it to the summarizer folder
    for doc in parsed_docs:
        print(f"\n--- Generating summary for {doc['filename']} ---")
        summary = summarize_with_llama(doc["content"])
        print(summary)
        save_summary_to_file(summary, doc['filename'])  # Save the summary to a file
        print(f"Summary saved for {doc['filename']}")
        print("\n" + "-"*80 + "\n")


