import json
import os
from google import genai
from PIL import Image
import streamlit as st
st.title("Smart Fridge Recipe Assistant 🍳")
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
class RecipeAssistant:
    def __init__(self):
        self.recipes =[]
    def get_recipes_from_gemini(self,image):
        """Using gemini to identify ingredients and suggest recipes"""
        img=image
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
        st.markdown(f"##**Recipes you can make in {max_time} mins or less** ")
        found=False
        rno=1
        for r in self.recipes:
            time_number=int(''.join(filter(str.isdigit,r['time'])))
            if time_number<=max_time:
                st.markdown(f"-----{rno}.{r['name']}-----")
                st.write(f"Time:{r['time']}")
                st.write(f"Difficulty:{r['difficulty']}")
                st.write("---")
                st.write("Steps:")
                for i, step in enumerate(r['steps'],1):
                    st.write(f"{i}.{step}")
                st.markdown("---")
                rno+=1
                found=True
        if not found:
          st.warning("No recipes found for the time given")
assistant=RecipeAssistant()
upload_file=st.file_uploader(
    "Upload an image of your fridge",
    type=["jpg","jpeg","png"]
)
if upload_file is not None:
    image=Image.open(upload_file)
    time_limit=st.number_input(
        "Enter the max cooking time(mins)",
        min_value=1,
        max_value=200,
        step=5
    )
    st.image(image,caption="Uploaded image",use_column_width=True)
    if st.button("Get Recipes 🍽️"):
        st.write("Calling Gemini... 👀")
        assistant.get_recipes_from_gemini(image)
        assistant.filter_recipes(time_limit)
