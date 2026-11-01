api_name = input("Please enter your api name: ")
statusCode = int(input("Please enter your status code: "))
response_time = float(input("Please enter your response time: "))
isAPiCritical = bool(input("Please enter your isAPICritical: "))


print(api_name)
print(statusCode)
print(response_time)
print(isAPiCritical)

print(type(api_name))
print(type(statusCode))
print(type(response_time))
print(type(isAPiCritical))

if response_time == 200:
    print("Status Code OK")
else:
    print("Status Code Not OK")