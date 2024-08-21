from database.db5 import criar_tabela, inserir_pagamento, consultar_pagamento
from datetime import datetime

if __name__ == "__main__":
    # Cria a tabela no banco de dados, se não existir
    criar_tabela()

    # Insere alguns registros de pagamento com datas específicas
    inserir_pagamento(datetime(2024, 4, 6).strftime('%Y-%m-%d %H:%M:%S'))
    inserir_pagamento(datetime(2024, 9, 12).strftime('%Y-%m-%d %H:%M:%S'))

    # Consulta e exibe todos os pagamentos
    pagamentos = consultar_pagamento()
    for pagamento in pagamentos:
        print(pagamento)
