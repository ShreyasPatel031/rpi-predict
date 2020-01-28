import pandas as pd

inp = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/RPI_2333.csv',index_col=False)
inp.reset_index()
inp = inp[['type','protein_seq','rna_seq']]

inp = inp[ ( ~inp['protein_seq'].str.contains('X') ) & ( ~inp['rna_seq'].str.contains('N')) ]

inp = inp[ ( ~inp['rna_seq'].str.contains('X') ) & ( ~inp['rna_seq'].str.contains('n')) ]

inp = inp[ ( ~inp['rna_seq'].str.contains('I') ) ]


pid = pd.DataFrame( { 'Protein' : inp['protein_seq'].unique() }  ) 

rid = pd.DataFrame( { 'RNA' : inp['rna_seq'].unique() }  ) 

inp.to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/RPI_'+str(len(inp))+'_conv.csv',index=False)
pid.to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/IDs/Protein_ID.csv',index=False)
rid.to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/IDs/RNA_ID.csv',index=False)


print(len(inp))

