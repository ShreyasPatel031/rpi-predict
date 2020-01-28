import pandas as pd

def conv( seq , typ ) :
	# print(typ)
	inp = [0] * 1024
	for i in range( len(seq) - 4 ) :
		# print( list(seq[i:i+5]) )
		# print(('').join([ prot[i] for i in list(seq[i:i+5]) ]))
		if( typ == 'prot' ):
			no = ('').join([ prot[i] for i in list(seq[i:i+5]) ])
		if( typ == 'rna' ):
			no = ('').join([ rna[i] for i in list(seq[i:i+5]) ])
		ans = 0
		for i in range(len(no)) : 
			ind = len(no) - i - 1
			ans += int( no[i] )* ( 4 ** ind )
			# print(int( no[i] )* ( 4 ** ind ))
		# print(ans)
		inp[ans] +=1 
	return inp


prot = { }
prot.update( { key:'0' for key in ['R','K','H'] })
prot.update( { key:'1' for key in ['N','W','S','Q','Y','G','T'] })
prot.update( { key:'2' for key in ['P','M','F','D','A','V','L','I'] })
prot.update( { key:'3' for key in ['C','E'] })

rna = { }
rna.update( { key:'0' for key in ['A','a'] })
rna.update( { key:'1' for key in ['U','u','T','t'] })
rna.update( { key:'2' for key in ['G','g'] })
rna.update( { key:'3' for key in ['C','c'] })


pos = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/RPI_2333_conv.csv')
neg = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Negative_2333.csv')

final = pd.DataFrame(index = list(range(len(pos) + len(neg) ) ), columns = list(range(2048)) )
for i in final.index:
	print(i)
	if( i < len(pos) ):
		final.iloc[i] = dict( zip( final.columns , conv(pos['protein_seq'][i],'prot') + conv(pos['rna_seq'][i],'rna') )  )
	else :
		final.iloc[i] = dict( zip( final.columns , conv(neg['Protein'][i-len(pos)],'prot') + conv(neg['RNA'][i-len(pos)],'rna') ) )


final.to_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Input/Input_2333.csv')






# conv(neg['Protein'].iloc[-1],'prot') + conv(neg['RNA'].iloc[-1],'rna')

# [ 0.75138122 , 1.    ,      1.    ,      1.    ,      1.    ,      1.    ,      1.,
#   1.     ,     1.     ,     0.74907749]






