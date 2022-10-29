import pandas as pd
import numbers
import numpy as np


df = pd.read_csv('file.txt', sep=',')

x = [51483949, 46851488, 50994401, 47119728, 46431342, 37477356, 43257065, 39543154, 44982564, 37757813, 33753499, 38553146, 35732126, 34680458, 32749848, 30949417, 30711863, 31068833, 26843246, 28870939, 28516545, 27610325, 24850912, 23012646, 23820236, 20128124, 23512136, 21336697, 18718019, 18112907, 19906079, 16938942, 17870124, 17835909, 16248230, 16001107, 16195902, 19205178, 17041107, 14356181, 15417523, 14140274, 13763906, 14154937, 11625998, 11642959, 10932783, 10727148, 11557779, 11090085, 11248303, 10563757, 11194299, 10405832, 10806641, 9494246, 10365435, 9863480, 9849349, 9294505, 8916899, 9844246, 8524063, 9700609, 8642421, 7519496, 8007778, 8281732, 7473229, 7314773, 6787419, 6177950, 7309253, 6192235, 6398940, 6298598, 5914980, 6231066, 5766431, 5677796, 5479461, 5424444, 5190356, 4895242, 4612329, 4665760, 4819333, 4590590, 3946220, 3957099, 4254815, 3277388, 3771132, 3402818, 3524324, 2964749, 2878595, 2794445, 2414573, 2882481, 2963765, 2282704, 2253133, 2305171, 2028517, 2118521, 2107962, 2080862, 1991955, 1362142, 1314657, 1293153, 1187280, 730216, 743274, 633966, 569408, 456579, 331060]
y = [54179306, 54027487, 51815810, 51874024, 47558630, 47249585, 45510318, 44903225, 39701739, 44496122, 41128771, 39857145, 38454327, 37457971, 36408820, 34627652, 34049588, 33938221, 32969517, 33475870, 33696614, 30547580, 29611714, 27914536, 26177413, 26207977, 23893394, 21832143, 22673762, 22593590, 19659267, 20405317, 19603733, 19397998, 20017675, 17843908, 18001000, 22125249, 17564014, 17316449, 16767842, 17723315, 17597511, 16320537, 13859341, 13776698, 13352864, 12889576, 12356117, 12224110, 11655930, 11584996, 10913164, 11228821, 10384971, 11285869, 10270865, 10358074, 10549347, 10432860, 9441129, 9967308, 9952787, 9534954, 8939617, 7221365, 9038309, 8740472, 8848699, 8605718, 7529475, 6780744, 6781953, 6812341, 5489739, 6948392, 6630623, 6336392, 6430770, 5882261, 5540745, 5643453, 5434319, 5180829, 5302681, 5023109, 5579144, 5185288, 4736139, 4408581, 4030358, 3272996, 3744385, 3422794, 3233526, 3398366, 2780469, 2827377, 2695122, 2842321, 2750055, 2567012, 2705992, 2630296, 2388992, 2305825, 2093599, 2119844, 1850651, 1472233, 1326062, 1299469, 1251488, 836774, 782455, 627082, 647599, 533286, 372899]

x = df['Population_1980']

import matplotlib.pyplot as plt

x_random = np.random.normal(0, 2, 10000)

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.hist(x_random, bins='auto')
ax1.set_title('probability density (random)')
ax2.hist(x, bins='auto')
ax2.set_title('(your dataset)')
plt.tight_layout()

plt.show()



# if len(column_1) != len(column_2):
#     print(1)
#
#
# def is_all_ints(lst):
#     return all(isinstance(i, numbers.Number) for i in lst)
#
#
# if not (is_all_ints(column_1) and (is_all_ints(column_2))):
#     print(2)
