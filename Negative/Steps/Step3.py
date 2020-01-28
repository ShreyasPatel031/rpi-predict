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

p_grid = pd.DataFrame(index = pid.index,columns = ['Protein'] )
conv(pid['Protein'])
os.system('sh /Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Shell_scripts/make_r.sh')
while( not path.exists('/Users/shreyaspatel/blast/db/database.fa.psq')):
	_

for i in pid.index :
	print(i)
	protein = pid.iloc[i][0]
	f2 = open("/Users/shreyaspatel/blast/db/query.fa", "w+")
	_=f2.write( '>'+ str(i) + '\n' )
	_=f2.write( protein + '\n' )
	f2.close()
	a = os.system('sh /Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Shell_scripts/run_r.sh')	
	while( not path.exists('/Users/shreyaspatel/blast/db/op.csv')):
		_
	if( os.stat("/Users/shreyaspatel/blast/db/op.csv").st_size  ):
		results = pd.read_csv('/Users/shreyaspatel/blast/db/op.csv')
		if( results.shape[0] > 0 ):	
			p_grid.iloc[i] = results.iloc[0,-1]
	p_grid.to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/Self_p.csv',index=False)


r_grid = pd.DataFrame(index = rid.index,columns = ['RNA'] )
conv( rid['RNA'] )
os.system('sh /Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Shell_scripts/make.sh')
while( not path.exists('/Users/shreyaspatel/blast/db/database.fa.nsq')):
	_

for i in rid.index :
	print(i)
	rna = rid.iloc[i][0]
	f2 = open("/Users/shreyaspatel/blast/db/query.fa", "w+")
	_=f2.write('>'+ str(i) + '\n' )
	_=f2.write( rna + '\n' )
	f2.close()
	a = os.system('sh /Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Shell_scripts/run.sh')	
	while( not path.exists('/Users/shreyaspatel/blast/db/op.csv')):
		_
	if( os.stat("/Users/shreyaspatel/blast/db/op.csv").st_size ):
		results = pd.read_csv('/Users/shreyaspatel/blast/db/op.csv')
		if( results.shape[0] > 0 ):
			r_grid.iloc[i] = results.iloc[0,-1]
			# print(results.iloc[0,-1])
r_grid.to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Grids/Self_r.csv',index=False)


