day = input("Enter day 'd' -> ")
month = input("Enter month 'm' -> ")
year = input("Enter year 'yyyy' -> ")

#day's basic number
if (day==7 or day==14 or day==21 or day==28):
    basicday=0
elif (day==1 or day==8 or day==15 or day==22 or day==29):
    basicday=1
elif (day==2 or day==9 or day==16 or day==23 or day==30):
    basicday=2
elif (day==3 or day==10 or day==17 or day==24 or day==31):
    basicday=3
elif (day==4 or day==11 or day==18 or day==25):
    basicday=4
elif (day==5 or day==12 or day==19 or day==26):
    basicday=5
elif (day==6 or day==13 or day==20 or day==27):
    basicday=6

#month's basic number
if (month==4 or month==07):
    basicmonth=0
elif (month==1 or month==10):
    basicmonth=1
elif (month==5):
    basicmonth=2
elif (month==8):
    basicmonth=3
elif (month==2 or month==3 or month==11):
    basicmonth=4
elif (month==6):
    basicmonth=5
elif (month==9 or month==12):
    basicmonth=6

#century's basic number
century=(year/100)+1

centtemp=century % 4
if (centtemp==0):
    basiccentury=0
elif (centtemp==3):
    basiccentury=2
elif (centtemp==2):
    basiccentury=4
elif (centtemp==1):
    basiccentury=6

#year's basic number
yeartemp=year-(year/100)*100

if (yeartemp==01 or yeartemp==07 or yeartemp==18 or yeartemp==24 or yeartemp==29 or yeartemp==35 or yeartemp==46 or
yeartemp==52 or yeartemp==57 or yeartemp==63 or yeartemp==74 or yeartemp==80 or yeartemp==85 or yeartemp==91):
    basicyear=0
elif (yeartemp==02 or yeartemp==8 or yeartemp==13 or yeartemp==19 or yeartemp==30 or yeartemp==36 or yeartemp==41 or
yeartemp==47 or yeartemp==58 or yeartemp==64 or yeartemp==69 or yeartemp==75 or yeartemp==86 or yeartemp==92 or yeartemp==97):
    basicyear=1
elif (yeartemp==03 or yeartemp==14 or yeartemp==20 or yeartemp==25 or yeartemp==31 or yeartemp==42 or yeartemp==48 or
yeartemp==53 or yeartemp==59 or yeartemp==70 or yeartemp==76 or yeartemp==81 or yeartemp==87 or yeartemp==98):
    basicyear=2
elif (yeartemp==04 or yeartemp==9 or yeartemp==15 or yeartemp==26 or yeartemp==32 or yeartemp==37 or yeartemp==43 or
yeartemp==54 or yeartemp==60 or yeartemp==65 or yeartemp==71 or yeartemp==82 or yeartemp==88 or
yeartemp==93 or yeartemp==99):
    basicyear=3
elif (yeartemp==10 or yeartemp==16 or yeartemp==21 or yeartemp==27 or yeartemp==38 or yeartemp==44 or yeartemp==49 or
yeartemp==55 or yeartemp==66 or yeartemp==72 or yeartemp==77 or yeartemp==83 or yeartemp==94 or yeartemp==00):
    basicyear=4
elif (yeartemp==05 or yeartemp==11 or yeartemp==22 or yeartemp==28 or yeartemp==33 or yeartemp==39 or yeartemp==50 or
yeartemp==56 or yeartemp==61 or yeartemp==67 or yeartemp==78 or yeartemp==84 or yeartemp==89 or yeartemp==95):
    basicyear=5
elif (yeartemp==06 or yeartemp==12 or yeartemp==17 or yeartemp==23 or yeartemp==34 or yeartemp==40 or yeartemp==45 or
yeartemp==51 or yeartemp==62 or yeartemp==68 or yeartemp==73 or yeartemp==79 or yeartemp==90 or yeartemp==96):
    basicyear=6

#leap year correction
if year % 4 == 0 and year %100 != 0 or year % 400 == 0:
    if (month==03 or month==12):
        basicmonth=basicmonth+1
    if (yeartemp==00):
        basiccentury=0


result = basicyear + basiccentury + basicmonth + basicday
result1 = result % 7

if result1==0:
    print "Sunday"
elif result1==1:
    print "Monday"
elif result1==2:
    print "Tuesday"
elif result1==3:
    print "Wednesday"
elif result1==4:
    print "Thursday"
elif result1==5:
    print "Friday"
else:
    print "Saturday"



#http://www.wikihow.com/Know-the-Day-of-the-Week-for-Any-Day-of-Any-Year
