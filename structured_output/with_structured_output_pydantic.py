
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    max_output_tokens=1024,
    temperature=0.7,
)

# Schema for structured output
class Review(BaseModel):
    key_themes: list[str] = Field(
        description="All key themes discussed in the review"
    )

    summary: str = Field(
        description="A brief summary of the review"
    )

    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="Overall sentiment of the review"
    )

    pros: Optional[list[str]] = Field(
        default=None,
        description="List of advantages"
    )

    cons: Optional[list[str]] = Field(
        default=None,
        description="List of disadvantages"
    )

    name: Optional[str] = Field(
        default=None,
        description="Name of the reviewer"
    )

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say,
    it is an absolute powerhouse. The Snapdragon 8 Gen 3 processor is fast,
    the 5000mAh battery lasts a full day, and the 200MP camera takes
    stunning pictures.

    However, the phone is bulky, One UI has bloatware, and the $1,300
    price is expensive.

    Pros:
    - Powerful processor
    - Excellent camera
    - Long battery life
    - S-Pen support

    Review by Nitish Singh"""
)

print(result)
print(result.name)
print(result.sentiment)
print(result.key_themes)
