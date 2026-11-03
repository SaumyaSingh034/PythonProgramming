status_code = [200,201,500,404,200]

#for Loop
for status in status_code:
    if(status == 200 or status == 201):
        print("API Passed")
    else:
        print("API Failed")