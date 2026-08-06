"""
Day 1: Advanced List Comprehensions & Dictionary Mappings.
Scenario: Ingesting raw order records, filtering high-value items, 
applying bulk discounts via dictionary lookup mappings, and generating a tax report.
"""

raw_transactions = [
    {"user_id": 101, "item": "Laptop", "amount": 1200, "status": "completed"},
    {"user_id": 102, "item": "Mouse", "amount": -25, "status": "completed"},  # Invalid: negative amount
    {"user_id": 103, "item": "Monitor", "amount": 300, "status": "pending"},  # Invalid: not completed
    {"user_id": 101, "item": "HDMI Cable", "amount": 15, "status": "completed"},
    {"user_id": 104, "item": "Keyboard", "amount": 80, "status": "completed"},
    {"user_id": 102, "item": "Desk Chair", "amount": 150, "status": "completed"},
]

#Filter with List Comprehension
valid_transactions = [
    x for x in raw_transactions 
    if x["status"] == "completed" and x["amount"] > 0
]

#Transform with Dictionary Comprehension
user_spending = {
    tx["user_id"]: sum(t["amount"] for t in valid_transactions if t["user_id"] == tx["user_id"])
    for tx in valid_transactions
}