import pandas as pd;

df = pd.read_csv(' t-weight.csv', names=['A', 'B'])
data = df.values.tolist()
c1_tot = 0
c2_tot = 0
r1_tot = 0
r2_tot = 0
for i in range(2):
    for j in range(2):
        if (i == 0):
            r1_tot = r1_tot + (int)(data[i][j])
        if (i == 1):
            r2_tot = r2_tot + (int)(data[i][j])
        if (j == 0):
            c1_tot = c1_tot + (int)(data[i][j])
        if (j == 1):
            c2_tot = c2_tot + (int)(data[i][j])

print("row 1 total:" + r1_tot)
print("row 2 total:" + r2_tot)
print("col 1 total:" + c1_tot)
print("col 2 total:" + c2_tot)

for i in range(2):
    for j in range(2):
        if (i == 0):
            print("t-weight for data" + (str)(data[i][j]) + "is--->" + (float)(((data[i][j]) / r1_tot)) * 100)
        if (i == 1):
            print("t-weight for data" + (str)(data[i][j]) + "is--->" + (float)(((data[i][j]) / r2_tot)) * 100)
        if (j == 0):
            print("d-weight for data" + (str)(data[i][j]) + "is--->" + (float)(((data[i][j]) / c1_tot)) * 100)
        if (j == 1):
            print("d-weight for data" + (str)(data[i][j]) + "is--->" + (float)(((data[i][j]) / c2_tot)) * 100)