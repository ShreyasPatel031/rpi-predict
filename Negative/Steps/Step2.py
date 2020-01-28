import pandas as pd
import os
from os import path

def conv( x ):
	f = open("/Users/shreyaspatel/blast/db/database.fa", "w+")
	for i in x.index :
		f.write('>'+ str(i) + '\n' )
		f.write( x[i] + '\n' )
	f.close()



pid = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/IDs/Protein_ID.csv')
rid = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/IDs/RNA_ID.csv')


p_grid = pd.DataFrame(index = pid.index,columns=rid.index)
r_grid = pd.DataFrame(index = pid.index,columns=rid.index)
inp = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/RPI_2333_conv.csv')



for i in pid.index :
	protein = pid.iloc[i][0]
	lst = inp.loc[ inp['protein_seq'] == protein ]['rna_seq']
	conv(lst)
	print("protein:",i)
	os.system('sh /Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Shell_scripts/make.sh')
	for j in rid.index :
		f2 = open("/Users/shreyaspatel/blast/db/query.fa", "w+")
		_=f2.write('>'+ str(j) + '\n' )
		_=f2.write( rid.iloc[j][0] + '\n' )
		f2.close()
		f2 = open("/Users/shreyaspatel/blast/db/query.fa", "r")
		print("protein:",i,"\nRNA:",f2.read())
		f2.close()
		while( not path.exists('/Users/shreyaspatel/blast/db/database.fa.nsq')):
			_
		a = os.system('sh /Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Shell_scripts/run.sh')	
		while( not path.exists('/Users/shreyaspatel/blast/db/op.csv')):
			_
		if( os.stat("/Users/shreyaspatel/blast/db/op.csv").st_size ):
			results = pd.read_csv('/Users/shreyaspatel/blast/db/op.csv')
			p_grid[j][i] = float ( results.columns[-1] )  
	

p_grid.to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/Protein_map.csv')


for i in rid.index :
	rna = rid.iloc[i][0]
	lst = inp.loc[ inp['rna_seq'] == rna ]['protein_seq']
	conv(lst)
	print("rna:",i)
	os.system('sh /Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Shell_scripts/make_r.sh')
	for j in pid.index :
		f2 = open("/Users/shreyaspatel/blast/db/query.fa", "w+")
		_=f2.write('>'+ str(j) + '\n' )
		_=f2.write( pid.iloc[j][0] + '\n' )
		f2.close()
		f2 = open("/Users/shreyaspatel/blast/db/query.fa", "r")
		print("rna:",i,"\nProtein:\n",f2.read())
		f2.close()
		while( not path.exists('/Users/shreyaspatel/blast/db/database.fa.psq')):
			_
		a = os.system('sh /Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Shell_scripts/run_r.sh')
		while( not path.exists('/Users/shreyaspatel/blast/db/op.csv')):
			_
		if( os.stat("/Users/shreyaspatel/blast/db/op.csv").st_size ):
			results = pd.read_csv('/Users/shreyaspatel/blast/db/op.csv',header = None)
			# print(results)
			r_grid[i][j] = float ( results[11][0] )  


r_grid.to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/RNA_map.csv')



