This is our final year project about the recovery of lost Bitcoins

These are the main features of our project:

- Propose a probabilistic model to dentine if a satushi is lost or not, and then recover it using two
parameters: how old is the satushi (i.e. last time it was transmitted) and the value of the wallet
this Satushi belongs to.
- Mechanism to refresh wallet contents, i.e. so that the alive wallets are not considered lost even
if they are not practically used for long time.
- Recovery mechanism: in order to resend any satushi that has been taken from a wallet, and
then this wallet is found to be a live.
- How long it takes to recover all the coins in lost wallet that has 1, 10, 100, 1000, etc… If every
one, is 100000, 200000, 300000, 400000, 500000, 600000 blocks old (this can be a 3D plot)
- We can also identify the parameters in the probabilistic model to show that the proposed
method can maintain a sustainable ecosystem where the lost bitcoins will not grow, and in
addition, the system will not abuse alive bitcoins.
- Finally, if this proposed method is not practical on Bitcoin, it can be easily considered for similar
new public coins !

### Noobcoin
Since this is only a simulation, we called our simulation coin: "noobcoin", thus our simulation blockchain's name is: "noobchain"
We have got inspired from this very interesting medium tutorial about creating a blockchain using Java and from Reza Abbasi's repository on Github.
Here is the link of the medium article:(https://medium.com/programmers-blockchain/create-simple-blockchain-java-tutorial-from-scratch-6eeed3cb03fa).

### Install
`pip install -r requirements.txt`

### Run
`python main3.py`

### Credits
- Mohamed Amine AJINOU
- Karim HABOUCH
Mentors: Meryem AYACHE, Amjad GAWANMEH 

INPT Rabat School | Major: Cybersecurity & Digital Trust Engineering
©PFA June 2021
