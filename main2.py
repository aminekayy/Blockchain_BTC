from blockchain import Block, BlockChain, Wallet, Transaction
from typing import Dict
from blockchain import TransactionOutput
from blockchain.genesis import get_genesis_transaction


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

    wallet_one = Wallet("1",utxos)
    wallet_two = Wallet("2",utxos)

    wallet_coinbase = Wallet("coinbase",utxos)

    # create genesis transaction, which sends 100 coins to wallet_one
    genesis_transaction = get_genesis_transaction(wallet_coinbase, wallet_one, 100, utxos)
    print("Creating and mining genesis block")
    genesis = Block("0")
    genesis.add_transaction(genesis_transaction, utxos, minimum_transaction)
    print("Wallet one balance: %d" % wallet_one.get_balance())


    blockchain.append_block(genesis)
    print("Genesis Block")
    genesis.print()

    print()
    print("Attemping to send funds (40) to Wallet two")
    block1 = Block(genesis.hash)
    block1.add_transaction(wallet_one.send_funds(wallet_two.public_key_as_str(), 40), utxos, minimum_transaction)
    print("Wallet one balance: %d" % wallet_one.get_balance())
    print("Wallet two balance: %d" % wallet_two.get_balance())

    print("Wallet two is attempting to send funds (20) to wallet one")
    block1.add_transaction(wallet_two.send_funds(wallet_one.public_key_as_str(), 20), utxos, minimum_transaction)
    print("Wallet one balance: %d" % wallet_one.get_balance())
    print("Wallet two balance: %d" % wallet_two.get_balance())

    blockchain.append_block(block1)
    print("Block 1")
    block1.print()

    print("is chain valid?", blockchain.check_valid(genesis_transaction))

    print()

    block2 = Block(block1.hash)
    print("Wallet one is attempting to send funds (30) to wallet two")
    block2.add_transaction(wallet_one.send_funds(wallet_two.public_key_as_str(), 30), utxos, minimum_transaction)
    print("Wallet one balance: %d" % wallet_one.get_balance())
    print("Wallet two balance: %d" % wallet_two.get_balance())

    print()
    print("Wallet two is attempting to send funds (15) to wallet one")
    block2.add_transaction(wallet_two.send_funds(wallet_one.public_key_as_str(), 15), utxos, minimum_transaction)
    print("Wallet one balance: %d" % wallet_one.get_balance())
    print("Wallet two balance: %d" % wallet_two.get_balance())

    blockchain.append_block(block2)
    print("Block 2")
    block2.print()

    print("is chain valid?", blockchain.check_valid(genesis_transaction))

