import numpy as np

# Population Data
pop_x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,
                  120, 130, 140, 150, 160, 170, 180, 190])
y_poptime1 = np.array([0.00616650001029484, 0.011956300004385412, 0.01471020000462886, 0.019692700006999075, 0.023833500003092922, 0.030551200004993007, 0.03135869999823626, 0.03507629998784978, 0.04222410000511445, 0.049608399989665486,
                       0.05220249999547377,  0.053554199999780394, 0.062411799997789785, 0.06658850000530947, 0.07323039999755565, 0.07933090000005905, 0.09272420000343118, 0.09640710000530817,  0.10696920000191312])
y_poptime2 = np.array([0.0077791000076103956, 0.01385149999987334, 0.014138200000161305, 0.018599599992739968, 0.02611629999591969, 0.027193699992494658, 0.031047600001329556, 0.038699099997757, 0.042404400010127574,
                       0.04578169999876991, 0.05234270000073593, 0.06107429999974556, 0.06725039999582805, 0.06886040000244975, 0.09148370000184514, 0.08048869999765884,  0.09144770000420976, 0.10549810000520665, 0.10681789999944158])
y_poptime3 = np.array([0.006833999999798834, 0.01257140000234358, 0.01663630000257399, 0.0181773000076646, 0.025333500001579523,  0.02763039999990724, 0.03188709999085404, 0.035916299995733425, 0.040313700010301545,
                       0.050989199997275136, 0.05216110000037588, 0.05669290000514593, 0.06161230000725482, 0.06751530000474304, 0.07699280000815634, 0.07769140000164043, 0.08904900000197813, 0.09335410001222044, 0.1011992999992799])

y_poplen1 = np.array([8.090169943749475, 8.090169943749475, 7.854101966249685, 7.854101966249685, 7.854101966249685, 8.090169943749475, 7.854101966249685, 7.854101966249685, 7.854101966249685,
                      7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685,  7.854101966249685, 7.854101966249685, 7.854101966249685])
y_poplen2 = np.array([8.090169943749475, 8.090169943749475,  7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685,
                      7.854101966249685,  7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685])
y_poplen3 = np.array([8.47213595499958, 7.854101966249685, 7.854101966249685, 8.090169943749475, 7.854101966249685, 8.090169943749475, 8.090169943749475, 7.854101966249685, 7.854101966249685,
                      7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685])

# Mutation Rate Data
mut_x = np.array([0.01, 0.03, 0.05, 0.075, 0.1, 0.125,
                 0.15, 0.175, 0.2, 0.225, 0.25])
y_muttime1 = np.array([0.0470760999887716, 0.04471499999635853, 0.049608399989665486, 0.0459368000010727, 0.04376980000233743,
                      0.04282909999892581, 0.043880700002773665, 0.047473799997533206, 0.04511300000012852,  0.043951399995421525, 0.04372079999302514])
y_muttime2 = np.array([0.043547199995373376, 0.045521200001530815, 0.04578169999876991, 0.04764200000499841, 0.04610500000126194,
                      0.04340270000102464, 0.04339990000153193, 0.046258800000941847, 0.04544690000329865, 0.057841399997414555, 0.043892600006074645])
y_muttime3 = np.array([0.04461050000099931, 0.043503799999598414, 0.050989199997275136, 0.050113299999793526, 0.04568049999943469,
                      0.04297910000605043,  0.049148300000524614, 0.04811409999820171, 0.047025600004417356, 0.04466880000109086,  0.04302770001231693])
y_mutlen1 = np.array([7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685,
                     7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685])
y_mutlen2 = np.array([7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685,
                     7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685])
y_mutlen3 = np.array([7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685,
                     7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685])


# Chromosome Length Data
chr_x = np.array([9, 10, 11, 12, 13, 14, 15])
# y_chrtime1 = np.array([0.037207400004263036,  0.04357559999334626,
#                       0.042780699994182214, 0.049608399989665486, 0.04699919999984559])
# y_chrtime2 = np.array([0.03887839999515563, 0.04155429999809712,
#                       0.05099519999930635, 0.04578169999876991, 0.046034300001338124])
# y_chrtime3 = np.array([0.038601699998253025, 0.04056139999011066,
#                       0.04782399999385234, 0.050989199997275136, 0.045547699999588076])
# y_chrlen1 = np.array([7.854101966249685, 7.854101966249685,
#                      7.854101966249685, 7.854101966249685, 7.854101966249685])
# y_chrlen2 = np.array([7.854101966249685, 7.854101966249685,
#                      7.854101966249685, 7.854101966249685, 7.854101966249685])
# y_chrlen3 = np.array([7.854101966249685, 7.854101966249685,
#                      7.854101966249685, 7.854101966249685, 7.854101966249685])

y_chrtime1 = np.array([0.06866460001037922, 0.0986024999874644, 0.11269170000741724,
                      0.10791199999221135, 0.11335420000250451, 0.1167762999975821, 0.11936470000364352])
y_chrtime2 = np.array([0.06884980000904761, 0.0733236000087345, 0.07945190000464208,
                      0.09544019999157172, 0.11448799999197945, 0.13382049999199808, 0.11692429998947773])
y_chrtime3 = np.array([0.061900099986814894, 0.07415600000240374, 0.0886224999994738,
                      0.09546759999648202, 0.11025030000018887, 0.10554080001020338, 0.12488879999727942])

y_chrlen1 = np.array([7.854101966249685, 7.854101966249685, 7.854101966249685,
                     7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685])
y_chrlen2 = np.array([7.854101966249685, 7.854101966249685, 7.854101966249685,
                     7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685])
y_chrlen3 = np.array([7.854101966249685, 7.854101966249685, 7.854101966249685,
                     7.854101966249685, 7.854101966249685, 7.854101966249685, 7.854101966249685])


# Stop Criteria Data
st_x = np.array([2, 3, 4, 5, 6])
y_sttime1 = np.array([0.03402829999686219, 0.041173899997374974, 0.05260619999899063,
                     0.05719219999446068, 0.07571920000191312])
y_sttime2 = np.array([0.033546700004080776, 0.04666720000386704, 0.04991870000958443,
                     0.060200399995665066, 0.06383090000599623])
y_sttime3 = np.array([0.031807899998966604, 0.039492999989306554,  0.05179890000727028,
                     0.06123989999468904, 0.07695039999089204])
y_stlen1 = np.array([7.854101966249685, 7.854101966249685, 7.854101966249685,
                     7.854101966249685, 7.854101966249685])
y_stlen2 = np.array([7.854101966249685, 7.854101966249685, 7.854101966249685,
                     7.854101966249685, 7.854101966249685])
y_stlen3 = np.array([7.854101966249685, 7.854101966249685, 7.854101966249685,
                     7.854101966249685, 7.854101966249685])
