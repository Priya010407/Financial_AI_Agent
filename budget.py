def get_budget(category):

    if category == "Food":
        return "Recommended Budget: Keep food expenses below ₹5000 per month."

    elif category == "Transport":
        return "Recommended Budget: Keep transport expenses below ₹3000 per month."

    elif category == "Shopping":
        return "Recommended Budget: Avoid spending more than 20% of your income on shopping."

    else:
        return "Recommended Budget: Follow the 50-30-20 budgeting rule."