# Estudo: mais paginas nos dois sites (06/10/2026)

Fontes: Search Console dos dois dominios (90 dias, 07/07 a 04/10/2026, via API) e volume de busca do Google Ads
(DataForSEO, um pedido por mercado, 189 termos; US$ 0,36 no total porque o MCP truncou a primeira resposta).
CSVs ao lado: `volumes-paginas-us-uk-2026-10-06.csv`, `gsc-*-query-page-90d-2026-10-06.csv`.

## 1. O que o Search Console diz (pouco, mas util)

Os dois sites sao novos. Em 90 dias: googleadsfreelancer.com teve 2 cliques e cerca de 170 impressoes;
ppcconsultancy.uk teve 0 cliques e cerca de 640 impressoes, quase tudo entre a posicao 60 e 100. O GSC nao mede
demanda ainda; mostra para quais termos o Google ja associa cada pagina. Sete achados:

1. **ppcconsultancy.uk nao tem pagina de "Google Ads consultant"** e mesmo assim esse termo e o que mais aparece
   (49 impressoes, posicao 88), caindo na pagina de management. E a maior lacuna do .uk: 210 buscas/mes no UK.
2. **O .uk ja recebe buscas por cidade** na pagina de management: Belfast, Edinburgh, Glasgow, Milton Keynes,
   Salford, Slough, Brentwood, Knowle. O Google trata o site como servico local, o que sustenta paginas de cidade.
3. **"ppc consultancy" esta dividido** entre home (45), agency-vs-consultant (18), London (16), management (3) e
   results (1). Nao e grave, mas a home deve ficar como alvo unico desse termo nos links internos.
4. **A pagina /landing-pages/ do .uk ranqueia melhor que a home** para "ppc consultant uk" (26), "google ads
   consultancy" (37) e "google ads consultant london" (8). Sinal de que o Google ainda nao entendeu a hierarquia;
   melhora com a pagina de consultant e com ancoras internas.
5. **/ppc-audit/ do .uk e a pagina mais fina (597 palavras) e ja tem 67 impressoes** ("ppc audit services",
   "ppc audit agency"). Enriquecer antes de criar coisa nova.
6. **No .com, "contract ppc consultant" esta na posicao 4,8** (UK) e "ppc contractor" tem 210 buscas/mes nos EUA.
   O site nao usa a palavra "contractor".
7. **No .com, "google ads for small business" tem 1.900 buscas/mes nos EUA** e a pagina de small business e
   intitulada "Small Business PPC Management" (170/mes). Trocar o titulo e a frase principal vale mais que uma
   pagina nova.

## 2. Volume de busca: onde ha demanda que os sites nao cobrem

Volumes mensais (US / UK). Termos com 0 nos dois mercados foram descartados: flat fee, fractional, interim, part
time, hourly rate, agency vs consultant, second opinion, Performance Max consultant, setup service, consent mode,
server-side tagging, copywriting, "ppc for agencies".

### Servicos que um site tem e o outro nao

| Pagina | Termos e volume | Falta em |
|---|---|---|
| Google Ads consultant | google ads consultant 390 / 210; google ads consultation 390 / 210 | .uk |
| E-commerce PPC | ecommerce ppc agency 260 / 480; google shopping management 70 / 210; ecommerce ppc management 170 / 90; shopify google ads 390 / 70 | .uk |
| LinkedIn Ads | linkedin ads management 2.400 / 1.000; linkedin ads agency 390 / 260 | .uk |
| Facebook Ads | facebook ads management 60.500 / 12.100 (intencao mista, CPC baixo); facebook ads freelancer 90 / 50 | .uk (no .com, titular com "Facebook Ads Management" antes de "Meta") |
| Microsoft Ads | bing ads management 260 / 170; microsoft advertising agency 90 / 170 | .uk |
| Small business | google ads for small business 1.900 / 210; ppc for small business 210 / 110 | .uk (no .com, retitular) |
| B2B PPC | b2b ppc agency 210 / 170; b2b ppc 170 / 140; lead generation ppc 210 / 140 | .com |
| Landing pages e CRO | conversion rate optimisation consultant 210 / 110; landing page consultant 30 / 10 | .com |
| White label | white label ppc 260 / 90; white label google ads 170 / 50 | .uk (menor prioridade) |

### Servicos novos, dentro do que ja e oferecido

| Pagina | Termos e volume | Site |
|---|---|---|
| Google Ads expert / specialist | google ads expert 880 / 260; google ads specialist 720 / 320; ppc specialist 480 / 320; ppc expert 170 / 320 | .com como /google-ads-expert/, .uk como /ppc-specialist/ |
| YouTube Ads management | youtube ads management 480 / 90; youtube ads agency 210 / 110; demand gen google ads 590 / 260 (parte informacional) | .com primeiro |
| PPC contractor | ppc contractor 210 / 30; GSC ja mostra "contract ppc consultant" em 4,8 | .com |
| GA4 e Tag Manager consultant | google analytics consultant 260 / 90; gtm consultant 170 / 90; google tag manager consultant 90 / 70 | .com: retitular /conversion-tracking-setup/ (o .uk ja usa esse titulo) |
| Consultation (sessao avulsa) | google ads consultation 390 / 210; ppc consultation 210 / 320; google ads coaching 90 / 10 | ambos, se Diego quiser vender a hora avulsa |
| Google Ads training | 1.300 / 720 | decisao de Diego: e um servico novo (treinar equipe interna) |
| Remarketing | remarketing agency 140 / 170 | ambos, prioridade baixa |

### Setores

| Setor | Termos e volume | Observacao |
|---|---|---|
| Law firms | ppc for law firms 720 / 480 (CPC US$ 112); google ads for lawyers 260 / 50 | Maior CPC da lista: cliente de alto valor. Sem caso proprio, escrever sem claims. |
| Dentists | google ads for dentists 390 / 90; ppc for dentists 170 / 50 | .com |
| Home services | hvac ppc 170; google ads for contractors 170; plumber ppc 110; google ads for electricians 70 | .com, com o caso de Houston |
| Healthcare | healthcare ppc 170 / 90; google ads for doctors 110 / 20 | ambos; ja e setor declarado |
| SaaS | saas ppc agency 140 / 90; saas ppc 110 / 50 | ambos; o .uk ja recebe buscas longas de SaaS na pagina de tracking |
| Real estate | google ads for real estate 390 / 10 | .com, prioridade media |
| Nonprofits e Ad Grants | google ads for nonprofits 720 / 30; google ad grants management 110 / 30 | so se Diego ja operou Ad Grants |
| Charities (UK) | ppc for charities 110 | mesma ressalva |
| Hotels | ppc for hotels 70 / 70 | baixa |

### Cidades

UK: ppc agency manchester 480, birmingham 480, leeds 260, bristol 260, glasgow 110, edinburgh 50; "ppc consultant
manchester/birmingham/bristol" 20 cada. O termo com volume e "agency", e a pagina de consultor compete com ele
mostrando a comparacao agencia vs consultor, como a de Londres (210) ja faz.

EUA e Canada: ppc agency houston 210, new york 170, chicago 90, toronto 40. "ppc consultant <cidade>" fica em 0 a 10.
So Houston se justifica agora, por causa do caso de HVAC de Houston.

## 3. Plano, em ordem

**Fase 0, sem pagina nova (uma tarde):**
- .com /small-business-ppc-management/: titulo e H1 com "Google Ads for Small Business" (1.900/mes).
- .com /meta-ads-management/: titulo comecando por "Facebook Ads Management".
- .com /conversion-tracking-setup/: titulo "GA4 & Google Tag Manager Consultant | Conversion Tracking Setup".
- .com /freelance-ppc-consultant/: um H2 e uma FAQ com "PPC contractor" e "contract".
- .uk /ppc-audit/: levar de 597 para cerca de 1.000 palavras, com "PPC audit services" e a comparacao com
  auditoria de agencia.
- .uk: links internos com ancora "PPC consultancy" apontando so para a home.

**Fase 1, espelhar o que ja existe no outro site (10 paginas):**
- .uk: google-ads-consultant, ecommerce-ppc, linkedin-ads-management, facebook-ads-management,
  microsoft-ads-management, google-ads-for-small-business.
- .com: b2b-ppc, landing-pages, youtube-ads-management, google-ads-expert.

**Fase 2, setores (8 paginas):** law firms (ambos), home services (.com), dentists (.com), healthcare (ambos),
SaaS (ambos). Depois .uk /ppc-specialist/ e, se Diego decidir vender, /google-ads-consultation/ nos dois.

**Fase 3, cidades (5 paginas):** .uk Manchester, Birmingham, Leeds, Bristol no modelo da pagina de Londres
(tabela de CPC por cidade, setores locais, agencia vs consultor); .com Houston com o caso.

Resultado: .com de 18 para cerca de 31 paginas, .uk de 14 para cerca de 30. Soma de volume dos termos
principais cobertos por pagina nova: cerca de 9.000 buscas/mes nos EUA e 6.000 no UK, sem contar
"facebook ads management", que sozinho e maior que tudo isso mas tem intencao mista.

## 4. O que nao fazer

- Paginas de "flat fee", "fractional", "interim", "hourly rate" e "agency vs consultant" como alvo de busca: volume
  zero. Servem como argumento dentro de outras paginas, nao como URL.
- Cidades dos EUA alem de Houston, e Dublin: volume de 0 a 20.
- Setores sem experiencia declarada (Ad Grants, charities, hotels, automotivo) ate Diego confirmar.
- Nada de novo em claims: as paginas de setor descrevem o metodo e o que muda no setor, sem resultados que nao
  existam. Sem travessao.
