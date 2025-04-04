from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class InputModel(BaseModel):
    pot_size: float = Field(..., gt=0)
    call_amount: float = Field(..., gt=0)
    current_bet: float = Field(..., ge=0)
    hand_equity: Optional[float] = Field(None, ge=0.0, le=1.0)

class OutputModel(BaseModel):
    pot_odds_percent: str
    is_call_profitable: str
    break_even_equity: str

@app.post("/execute", response_model=OutputModel)
def calculate_pot_odds(input_data: InputModel):
    """
    Calculate pot odds, determine if a call is profitable, and calculate break-even equity.
    
    Parameters:
    - input_data: InputModel
    
    Returns:
    - OutputModel: Calculated pot odds, profitability of the call, and break-even equity.
    """
    try:
        # Calculate pot odds
        pot_odds = input_data.call_amount / (input_data.pot_size + input_data.call_amount + input_data.current_bet)
        pot_odds_percent = f"{pot_odds * 100:.2f}%"
        
        # Calculate break-even equity
        break_even_equity = input_data.call_amount / (input_data.pot_size + input_data.call_amount)
        break_even_equity_str = f"{break_even_equity * 100:.2f}%"
        
        # Determine if call is profitable
        if input_data.hand_equity is not None:
            is_call_profitable = "Yes" if input_data.hand_equity > break_even_equity else "No"
        else:
            is_call_profitable = "Unknown"
        
        return OutputModel(
            pot_odds_percent=pot_odds_percent,
            is_call_profitable=is_call_profitable,
            break_even_equity=break_even_equity_str
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

# Example usage:
# curl -X 'POST' \
#   'http://127.0.0.1:8000/execute' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "pot_size": 100,
#   "call_amount": 20,
#   "current_bet": 10,
#   "hand_equity": 0.5
# }'
