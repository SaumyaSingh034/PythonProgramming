api_name = input("Please enter your api name: ")
statusCode = int(input("Please enter your status code: "))
response_time = float(input("Please enter your response time: "))
isAPiCritical = input("Is this API critical? (yes/no): ").strip().lower() == "yes"


print(api_name)
print(statusCode)
print(response_time)
print(isAPiCritical)

print(type(api_name))
print(type(statusCode))
print(type(response_time))
print(type(isAPiCritical))

if statusCode == 200:
    print("Status Code OK")
else:
    print("Status Code Not OK")

api_name = input("Please enter your API name: ")
status_code = int(input("Please enter your status code: "))
response_time = float(input("Please enter your response time: "))

is_api_critical = (
    input("Is this API critical? (yes/no): ").strip().lower() == "yes"
)

print("\nAPI DETAILS")
print(api_name)
print(status_code)
print(response_time)
print(is_api_critical)

print("\nDATA TYPES")
print(type(api_name))
print(type(status_code))
print(type(response_time))
print(type(is_api_critical))

if status_code == 200:
    print("API TEST PASSED")
else:
    print("API TEST FAILED")