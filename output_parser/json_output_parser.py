""" 
Using JSON Output Parser with Prompt Templates
1. Format Instructions: When using JsonOutputParser, you pass format instructions into your prompt template so the LLM knows how to structure its output.
It fill before the run time because of get_format_instructions() function

2. get_format_instructions(): Instead of writing output formatting rules manually, calling parser.get_format_instructions() generates instructions (e.g., "Return a JSON object") automatically.

3. Partial Variables: These formatting instructions are passed as a partial_variable because they are fixed before runtime rather than filled in dynamically by the user.
"""
"""
In Json Output Parser :

format_instruction: isme hum phele hi bta dete hai ki hume output kaisa chahiye hoga LLM se .
ye ouput hume humara parser btata hai jab hum parser.get_format_instructions() ko call krenge

hume ise partial_variables isiliye bol rahe hai kyuki ye run time pr fill nhi ho raha user nhi bta raha hai ye run time se phele hi fill ho jaa raha hai with the help of parser.get_format_instructions() fumction call.

JSON Output Parser hume flexibility provide nhi krta hai ki hum khud se output structure or Schema define kre like fact: 1).......   2)....... 3)......
Output structure or Schema decide khud LLM krta hai .

Is Limitation ko overcome krne k liye StructuredOutPutParser ka use krte hai.
"""

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

