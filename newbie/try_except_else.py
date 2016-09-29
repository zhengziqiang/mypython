try:
	print "try to do something"
	r=10/int('2')
	print ('result:',r)
except ValueError as e:
	print ('valueError',e)
except ZeroDivisionError as e:
	print ("zerodivisionerror",e)
else:
	print 'no error'
finally:
	print "finally"
print 'end'