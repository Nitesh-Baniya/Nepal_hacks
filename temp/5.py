def generate_answer(query, relevant_passages, relevance_scores):
    """
    Generate an answer to the query using Hugging Face model and retrieved context

    Args:
        query: The user's question
        relevant_passages: Retrieved relevant passages
        relevance_scores: Similarity scores for the relevant passages

    Returns:
        Generated answer
    """
    # Prepare context from relevant passages
    context = "\n\n".join(
        [
            f"Passage {i+1} [Relevance: {score:.2f}]: {passage}"
            for i, (passage, score) in enumerate(
                zip(relevant_passages, relevance_scores)
            )
        ]
    )

    # Construct the prompt for TinyLlama
    prompt = f"""<|system|>
You are a cybersecurity expert assistant. Your task is to answer user questions about cybersecurity concepts accurately.
Use ONLY the provided context to formulate your answer.
If the context doesn't contain relevant information, admit that you don't have enough information to answer accurately.
Keep your answers concise, informative, and focused on cybersecurity.

Context:
{context}
<|user|>
{query}
<|assistant|>"""

    # Generate text using Hugging Face model
    try:
        result = generator(
            prompt,
            max_new_tokens=250,
            do_sample=True,
            temperature=0.3,
            top_p=0.9,
            num_return_sequences=1,
        )

        # Extract the generated text
        generated_text = result[0]["generated_text"]

        # Extract only the assistant's response part
        assistant_part = generated_text.split("<|assistant|>")[-1].strip()

        # Clean up any trailing model tokens
        if "<|" in assistant_part:
            assistant_part = assistant_part.split("<|")[0].strip()

        return assistant_part
    except Exception as e:
        return f"Error generating answer: {e}"
