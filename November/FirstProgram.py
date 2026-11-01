from http.client import responses

teat_name="Login API Test"
status_code = 200
response_time = 1.25

print("Test Name", teat_name)
print("Status Code", status_code)
print("Response Time", response_time)

if status_code == 200:
    print("Status Code OK")

else:
    print("Status Code Not OK")