
# FarmTech Solutions - Entrega 2

## 🗄️ Armazenamento de Dados em Banco SQL com Python

Este script simula o armazenamento dos dados coletados do sistema de irrigação em um banco SQL local usando SQLite.

### 🔍 Operações CRUD Implementadas:
- Inserção de dados simulados.
- Consulta de todos os dados.
- Atualização de campos específicos.
- Remoção de registros.

### 📘 Estrutura do Banco:
```sql
CREATE TABLE sensores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fosforo BOOLEAN,
    potassio BOOLEAN,
    ph REAL,
    umidade REAL,
    irrigacao_ativa BOOLEAN
)
```

### 🧬 Relação com MER da Fase 2:
A estrutura de dados reflete os atributos principais simulados no sistema físico:
- Nutrientes (P, K);
- pH (analógico);
- Umidade;
- Status da bomba (ligada/desligada).

## 📁 Arquivos
- `sensor_storage.py`: Script principal com as operações CRUD e simulações.
- `sensor_data.db`: Banco gerado após execução do script.
