d={}
l1=['HTTP','HTTPS','FTP','DNS']
l2=[80,433,20,53]
for i,j in zip (l1,l2):
    d[i]=j
print(d)

