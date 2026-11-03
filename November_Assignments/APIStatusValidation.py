status_codes = [200, 201, 500, 404, 200, 503, 201]


success = 0
failed = 0

for status in status_codes:
    if status == 200 or status == 201:
        print("SUCCESS")
        success += 1
    else:
        print("FAILURE")
        failed += 1


print("Successful: ", success)
print("Failed: ", failed)