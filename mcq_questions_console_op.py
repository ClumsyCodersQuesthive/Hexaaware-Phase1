from groq import Groq

num_questions = int(input("Enter the no of Question: "))
topic = input("Enter the Topic: ")
difficulty = input("Enter the Difficulty Level ('easy', 'medium', 'hard'): )")
client = Groq(api_key= ("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"))
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": f"Generate {num_questions} multiple-choice questions about {topic} with difficulty level {difficulty}.Get the output in list format"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")