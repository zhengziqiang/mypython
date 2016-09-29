try:
	print "try to do something"
	r=10/0
	print ("result:",r)
except ZeroDivisionError as e:
	print ("except:",e)
finally:
	print ("finally....")
print 'end'