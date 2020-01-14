
# chi-squared test with similar proportions
from scipy.stats import chi2_contingency
from scipy.stats import chi2
from scipy import stats
import numpy as np

'''

a1 = [11,  17,  10,  1,  7]
a2 = [7,  17,  12,  1,  3]
a3 = [4,  10, 9, 6, 10]
a4 = [2,  14, 10, 18, 5]
a5 = [6, 26, 5, 4, 6]
a6 = [6, 18, 13, 3, 14]
a7 = [6, 18, 19, 1, 28]
a8 = [8, 20, 20, 0, 13]
'''

a1 = [19,19,25,3]
a2 = [17,23,10,1]
a3 = [36,41,49,17]
a4 = [16,37,34,9]
a5 = [14,25,21,4]
a6 = [38,38,18,12]
a7 = [53,24,13,22]
a8 = [40,19,8,14]

t_1 = np.array([a4, a1])
t_2 = np.array([a4, a2])
t_3 = np.array([a4, a3])
t_5 = np.array([a4, a5])
t_6 = np.array([a4, a6])
t_7 = np.array([a4, a7])
t_8 = np.array([a4, a8])

print('<<a4 and rest>>')
print(1, stats.chi2_contingency(t_1)[0:3])
print(2, stats.chi2_contingency(t_2)[0:3])
print(3, stats.chi2_contingency(t_3)[0:3])
print(5, stats.chi2_contingency(t_5)[0:3])
print(6, stats.chi2_contingency(t_6)[0:3])
print(7, stats.chi2_contingency(t_7)[0:3])
print(8, stats.chi2_contingency(t_8)[0:3])

print('-----------------')

a3_1 = np.array([a3, a1])
a3_2 = np.array([a3, a2])
a3_4 = np.array([a3, a4])
a3_5 = np.array([a3, a5])
a3_6 = np.array([a3, a6])
a3_7 = np.array([a3, a7])
a3_8 = np.array([a3, a8])

print('<<a3 and rest>>')

print(1, stats.chi2_contingency(a3_1)[0:3])
print(2, stats.chi2_contingency(a3_2)[0:3])
print(4, stats.chi2_contingency(a3_4)[0:3])
print(5, stats.chi2_contingency(a3_5)[0:3])
print(6, stats.chi2_contingency(a3_6)[0:3])
print(7, stats.chi2_contingency(a3_7)[0:3])
print(8, stats.chi2_contingency(a3_8)[0:3])

print('-----------------')

a1_2 = np.array([a1, a2])
a5_6 = np.array([a5, a6])
a7_8 = np.array([a7, a8])

print(6, stats.chi2_contingency(a1_2)[0:3])
print(7, stats.chi2_contingency(a5_6)[0:3])
print(8, stats.chi2_contingency(a7_8)[0:3])


print('-----------------')

print('<<a7 and rest>>')

a7_1 = np.array([a7, a1])
a7_2 = np.array([a7, a2])
a7_4 = np.array([a7, a4])
a7_5 = np.array([a7, a5])
a7_6 = np.array([a7, a6])
a7_3 = np.array([a3, a7])
a7_8 = np.array([a7, a8])

print(1, stats.chi2_contingency(a7_1)[0:3])
print(2, stats.chi2_contingency(a7_2)[0:3])
print(3, stats.chi2_contingency(a7_3)[0:3])
print(4, stats.chi2_contingency(a7_4)[0:3])
print(5, stats.chi2_contingency(a7_5)[0:3])
print(6, stats.chi2_contingency(a7_6)[0:3])
print(8, stats.chi2_contingency(a7_8)[0:3])


print('-----------------')

print('<<a8 and rest>>')

a8_1 = np.array([a8, a1])
a8_2 = np.array([a8, a2])
a8_3 = np.array([a3, a8])
a8_4 = np.array([a8, a4])
a8_5 = np.array([a8, a5])
a8_6 = np.array([a8, a6])
a8_7 = np.array([a8, a7])

print(1, stats.chi2_contingency(a8_1)[0:3])
print(2, stats.chi2_contingency(a8_2)[0:3])
print(3, stats.chi2_contingency(a8_3)[0:3])
print(4, stats.chi2_contingency(a8_4)[0:3])
print(5, stats.chi2_contingency(a8_5)[0:3])
print(6, stats.chi2_contingency(a8_6)[0:3])
print(8, stats.chi2_contingency(a8_7)[0:3])


print('-----------------')

print('<<a5 and rest>>')

a5_1 = np.array([a5, a1])
a5_2 = np.array([a5, a2])
a5_3 = np.array([a5, a3])
a5_4 = np.array([a5, a4])
a5_6 = np.array([a5, a6])
a5_7 = np.array([a5, a7])
a5_8 = np.array([a5, a8])

print(1, stats.chi2_contingency(a5_1)[0:3])
print(2, stats.chi2_contingency(a5_2)[0:3])
print(3, stats.chi2_contingency(a5_3)[0:3])
print(4, stats.chi2_contingency(a5_4)[0:3])
print(6, stats.chi2_contingency(a5_6)[0:3])
print(7, stats.chi2_contingency(a5_7)[0:3])
print(8, stats.chi2_contingency(a5_8)[0:3])

print('-----------------')

print('<<a6 and rest>>')


a6_1 = np.array([a6, a1])
a6_2 = np.array([a6, a2])
a6_3 = np.array([a3, a6])
a6_4 = np.array([a6, a4])
a6_5 = np.array([a6, a5])
a6_7 = np.array([a6, a7])
a6_8 = np.array([a6, a8])

print(1, stats.chi2_contingency(a6_1)[0:3])
print(2, stats.chi2_contingency(a6_2)[0:3])
print(3, stats.chi2_contingency(a6_3)[0:3])
print(4, stats.chi2_contingency(a6_4)[0:3])
print(5, stats.chi2_contingency(a6_5)[0:3])
print(7, stats.chi2_contingency(a6_7)[0:3])
print(8, stats.chi2_contingency(a6_8)[0:3])

print('-----------------')

print('<<a1 and rest>>')

a1_2 = np.array([a1, a2])
a1_3 = np.array([a3, a1])
a1_4 = np.array([a1, a4])
a1_5 = np.array([a1, a5])
a1_6 = np.array([a1, a6])
a1_7 = np.array([a1, a7])
a1_8 = np.array([a1, a8])


print(2, stats.chi2_contingency(a1_2)[0:3])
print(3, stats.chi2_contingency(a1_3)[0:3])
print(4, stats.chi2_contingency(a1_4)[0:3])
print(5, stats.chi2_contingency(a1_5)[0:3])
print(6, stats.chi2_contingency(a1_6)[0:3])
print(7, stats.chi2_contingency(a1_7)[0:3])
print(8, stats.chi2_contingency(a1_8)[0:3])


print('-----------------')

print('<<a2 and rest>>')

a2_1 = np.array([a2, a1])
a2_3 = np.array([a3, a2])
a2_4 = np.array([a2, a4])
a2_5 = np.array([a2, a5])
a2_6 = np.array([a2, a6])
a2_7 = np.array([a2, a7])
a2_8 = np.array([a2, a8])


print(1, stats.chi2_contingency(a2_1)[0:3])
print(3, stats.chi2_contingency(a2_3)[0:3])
print(4, stats.chi2_contingency(a2_4)[0:3])
print(5, stats.chi2_contingency(a2_5)[0:3])
print(6, stats.chi2_contingency(a2_6)[0:3])
print(7, stats.chi2_contingency(a2_7)[0:3])
print(8, stats.chi2_contingency(a2_8)[0:3])



