class LocalLLM:
    def __init__(self, model_name="EleutherAI/gpt-neo-1.3B"):
        from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        self.generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

    def generate_response(self, query):
        prompt = f"Answer the following query concisely and accurately:\nQuery: {query}\nResponse:"
        response = self.generator(prompt, max_length=200)
        return response[0]["generated_text"]
