#coding=utf-8
from docopt import docopt
def cli():
	arguments=docopt(__doc__)
	print (arguments)

if __name__=='__main__':
	cli()