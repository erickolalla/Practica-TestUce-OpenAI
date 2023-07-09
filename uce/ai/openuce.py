import openai
from pydantic import BaseModel

openai.organization = 'org-VuqI6upRDoGnYHHjA7hWBHkS'
openai.api_key = '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'


class Document(BaseModel):
    item: str = ''

def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = 0.2,
        messages=[
            {"role": "system", "content": """Eres un profesor de programación para estudiantes universitarios de la carrera de sistemas de información, necesito que respondas de forma clara y concisa lo que se te pregunte y ejemplificar"""},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    return [response, total_tokens]
