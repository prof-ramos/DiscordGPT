#!/bin/bash
# Script para iniciar o bot Discord

# Verificar se o ambiente virtual existe
if [ -d "venv" ]; then
    echo "Ativando ambiente virtual..."
    source venv/bin/activate
else
    echo "Criando ambiente virtual..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Instalando dependências..."
    pip install -r requirements.txt
fi

# Verificar se o arquivo .env existe
if [ ! -f ".env" ]; then
    echo "Criando arquivo .env a partir do exemplo..."
    cp .env.example .env
    echo "Por favor, edite o arquivo .env e adicione seu DISCORD_BOT_TOKEN"
    exit 1
fi

# Verificar se o token do bot está configurado
if grep -q "your_discord_bot_token_here" .env; then
    echo "Por favor, edite o arquivo .env e adicione seu DISCORD_BOT_TOKEN"
    exit 1
fi

echo "Iniciando o bot Discord..."
python3 main.py