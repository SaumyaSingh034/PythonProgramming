ai_responses = [
    "Payment successful",
    "Payment pending",
    "",
    "Unknown transaction",
    "Payment successful"
]

TotalCount = 0
NonEmptyResponseCount = 0
EmptyResponseCount = 0
for response in ai_responses:
    if response == "":
        EmptyResponseCount +=1
    else:
        NonEmptyResponseCount +=1
    TotalCount += 1

print("Total Count : ",TotalCount)
print("NonEmptyCount : ",NonEmptyResponseCount)
print("EmptyCount : ",EmptyResponseCount)
