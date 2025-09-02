# 📚 Documentação Discord ChatGPT Bot

Esta é a documentação oficial do [Discord ChatGPT Bot](https://github.com/prof-ramos/DiscordGPT) construída com [Hugo](https://gohugo.io/).

## 🚀 Acesso Rápido

- **📖 Documentação Online**: [prof-ramos.github.io/DiscordGPT](https://prof-ramos.github.io/DiscordGPT/)
- **🏠 Repositório Principal**: [github.com/prof-ramos/DiscordGPT](https://github.com/prof-ramos/DiscordGPT)

## 🏗️ Estrutura

```
docs/
├── config.yaml              # Configuração Hugo
├── content/                  # Conteúdo da documentação
│   ├── _index.md            # Homepage
│   ├── getting-started/     # Guia inicial
│   ├── configuration/       # Configurações
│   ├── features/           # Funcionalidades
│   ├── api/                # API Reference
│   ├── deployment/         # Deploy
│   └── development/        # Desenvolvimento
├── static/                  # Assets estáticos
├── layouts/                 # Templates personalizados
└── themes/                  # Tema Hugo
```

## 🛠️ Desenvolvimento Local

### Pré-requisitos

- [Hugo Extended](https://gohugo.io/installation/) v0.128+
- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/) (para dependências do tema)

### Setup Local

```bash
# 1. Clone o repositório
git clone https://github.com/prof-ramos/DiscordGPT.git
cd DiscordGPT/docs

# 2. Instalar tema (se necessário)
git submodule update --init --recursive

# 3. Instalar dependências Node.js (se houver)
npm install

# 4. Executar servidor local
hugo server -D

# 5. Abrir no navegador
# http://localhost:1313
```

### Comandos Úteis

```bash
# Servidor com drafts e live reload
hugo server -D --disableFastRender

# Build para produção
hugo --gc --minify

# Verificar links quebrados
hugo --printUnusedTemplates --printI18nWarnings
```

## 🎨 Tema e Estilo

- **Tema Base**: [Docsy](https://www.docsy.dev/)
- **Customizações**: Cores, logos, layouts específicos
- **Responsive**: Otimizado para desktop e mobile
- **Dark Mode**: Suporte a tema escuro/claro
- **Busca**: Busca full-text integrada

## 📝 Contribuindo

### Adicionando Conteúdo

1. **Criar nova página:**
   ```bash
   hugo new content/nova-secao/pagina.md
   ```

2. **Estrutura do frontmatter:**
   ```yaml
   ---
   title: "Título da Página"
   description: "Descrição para SEO"
   weight: 10
   draft: false
   toc: true
   ---
   ```

3. **Shortcodes disponíveis:**
   ```markdown
   {{< alert title="Título" color="info" >}}
   Conteúdo do alerta
   {{< /alert >}}

   {{< tabs name="exemplo" >}}
   {{% tab name="Tab 1" %}}
   Conteúdo da tab 1
   {{% /tab %}}
   {{< /tabs >}}
   ```

### Guidelines de Escrita

- **Linguagem**: Português brasileiro
- **Tom**: Profissional mas acessível
- **Estrutura**: Usar headings (H1, H2, H3) consistentemente
- **Código**: Sempre incluir exemplos práticos
- **Links**: Usar links internos quando possível

## 🚀 Deploy

### GitHub Pages (Automático)

O deploy é feito automaticamente via GitHub Actions quando:
- Push para branch `main`
- Mudanças no diretório `docs/`

Configuração em `.github/workflows/hugo.yml`.

### Deploy Manual

```bash
# Build
hugo --gc --minify --baseURL "https://prof-ramos.github.io/DiscordGPT/"

# Deploy para GitHub Pages
# (feito automaticamente via Actions)
```

## 📊 Analytics e SEO

### Configurações SEO

- **Sitemap**: Gerado automaticamente
- **RSS**: Feed disponível
- **Meta tags**: OpenGraph e Twitter Cards
- **Schema.org**: Marcação estruturada

### Analytics

Configurado no `config.yaml`:
```yaml
params:
  google_analytics: "G-XXXXXXXXXX"  # Se configurado
```

## 🔧 Configurações Avançadas

### Customização do Tema

```yaml
# config.yaml
params:
  ui:
    sidebar_menu_compact: true
    breadcrumb_disable: false
    sidebar_search_disable: false
    navbar_logo: true
  
  # Cores personalizadas
  primary_color: "#1e88e5"
  secondary_color: "#00acc1"
```

### Funcionalidades Especiais

- **Copy Code**: Botões automáticos para copiar código
- **Edit Page**: Links para editar no GitHub
- **Last Modified**: Data da última modificação
- **Print**: Otimização para impressão

## 🆘 Troubleshooting

### Problemas Comuns

**Hugo não encontrado:**
```bash
# Instalar Hugo Extended
brew install hugo  # macOS
# ou baixar do GitHub Releases
```

**Servidor não inicia:**
```bash
# Verificar versão
hugo version

# Limpar cache
hugo --gc
```

**Tema não carrega:**
```bash
# Atualizar submodules
git submodule update --remote --merge
```

### Logs de Build

```bash
# Build com logs detalhados
hugo --verbose --debug
```

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/prof-ramos/DiscordGPT/issues)
- **Discussões**: [GitHub Discussions](https://github.com/prof-ramos/DiscordGPT/discussions)
- **Hugo Docs**: [gohugo.io/documentation](https://gohugo.io/documentation/)

## 📜 Licença

Esta documentação está sob a mesma licença do projeto principal (MIT). Ver [LICENSE](../LICENSE) no repositório principal.