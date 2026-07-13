from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import AIMMessage, HumanMessage, SystemMessage, ToolMessage


@tool
def get_product_price(product_name: str) -> float:
    """Lookup price for the product"""
    print(f"Executing get_product_price for: {product_name}")
    price_catalogue = {"keyboard": 254, "laptop": 550, "headphone": 120}
    return price_catalogue.get(product_name, 0)


@tool
def apply_discount(price: float, discount_tier: str) -> float:
    discount_catalog = {"Gold": 0.25, "Silver": 0.15, "Bronze": 0.10}
    dicount = discount_catalog.get(discount_tier, 0)
    price = price - (price * dicount)


load_dotenv()

# It is a good practice to inititaliza variables on top rather than spreading across files.
chat_model = "qwen3.5:0.8b"
chat_model_provider = "ollama"
chat_model_iterations = 10
chat_model_temperature = 0.3

chat = init_chat_model(
    model=chat_model,
    model_provider=chat_model_provider,
    temperature=chat_model_temperature,
)
