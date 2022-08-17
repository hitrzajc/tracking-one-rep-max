from math import e
import matplotlib.pyplot as plt

lifts = ["squat.txt","bench.txt","deadlift.txt"]

def get_data(txt):
    with open(txt) as f:
        data = list(map(float,(' '.join(f.readlines())).split()))
        return data

fig, axs = plt.subplots(len(lifts), 1)

#weight reps
def f1(w, r): #Epley S=1% B=0.03% D=10%
    return w*(r/30+1)
f1.name = "Epley"

def f2(w, r): #Brzycki S=4% B=0.05% D=10%
    return w*36/(37 - r)
f2.name="Brzycki"

def f3(w, r): #lombardi S=3% B=0.05% D=11%
    return w*r**(1/10)
f3.name = "Lombardi"

def f4(w, r): #watham S=0.8% B=0.02% D=9%
    return 100*w/(48.8+53.8*e**(-0.075*r))
f4.name = "Watham"
funs = [f1,f2,f4]

for i_lift in range(len(lifts)):
    lift = lifts[i_lift]
    data = get_data(lift)
    y = [[f(data[i],data[i+1]) for i in range(0, len(data), 2)] for f in funs]
    x = [i+1 for i in range(len(data)//2)]
    # for i in y:
    #     plt.plot(x,i)
    for i in y:
        axs[i_lift].plot(x,i)
    # axs[i_lift].plot(x,y)
    axs[i_lift].set_ylabel("kg")
    axs[i_lift].grid(True)
    axs[i_lift].set_title(lift)

    if(i_lift == len(lifts)-1):
        axs[i_lift].set_xlabel("frequency")
    

    
#plt.legend(["f"+str(i+1) for i in range(len(funs))])
plt.legend([f.name for f in funs])
plt.show()

