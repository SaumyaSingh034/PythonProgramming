responses = [
    "Your payment was successful",
    "Your transaction is pending",
    "",
    "Transaction failed",
    "Refund processed"
]

for response in responses:
    if response == "":
        print("Failed: Empty Response")
    else:
        print("PASSED:", response)