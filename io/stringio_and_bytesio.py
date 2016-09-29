from io import StringIO
#import io
f=StringIO()
f.write("hello")
f.write(" ")
f.write("world")
print (f.getvalue())

