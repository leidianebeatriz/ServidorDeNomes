import rpyc
import sys
 
if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
 
conn = rpyc.connect(server,18861)

print(c.root)
print(c.root.get_answer())
print(c.root.the_real_answer_though)

