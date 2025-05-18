from langchain_core.pydantic_v1 import BaseModel,Field
from typing import Optional


class Expenses(BaseModel):
    amount:Optional[str]=Field(title="expenses",description="Expenses made in the transaction")
    merchant:Optional[str]=Field(title="merchant",description="Merchant name whom the transaction has been made")
    currency:Optional[str]=Field(title="currency",description="Currency of the transaction")