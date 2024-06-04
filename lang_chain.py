from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain  # For creating and managing chains of language model calls
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

import os
os.environ['OPENAI_API_KEY'] = '' #secret openai api key to be added

llm = OpenAI(temperature=0.6)  # 0 = least creative/risky   1 = most creative/risky

def generate_restaurant_name_and_menuitems(cuisine):
    llm = OpenAI(temperature=0.6)

    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template= "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain( llm=llm, prompt=prompt_template_name, output_key="restaurant_name" )

    prompt_template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template= """Return some food menu item names for {restaurant_name} as a single list separated with commas only."""
    )

    food_items_chain = LLMChain( llm=llm, prompt=prompt_template_items, output_key="menu_items" )

    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine':cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_menuitems("Pakistani"))