mean = float(input("what is the mean"))
sd = float(input("what is the standard deviation"))

up = mean + sd
down = mean - sd
upp = mean +sd +sd
downn = mean -sd -sd
uppp = mean + sd +sd+sd
downnn = mean -sd -sd - sd



print("68 percent of the data lies between " + str(up) + "and" + str(down) +"\n")
print("95 percent of the data lies between " + str(upp) + "and" + str(downn) +"\n")
print("99.7 percent of the data lies between " + str(uppp) + "and" + str(downnn) +"\n")
