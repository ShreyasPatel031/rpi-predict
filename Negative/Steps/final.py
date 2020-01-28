import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

inp = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/RPI_2333_conv.csv',index_col=0)

pid = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/IDs/Protein_ID.csv')
rid = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/IDs/RNA_ID.csv')

grid = pd.DataFrame(0,index = pid.index,columns=rid.index)

pos = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/Pos_grid.csv',index_col=0)
pos.fillna(0,inplace=True)
pos.index = pid.index
pos.columns = rid.index

self_p = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/Self_p.csv')
self_r = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/Self_r.csv')
self_r.fillna(0,inplace=True)
self_p.fillna(0,inplace=True)

r_map = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/RNA_map.csv',index_col=0)
p_map = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/Protein_map.csv',index_col=0)
r_map.fillna(0,inplace=True)
p_map.fillna(0,inplace=True)
r_map.index = pid.index
r_map.columns = rid.index
p_map.index = pid.index
p_map.columns = rid.index




pself_cut = 500
rself_cut = 3000

pidx = self_p[ self_p > pself_cut].dropna().index.tolist()
ridx = self_r[ self_r > rself_cut].dropna().index.tolist()

len(pidx)
len(ridx)

# y=[]
# x = list(range(0, int(self_p.max()[0]),50))
# for i in range(0, int(self_p.max()[0]),50):
# 	pidx = self_p[ self_p > i ].dropna().index.tolist()
# 	y.append(len(pidx))

# plt.plot(x,y)
# plt.show()

# y=[]
# x = list(range(0,int(self_r.max()[0]),50))
# for i in range(0,int(self_r.max()[0]),50):
# 	ridx = self_r[ self_r > i].dropna().index.tolist()
# 	y.append(len(ridx))

# plt.plot(x,y)
# plt.show()


pos.iloc[pidx] = -1
pos.iloc[:,ridx] = -1 


r_cut = 0 #20
p_cut = 0 #60

# fin = {'Protein':[],'RNA':[]}
# cutoff = pd.DataFrame(index = list(range(0,100,20)),columns = list(range(0,100,20)))
# for r in cutoff.index:
# 	for c in cutoff.columns:
# 		cnt = 0
# 		# fin = {'Protein':[],'RNA':[]}
# 		pos = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/Pos_grid.csv',index_col=0)
# 		pos.fillna(0,inplace=True)
# 		pos.index = pid.index
# 		pos.columns = rid.index
# 		pos.iloc[pidx] = -1
# 		pos.iloc[:,ridx] = -1 
# 		print(r,c)
# 		for i in grid.columns:
# 			for j in grid.index:
# 				if r_map[i][j] > c :
# 					pos[i][j] = -1
# 				if p_map[i][j] > r :
# 					pos[i][j] = -1
# 				if( pos[i][j] >= 0 ):
# 					cnt += 1
# 					fin['Protein'].append(pid['Protein'].iloc[j])
# 					fin['RNA'].append(rid['RNA'].iloc[i])
					
# 		cutoff[c][r] = [cnt,len(pd.Series(fin['Protein']).unique()),len(pd.Series(fin['RNA']).unique())]
# 		print(cutoff)





fin = {'Protein':[],'RNA':[]}
pos = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/Pos_grid.csv',index_col=0)
pos.fillna(0,inplace=True)
pos.index = pid.index
pos.columns = rid.index
pos.iloc[pidx] = -1
pos.iloc[:,ridx] = -1 
fin = {'Protein':[],'RNA':[]}
for i in grid.columns:
	for j in grid.index:
		if r_map[i][j] > 0 :
			pos[i][j] = -1
		if p_map[i][j] > 0 :
			pos[i][j] = -1
		if( pos[i][j] >= 0 ):
			fin['Protein'].append(pid['Protein'].iloc[j])
			fin['RNA'].append(rid['RNA'].iloc[i])
		

fin = pd.DataFrame(fin)
y=[]
for i in range(1000):
	test = fin.sample(n=len(inp),random_state=i).reset_index()[['Protein','RNA']]
	y.append( len(test['RNA'].unique()) + len(test['Protein'].unique()) )

fin.sample(n=len(inp),random_state = np.asarray(y).argmax() ).reset_index()[['Protein','RNA']].to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Negative_2333.csv',index=False)
# print(pos[pos>=0].count().sum(),p_del,r_del)
