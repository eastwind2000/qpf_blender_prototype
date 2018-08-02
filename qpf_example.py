


from pylab import *

ens1 = np.array([ 5.  ,  6.  ,  6.  ,  7.  ,  9.72,  9.89, 10.15, 10.16, 10.26,  10.49,  10.56, 10.86])

ens2 = np.array([ 9.18,  9.42,  9.45,  9.91,  9.96, 10.3 , 10.45, 10.55, 11.08,  11.12, 11.54, 11.74])

combine = np.append(ens1, ens2)


x=arange(len(ens1))

# plot(x, ens1, 'b+', x, ens2, 'rx')
#
# p1 = hist(ens1, cumulative=True)[1]
#
# print(p1)
#
# p2 = hist(ens2, cumulative=True)[1]
#
# print(p2)
#
# px = hist(combine, cumulative=True)[1]
#
# print(px)

p1=np.percentile(ens1, [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99], interpolation="linear")

print(["cdf1: ", p1])

p2=np.percentile(ens2, [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99], interpolation="linear")

print(["cdf2: ", p2])

px=np.percentile(combine, [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99], interpolation="linear")

print(["combine: ", px])

plot(p1, color="green", linewidth=2)
plot(p2, color="red", linewidth=2)

plot(p1*0.5+p2*0.5, color="black", linewidth=2, linestyle="--")

plot(px, color="black", linewidth=5)



