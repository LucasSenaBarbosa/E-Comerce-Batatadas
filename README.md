# 🛒 Batatadas E-commerce

Sistema de E-commerce desenvolvido em Python utilizando Streamlit, com foco em boas práticas de desenvolvimento, Quality Assurance (QA), validações de segurança e experiência do usuário.

---

# 📌 Sobre o Projeto

O Batatadas E-commerce é uma aplicação web de loja virtual de roupas que permite:

- Cadastro de usuários
- Login seguro
- Visualização de produtos
- Adição de produtos ao carrinho
- Controle de quantidade
- Exclusão de produtos
- Simulação de compra parcelada

O projeto foi desenvolvido com foco em:

- Segurança básica
- Validações de entrada
- Organização do código
- Experiência do usuário
- Boas práticas de QA

---

# 🚀 Tecnologias Utilizadas

- Python
- Streamlit
- Requests
- Regex (re)
- Hashlib
- Fake Store API

---

# 📂 Estrutura do Projeto

```bash
batatadas-ecommerce/
│
├── app.py
├── README.md
└── requirements.txt
```

---

# ▶️ Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/LucasSenaBarbosa/batatadas-ecommerce.git
```

---

## 2️⃣ Acesse a pasta do projeto

```bash
cd batatadas-ecommerce
```

---

## 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

Ou:

```bash
pip install streamlit requests
```

---

## 4️⃣ Execute a aplicação

```bash
streamlit run app.py
```

---

# 🛍️ Funcionalidades

## 👤 Autenticação

- Cadastro de usuários
- Login
- Logout
- Validação de email
- Validação de senha forte
- Controle de tentativas de login

---

## 🔐 Segurança Implementada

### ✔️ Hash de senha

As senhas são criptografadas utilizando:

```python
hashlib.sha256()
```

---

### ✔️ Validação de senha forte

A senha deve possuir:

- 8 caracteres
- Letra maiúscula
- Letra minúscula
- Número

---

### ✔️ Controle de tentativas de login

O sistema limita múltiplas tentativas inválidas de login.

---

### ✔️ Tratamento de exceções

Tratamento de erros da API:

- Timeout
- Erro de conexão
- Falhas inesperadas

---

### ✔️ Sanitização de entrada

Os emails são tratados com:

```python
.strip().lower()
```

---

# 🧪 Testes e QA Aplicados

## ✔️ Testes Funcionais

- Cadastro de usuário
- Login válido
- Login inválido
- Adicionar ao carrinho
- Atualizar quantidade
- Excluir item
- Finalizar compra

---

## ✔️ Testes de Validação

- Campos vazios
- Email inválido
- Senha fraca
- Quantidade inválida
- Carrinho vazio

---

## ✔️ Testes de Segurança

- Tentativas múltiplas de login
- Validação de entradas
- Criptografia de senha

---

## ✔️ Testes de Usabilidade

- Navegação simples
- Feedback visual
- Mensagens amigáveis
- Organização visual dos produtos

---

# 🛒 Funcionalidades do Carrinho

- Adicionar produtos
- Alterar quantidade
- Excluir produtos
- Exibição de imagem
- Cálculo automático do total
- Parcelamento em até 12x

---

# 🌐 API Utilizada

Fake Store API:

:contentReference[oaicite:0]{index=0}

---

# 📸 Interface

O sistema possui:

- Sidebar para autenticação
- Catálogo de roupas
- Carrinho interativo
- Layout responsivo

---

# 📈 Melhorias Futuras

- Banco de dados
- Login JWT
- Integração com pagamento
- Dashboard administrativo
- Persistência de carrinho
- Favoritos
- Busca de produtos
- Filtro por categoria

---

# 👨‍💻 Desenvolvido por

Gustavo de Carvalho Azzola
Lucas Sena Barbosa
Luis Henrique Marques

---

# 📚 Objetivo Acadêmico

Projeto desenvolvido para fins acadêmicos com foco em:

- Engenharia de Software
- Quality Assurance (QA)
- Segurança de Aplicações
- Desenvolvimento Web em Python

---

# 📄 Licença

Projeto desenvolvido para fins educacionais.
