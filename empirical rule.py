mean = float(input("what is the mean of your data set"))
sd = float(input("what is the standard deviationof your data set"))

up = mean + sd
down = mean - sd
upp = mean +sd +sd
downn = mean -sd -sd
uppp = mean + sd +sd+sd
downnn = mean -sd -sd - sd



print("\n68 percent of the data lies between " + str(down) + " and " + str(up) +"\n")
print("95 percent of the data lies between " + str(downn) + " and " + str(upp) +"\n")
print("99.7 percent of the data lies between " + str(downnn) + " and " + str(uppp) +"\n")
