# Leitura do Search Console: googleadsfreelancer.com (26/10/2026)

Fontes: Search Console via API (90 dias, 27/07 a 24/10/2026; inspeção de URL das 30 páginas do sitemap), DataForSEO
(volumes EUA para 60 termos em um pedido, US$ 0,09; resumo e domínios de backlinks, cerca de US$ 0,06; duas SERPs ao
vivo, US$ 0,004) e o próprio `dist/` do site (títulos, H1, palavras, links internos). CSVs ao lado:
`gsc-googleadsfreelancer-*-2026-10-26.csv` e `volumes-us-2026-10-26.csv`.

Comparação com o estudo de 06/10: naquela leitura o site tinha 2 cliques e cerca de 170 impressões em 90 dias.

## 1. Onde o site está

**Números.** 90 dias: 1.803 impressões, 4 cliques. Últimos 28 dias: 1.753 impressões, 4 cliques. Os 28 dias
anteriores: 50 impressões, 0 cliques. Ou seja, quase tudo aconteceu depois de 7 a 13 de outubro, quando as 24 páginas
novas entraram no índice. A média diária subiu de 10 a 20 impressões para 60 a 95. Posição média entre 65 e 75.

**Índice.** 29 das 30 páginas indexadas. A exceção é `/conversion-tracking-setup/`: "Descoberta, não indexada",
nunca rastreada, apesar de estar no sitemap desde 09/10, no menu de serviços de todas as páginas e em 32 links de
conteúdo. O Google sabe que ela existe (cita três páginas que apontam para ela) e ainda não gastou rastreio nela.
`/youtube-ads-management/` e `/google-ads-for-dentists/` estão indexadas e com 0 impressões: posição acima de 100.

**De onde vem.** EUA 61% das impressões, Reino Unido 13% (vazamento que o .uk deveria pegar; posições 75 a 90, sem
efeito prático), Canadá 5%, depois Holanda, Austrália, Índia. 87% em desktop: busca de empresa, não de celular.

**Os 4 cliques** vieram da home, `/about/` (posição 4, busca pelo nome), `/google-ads-setup/` e `/google-ads-audit/`.
Nenhum clique em termo comercial genérico ainda.

**O Google já associa cada termo à página certa.** Isso é o principal sinal positivo: o trabalho de página está feito.

| Termo (28 dias) | Impressões | Posição | Página que aparece | Volume EUA/mês |
|---|---|---|---|---|
| google ads consultant | 298 | 73 | /google-ads-consultant/ | 390 |
| microsoft ads management | 117 | 80 | /microsoft-ads-management/ | 210 |
| google ads expert | 113 | 72 | /google-ads-expert/ | 880 |
| google ppc consultant | 72 | 49 | /freelance-ppc-consultant/ (e mais 3) | 210 |
| freelance ppc consultant | 60 | 25 | /freelance-ppc-consultant/ | 20 (UK 90) |
| google ads consultation | 48 | 33 | /google-ads-consultation/ | 390 |
| google ads freelancer | 32 | 62 | / (e /faq/) | 140 (UK 140) |
| ppc management (for) small business | 42 | 90 | /small-business-ppc-management/ | 110 + 110 |
| flat fee ppc management | 18 | 85 | /ppc-management/ | 0 |
| google ads setup service(s) | 28 | 70 | /google-ads-setup/ | 0 |
| white label ppc pricing | 17 | 81 | /white-label-ppc/ | 20 (white label ppc: 170) |
| ppc consultant | 9 | 41 | /freelance-ppc-consultant/ | 210 |
| contract ppc consultant | 4 | 4,8 | /freelance-ppc-consultant/ | (ppc contractor: 90) |

**As páginas mais perto da primeira página** são `/freelance-ppc-consultant/` (posição 22 a 41 em "freelance ppc
consultant", "adwords ppc consultant", "google ppc consultant", "ppc consultant", "ppc freelancer") e
`/google-ads-consultation/` (33). Tudo o mais está entre 60 e 95.

**Um sinal de alerta.** `/google-ads-expert/` teve 17, 26, 56, 70 e 46 impressões por dia entre 11 e 15/10 e depois
caiu para zero, onde está há oito dias. `/google-ads-consultant/`, no mesmo período, ficou estável em 25 a 39 por dia.
O Google testou a página de expert, não gostou, e hoje ela está fora das 100 primeiras. As duas páginas, mais
`/freelance-ppc-consultant/`, `/google-ads-consultation/` e a home, disputam a mesma família de termos (consultant,
expert, specialist, freelancer); "google ppc consultant" aparece em quatro páginas diferentes. Não é grave com um
mês de vida, mas é a parte do site que precisa de hierarquia.

**Buscas que não são demanda.** Termos como `site:linkedin.com/posts "hire a freelancer" ...` e
`site:reddit.com cerco uno specialista google ads` (posição 1 a 3) são as buscas de prospecção das rotinas do próprio
Diego, em que o Google inclui o site nos resultados. Ignorar na leitura.

## 2. O que segura o site: autoridade, não conteúdo

**Links reais: dois domínios, os dois do Diego.** diwizi.com (4 links) e ppcconsultancy.uk (37, metade hreflang).
Nenhum terceiro aponta para o site. Com 30 páginas bem mapeadas e zero autoridade externa, posição 60 a 90 é o
resultado esperado, e nenhuma troca de título muda isso sozinha.

**O surto de 2.690 domínios de hoje.** O DataForSEO lista 2.690 domínios apontando para o site, todos vistos pela
primeira vez em 26/10/2026, com pontuação de spam 35 a 45, em TLDs .shop, .store, .site, .space, .online
(freebacklink.site, seoscore.space, buyadulttraffic.space e similares). São páginas geradas automaticamente por
"ferramentas de SEO" de spam; o mesmo aconteceu com diwizi.com (2.741) no mesmo dia. O Google ignora esse tipo de
link. Não contratar desautorização (disavow), não responder a quem oferecer "limpeza"; só olhar de vez em quando a
aba Ações manuais do Search Console.

**Quem ranqueia hoje nos EUA** (SERP ao vivo):

- "freelance ppc consultant": Freelancer.com, Reddit (r/PPC), um blog sobre tarifas de freelancer, um blog "como
  virar freelancer de PPC", Indeed, newsletter, Upwork, ZipRecruiter. Intenção mista (metade quer emprego), nenhum
  site de consultor forte.
- "google ads consultant": GrowTal (marketplace), Reddit ("Looking for a Google Ads Consultant", r/PPC), um site de
  ferramenta, Upwork, Indeed, Quora, Coursera, Upwork de novo.

Leitura: a primeira página é fraca em sites de consultores, então uma página de serviço com alguma autoridade
chega à página 1 ou 2. Mas parte de quem busca esses termos procura trabalho, não contratação, e o CTR vai refletir
isso. Os threads do r/PPC ranqueando em segundo e terceiro nas duas buscas são também o lugar onde os compradores
estão perguntando.

## 3. Ajustes na página, em ordem de valor

1. **Pedir indexação de `/conversion-tracking-setup/`** no Search Console (Inspecionar URL, Solicitar indexação).
   Um minuto, só o dono consegue. É a única página do site que o Google ainda não leu.
2. **Home: colocar "Google Ads freelancer" no H1 e na primeira frase.** O título já tem; o H1 ("Google Ads, run by
   the senior specialist you hired") não. A home está na posição 62 para o próprio nome do site, e `/faq/` aparece
   junto. Proposta de H1: "A Google Ads freelancer with 14+ years on the account: the senior specialist you hire is
   the one who runs it. Meta and Microsoft when they fit."
3. **Hierarquia do grupo consultant / expert / freelancer.** Um termo principal por página e âncoras internas
   coerentes:
   - `/freelance-ppc-consultant/`: "PPC consultant", "freelance PPC consultant", "PPC contractor" (já está em 4,8
     para "contract ppc consultant"; "ppc contractor" tem 90 buscas/mês).
   - `/google-ads-consultant/`: "Google Ads consultant" e "Google Ads consulting" (320 buscas/mês, CPC US$ 147, hoje
     ausente do título; trocar "PPC Consulting & Strategy" por "Google Ads Consulting & Strategy").
   - `/google-ads-expert/`: "Google Ads expert" e "specialist" (720 e 390 buscas/mês para specialist).
   - home: "Google Ads freelancer".
   - Toda âncora "PPC consultant" e "Google PPC consultant" no conteúdo aponta para `/freelance-ppc-consultant/`;
     toda âncora "Google Ads consultant" aponta para `/google-ads-consultant/`.
4. **Dar peso interno a `/freelance-ppc-consultant/`.** É a página mais bem posicionada e a menos linkada entre as
   de serviço: 8 links de conteúdo (pricing tem 74, management 38, audit 36) e está fora do painel de serviços do
   desktop (só no menu do celular e no rodapé). Incluir no painel e em duas ou três frases de páginas fortes.
5. **Microsoft: título com "Microsoft Ads".** A página soma 200 impressões por "microsoft ads management" e "bing
   ads management" e o título diz "Microsoft Advertising Management". Mesmo volume (210), concorrência média, CPC
   baixo, poucos consultores disputam. Proposta: "Microsoft Ads Management | Bing Ads Run by a Freelance Specialist".
6. **Small business: a página mais fina (803 palavras) mira o maior termo do site.** "google ads for small
   business" tem 1.600 buscas/mês nos EUA, concorrência baixa, CPC US$ 62, e a página só aparece para as variantes
   "ppc management small business" na posição 90. Vale a única expansão de conteúdo deste ciclo: uma tabela do que
   US$ 1.000, 3.000 e 10.000 por mês compram em cliques e leads por setor (estimativas de mercado), quando não vale
   anunciar, fazer sozinho ou contratar, e um FAQ "How much should a small business spend on Google Ads?". Meta:
   1.300 a 1.500 palavras. Precisa de aprovação do texto.
7. **Não mexer** em `/ppc-management/` e `/google-ads-management/`: "ppc management services" (1.000/mês) e "google
   ads management services" (590/mês) já estão nos títulos; a posição 80 ali é autoridade, não página.

## 4. Autoridade: o que fazer fora do código (dono)

- **r/PPC.** Os threads "Looking for a Google Ads consultant" e "Advice for finding PPC freelancer" ranqueiam em
  segundo e terceiro lugar nas duas buscas principais. Responder com substância, sem vender, com o site no perfil.
  É o canal mais barato que existe para estes termos, e o único que o relatório mostra funcionando hoje.
- **LinkedIn.** A página da empresa já existe; o campo "site" do perfil pessoal e da página devem apontar para
  googleadsfreelancer.com, não só para diwizi.com.
- **Perfis.** Clutch, Sortlist e ZoomInfo foram feitos para a Diwizi. Onde for possível um segundo perfil, ou o
  campo de site aceitar dois, incluir o .com. Cal.com e o rodapé de e-mail também.
- **Uma peça publicável por mês** fora do site: o caso de Houston contado em artigo convidado em blog de PPC ou em
  podcast, com link. Um link editorial de um site do setor vale mais do que todos os diretórios.
- **Prazo.** Reler o Search Console em 30 dias (26/11). O que se espera ver: as páginas de consultant e freelance
  saindo da faixa 25 a 75 para 15 a 40, e os primeiros cliques não-marca. Se nada se mover, o problema é link, e aí
  vale investir em divulgação em vez de em páginas.

## 5. O que não fazer

- Não criar páginas novas agora. São 30 páginas e dois domínios de link; o gargalo é autoridade, não cobertura.
- Não comprar links, não disavow do spam de hoje, não trocar títulos toda semana (cada troca zera o teste do Google).
- Não tentar ranquear "google ads help" (1.300/mês): é busca de suporte da plataforma, não de contratação.
