from myweb3 import Web3

# Connect to a local Ethereum node (Ganache) or Infura by updating the URL
myweb3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

# Check if connected to a node
if myweb3.isConnected():
    print("Connected to Ethereum node")
else:
    print("Unable to connect to Ethereum node. Check your connection settings.")

# Replace with your deployed contract address and ABI
contract_address = 'YOUR_CONTRACT_ADDRESS'
contract_abi = [
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getIdentity",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "string", "name": "newIdentity", "type": "string"}],
        "name": "setIdentity",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Create a contract object
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Example function to set identity
def set_identity(identity, sender_address):
    transaction = contract.functions.setIdentity(identity).buildTransaction({
        'from': sender_address,
        'gas': 200000,
        'gasPrice': myweb3.toWei('50', 'gwei'),
        'nonce': myweb3.eth.getTransactionCount(sender_address),
    })
    private_key = 'YOUR_PRIVATE_KEY'  # Replace with the private key of the sender's Ethereum address
    signed_transaction = myweb3.eth.account.sign_transaction(transaction, private_key)
    transaction_hash = myweb3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    return transaction_hash

# Example function to get identity
def get_identity(sender_address):
    identity = contract.functions.getIdentity().call({'from': sender_address})
    return identity

# Replace with actual values
user_address = 'USER_ADDRESS'
user_private_key = 'USER_PRIVATE_KEY'
new_identity = 'New Identity'

# Set and get identity
transaction_hash = set_identity(new_identity, user_address)
print(f'Transaction Hash: {transaction_hash}')

current_identity = get_identity(user_address)
print(f'Current Identity: {current_identity}')
