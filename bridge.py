from ethers import (
    EthereumProvider,
    EthereumPrivateKey,
    Contract,
    contract_function,
    address,
)

# Set up a connection to the Polygon network
polygon_provider = EthereumProvider('https://polygon-rpc.com/')
private_key = EthereumPrivateKey.from_hex('your_private_key_here')
polygon_provider.set_signer(private_key)

# Define the contract ABI and bytecode
contract_abi = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_user",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_guildId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_channelId",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "_content",
                "type": "string"
            }
        ],
        "name": "addMessage",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getMessageCount",te
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract_bytecode = '0x...'

# Create a Contract object and deploy the contract to the network
contract = Contract(polygon_provider, contract_abi, bytecode=contract_bytecode)
deploy_txn = contract.constructor().as_transaction({'from': address(private_key)})
receipt = polygon_provider.eth_send_transaction(deploy_txn)
contract_address = receipt['contractAddress']

# Create a Contract object for the deployed contract
contract_instance = Contract(polygon_provider, contract_abi, address=contract_address)

# Add a new message to the contract
user_address = '0x...'
guild_id = 123
channel_id = 456
content = 'Hello, world!'
add_message_fn = contract_function(contract_instance.functions.addMessage)
add_message_fn(user_address, guild_id, channel_id, content)

# Retrieve the number of messages stored in the contract
get_message_count_fn = contract_function(contract_instance.functions.getMessageCount)
message_count = get_message_count_fn()
print(f'Number of messages stored in contract: {message_count}')