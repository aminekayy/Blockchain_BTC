from blockchain import Block, BlockChain, Wallet, Transaction
from typing import Dict
from blockchain import TransactionOutput
from blockchain.genesis import get_genesis_transaction
import random



if __name__ == '__main__':
    print("██████  ██       ██████   ██████ ██   ██  ██████ ██   ██  █████  ██ ███    ██ ")
    print("██   ██ ██      ██    ██ ██      ██  ██  ██      ██   ██ ██   ██ ██ ████   ██ ")
    print("██████  ██      ██    ██ ██      █████   ██      ███████ ███████ ██ ██ ██  ██ ")
    print("██   ██ ██      ██    ██ ██      ██  ██  ██      ██   ██ ██   ██ ██ ██  ██ ██ ")
    print("██████  ███████  ██████   ██████ ██   ██  ██████ ██   ██ ██   ██ ██ ██   ████ ")
    # a dictionary tracking unspent transaction outputs
    utxos = {}  # type: Dict[str, TransactionOutput]
    minimum_transaction = 0.1
    difficulty = 1

    blockchain = BlockChain(difficulty)


    # create wallet_genesis
    wallet_genesis = Wallet("genesis", utxos)

    # create wallet_coinbase
    wallet_coinbase = Wallet("coinbase", utxos)


    # send 100.000.000 utxos from wallet_genesis => wallet_coinbase
    genesis_transaction = get_genesis_transaction(wallet_genesis, wallet_coinbase, 100000000, utxos)
    print("Creating and mining genesis block")
    genesis = Block("genesis","0")
    genesis.add_transaction(genesis_transaction, utxos, minimum_transaction)
    print("Wallet coinbase balance: %d" % wallet_coinbase.get_balance())
    blockchain.append_block(genesis)
    print("Genesis Block")
    genesis.print()


    n = int(input("Enter a number of Wallets you want to simulate:\t\t"))
    # generate n wallets through a loop
    Numbers = [str(i) for i in range (1,n+1)]
    wallets_names = {}
    for number in Numbers:
        wallet_tmp = Wallet(number,utxos)
        wallets_names[wallet_tmp.name]= wallet_tmp
    print(wallets_names)
    print("is chain valid?", blockchain.check_valid(genesis_transaction))

    # generate n random numbers from 1 to 100
    balances = [random.randint(1,100) for i in range(1,n+1)]

    # send the random values to the n wallets from wallet_coinbase and add all this to the block1
    n_blocks = (n//5)+1
    nbr = 1
    Numbers_b = [str(i) for i in range(2, n_blocks + 1)]
    block_names = {"block 1":Block("1",genesis.hash)}

    ctr = 1
    for i in range(1,n+1):

        print()
        print("Attemping to send funds "+str(balances[i-1])+ " to "+ "Wallet "+str(i))
        block_names['block '+str(nbr)].add_transaction(wallet_coinbase.send_funds(wallets_names['wallet '+str(i)].public_key_as_str(), balances[i-1]), utxos, minimum_transaction)
        print("Wallet coinbase balance: %d" % wallet_coinbase.get_balance())
        print("Wallet "+str(i)+": %d" % wallets_names['wallet '+str(i)].get_balance())
        #print("Wallet " + str(i) + ": %s" % wallets_names['wallet ' + str(i)].print())
        if ctr%5==0 and ctr!=0:
            print('\nBlock ' + str(nbr))
            blockchain.append_block(block_names['block '+str(nbr)])
            print(block_names['block '+str(nbr)])
            block_names['block ' + str(nbr)].print()
            print("is chain valid?", blockchain.check_valid(genesis_transaction))
            nbr += 1
            block_tmp = Block(nbr, block_names['block ' + str(int(nbr) - 1)].hash)
            block_names[block_tmp.name] = block_tmp
        ctr += 1

    if ctr%5!=0:
        print('\nBlock ' + str((ctr // 5)+1))
        blockchain.append_block(block_names['block ' + str((ctr // 5)+1)])
        print(block_names['block ' + str((ctr // 5)+1)])
        block_names['block ' + str((ctr // 5)+1)].print()
        print("is chain valid?", blockchain.check_valid(genesis_transaction))


