def try_alternative_model():
    """
    Function to try a different model from Hugging Face

    This is provided as an optional exercise for students to experiment with
    different models and compare their performance.
    """
    print("\n=== Try Alternative Model ===")
    print("You can experiment with other models from Hugging Face.")
    print("Here are some options to try:")
    print("1. google/flan-t5-small (smaller, faster)")
    print("2. facebook/opt-350m (medium size)")
    print("3. databricks/dolly-v2-3b (larger, may need more memory)")

    choice = input("Enter a number to select a model, or 'c' to continue with current model: ")

    if choice.lower() == 'c':
        return True

    try:
        model_options = {
            "1": "google/flan-t5-small",
            "2": "facebook/opt-350m",
            "3": "databricks/dolly-v2-3b"
        }

        if choice in model_options:
            model_name = model_options[choice]
            print(f"Loading {model_name}... (this may take a few minutes)")

            global generator
            generator = pipeline(
                "text-generation",
                model=model_name,
                torch_dtype="auto",
                device_map="auto"
            )

            print(f"Successfully loaded {model_name}!")
            return True
        else:
            print("Invalid choice. Continuing with current model.")
            return True
    except Exception as e:
        print(f"Error loading alternative model: {e}")
        print("Continuing with the default model.")
        return True

