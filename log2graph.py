import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('teraterm.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    counter = 0
    for line in lines:
        if len(line) > 1:
            y = int(line[6:])
            ys.append(y)
            xs.append(counter)
            counter += 1
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
