
from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTCTEST as SYMBOL
from typing import Optional

# Escolha entre 128, 160, 192, 224 ou 256 - determinando o numero de palavras do mnemonico
STRENGTH: int = 128  # Default = 128
# Escolha a linguagem english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese ou korean
LANGUAGE: str = "english"  # Default = english
# Gerar entropia
ENTROPY: str = generate_entropy(strength=STRENGTH)
# Senha da passphrase
PASSPHRASE: Optional[str] = None

def main():
    # Inicializar carteira.
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)

    # Criar carteira pela entropia
    hdwallet.from_entropy(entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE)
    hdwallet.from_path(path=f"m/49/1/0/0/0")

    # Exibir a mensagem final com detalhes da carteira
    print(f"Carteira Gerada")
    print(f"===============\n")
    print(f"Endereço: {hdwallet.p2pkh_address()}\n")
    print(f"Chave Privada WIF: {hdwallet.wif()}\n")
    print(f"Seed: {hdwallet.mnemonic()}")

if __name__ == "__main__":
    main()
