import streamlit as st
import requests
import re
import hashlib

# =====================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================

st.set_page_config(
    page_title="Batatadas E-commerce",
    page_icon="🛒",
    layout="wide"
)

# =====================================
# SESSION STATE
# =====================================

if "usuarios" not in st.session_state:
    st.session_state.usuarios = {}

if "usuario_logado" not in st.session_state:
    st.session_state.usuario_logado = None

if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

if "tentativas_login" not in st.session_state:
    st.session_state.tentativas_login = 0

# =====================================
# VALIDAR EMAIL
# =====================================

def email_valido(email):

    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(padrao, email)

# =====================================
# VALIDAR SENHA
# =====================================

def senha_forte(senha):

    if len(senha) < 8:
        return (
            False,
            "A senha deve ter no mínimo 8 caracteres!"
        )

    if not re.search(r"[A-Z]", senha):
        return (
            False,
            "A senha deve conter letra maiúscula!"
        )

    if not re.search(r"[a-z]", senha):
        return (
            False,
            "A senha deve conter letra minúscula!"
        )

    if not re.search(r"\d", senha):
        return (
            False,
            "A senha deve conter número!"
        )

    return (True, "")

# =====================================
# CRIPTOGRAFAR SENHA
# =====================================

def criptografar_senha(senha):

    return hashlib.sha256(
        senha.encode()
    ).hexdigest()

# =====================================
# LOGIN
# =====================================

def login(email, senha):

    usuarios = st.session_state.usuarios

    email = email.strip().lower()

    senha_criptografada = criptografar_senha(
        senha
    )

    if email in usuarios:

        if usuarios[email] == senha_criptografada:

            st.session_state.usuario_logado = email

            st.session_state.tentativas_login = 0

            return True

    st.session_state.tentativas_login += 1

    return False

# =====================================
# CADASTRO
# =====================================

def cadastrar(email, senha):

    usuarios = st.session_state.usuarios

    email = email.strip().lower()

    if not email_valido(email):

        return "Email inválido!"

    senha_valida, mensagem = senha_forte(
        senha
    )

    if not senha_valida:

        return mensagem

    if email in usuarios:

        return "Email já cadastrado!"

    senha_criptografada = criptografar_senha(
        senha
    )

    usuarios[email] = senha_criptografada

    return "sucesso"

# =====================================
# BUSCAR PRODUTOS
# =====================================

@st.cache_data(ttl=300)

def buscar_produtos():

    try:

        url = "https://fakestoreapi.com/products"

        resposta = requests.get(
            url,
            timeout=10
        )

        if resposta.status_code == 200:

            produtos = resposta.json()

            produtos_roupas = []

            for produto in produtos:

                categoria = produto.get(
                    "category",
                    ""
                )

                if (
                    categoria == "men's clothing"
                    or categoria == "women's clothing"
                ):

                    produtos_roupas.append(produto)

            return produtos_roupas

        else:

            st.error(
                "Erro ao buscar produtos!"
            )

    except requests.exceptions.Timeout:

        st.error(
            "Tempo de resposta da API excedido!"
        )

    except requests.exceptions.ConnectionError:

        st.error(
            "Erro de conexão com a API!"
        )

    except Exception:

        st.error(
            "Erro inesperado ao carregar produtos!"
        )

    return []

# =====================================
# LOGOUT
# =====================================

def logout():

    st.session_state.usuario_logado = None
    st.session_state.carrinho = []

    st.rerun()

# =====================================
# VALIDAR QUANTIDADE
# =====================================

def quantidade_valida(quantidade):

    if quantidade < 1:
        return 1

    if quantidade > 20:
        return 20

    return quantidade

# =====================================
# TÍTULO
# =====================================

st.title("🛒 Batatadas E-commerce")

st.write("Loja online de roupas")

# =====================================
# MENSAGEM
# =====================================

if "mensagem_sucesso" in st.session_state:

    st.success(
        st.session_state.mensagem_sucesso
    )

    del st.session_state.mensagem_sucesso

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.header("👤 Usuário")

    # =====================================
    # USUÁRIO LOGADO
    # =====================================

    if st.session_state.usuario_logado:

        st.success(
            f"Logado como:\n{st.session_state.usuario_logado}"
        )

        if st.button("Sair da Conta"):

            logout()

    else:

        opcao = st.selectbox(
            "Escolha uma opção",
            ["Login", "Cadastro"]
        )

        email = st.text_input(
            "E-mail",
            max_chars=100
        )

        senha = st.text_input(
            "Senha",
            type="password",
            max_chars=30
        )

        # =====================================
        # CADASTRO
        # =====================================

        if opcao == "Cadastro":

            st.info("""
            Senha segura:
            • 8 caracteres
            • Letra maiúscula
            • Letra minúscula
            • Número
            """)

            if st.button("Cadastrar"):

                email = email.strip().lower()

                if email == "" or senha == "":

                    st.error(
                        "Preencha todos os campos!"
                    )

                else:

                    resultado = cadastrar(
                        email,
                        senha
                    )

                    if resultado == "sucesso":

                        st.session_state.mensagem_sucesso = (
                            "Cadastro realizado com sucesso!"
                        )

                        st.rerun()

                    else:

                        st.error(resultado)

        # =====================================
        # LOGIN
        # =====================================

        if opcao == "Login":

            if st.button("Entrar"):

                email = email.strip().lower()

                if email == "" or senha == "":

                    st.error(
                        "Preencha todos os campos!"
                    )

                else:

                    if (
                        st.session_state.tentativas_login
                        >= 5
                    ):

                        st.error(
                            "Muitas tentativas de login!"
                        )

                    else:

                        sucesso = login(
                            email,
                            senha
                        )

                        if sucesso:

                            st.success(
                                "Login realizado!"
                            )

                            st.rerun()

                        else:

                            st.error(
                                f"""
                                Email ou senha inválidos!

                                Tentativas:
                                {st.session_state.tentativas_login}/5
                                """
                            )

# =====================================
# ÁREA LOGADA
# =====================================

if st.session_state.usuario_logado:

    st.success(
        f"Bem-vindo, {st.session_state.usuario_logado}"
    )

    st.divider()

    # =====================================
    # PRODUTOS
    # =====================================

    st.header("👕 Catálogo de Roupas")

    produtos = buscar_produtos()

    colunas = st.columns(3)

    for index, produto in enumerate(produtos):

        coluna = colunas[index % 3]

        with coluna:

            st.image(
                produto["image"],
                width=200
            )

            st.subheader(
                produto["title"]
            )

            preco = float(
                produto["price"]
            )

            st.write(
                f"💰 R$ {preco:.2f}"
            )

            quantidade = st.number_input(
                "Quantidade",
                min_value=1,
                max_value=10,
                value=1,
                key=f"qtd_{produto['id']}"
            )

            if st.button(
                "Adicionar ao Carrinho",
                key=f"botao_{produto['id']}"
            ):

                quantidade = quantidade_valida(
                    quantidade
                )

                produto_existe = False

                for item in st.session_state.carrinho:

                    if item["produto"] == produto["title"]:

                        item["quantidade"] += quantidade

                        produto_existe = True

                if not produto_existe:

                    st.session_state.carrinho.append({

                        "produto": produto["title"],

                        "preco": preco,

                        "quantidade": quantidade,

                        "imagem": produto["image"]
                    })

                st.success(
                    "Produto adicionado!"
                )

    st.divider()

    # =====================================
    # CARRINHO
    # =====================================

    st.header("🛍️ Carrinho")

    total = 0

    if st.session_state.carrinho:

        for index, item in enumerate(
            st.session_state.carrinho
        ):

            item["quantidade"] = quantidade_valida(
                item["quantidade"]
            )

            subtotal = (
                item["preco"] *
                item["quantidade"]
            )

            total += subtotal

            col1, col2, col3, col4, col5 = st.columns(
                [2, 4, 2, 2, 2]
            )

            with col1:

                st.image(
                    item["imagem"],
                    width=80
                )

            with col2:

                st.write(
                    f"**{item['produto']}**"
                )

            with col3:

                st.write(
                    f"R$ {subtotal:.2f}"
                )

            with col4:

                nova_quantidade = st.number_input(
                    "Qtd",
                    min_value=1,
                    max_value=20,
                    value=item["quantidade"],
                    key=f"carrinho_{index}"
                )

                item["quantidade"] = quantidade_valida(
                    nova_quantidade
                )

            with col5:

                if st.button(
                    "Excluir",
                    key=f"excluir_{index}"
                ):

                    st.session_state.carrinho.pop(
                        index
                    )

                    st.rerun()

            st.divider()

        st.subheader(
            f"💵 Total da Compra: R$ {total:.2f}"
        )

        parcelas = st.slider(
            "Quantidade de parcelas",
            min_value=1,
            max_value=12,
            value=1
        )

        valor_parcela = total / parcelas

        st.info(
            f"{parcelas}x de R$ {valor_parcela:.2f}"
        )

        if st.button(
            "Finalizar Compra"
        ):

            if total <= 0:

                st.error(
                    "Carrinho inválido!"
                )

            else:

                st.success(f"""
                Compra realizada com sucesso!

                Total: R$ {total:.2f}

                Parcelado em {parcelas}x de
                R$ {valor_parcela:.2f}
                """)

                st.balloons()

                st.session_state.carrinho = []

    else:

        st.info("Carrinho vazio!")

# =====================================
# NÃO LOGADO
# =====================================

else:

    st.warning(
        "Faça login para acessar a loja."
    )