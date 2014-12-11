# Test file


# Run for test python Manager.py 
# Run for test python gui.py 

# Run for test python Manager.py 1
# Run for test python gui.py 1


from Nymph import *
ismail_m=nymphdata("ismail","127.0.0.1",8658)
ismail_g=nymphdata("ismail","127.0.0.1",8659)
erdem=nymphdata('erdem','127.0.0.1',8778)
ferhat=nymphdata('ferhat','127.0.0.1',8669)
alptug=nymphdata('alptug','127.0.0.1',9555)
ali=nymphdata('ali','127.0.0.1',8890)
veli=nymphdata('veli','127.0.0.1',8891)
firuze=nymphdata('firuze','127.0.0.1',8892)
halil=nymphdata('halil','127.0.0.1',8893)
nihal=nymphdata('nihal','127.0.0.1',8894)
nuran=nymphdata('nuran','127.0.0.1',8895)
im=nymphdata('akbudak','192.168.1.24',    8090)
ig=nymphdata('akbudak_gui','192.168.1.24',8091)
em=nymphdata('aybek','192.168.1.206',     8092)
eg=nymphdata('aybek_gui','192.168.1.206', 8093)

from Manager import *; ismail_m=GDManager(nodes[1],nodes_gui[1])
from helper_try import *; erdem_gui=helpertry(ismail,erdem) 


# Helpers
from gui_helper import *;nihal=helper(nihal)
from gui_helper import *;nuran=helper(nuran)

# Helper tries
 from helper_try import *; firuze=helpertry(firuze) 
 from helper_try import *; halil=helpertry(halil) 



from Manager import *; f=GDManager(ferhat,alptug)
from helper_try import *; fg=helpertry(alptug,ferhat) 


# Gui - manager
nuran=erdem
halil=ismail
from IP import *; from helper_try import *; n=helpertry(nuran,halil) 
from Manager import *; h=GDManager(halil,nuran)

#create a nymph example
#ismail=nymph(ismail)

# Real world is here cruel world
#im=nymphdata('akbudak','192.168.1.24',8080)
#ig=nymphdata('akbudak','192.168.1.24',8081)

# Run this
from Manager import *; i=GDManager(im,ig)
from IP import *; from helper_try import *; ig=helpertry(ig,im) 





e=nymphdata('aybek','192.168.1.206', 8082)
eg=nymphdata('aybek','192.168.1.206',8083)



