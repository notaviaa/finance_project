# Finance Project
If you're reading this README, welcome! I'm just a fellow unemployed undergraduate trying to put on different shoes in the financial world. Any supports or recommendations are fully welcome!

## What is this?
This is a simple environment that I use to backtest not only trading strategies but also stock manipulation and any detection programs. This project was start near Christmas 2025, and I've been slowly adding on more and more features to come.

## Any upcoming features to look forward too
I've in mind quite a lot of projects/algos that I want to try out, but first, here's a few of the upcoming "milestone" in mind in no chronological order:

1. Environment
   
    [a] Support stock fetching from all exchanges *(currently, we're only use vnstock - since my HSC internship duh)*

    [b] Simple Monte-Carlo simulation for analysis

    [c] More advanced Agent-based simulation for backtesting

2. Algorithms
    
    [a] Back-testing using traditional approach algos

    [b] Slightly more advance, LLM-assisted algos (to see how far I can push it before any limitations)

## Setup
Create and activate a virtual environment, then install in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

For notebooks, select the same virtual environment/kernel so imports resolve correctly.

Example imports:

```python
from fin_helpers import fetch_stock, mpt_sim
from fin_helpers.fetching import fetch_stock
from fin_helpers.finana import mpt_sim
```

## Contacts
For anything, and anything at all, feel free to contact me through one of the means (as attached below)

[LinkedIn](https://www.linkedin.com/in/huuanhduy-nguyen/) | [Email](andy.duynguyen.work@gmail.com) | 
