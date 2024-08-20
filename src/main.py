from database.db5 import criar_tabela
from src.database.db5 import inserir_pagamento, consultar_pagamento

if __name__ == "__main__":
    criar_tabela()
    inserir_pagamento("Dia 20")

    pagamento = inserir_pagamento()
    for item in pagamento:
        print(item)
