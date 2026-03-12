from transformers import pipeline

class LLMGenerator:

    def __init__(self):

        self.generator = pipeline(
            "text-generation",
            model="mistralai/Mistral-7B-Instruct"
        )

    def generate(self, prompt):

        output = self.generator(prompt, max_length=512)

        return output[0]["generated_text"]