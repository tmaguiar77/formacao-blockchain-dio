from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTCTEST as SYMBOL
from typing import Optional

# Escolha entre 128, 160, 192, 224 ou 256 - determinando o numero de palavras
STRENGTH: int = 128  # Default = 128
# Escolha a linguagem english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese ou korean
LANGUAGE: str = "english"  # Default = english
# Gerar entropia
ENTROPY: str = generate_entropy(strength=STRENGTH)
# Senha da passphrase
PASSPHRASE: Optional[str] = None

# Inicializar carteira.
hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)

# Criar carteira pela entropia
hdwallet.from_entropy(entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE)
hdwallet.from_index(49, hardened=True)

# Exibir a mensagem final com detalhes da carteira
print("Carteira gerada")
print(f"Endereço: {hdwallet.p2pkh_address()}")
print(f"Chave Privada: {hdwallet.private_key()}")
print(f"Seed: {hdwallet.mnemonic()}")
