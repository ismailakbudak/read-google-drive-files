# Test file
from Nymph import *
ismail=nymphdata("ismail","127.0.0.1",8658)
erdem=nymphdata('erdem','127.0.0.1',8778)

ferhat=nymphdata('ferhat','127.0.0.1',8669)
alptug=nymphdata('alptug','127.0.0.1',9555)

ali=nymphdata('ali','127.0.0.1',8890)
veli=nymphdata('veli','127.0.0.1',8891)

firuze=nymphdata('firuze','127.0.0.1',8892)
halil=nymphdata('halil','127.0.0.1',8893)

nihal=nymphdata('nihal','127.0.0.1',8894)
nuran=nymphdata('nuran','127.0.0.1',8895)


realis=nymphdata('akbudak','192.168.2.127',8090)
realisgui=nymphdata('akbudak','192.168.2.127',8091)

realer=nymphdata('aybek','192.168.2.118',8092)
realergui=nymphdata('aybek','192.168.2.118',8093)



from Manager import *; erdem=GDManager(erdem,ismail)
from IP import *; from helper_try import *; erdem_gui=helpertry(ismail,erdem) 


# Helpers
from IP import *;from gui_helper import *;nihal=helper(nihal)
from IP import *;from gui_helper import *;nuran=helper(nuran)

# Helper tries
from IP import *; from helper_try import *; firuze=helpertry(firuze) 
from IP import *; from helper_try import *; halil=helpertry(halil) 



from Manager import *; f=GDManager(ferhat,alptug)
from IP import *; from helper_try import *; fg=helpertry(alptug,ferhat) 


# Gui - manager
nuran=erdem
halil=ismail
from IP import *; from helper_try import *; n=helpertry(nuran,halil) 
from Manager import *; h=GDManager(halil,nuran)

#create a nymph example
#ismail=nymph(ismail)

