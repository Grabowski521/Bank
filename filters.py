import re
from datetime import datetime

def filter_transactions_by_description(transactions, search_string):
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]

def categorize_transactions(transactions, categories):
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
                break
    return category_count