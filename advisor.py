def get_advice(text):

    text = text.lower()

    if "domino" in text or "dominos" in text:
        return """
Spending Analysis:
You spent money on food.

Savings Tip:
Reduce food delivery expenses.

Budget Recommendation:
Keep food spending below 20% of monthly income.
"""

    elif "uber" in text:
        return """
Spending Analysis:
You spent money on transport.

Savings Tip:
Use public transport when possible.

Budget Recommendation:
Allocate a fixed monthly transport budget.
"""

    else:
        return """
Spending Analysis:
Expense detected.

Savings Tip:
Track your spending regularly.

Budget Recommendation:
Follow the 50-30-20 budgeting rule.
"""