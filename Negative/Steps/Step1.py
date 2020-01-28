import pandas as pd

pid = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/IDs/Protein_ID.csv')
rid = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/IDs/RNA_ID.csv')
pid.reset_index(inplace=True)
rid.reset_index(inplace=True)
inp = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/RPI_2333_conv.csv')

inp = inp.merge(pid,left_on = 'protein_seq',right_on = 'Protein',how='inner')

inp = inp.merge(rid,left_on = 'rna_seq',right_on = 'RNA',how='inner')

grid = pd.DataFrame(index = pid.index,columns=rid.index)

# inp[['index_x','index_y']]

for i in inp.index :
	x = inp.iloc[i]['index_y']
	y = inp.iloc[i]['index_x']
	grid[x][y] = -1

grid.to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/Pos_grid.csv')