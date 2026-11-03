responses = [
    "Transaction successful",
    "",
    "Transaction pending",
    "",
    "Transaction failed"
]


totalResponse = 0
emptyResponse = 0
nonEmptyResponse = 0

for response in responses:
    totalResponse += 1
    if response == "":
        emptyResponse += 1
    else:
        nonEmptyResponse += 1

print("Total: ",totalResponse)
print("Empty: ",emptyResponse)
print("NonEmpty: ",nonEmptyResponse)
print("NonEmpty Percentage: ",nonEmptyResponse/totalResponse*100)
