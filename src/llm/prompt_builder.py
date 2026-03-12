class PromptBuilder:

    def build(self, query, contexts):

        context_text = "\n".join(contexts)

        prompt = f"""
Use the following context to answer the question.

Context:
{context_text}

Question:
{query}

Answer:
"""

        return prompt