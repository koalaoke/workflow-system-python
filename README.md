# Sistema de Workflow Corporativo

#### EQUIPE: BERNARNO BRITO, PEDRO HENRIQUE CASTRO E RUAN RIPARDO
#### DISCIPLINA: Programação Orientada a Objetos (POO)
Um sistema de gerenciamento de processos desenvolvido em Python, focado na aplicação de Programação Orientada a Objetos (POO) para um trabalho da disciplina de POO.

O projeto utiliza Polimorfismo e Padrões de Projeto (State Pattern) para orquestrar transições de estados de forma dinâmica, garantindo uma arquitetura desacoplada, segura e de fácil manutenção.

Ele resolve problemas comuns em grandes corporações, como:
- Compliance e Auditoria: Rastreabilidade total de quem alterou o quê e quando (através do componente de Histórico imutável).
- Regras de Negócio Dinâmicas: A capacidade de adicionar novos estados (ex: "Em Revisão Jurídica") sem quebrar o código existente, simulando a evolução natural de processos empresariais.
- Segurança de Dados: O encapsulamento impede que o sistema entre em estados inconsistentes (ex: aprovar um documento já rejeitado).

## Arquitetura do Projeto
O sistema segue os princípios da Clean Architecture, dividindo o código em camadas com responsabilidades isoladas e regras de dependência estritas.

```Plaintext
sistema_workflow/
├── main.py                  # Entry Point
└── src/
    ├── domain/              # Camada de Domínio (Core)
    │   ├── interfaces.py    # Contratos 
    │   ├── entities.py      # Entidades (Processo, Historico)
    │   └── states.py        # Regras de Negócio (Estados)
    │
    ├── services/            # Camada de Aplicação
    │   └── manager.py       # Orquestração e Gerenciamento
    │
    └── ui/                  # Camada de Apresentação
        └── cli.py           # Interface de Linha de Comando
```

### Definição das Camadas
1. Domain: Contém as regras de negócio puras. Define o que o sistema faz.
2. Services: Gerencia o ciclo de vida dos objetos e atua como uma fachada para o mundo externo.
3. UI (Interface): Responsável apenas pela interação com o usuário (Input/Output).

### Tecnologias e Conceitos
- Linguagem: Python 3.10+
- Paradigmas: Orientação a Objetos (OOP)
- Princípios: SOLID

### Padrões de Projeto (Design Patterns) Aplicados
1. State Pattern (Padrão de Estado)
Utilizado para gerenciar as transições do processo (CRIADO ➝ EM_ANALISE ➝ APROVADO/REJEITADO).
    
    Como funciona: Cada estado é uma classe separada. O objeto Processo delega a ação para o estado atual.
    
    Benefício: Elimina complexidade ciclomática e permite criar novos estados sem alterar a classe principal (Open/Closed Principle).

2. Strategy Pattern (Estratégia)
Utilizado na gestão de comportamentos intercambiáveis (como exportação ou exibição de dados). Permite injetar diferentes algoritmos sem acoplar o código.

3. Composition over Inheritance (Composição)
O sistema prioriza composição.

Exemplo: Processo tem um Historico. Isso isola a responsabilidade de auditoria da responsabilidade de fluxo.

### Fluxo de Estados
O sistema implementa uma máquina de estados finita com as seguintes regras:

- CRIADO: Estado inicial. Só permite avançar para Em Análise.
- EM ANÁLISE: Permite Aprovar ou Rejeitar.
- APROVADO: Estado terminal (Final). Bloqueia novas alterações.
- REJEITADO: Estado terminal (Final). Bloqueia novas alterações.

### Como Executar
O projeto possui um ponto de entrada único na raiz para garantir a resolução correta dos módulos.

- Clone o repositório:

```Bash
git clone https://github.com/seu-usuario/workflow-system-python.git
cd workflow-system-python
```
- Execute o sistema:
```Bash
python3 main.py # ou apenas python main.py
```