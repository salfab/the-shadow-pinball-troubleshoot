# Liste d'achats — réparation de la Power Driver (A-12697-3)

> Préparée le 01/11/2026 pour la séance au banc, mise à jour le 02/11/2026. Seul **Q82** est certainement défectueux ; le reste est une réserve bon marché pour ne pas bloquer la séance si un test révèle une autre pièce abîmée.
>
> ⚠️ **Boîtier du TIP36C :** prendre le **TO-247 (ou TO-218 / TO-3P)**, comme l'original : plastique large, trou de fixation. Pas le TO-220, plus petit.
> ⚠️ **Fusibles :** **6,3 × 32 mm**, temporisés (T). Pas 5 × 20 mm.

**Légende des tableaux** : prix **par pièce, en CHF**, tels qu'affichés sur chaque site (voir la section « Sources » pour HT/TTC). **Gras** = le moins cher qui répond au besoin. « n.v. » = non vérifié. « — » = introuvable. Les quantités à commander (colonne *Qté*) comptent une petite marge.

## Résultat des tests au banc du 05/11/2026 (carte sortie, tests en circuit)

- **Défectueux, confirmé :** **Q82** (TIP36C, court-circuit C-E), **Q86** (TIP102 d'une rangée de lampes, court-circuit C-E), **R153** (0,22 Ω 1 W, coupée). La résistance 0,22 Ω passe donc d'« réserve » à **indispensable** (1 pièce, le reste en réserve).
- **Q86 :** un TIP102 du stock Reichelt, rien à commander.
- **Sains :** les 7 autres 0,22 Ω, les TIP102 des rangées (Q83–Q85, Q87–Q90), les **8 TIP107** des colonnes (les TIP107 deviennent une simple réserve, non nécessaire), Q32 et D11 (réparation de l'utilisateur), les autres TIP102 des sorties (à remesurer le 06/11) et **toutes les diodes 1N4004** (vérifiées deux fois).
- **Étage Sol 01 (Q81, Q71, R123–R125) :** remplacé comme prévu ; Q81 (ST TIP102) sera remesuré hors circuit.
- **En suspens :** C7 (15 000 µF, dépôt gris sur le dessus) ; pied, soudures et bombement à inspecter avant d'ajouter C6/C7 à la commande.

## Déjà en stock ?

- **TIP102 × 10** (Reichelt « TIP 102 MBR », NPN Darlington TO-220 100 V 8 A 80 W, acheté il y a 2–3 ans) : c'est le **bon modèle** et il y en a plus qu'il n'en faut (4 prévus). **Ne pas en recommander.**
- **Tresse à dessouder EL 235** (Reichelt) : si elle est encore dans le tiroir, la retirer de la commande.
- Vérifier aussi s'il reste de la **soudure au plomb**, du **flux** et des **fusibles 6,3 × 32**.

## 1. Les pièces, distributeur par distributeur

### 1.1 Indispensable

| Pièce | Qté | Distrelec | Mouser | Conrad | Reichelt |
|---|---|---|---|---|---|
| **TIP36C** — Q82, sortie de la Sol 01 (en court-circuit). PNP 100 V 25 A, **TO-247 / TO-218 / TO-3P** | 2 | **—** (aucun résultat) | **2.62** · ST TIP36C, TO-247-3 · 3 528 en stock · [lien](https://www.mouser.ch/en/ProductDetail/STMicroelectronics/TIP36C?qs=JV7lzlMm3yLzusij15X%2FdA%3D%3D). Variante : onsemi TIP36CG, 3.94 | **1.75** · ST TIP36C, TO-247-3 · 46 en stock · [lien](https://www.conrad.ch/fr/search.html?search=TIP36C) | **1.17** · « TIP 36C STM », ST, **TO-247** · en stock · [lien](https://www.reichelt.com/ch/fr/shop/produit/transistor_de_puissance_pnp_100v_25a_125w_to-247-21503). Variantes : TO-3PN 0.97, TO-218 1.20 (stock limité) |

### 1.2 Réserve : chaîne de commande de la Sol 01

| Pièce | Qté | Distrelec | Mouser | Conrad | Reichelt |
|---|---|---|---|---|---|
| **TIP102** — Q81 et pilotes de rangées Q83–Q90. NPN Darlington 100 V 8 A, TO-220 | 4 | 7.41 TTC le sachet de 5 · 445 en stock · [lien](https://www.distrelec.ch/fr/darlington-transistor-npn-100-hfe-200-to-200-5pcs-st-tip102/p/30505942) | 1.59 · ST TIP102 · 4 875 en stock · [recherche](https://www.mouser.ch/c/?q=TIP102) | — (seulement TIP120 / TIP121, non équivalents) | ✅ **Déjà acheté** (10 en stock) |
| **2N5401** — Q71. PNP 150 V, TO-92 | 2 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=2N5401) | 0.145 · Diotec · 17 932 en stock · [recherche](https://www.mouser.ch/c/?q=2N5401) | 0.037 · Diotec · 872 en stock · [recherche](https://www.conrad.ch/fr/search.html?search=2N5401) | **0.05** · « 2N 5401 » · en stock · [lien](https://www.reichelt.com/ch/fr/shop/produit/transistor_bipolaire_pnp_160v_0_6a_0_625w_to-92-2053) |
| **1N4004** — roue libre (D17–D32) et « tieback » (D5–D12). DO-41 | 5 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=1N4004) | 0.137 · Diotec · 194 379 en stock · [recherche](https://www.mouser.ch/c/?q=1N4004) | 0.03 · Diotec · 20 387 en stock · [recherche](https://www.conrad.ch/fr/search.html?search=1N4004) | **0.02** · « 1N 4004 » · en stock · [lien](https://www.reichelt.com/ch/fr/shop/produit/diode_de_redressement_do41_400_v_1_a-1726) |
| **Résistance 68 Ω ½ W** — R124. Traversante | 2 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=resistance%2068%20ohm%200.5W) | 0.29 · Vishay NFR25H0006809JR500 · 11 443 en stock · **puissance à confirmer** sur la fiche · [recherche](https://www.mouser.ch/c/?q=68%20ohm%200.5W%20through%20hole%20resistor) | **0.04** · Weltron 405116, carbone, 0,5 W · 1 510 en stock · [recherche](https://www.conrad.ch/fr/search.html?search=r%C3%A9sistance%2068%20ohm%200%2C5W%20traversante) | 0.08 · METALL 68,0, métal, 0,6 W, 1 % · en stock · [recherche](https://www.reichelt.com/ch/en/shop/search/metal%20film%20resistor%2068%20ohm) |
| **Résistance 220 Ω ¼ W** — R125. Traversante | 2 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=resistance%20220%20ohm%200.25W) | 0.095 · KOA CFS1/4CT52R221J · 7 142 en stock · [recherche](https://www.mouser.ch/c/?q=220%20ohm%200.25W%20through%20hole%20resistor) | **0.02** · TRU Components, métal, 0,25 W · 5 206 en stock · [recherche](https://www.conrad.ch/fr/search.html?search=r%C3%A9sistance%20220%20ohm%200%2C25W) | 0.07 · METALL 220, métal, 0,6 W · en stock · [recherche](https://www.reichelt.com/ch/en/shop/search/metal%20film%20resistor%20220%20ohm) |
| **Résistance 2,7 kΩ ¼ W** — R123. Traversante | 2 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=resistance%202.7k%200.25W) | **0.112** · Yageo CFR25SJT-26-2K7 · 10 416 en stock · [recherche](https://www.mouser.ch/c/?q=2.7k%200.25W%20through%20hole%20resistor) | — (la recherche a renvoyé des 27 kΩ) | **0.11** · « 1/4W 2,7K », carbone · en stock · [recherche](https://www.reichelt.com/ch/en/shop/search/1%2F4W%202%2C7K) |

### 1.3 Réserve : zone des lampes qui a « brillé »

| Pièce | Qté | Distrelec | Mouser | Conrad | Reichelt |
|---|---|---|---|---|---|
| **TIP107** — pilotes des colonnes (Q91–Q98). PNP Darlington 100 V 8 A, TO-220 | 2 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=TIP107) | **1.26** · ST TIP107 · 5 126 en stock · [recherche](https://www.mouser.ch/c/?q=TIP107) | — | 0.96 · « TIP 107 MBR » · ⚠️ **indisponible avant le 06/02/2027** · [lien](https://www.reichelt.com/ch/fr/shop/produit/transistor_darlington_pnp_100v_8a_80w_to-220-21462) |
| **Résistance 0,22 Ω 1 W** — R150–R153, R172–R175 (mesure des rangées). Axiale | 4 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=resistance%200.22%20ohm%201W) | 0.233 · Yageo KNP100JR-73-0R22 · 9 396 en stock · [recherche](https://www.mouser.ch/c/?q=0.22%20ohm%201W%20resistor) | **0.136** · Yageo KNP100JT-73-0R22 (prix remisé) · 300 en stock · [recherche](https://www.conrad.ch/fr/search.html?search=r%C3%A9sistance%200%2C22%20ohm%201W) | ⚠️ **pas de 1 W** : seulement 5 W (0.28, 25 mm de long) ou plus, plus encombrantes que l'original · [recherche](https://www.reichelt.com/ch/en/shop/search/wirewound%200.22%20ohm%201%20W) |

### 1.4 Fusibles 6,3 × 32 mm, temporisés

| Pièce | Qté | Distrelec | Mouser | Conrad | Reichelt |
|---|---|---|---|---|---|
| **T5A 250 V** — remplacement de F108 et réserve GI (F106–F110) | 3 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=fusible%206.3x32%205A%20temporis%C3%A9) | 4.02 · Schurter SPT 0001.2531 · 558 en stock · [recherche](https://www.mouser.ch/c/?q=6.3x32%20time%20delay%20fuse%205A%20250V) | **3.10 le sachet de 10** · Püschel FSUT5,0B · 52 en stock · [recherche](https://www.conrad.ch/fr/search.html?search=fusible%206%2C3%20x%2032%20mm%205%20A%20temporis%C3%A9) | 1.70 · Littelfuse 0326005.MXP, tube **céramique** · en stock · [recherche](https://www.reichelt.com/ch/en/shop/search/Fuse%206.3x32mm%205A%20Slow-blow) |
| **T3A 250 V** — réserve pour F101–F105 | 3 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=fusible%206.3x32%203A%20temporis%C3%A9) | 3.78 · Schurter SPT 3,15 A 0001.2529 · 463 en stock · pas de 3 A exact · [recherche](https://www.mouser.ch/c/?q=6.3x32%20time%20delay%20fuse%203A%20250V) | **3.10 le sachet de 10** · Püschel FSUT3,15B (3,15 A) · 40 en stock · [recherche](https://www.conrad.ch/fr/search.html?search=fusible%206%2C3%20x%2032%20mm%203%2C15%20A%20temporis%C3%A9) | 0.94 · Littelfuse 0313003.HXP, 3 A, **verre** · ⏳ livrable le **09/11/2026** · [recherche](https://www.reichelt.com/ch/en/shop/search/Fuse%206.3x32mm%203A%20Slow-blow) |

### 1.5 Consommables de soudure (si pas déjà en stock)

| Pièce | Qté | Distrelec | Mouser | Conrad | Reichelt |
|---|---|---|---|---|---|
| **Flux** sans nettoyage, stylo ou seringue | 1 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=flux%20soudure) | 6.40 · Chip Quik CQ4LF, stylo 10 ml · 1 036 en stock · [recherche](https://www.mouser.ch/c/?q=no%20clean%20flux%20pen) | — (seulement du flux liquide au litre, 24.95) | **5.98** · Stannol X32-10i, stylo 10 ml · en stock · [recherche](https://www.reichelt.com/ch/en/shop/search/flux%20pen). Autre : gel CW 8500, 17.03 |
| **Tresse à dessouder** (2 à 2,5 mm) | 1 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=tresse%20%C3%A0%20dessouder) | 2.15 · Soldered 555022, 2 mm · 900 en stock · [recherche](https://www.mouser.ch/c/?q=desoldering%20braid) | **2.10** · Stannol Solder Ex, 2,5 mm × 1,6 m · 1 021 en stock · [recherche](https://www.conrad.ch/fr/search.html?search=tresse%20%C3%A0%20dessouder) | 4.25 · CFH EL 235, 2 mm × 1,6 m · en stock · [recherche](https://www.reichelt.com/ch/en/shop/search/desoldering%20braid) |
| **Soudure fine au plomb** (Sn60/Pb40 ou Sn63/Pb37, 0,5 à 0,8 mm), petite bobine | 1 | n.v. · [recherche](https://www.distrelec.ch/fr/search?q=soudure%20Sn60Pb40%200.8mm) | **11.21** · Chip Quik SMDSW.031, 63/37 no-clean, 0,8 mm, 1 oz · 54 en stock · [recherche](https://www.mouser.ch/c/?q=Sn63Pb37%20solder%20wire) | — (seulement du sans plomb) | — (60/40 et 63/37 ne renvoient rien d'utile) |

### 1.6 Ampoule de flasher (hors tableau)

- [ ] **Ampoule de flasher** × 2 — flasher Sol 26 de la tête. Probablement une **#906** (culot à coin) : **vérifier d'abord celle en place** avant de commander. Plutôt chez un revendeur de pièces de flipper (par exemple [Marco Specialties](https://www.marcospecialties.com/), qui livre à l'international). Disponibilité chez les quatre distributeurs ci-dessus : non vérifiée.

## 2. Combien ça coûte, port compris

Total de la liste ci-dessus **sans les TIP102** (déjà en stock) et en prenant, pour chaque distributeur, la référence listée. Un sachet de 10 fusibles chez Conrad (2 sachets, un par calibre) couvre le besoin.

| | Distrelec | Mouser | Conrad | Reichelt |
|---|---|---|---|---|
| **Marchandises** | impossible (pas de TIP36C) | ≈ 53.82 | ≈ 12.69 | ≈ 19.56 (+ 2.82 pour le T3A, dès le 09/11) |
| **Frais de port vers la Suisse** | n.v. | 23.00 (UPS) | 9.95 (CHF 15.95 pour un professionnel) | ≈ 9.50 (DPD, € 10.33, jusqu'à 10 kg) |
| **Gratuit dès** | n.v. | CHF 70 (sur la plupart des commandes) | CHF 200 | non trouvé |
| **Total, port compris** | — | **≈ 76.82** | ≈ 22.64 | **≈ 29.06** |
| **Ce qui manque** | tout ou presque | rien | TIP107, 2,7 kΩ, flux, soudure | TIP107, T3A (dès le 09/11), 0,22 Ω 1 W, soudure |

*Détail Mouser* : TIP36C 5.24 + 2N5401 0.29 + 1N4004 0.69 + 68 Ω 0.58 + 220 Ω 0.19 + 2,7 kΩ 0.22 + TIP107 2.52 + 0,22 Ω 0.93 + fusibles 23.40 + flux 6.40 + tresse 2.15 + soudure 11.21.
*Détail Conrad* : TIP36C 3.50 + 2N5401 0.07 + 1N4004 0.15 + 68 Ω 0.08 + 220 Ω 0.04 + 0,22 Ω 0.55 + 2 sachets de fusibles 6.20 + tresse 2.10.
*Détail Reichelt* : TIP36C 2.34 + 2N5401 0.10 + 1N4004 0.15 + 68 Ω 0.16 + 220 Ω 0.14 + 2,7 kΩ 0.22 + 0,22 Ω en 5 W 1.12 + T5A 5.10 + flux 5.98 + tresse 4.25.

Si la tresse est déjà dans le tiroir, retirer 2.15 (Mouser), 2.10 (Conrad) ou 4.25 (Reichelt).

## 3. Recommandation

1. **Le moins cher : Reichelt, ≈ CHF 29 port compris.** Il a **le TIP36C en TO-247** (CHF 1.17, en stock), qui est la seule pièce indispensable, et la plus grande partie de la réserve.
2. **Ce que Reichelt ne couvre pas** : la **soudure au plomb** (à prendre dans un magasin local, ou chez Mouser à CHF 11.21), les **TIP107** (non essentiels, en rupture jusqu'en juin 2027) et la **résistance 0,22 Ω 1 W** (la 5 W de Reichelt, **après avoir vérifié la place** sur la carte ; sinon Conrad ou Mouser). Un second distributeur ajoute son port (CHF 9.95 ou 23) : à éviter si une alternative locale existe.
3. **Tout au même endroit : Mouser, ≈ CHF 77** (≈ CHF 70 si on complète le panier jusqu'à CHF 70 pour obtenir la gratuité du port). Plus cher, mais un seul envoi et rien ne manque.
4. **Conrad seul** ne suffit pas (pas de TIP107, 2,7 kΩ, flux ni soudure), mais il est le moins cher pour les fusibles (10 pour CHF 3.10) et le 0,22 Ω.

## Sources et réserves

- **Reichelt** (reichelt.com/ch, relevé le **02/11/2026** dans le navigateur intégré) : prix en CHF **TTC (TVA suisse 8,1 %)** ; pas de douane ni de TVA à l'importation pour la Suisse ; livraison 3–4 jours ouvrés pour ce qui est en stock. Frais de port : [page officielle](https://www.reichelt.com/ch/en/shop/service/-12_28).
- **Mouser** (mouser.ch, relevé le **01/11/2026**) : prix unitaires pour 1 pièce (dégressifs) ; HT ou TTC **non précisé** sur la page, à contrôler au panier. Port lu au panier (une pièce mise au panier puis retirée, rien commandé) ; droits et douane payés par Mouser (DDP). Boîtier confirmé sur fiche seulement pour le TIP36C (TO-247-3).
- **Conrad** (conrad.ch, relevé le **01/11/2026**) : prix **TTC**, plus frais de port ; livraison annoncée le 5 novembre pour les pièces en stock. Frais de port : [aide Conrad](https://help.conrad.ch/hc/fr-ch/articles/360001281777-A-combien-s-%C3%A9l%C3%A8vent-les-frais-de-port-standard-chez-Conrad).
- **Distrelec** : seules deux pages ont pu être lues avant un **CAPTCHA** (Radware), non contourné. Tout le reste est « n.v. » (à contrôler à la main).
- Les prix et les stocks changent : **recontrôler au moment de commander**.

**À vérifier au moment de commander :** la tension (au moins celle indiquée), le boîtier (TO-247 / TO-218 pour le TIP36C, TO-220 pour TIP102 et TIP107), la puissance de la résistance 68 Ω (≥ ½ W), la taille des fusibles (6,3 × 32 mm, pas 5 × 20 mm) et la place disponible pour une 0,22 Ω de 5 W.
