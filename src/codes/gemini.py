from dotenv import load_dotenv
import google.generativeai as genai
import os

credentials = load_dotenv()
variables = os.getenv('API_KEY')
genai.configure(api_key=variables)

class Gemini:
	def __init__(self,prompt:str) -> None:
		self.prompt = prompt

	def generate(self, prompt:str) -> str:
		generation_config ={
            "candidate_count": 1,
            "temperature": 1,
        }
		model = genai.GenerativeModel(model_name="gemini-1.5-flash")
		response = model.generate_content(prompt, generation_config=generation_config)
		return response.text