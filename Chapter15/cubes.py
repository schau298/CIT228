import matplotlib.pyplot as plt

cubed=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    cubed.append(num*num*num) 
ax1 = plt.subplot(1,2,1)    
ax1.plot(inputVal,cubed, marker='H', lw='3.0', ls='--', c='red')
plt.title("Cubed Numbers")
plt.ylabel("Values Squared")
plt.xlabel("Input Values")
plt.grid()


raised=[]
inputVal2=[1,2,3,4,5]
for num2 in inputVal2:
    raised.append(num2**2) 
ax2 = plt.subplot(1,2,2)    
plt.style.use("seaborn-paper")
ax2.plot(inputVal2,raised,color="orange",lw="4",marker="D")
plt.title("Numbers Raised", color="orange")  
plt.ylabel("Second Power")
plt.xlabel("Input Values")
plt.grid()

plt.suptitle("Numbers Time",c="blue",fontfamily="Arial", fontsize="18")
plt.subplots_adjust(top=.9,wspace=1.5)
plt.show()