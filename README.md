# 🤖 Discord ChatGPT Bot

Um bot Discord poderoso com múltiplos provedores de IA, incluindo modelos OpenAI, Claude, Gemini, Grok e um provedor gratuito baseado no g4f.

## 🚀 Recursos

- **Multi-Provider**: Suporte para OpenAI, Claude, Gemini, Grok e provedor gratuito
- **Personas**: Múltiplas personalidades de IA (padrão, criativa, técnica, casual)
- **Jailbreak**: Modos de contorno para administradores (restrito)
- **Imagens**: Geração de imagens com provedores compatíveis
- **Admin Panel**: Painel administrativo com Streamlit para gerenciamento completo

## 📋 Requisitos

- Python 3.9 ou superior
- Token de bot Discord
- Chaves API opcionais para provedores premium

## 🛠️ Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/prof-ramos/DiscordGPT.git
cd DiscordGPT
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure o ambiente:**
- Copie `.env.example` para `.env`
- Configure seu `DISCORD_BOT_TOKEN` no arquivo `.env`
- Opcionalmente, adicione chaves API para provedores premium

5. **Execute o bot:**
```bash
python3 main.py
```

## 🎛️ Painel Administrativo

O bot inclui um painel administrativo completo com Streamlit:

```bash
streamlit run admin_panel.py
```

## 🧪 Testes

Execute os testes com pytest:

```bash
python3 -m pytest tests/ -v
```

## 📚 Documentação

A documentação completa está disponível em: https://prof-ramos.github.io/DiscordGPT/

## 🔧 Comandos Disponíveis

- `/chat [mensagem]` - Conversar com a IA
- `/provider` - Trocar provedor e modelo de IA
- `/draw [prompt]` - Gerar imagem (provedores compatíveis)
- `/switchpersona [nome]` - Trocar personalidade da IA
- `/reset` - Limpar histórico de conversa
- `/help` - Mostrar ajuda com todos os comandos

## 🛡️ Segurança

- Personas de jailbreak são restritas a administradores
- Rate limiting por usuário
- Validação de entradas
- Logs de auditoria para acesso a personas restritas

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, leia o guia de contribuição antes de enviar pull requests.