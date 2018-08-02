


from pylab import *

from scipy import stats

import pandas as pd



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

quantile = np.array( [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99] )

p1=np.percentile(ens1, quantile, interpolation="linear")  # percentile of ens1

print(["cdf1: ", p1])

p2=np.percentile(ens2, quantile, interpolation="linear") # percentile of ens2

print(["cdf2: ", p2])

px=np.percentile(combine, quantile, interpolation="linear") # percnetile of combined of ens1 and ens2

print(["combine: ", px])

plot(p1, color="green", linewidth=2, label="ens1 percentile")
plot(p2, color="red", linewidth=2, label="ens2 percentile")

plot(p1*0.5+p2*0.5, color="black", linewidth=2, linestyle="--", label="average precentile")

plot(px, color="black", linewidth=5, label="combine percentile")

plt.legend()

# setup new datalist using p1, p2

ens3 = np.append(p1, p2)

# reverse to probability space of dataset-ens1

# p1        = [ pi,                          ]
# quantile  = [ 5, 10, 20, 30, ..., etc      ]
# useing linear interpolation

p_ens3 = np.interp( ens3, p1, quantile, left=0, right=100 )

print(ens3)
print(p_ens3)





