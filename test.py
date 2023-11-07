# def divide(a,b):
#     try:
#         print(a//b)
#     except Exception as e:
#         msg={"error":e}
        
#         print(msg)
#         print(e)
# divide(5,2)
# divide(5,0)

rsms=["x123","x456","x789"]
rsms_new=""
for i in rsms:
    rsms_new+=i
    rsms_new+=" "
print (rsms_new)
print(type(rsms_new))