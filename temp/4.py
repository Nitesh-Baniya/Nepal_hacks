def setup_huggingface_model():
    """Setup Hugging Face model for text generation"""
    print("\n=== Hugging Face Model Setup ===")
    print("Loading text generation model. This may take a few minutes...")

    try:
        # Load a smaller model suitable for Google Colab
        model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        print(f"Loading model: {model_name}")

        # Create a text generation pipeline
        global generator
        generator = pipeline(
            "text-generation",
            model=model_name,
            torch_dtype="auto",
            device_map="auto"
        )
        print("Model loaded successfully!")
        return True
    except Exception as e:
        print(f"Error loading Hugging Face model: {e}")
        return False
