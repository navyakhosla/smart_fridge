import json
from google import genai
from PIL import Image
client=genai.Client(api_key="AIzaSyBuBw2LML6N4Q7SS3V9_iDfryollp8y-No")
class RecipeAssistant:
    def __init__(self):
        self.recipes =[]
    def get_recipes_from_gemini(self,image_path):
        """Using gemini to identify ingredients and suggest recipes"""
        img=Image.open(image_path)
        prompt=("Identify the items in this image and suggest 3 recipes."
        "Return the output as a valid JSON list of objects."
        "Each object must have these keys:'name','time','difficulty', and'steps'(list of strings, each string is one step )."
        "Do not include conversational text, just raw JSON.")
        response=client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=[prompt,img]
        )
        self._parse_recipes(response.text)
    def _parse_recipes(self,raw_text):
        """ Converts the AI's JSON string directly into a python list"""
        try:
            clean_json = raw_text.replace("```json", "").replace("```", "").strip()
            self.recipes=json.loads(clean_json)
            # print("Recipes from gemini:",self.recipes)
            print("Data successfully parsed using JSON.")
        
        except json.JSONDecodeError as e:
            print(f" Error: The AI sent invalid JSON. {e}")
    def filter_recipes(self,max_time):
        """Sorts the recipe based on the user time"""
        print(f"\n ***** Recipes you can make in {max_time} mins or less ***** ")
        found=False
        rno=1
        for r in self.recipes:
            time_number=int(''.join(filter(str.isdigit,r['time'])))
            if time_number<=max_time:
                print(f"-----{rno}.{r['name']}-----")
                print(f"Time:{r['time']}")
                print(f"Difficulty:{r['difficulty']}")
                print()
                print("Steps:")
                for i, step in enumerate(r['steps'],1):
                    print(f"{i}.{step}")
                print()
                rno+=1
                found=True
        if not found:
          print("No recipes found for the time given")
assistant=RecipeAssistant()
image_path=input("Enter the image path:")
time_limit=int(input("Enter the cooking time(minutes): "))
assistant.get_recipes_from_gemini(image_path)
assistant.filter_recipes(time_limit)