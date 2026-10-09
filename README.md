# Automação de Testes E2E (Playwright + Python)

Projeto de automação de testes desenvolvido para validar os fluxos de login da página de demonstração [Sauce Demo](https://www.saucedemo.com/), utilizando o padrão **Page Object Model (POM)**.

---

## Tecnologias Utilizadas

* **Python**
* **Playwright** (Automação web)
* **Pytest** (Framework de execução de testes)

---

## Estrutura do Projeto

```text
automacao_teste/
├── pages/
│   └── login_page.py       # Mapeamento de elementos e ações da tela de login
├── tests/
│   └── test_example.py     # Casos de teste automatizados
├── .gitignore              # Arquivos ignorados pelo controle de versão
├── pytest.ini              # Configurações do Pytest
└── requirements.txt        # Dependências do projeto
```

⚙️ Como Executar o Projeto
Siga os passos abaixo para rodar os testes na sua máquina:

1. Clonar o repositório
Bash
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/Marcozzs/automacao_teste.git)
cd automacao_teste
------------------------------------------------------------------------------------------------------------------
2. Criar e ativar o ambiente virtual (venv)
No macOS / Linux:
Bash
python3 -m venv venv
source venv/bin/activate
No Windows:
Bash
python -m venv venv
venv\Scripts\activate
------------------------------------------------------------------------------------------------------------------
3. Instalar as dependências
Bash
pip install -r requirements.txt
playwright install
------------------------------------------------------------------------------------------------------------------
4. Executar os testes
Para rodar os testes abrindo o navegador visualmente (--headed) e exibindo as mensagens no terminal (-s):

```bash
pytest -s --headed
```
------------------------------------------------------------------------------------------------------------------
