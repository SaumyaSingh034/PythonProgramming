status_code = [200,201,500,409,404,400,201,200]

for status in status_code:
    if status == 500:
        print("Internal Server Failure")
        break

    print("Checking : ",status)


status_codes = [200, 0, 201, 0, 500]

for status in status_codes:

    if status == 0:
        continue

    print("Valid status:", status)