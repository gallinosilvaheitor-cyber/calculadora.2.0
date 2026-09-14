# Calculadora em Python

Projeto completo de calculadora desenvolvido em Python moderno, com arquitetura modular, motor de cálculo seguro com análise sintática (AST), suporte a histórico de operações, gerenciamento de memória (M+, M-, MR, MC), interface gráfica desktop (Tkinter) e interface de linha de comando (CLI).

---

## Recursos

- **Interface Gráfica Desktop (Tkinter):**
  - Tema escuro moderno e responsivo.
  - Visor duplo (expressão e resultado).
  - Suporte completo a atalhos do teclado físico (teclas numéricas, operadores, Enter, Esc, Backspace).
  - Painel de visualização e limpeza de histórico.
  - Funções científicas acessíveis (`√`, `x²`, parênteses, inverso de sinal `±`).

- **Interface de Terminal (CLI Interativa):**
  - Ambiente interativo REPL com ajuda integrada (`ajuda`).
  - Suporte a comandos de histórico (`hist`), memória (`mr`, `ms`, `mc`) e limpeza (`limpar`).
  - Permite reutilizar o último resultado com a variável `ans` (ex: `ans * 2`).

- **Motor de Cálculo Seguro:**
  - Avaliação de expressões usando Árvore Sintática Abstrata (`ast`), prevenindo execução de código arbitrário (`eval` inseguro bloqueado).
  - Suporte a precedência correta de operadores, parênteses e funções (`sqrt`, `abs`, `round`, `sin`, `cos`, `tan`, `log`, etc.).
  - Tratamento elegante de erros (divisão por zero, expressões inválidas, raízes negativas).

- **Qualidade de Código & Testes:**
  - Suíte completa de testes automatizados com `unittest`.

---

## Estrutura do Projeto

```
calculadora/
├── calculadora/
│   ├── __init__.py
│   ├── core.py          # Operações matemáticas, classes de memória e histórico
│   ├── parser.py        # Avaliador seguro de expressões via AST
│   ├── cli.py           # Interface interativa de linha de comando
│   └── gui.py           # Interface gráfica Desktop (Tkinter)
├── tests/
│   ├── __init__.py
│   └── test_calculator.py  # Testes unitários
├── main.py              # Ponto de entrada da aplicação
└── README.md            # Documentação
```

---

## Como Executar

Abra o terminal (PowerShell ou Prompt de Comando) na pasta do projeto:

```powershell
cd C:\Users\Heitor\.gemini\antigravity\scratch\calculadora
```

### 1. Iniciar no Modo Gráfico (Desktop)
Para abrir a janela interativa da calculadora no seu Windows:
```powershell
python main.py
```
*(ou explicitamente `python main.py --gui`)*

### 2. Iniciar no Modo Terminal (CLI)
Para usar diretamente pelo terminal sem abrir janelas:
```powershell
python main.py --cli
```

### 3. Iniciar no Modo Web / Celular (Mobile PWA)
Para abrir no navegador e no celular pelo Wi-Fi:
```powershell
python main.py --web
```
O terminal exibirá o endereço de acesso, por exemplo:
- No computador: `http://localhost:5000`
- No celular (mesmo Wi-Fi): `http://192.168.0.12:5000`

> **Dica PWA no Celular:** Abra o link no Chrome ou Safari do celular, toque no menu de opções e selecione **"Adicionar à tela de início"**. A calculadora passará a se comportar como um aplicativo nativo!

---

### 4. Rodar os Testes Automatizados
Para executar todos os testes unitários e verificar a integridade do código:
```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```
