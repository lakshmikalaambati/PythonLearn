print("What is Today date")
todaydate=input()
print("Enter Breakfast cal")
breakfastcal=int(input())

print("Enter lunch cal")
lunchcal=int(input())

print("Enter dinner cal")
dinnercal=int(input())

print("Enter snacks Cal")
snackscal=int(input())

totalcal=breakfastcal+lunchcal+dinnercal+snackscal
print("calarie content for "+str(todaydate)+"is " + str(totalcal))
