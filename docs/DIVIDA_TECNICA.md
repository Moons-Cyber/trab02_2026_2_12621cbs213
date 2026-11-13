# Dívida técnica e refatorações (S5_01)

Documento do card S5_01. Lista o que foi refatorado, os *code smells* que
sobraram e as *issues* a registrar no repositório. Cada refatoração é um
commit à parte (`git log --oneline`), com os 272 testes passando antes e depois.

## Code smells encontrados

| # | Onde | Smell |
| :-- | :-- | :-- |
| 1 | `src/api/aplicacao.py`, `criar_app` | Função longa: 535 linhas, com ~48 ramificações |
| 2 | `src/servicos/analise_risco.py`, `construir_matriz_dependencias` (77 linhas) | Função longa e com muitos `if` |
| 3 | `main.py` | Cadeias `if/elif` repetidas em cinco menus |
| 4 | `src/modelos/*.py` | Código duplicado: o mesmo `para_dict` nas 4 subclasses de `Ativo` |
| 5 | Todo o `src/` | Nenhuma anotação de tipo (0 de 185 funções) |
| 6 | `src/api/aplicacao.py` e `main.py` | Validação repetida (`_texto`, `_inteiro`, `ler_inteiro`...) em vez de reaproveitar `modelos/validacoes.py` |
| 7 | `src/persistencia/repositorio_sqlite.py` | `salvar` apaga e reinsere tudo a cada gravação |

## Refatorações aplicadas (uma por commit)

| Commit | Refatoração (Fowler) | Smell resolvido |
| :-- | :-- | :-- |
| `refactor(api): extrai os tratadores de erro de criar_app` | Extrair Função | #1 (535 → 502 linhas) |
| `refactor(modelos): sobe para Ativo o para_dict repetido` | Subir Método | #4 |
| `refactor(menu): troca as cadeias if/elif dos menus por tabela de despacho` | Substituir Condicional por tabela de despacho | #3 |
| `refactor(tipos): anotações de tipo nas classes de domínio` | (tipagem) | #5 (parcial: 44 de 182 funções) |

Sobre polimorfismo: a escolha por tipo de ativo já era polimórfica antes
(`obter_fator_exposicao`, `campo_especifico`, `validar_campo_especifico`).
A cadeia de condicionais que sobrava era a dos menus, trocada pela tabela
de despacho acima.

## Relatório do mypy

O mypy não rodou no ambiente em que as refatorações foram feitas (sem acesso
para instalá-lo). Rode no seu computador e guarde a saída:

```powershell
pip install mypy
python -m mypy src/modelos --ignore-missing-imports > relatorio_mypy.txt
```

## Issues a registrar (dívida restante)

1. **Dividir `criar_app` em Blueprints por tema** (ativos, vulnerabilidades,
   dependências, risco, interface). Hoje ainda tem ~500 linhas.
2. **Extrair funções de `construir_matriz_dependencias`** (77 linhas): separar a
   validação da montagem da matriz.
3. **Anotar tipos nos serviços, na API e na persistência** (faltam ~138 funções)
   e rodar o mypy no CI.
4. **Unificar a validação**: `aplicacao.py` e `main.py` devem usar as mesmas
   funções de `modelos/validacoes.py`.
5. **Renomear o parâmetro `id`** (sombreia o `id` do Python) em `Ativo` e
   `Vulnerabilidade`, cuidando dos testes e do JSON.
6. **SQLite: gravar de forma incremental** (`INSERT ... ON CONFLICT`) em vez de
   apagar e reinserir tudo.
7. **SQLite: criar índices** e comparar com `EXPLAIN QUERY PLAN` (card de hash).
8. **Autenticação e permissões por setor**: combinada como trabalho futuro com
   o professor.
9. **Menu e API não podem rodar ao mesmo tempo** sobre os mesmos arquivos
   (cada um guarda os dados na memória).

### Criar as issues pelo terminal (opcional, precisa do GitHub CLI)

```powershell
gh issue create --title "Dividir criar_app em Blueprints por tema" --body "criar_app ainda tem ~500 linhas. Separar ativos, vulnerabilidades, dependências, risco e interface."
gh issue create --title "Extrair funções de construir_matriz_dependencias" --body "77 linhas. Separar validação e montagem da matriz."
gh issue create --title "Anotar tipos em serviços, API e persistência e rodar mypy no CI" --body "Hoje só as classes de domínio têm anotações."
gh issue create --title "Unificar a validação de entrada" --body "aplicacao.py e main.py repetem regras de modelos/validacoes.py."
gh issue create --title "Renomear o parâmetro id (sombreia o builtin)" --body "Ativo e Vulnerabilidade. Cuidar de testes e JSON."
gh issue create --title "SQLite: gravação incremental" --body "salvar apaga e reinsere tudo; trocar por INSERT ... ON CONFLICT."
gh issue create --title "SQLite: índices e EXPLAIN QUERY PLAN" --body "Medir antes e depois (card de hash)."
gh issue create --title "Autenticação e permissões por setor" --body "Combinado como trabalho futuro."
gh issue create --title "Menu e API sobre os mesmos arquivos" --body "Cada um guarda os dados em memória; um sobrescreve o outro."
```
