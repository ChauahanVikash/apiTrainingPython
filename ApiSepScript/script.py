import requests 

# name = input("Enter Name : ")
# age = int(input("Age : "))
# number = int(input("Enter random number : "))
name = 'Vikash'
age = 24
number = 12

res1 = requests.post('http://127.0.0.1:5001/' , json={'age' : age , 'number' : number})
##print(res1.status_code)
##print(res1.json())
val1 = res1.json()['ans1'] 
if(res1.status_code == 200):
    res2 = requests.post('http://127.0.0.1:5002/' , json={'number' : val1})
    if(res2.status_code == 200):
        ans = res2.json()['ans2']
        print(f'Output1 : {ans}')
    else:
       print( f"Some Error Occured {res1.status_code}" ) 
else : 
    print( f"Some Error Occured {res1.status_code}" )

