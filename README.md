148
* `technical` - Technical and precise responses
149
* `casual` - Casual and friendly tone
150
* `jailbreak-v1` - BYPASS mode (admin only)
151
* `jailbreak-v2` - SAM mode (admin only)
152
* `jailbreak-v3` - Developer Mode Plus (admin only)
153

154
### Bot Behavior
155
* `/private` - Bot replies only visible to command user
156
* `/public` - Bot replies visible to everyone (default)
157
* `/replyall` - Bot responds to all messages in channel (toggle)
158
## Security Features
159

160
### Admin-Only Jailbreak Access
161
Jailbreak personas require admin privileges for enhanced security:
162

163
1. Set `ADMIN_USER_IDS` in `.env` with comma-separated Discord user IDs
164
2. Only admin users can access jailbreak personas
165
3. Regular users see only safe personas in `/switchpersona`
166

167
> **Warning**
168
> Jailbreak personas may generate content that bypasses normal AI safety measures. Admin access required.
169

170
### Environment Security
171
- No cookie-based authentication (removed for reliability)
172
- Secure API key management via environment variables
173
- Docker security hardening with non-root user
174
- Read-only filesystem for container security
175

176
---
177

178
## 📚 Documentação Completa
179

180
Para documentação detalhada, tutoriais e guias avançados:
181

182
### 🌐 **[Acesse a Documentação Oficial](https://prof-ramos.github.io/DiscordGPT/)**
183

184
A documentação inclui:
185
- 🚀 **Guia de início rápido** (30 segundos)
186
- ⚙️ **Configuração detalhada** de provedores
187
- 🎭 **Sistema de personalidades** explicado
188
- 🔒 **Configurações de segurança**
189
- 🐳 **Deploy com Docker**
190
- 📚 **API Reference** completa
191
- 🛠️ **Guia de desenvolvimento**
192

193
> **💡 Nova Documentação!** Migração completa para Hugo com interface moderna e busca integrada.
194

195
---
196

197
# Atualização da feature
198

199
**⚡ Divirta-se conversando com a IA!**
200
