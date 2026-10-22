"""
This example demonstrates how to use the `with_structured_output` method with a TypedDict schema to extract structured information from a product review. The `Review` TypedDict defines the expected structure of the output, including key themes, summary, sentiment, pros, cons, and the reviewer's name. The model processes the input review text and returns the structured data according to the defined schema.
But It never ensures the Data validation. It will not give error even if the value types are not matching with the defined types.
For Data validation, you can use Pydantic models instead of TypedDict. Pydantic provides data validation and type checking, ensuring that the output conforms to the expected types and structure.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    max_output_tokens=1024,
    temperature=0.7,
    )

# Schema for structured output
class Review(TypedDict):
    """SIMPLE
    summary: str
    sentiment: str
    """
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]

    summary: Annotated[str, "A brief summary of the review"]

    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]

    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]

    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]

    name: Annotated[Optional[str], "Write the name of the reviewer"]

structured_model = model.with_structured_output(Review)


result = structured_model.invoke(
    """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware. The $1,300 price tag is also a hard pill to swallow.

Pros:
- Insanely powerful processor
- Stunning 200MP camera
- Long battery life with fast charging
- S-Pen support

Review by Nitish Singh"""
)
print(result)
print(result['name'])

