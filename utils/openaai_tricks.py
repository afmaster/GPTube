import openai
from config.env import OPENAI_API_KEY


openai.api_key = OPENAI_API_KEY
MODEL = 'text-davinci-003'

def create_completion(text_to_ai: str) -> str:
    """
    retrieve the first response from openAI model
    :param text_to_ai: user_input
    :return: openAI API text response
    """
    completion_resp = openai.Completion.create(
        prompt=text_to_ai,
        engine=MODEL,
        max_tokens=1000,
        temperature=0.1
    )
    response_text = str(completion_resp.choices[0].text)
    return response_text