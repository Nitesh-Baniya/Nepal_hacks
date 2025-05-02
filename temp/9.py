def run_cybersecurity_rag_lab():
    """Main function to run the lab session"""
    # Display header
    display(HTML("""
    <div style="background-color:#4CAF50; color:white; padding:10px; border-radius:5px; margin-bottom:20px;">
        <h1 style="text-align:center;">Cybersecurity RAG Lab Session</h1>
        <h3 style="text-align:center;">Retrieval Augmented Generation for Question Answering</h3>
    </div>
    """))

    # Setup Hugging Face model
    if not setup_huggingface_model():
        print("Failed to setup Hugging Face model. Please restart the notebook and try again.")
        return

    # Sample questions for the lab
    sample_questions = [
        "What is phishing and how can I identify it?",
        "Can you explain what a DDoS attack is?",
        "How does two-factor authentication improve security?",
        "What is the difference between encryption and hashing?",
        "How do zero-day vulnerabilities work?",
        "What is a supply chain attack and can you give an example?"
    ]

    print("\n=== Sample Questions ===")
    for i, question in enumerate(sample_questions):
        print(f"{i+1}. {question}")

    # Interactive Q&A session
    while True:
        print("\n" + "="*50)
        choice = input("Enter a number to select a sample question, or type your own question, or 'q' to quit: ")

        if choice.lower() == 'q':
            break

        try:
            # Check if user selected a sample question
            if choice.isdigit() and 1 <= int(choice) <= len(sample_questions):
                query = sample_questions[int(choice)-1]
            else:
                query = choice

            # Process the query
            start_time = time.time()
            answer = cybersecurity_rag_system(query, df, embeddings, top_k=3)
            end_time = time.time()

            print(f"\nProcessing time: {end_time - start_time:.2f} seconds")

            # Ask for feedback
            feedback = input("\nWas this answer helpful? (y/n): ")
            if feedback.lower() == 'n':
                print("Thank you for your feedback. Let's try another question.")

        except Exception as e:
            print(f"Error processing question: {e}")
