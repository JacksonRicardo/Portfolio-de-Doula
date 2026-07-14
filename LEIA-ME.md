# 🌸 Site Doula Malú — Django

Site profissional com painel de administração para edição de conteúdo.

---

## 🚀 Como instalar e rodar

### 1. Instale os requisitos
```bash
pip install django pillow
```

### 2. Entre na pasta do projeto
```bash
cd doula_malu
```

### 3. Rode as migrações (cria o banco de dados)
```bash
python manage.py migrate
```

### 4. Crie um superusuário (caso não use o padrão abaixo)
```bash
python manage.py createsuperuser
```
> **Usuário padrão já criado:**
> - Login: `malu`
> - Senha: `doula2024`
> ⚠️ Troque a senha após o primeiro login!

### 5. Inicie o servidor
```bash
python manage.py runserver
```

### 6. Acesse o site
- 🌐 **Site público:** http://localhost:8000
- 🔧 **Painel de admin:** http://localhost:8000/admin

---

## ✏️ Como editar o site (para a Malú)

1. Acesse **http://seusite.com/admin**
2. Entre com seu usuário e senha
3. Clique em **"Configuração do Site"** para editar textos, fotos, links
4. Clique em **"Serviços"** para adicionar, editar ou remover serviços
5. Clique em **"Fotos"** para gerenciar a galeria de fotos

### O que você pode editar:
- ✅ Título e subtítulo da página inicial
- ✅ Foto de fundo do hero
- ✅ Todos os textos da seção "Sobre mim"
- ✅ Foto de perfil
- ✅ Telefone, WhatsApp, Instagram, e-mail, endereço
- ✅ Serviços (título, descrição, ícone, ordem)
- ✅ Galeria de fotos (adicionar, remover, reordenar)
- ✅ Arquivo PDF do portfólio

---

## 🌍 Deploy (publicar na internet)

### Opção 1: Railway (gratuito para começar)
1. Crie conta em railway.app
2. Crie novo projeto → Deploy from GitHub
3. Adicione a variável: `SECRET_KEY=sua-chave-secreta`

### Opção 2: PythonAnywhere (gratuito)
1. Crie conta em pythonanywhere.com
2. Siga o tutorial deles para Django

---

## 📁 Estrutura do projeto
```
doula_malu/
├── core/               ← App principal
│   ├── models.py       ← Estrutura dos dados
│   ├── views.py        ← Lógica das páginas
│   ├── admin.py        ← Painel de administração
│   └── templates/      ← HTML das páginas
├── media/              ← Imagens e arquivos enviados
├── db.sqlite3          ← Banco de dados
└── manage.py           ← Comandos do Django
```
