from web3 import Web3

# RPC URLs
ETH_RPC_URL = "https://arbitrum-mainnet.infura.io/v3/d491f7f939ca4c3c9b8a97d75f8bd8b3"
web3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))

# Пример ABI
UNISWAP_PAIR_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "getReserves",
        "outputs": [
            {"internalType": "uint112", "name": "_reserve0", "type": "uint112"},
            {"internalType": "uint112", "name": "_reserve1", "type": "uint112"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
]

def fetch_dex_prices(symbols):
    dex_prices = {}

    # Пример адреса пары на Uniswap
    uniswap_pair_address = "0x1234567890abcdef1234567890abcdef12345678"

    try:
        # Преобразуем адрес в формат checksum
        checksum_address = Web3.to_checksum_address(uniswap_pair_address)

        pair_contract = web3.eth.contract(address=checksum_address, abi=UNISWAP_PAIR_ABI)
        reserves = pair_contract.functions.getReserves().call()

        # Расчёт цены
        price = reserves[1] / reserves[0]
        dex_prices.setdefault("ETHUSDT", {})['Uniswap'] = price

    except Exception as e:
        print(f"Error fetching Uniswap prices: {e}")

    return dex_prices
