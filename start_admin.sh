#!/bin/bash
# Script para iniciar o painel administrativo

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

echo "Iniciando o painel administrativo..."
streamlit run admin_panel.py