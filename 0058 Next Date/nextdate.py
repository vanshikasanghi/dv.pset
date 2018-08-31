day = input("Enter Day : ")
month = input("Enter Month : ")
year = input("Enter Year : ")

if(month == '12') and (day=='31') : #for last day of the year
	day = '1'
	month = '1'
	year = int(year)+1
	print(str(day)+" "+str(month)+" "+str(year))
#for all the last date of months with 31 days
elif(month == '1' or month == '3' or month == '5' or month == '7' or month == '8' or month == '10') and (day == '31') :
	day = '1'
	month = int(month)+1
	print(str(day)+" "+str(month)+" "+str(year))
#for all the last date of months with 30 days
elif(month == '4' or month == '6' or month == '9' or month == '11') and (day=='30') :
	day = '31'
	print(str(day)+" "+str(month)+" "+str(year))

elif(month == '2') and (day == '28') and (int(year)%4 == 0) and (int(year)%400 == 0) and (int(year)%100 !=0) : #for leap year
	day = '29'
	print(str(day)+" "+str(month)+" "+str(year))

elif(month == '2') and (day =='28') and (int(year)%4 != 0) and (int(year)%400 !=0) : #for non-leap year
	day = '1'
	month = '3'
	print(str(day)+" "+str(month)+" "+str(year))

else :
	day = int(day)+1
	print(str(day)+" "+str(month)+" "+str(year)) #for usual days



