import pandas as pd


val = ['2713','2333','380']

op = pd.DataFrame(index = ['accuracy','precision' ,'recall' ,'f1','roc_auc'],columns = ['Scores_'+i for i in val] )

inp = [ pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Scores/Scores_'+ i +'.csv')  for i in val ]

for i in range(len(val)):
	op['Scores_'+val[i]] = [ '{:.5f}({:.5f})'.format( float(inp[i].mean()['test_'+j]) , float(inp[i].std()['test_'+j]) ) for j in op.index]


op.to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Scores/Final.csv')