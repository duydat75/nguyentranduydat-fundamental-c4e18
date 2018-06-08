import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
# 1 Prepare data
labels = ['ios', 'android', 'web','react native']
colors = ['pink','violet','red','blue']
values = [20,15,40,25]
explode = [0,2,0,0.2]
# 2 Plot 
pyplot.pie(values, labels=labels, colors= colors,explode= explode)
pyplot.axis ("equal")

# 3 Show
pyplot.show()