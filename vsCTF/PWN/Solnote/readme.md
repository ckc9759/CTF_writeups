### Chall Desc: 
Come try out my blazing fast and memory safe super decentralized note-taking app built on the blockchain™️! What could possibly go wrong?

nc 104.197.118.147 10180

### File attached : [solnote_player.zip](solnote_player.zip)

### Soln: 

basically the program lets a user create a notepad, and allow others to buy and edit "notes" attached to that notepad, with each purchase giving a portion of the profits to whoever created the notepad + a central vault
the fee is fixed at 15% of the price and is stored in the notepad itself
however, there's still a lot that's suspicious about how it works
for one, it seems like there's no reason to store the fee percentage if it never changes, so its weird that it is stored
and it also is weird how the buying works:
1. full purchase price is sent to vault
2. fee is transferred from vault to the notepad owner
as opposed to just splitting it from the getgo
if we can somehow get a notepad with a fee larger than 100% (which is theoretically possible because it's stored in a u64), we can steal money from the vault by buying a note!
since there is nothing marking the difference between a note and a notepad account, we can deserialize a crafted note account as a notepad account with an extremely high royalty fee with the user account marked as the "owner", which we can then use to steal the needed 50 billion lamports from the vault

You can see details in the solve zip file here:  
[solve.zip](solve.zip)
