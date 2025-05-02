
import time
import requests

def generate_answer(policy, top_k_framework):
    start = time.time()

    top_k_text = "\n\n".join(
        [f"Passage {i+1}: {chunk}" for i, chunk in enumerate(top_k_framework)]
    )

    prompt = (
        "You are a compliance assistant.\n"
        "1) First write the requirement at the beginning of the answer.\n"
        "2) Given the evidence, find if the requirement is: 'Satisfied' or 'Not Satisfied'.\n\n"
        "3) Explain in short, why?"
        "Requirement:\n"
        f"{top_k_text}\n\n"
        "Evidence:\n"
        f"{policy}\n"
    )

    print("*** SENDING PROMPT TO LLaMA 3.2 ***")

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            },
            timeout=60  # Prevent hanging
        )

        response.raise_for_status()  # Raise HTTP errors explicitly

        result = response.json().get("response", None)
        if result is None:
            raise ValueError("No response content in model output.")
        print("*** RESPONSE RECEIVED ***")
        print("Time taken:", time.time() - start)
        return result.strip()

    except Exception as e:
        print("ERROR in generate_answer:", e)
        return "[ERROR: Failed to generate answer]"




if __name__ == "__main__":
    print("Running test call to generate_answer()...")
    test_policy = "This policy requires data to be encrypted at rest."
    test_framework = ["The system must support encryption for stored data."]
    result = generate_answer(test_policy, test_framework)
    
    with open("test_output.txt", "w", encoding="utf-8") as f:
        f.write("Test Output:\n")
        f.write(result)
        
    print(generate_answer(test_policy, test_framework))
