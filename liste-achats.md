# Liste d'achats — réparation de la Power Driver (A-12697-3)

> Version du **09/11/2026** : comparaison avec **Farnell**. Panier Farnell monté : 12 lignes sur 14, **CHF 36.54 TVA et port compris**, mais ni flux ni fusible 3/8 A (voir « Variante Farnell », en fin de fichier).
>
> Version du 07/11/2026 : compatibilité vérifiée contre la liste des pièces du manuel, liens directs Mouser, **panier Mouser monté et chiffré : CHF 55.31 port compris, hors TVA** (voir « Liste de courses finale »). Tests de la carte sortie : 05 et 06/11, détail dans `journal-diagnostic-the-shadow.md`, §4, lignes S3-*.
>
> **Pièces défectueuses, confirmées par mesure :** Q82 (TIP36C, Sol 01), Q86 (TIP102, rangée de lampes) et R153 (0,22 Ω 1 W, coupée).

## Panier Mouser (liens directs)

> Farnell revient moins cher pour 12 de ces 14 lignes : voir « Variante Farnell », en fin de fichier, et la recommandation du § 5.

Relevé le **07/11/2026** sur mouser.ch, puis vérifié au panier le même jour : minimum 1 pièce partout. Seule la 220 Ω Vishay était en rupture : remplacée par une Yageo au carbone, même valeur et même puissance. Prix en CHF ; la TVA n'apparaît pas au panier. Port : **CHF 23.00** (gratuit dès CHF 70), sans supplément pour petite commande.

| ✓ | Pièce | Pour | Qté | Réf. Mouser | Prix | Lien |
|---|---|---|---|---|---|---|
| [ ] | **TIP36C** STMicroelectronics, TO-247 | Q82 | 2 | 511-TIP36C | 2 × 2.62 = 5.24 | [ouvrir](https://www.mouser.ch/en/ProductDetail/STMicroelectronics/TIP36C?qs=JV7lzlMm3yLzusij15X%2FdA%3D%3D) |
| [ ] | **Résistance 0,22 Ω 1 W** Yageo KNP100JR-73-0R22 (Ø4,6 × 11,5 mm) | R153 | 4 | 603-KNP100JR-73-0R22 | 4 × 0.233 = 0.93 | [ouvrir](https://www.mouser.ch/en/ProductDetail/YAGEO/KNP100JR-73-0R22?qs=wcZjbqjoJehe%2FtK%2F9xdtBg%3D%3D) |
| [ ] | 2N5401 Diotec, TO-92 | Q71 (réserve) | 2 | 637-2N5401 | 2 × 0.145 = 0.29 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Diotec-Semiconductor/2N5401?qs=OlC7AqGiEDkcJQvsxuzVvg%3D%3D) |
| [ ] | 1N4004 Diotec | Diodes (réserve) | 10 | 637-1N4004 | 10 × 0.058 = 0.58 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Diotec-Semiconductor/1N4004?qs=OlC7AqGiEDk3eaZusDVIWQ%3D%3D) |
| [ ] | Résistance 68 Ω ½ W Vishay NFR25H0006809JR500 | R124 (réserve) | 2 | 594-NFR25H0006809JR5 | 2 × 0.29 = 0.58 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Vishay-BC-Components/NFR25H0006809JR500?qs=gQQ%2FpDEpiRKwYWNGueF5Vg%3D%3D) |
| [ ] | Résistance 220 Ω ½ W Yageo CFR-50JB-52-220R, carbone (la Vishay NFR25H prévue d'abord : en rupture) | R125 (réserve) | 2 | 603-CFR-50JB-52-220R | 2 × 0.08 = 0.16 | [ouvrir](https://www.mouser.ch/en/ProductDetail/YAGEO/CFR-50JB-52-220R?qs=oypCK0zG326TESPIftbMYg%3D%3D) |
| [ ] | Résistance 2,7 kΩ ¼ W Yageo CFR25SJT-26-2K7 | R123 (réserve) | 2 | 603-CFR25SJT-26-2K7 | 2 × 0.112 = 0.22 | [ouvrir](https://www.mouser.ch/en/ProductDetail/YAGEO/CFR25SJT-26-2K7?qs=xZ%2FP%252Ba9zWqYr54wciWJIlQ%3D%3D) |
| | **Sous-total des pièces de la carte** | | | | **8.00** | |
| [ ] | Fusible **5 A** temporisé, format 3AG (6,3 × 32 mm), verre, Littelfuse 0313005.HXP | F108 + réserve F106–F111, F113 | 5 | 576-0313005.HXP | 5 × 1.24 = 6.20 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0313005.HXP?qs=8QfiMw8FY5OwXK2QPOUCgQ%3D%3D) |
| [ ] | Fusible **3 A** temporisé, format 3AG, verre, Littelfuse 0313003.HXP | Réserve F101–F105, F116, F501–F502, F901–F904 | 5 | 576-0313003.HXP | 5 × 1.10 = 5.50 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0313003.HXP?qs=WtG364jHAdzb9YdwG1OIXA%3D%3D) |
| [ ] | Fusible **7 A** temporisé, 3AG, verre, Littelfuse 0313007.HXP | Réserve F112 (secondaire bobines) | 2 | 576-0313007.HXP | 2 × 1.24 = 2.48 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0313007.HXP?qs=qI%252BDxnNls1%2FxPz%2F3%2FU%2FQaQ%3D%3D) |
| [ ] | Fusible **8 A rapide**, 3AG, verre, Littelfuse 0312008.HXP, 250 V (l'original est 32 V : une tension plus élevée convient) | Réserve F114 (lampes +18 V) | 2 | 576-0312008.HXP | 2 × 0.443 = 0.89 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312008.HXP?qs=OJFHm2hVE4HQD4IUOZg1nA%3D%3D) |
| [ ] | Fusible **3/4 A rapide**, 3AG, verre, Littelfuse 0312.750HXP | Réserve F115 (contacts +12 V) | 2 | 576-0312.750HXP | 2 × 0.443 = 0.89 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312.750HXP?qs=YKoktUZms5IHRFJHqQyd%252Bw%3D%3D) |
| [ ] | Fusible **3/8 A rapide**, 3AG, verre, Littelfuse 0312.375HXP | Réserve F601–F602 (affichage) | 2 | 576-0312.375HXP | 2 × 0.973 = 1.95 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312.375HXP?qs=qI%252BDxnNls1%2FlVvJlY8L2IA%3D%3D) |
| ~~[ ]~~ | ~~Tresse à dessouder 2 mm, Soldered 555022~~ **en stock, ne pas commander** | Dessoudage | 1 | 392-100376 | 2.15 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Soldered/555022?qs=bDnubaabCY%2F8xXsgLHlzZQ%3D%3D) |
| [ ] | Flux sans nettoyage en stylo, 10 ml, Chip Quik CQ4LF | Soudure | 1 | 910-CQ4LF | 6.40 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Chip-Quik/CQ4LF?qs=sGAEpiMZZMtyU1cDF2RqUKX7eE1PyzPuDUbrgOk06lw%3D) |
| ~~[ ]~~ | ~~Soudure au plomb 63/37, Chip Quik SMDSW.031~~ **en stock, ne pas commander** | Soudure | 1 | 910-SMDSW.0311OZ | 11.21 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Chip-Quik/SMDSW.031-1oz.period?qs=8BX3xQzFIvnKjoNZf181FQ%3D%3D) |

- **Les 7 premières lignes** (pièces de la carte) : ≈ 8.00 + 23.00 de port = **≈ CHF 31.00**.
- **Stock vérifié le 07/11** : tresse et soudure au plomb en stock, donc pas à commander. Kit de fusibles de réserve ajouté le 07/11, d'après la **liste des fusibles du manuel p. 1-52** (`docs/manuel-the-shadow/1-52_fusibles.png`).
- **Panier monté le 07/11** (pièces de la carte + fusibles + flux) : **CHF 32.31 + 23.00 de port = CHF 55.31**. Détail et lien de partage dans la « Liste de courses finale », en fin de fichier. Seuil de port gratuit : CHF 70 de marchandises.
- **Farnell (09/11)** : les mêmes lignes, sauf le flux et le fusible 3/8 A, coûtent **CHF 36.54 TVA et port compris**. Voir « Variante Farnell », en fin de fichier.
- Format 6,3 × 32 mm confirmé sur la Power Driver seulement ; carte son, Fliptronic et affichage à vérifier d'un coup d'œil. Fusible du filtre secteur (5 A S.B., version export) non inclus : format non indiqué au manuel.
- **Hors commande** : alcool isopropylique (IPA, 99 % si possible) en pharmacie ou droguerie, pour nettoyer le flux.
- 0,22 Ω : 10 pièces coûtent 1.47 au lieu de 0.93 pour 4, si tu veux plus de réserve. 1N4004 : le lot de 10 (0.58) coûte moins cher que 5 à l'unité (0.69).

## Compatibilité avec la carte (vérifiée le 07/11/2026)

Chaque pièce comparée à la **liste des pièces A-12697-3** (manuel, p. 2-8 : `docs/manuel-the-shadow/2-8_PD_liste-pieces.png`) au **schéma** de l'étage Sol 01–04 (`docs/schema-power-driver/f3_etage-HP_Q71-Q82_sol01-04.png`) et, pour les fusibles, à la **liste des fusibles** (manuel, p. 1-52 : `docs/manuel-the-shadow/1-52_fusibles.png`).

| Repère | D'origine (manuel / schéma) | Pièce choisie | Verdict |
|---|---|---|---|
| Q82 | TIP36C PNP (5191-12179-00) | ST TIP36C, TO-247 | ✅ Même référence. Brochage standard B-C-E ; poser la face métallique du même côté que l'ancien |
| Q86 (et Q81) | TIP 102 (5162-12635-00) | « TIP 102 MBR » Reichelt, déjà en stock | ✅ Même référence |
| R153 | 0,22 Ω 1 W 5 % (5010-12427-00) | Yageo KNP100JR, 1 W 5 %, Ø4,6 × 11,5 mm | ✅ Tient entre les trous (20 mm) |
| Q71 | 2N5401 PNP (5194-09055-00) | Diotec 2N5401 | ✅ Même référence. ⚠️ Brochage de la version Diotec **non confirmé** (fiche illisible ici) : vérifier E-B-C avant de souder, s'il faut un jour changer Q71 |
| D5–D12, D17–D32 | 1N4004 1 A (5070-09054-00) | Diotec 1N4004 | ✅ Même référence |
| R124 | 68 Ω ½ W (schéma : « 68 OHM 1/2 W ») | Vishay NFR25H, 68 Ω 0,5 W | ✅ Fiche Mouser : « 500 mW (1/2 W) ». Le texte court du panier dit « 1/3W » : c'est la fiche qui fait foi |
| R125 | 220 Ω **½ W** (5010-09361-00, avec R104 à R122) | Yageo CFR-50JB, 220 Ω 0,5 W, carbone, Ø3,3 × 9 mm | ✅ **Corrigé** : la liste précédente disait ¼ W. La Vishay NFR25H choisie d'abord était en rupture le 07/11 |
| R123 | 2,7 kΩ ¼ W (5010-08997-00) | Yageo CFR25SJT, 2,7 kΩ ¼ W | ✅ |
| F108 (groupe F106–F111) | Fusible S-B 5 A 250 V (5731-09651-00), porte-fusible 3AG | Littelfuse 0313005.HXP, 3AG temporisé 5 A 250 V | ✅ Équivalent direct des Bussmann MDL d'origine |
| F101–F105 | Fusible S-B 3 A 250 V (5731-10356-00) ; F104 vu « BUSS MDL 3A » (O10) | Littelfuse 0313003.HXP, 3AG temporisé 3 A 250 V | ✅ **3 A exact**, plutôt que les 3,15 A envisagés avant |
| Réserve (p. 1-52) | F112 7 A 250 V S.B. ; F114 8 A **32 V** N.B. ; F115 3/4 A 250 V F.B. ; F601–F602 3/8 A 250 V F.B. | Littelfuse 0313007.HXP (temporisé) ; 0312008.HXP, 0312.750HXP et 0312.375HXP (rapides) ; tous 3AG verre 250 V | ✅ Même calibre et même type : « S.B. » = temporisé (série 313), « N.B. » et « F.B. » = rapide (série 312). Le 8 A est en 250 V au lieu de 32 V : sans inconvénient |

*R124 :* la liste des pièces imprime sa valeur de façon peu lisible (on croit lire « 68 K »). Le schéma l'écrit en toutes lettres, « 68 OHM 1/2 W ». C'est aussi la seule valeur qui laisse passer assez de courant pour que le TIP36C conduise.

*Variante Farnell (09/11) :*
- R153 : Multicomp Pro MCKNP01WJ022KA10, bobinée, ininflammable, 1 W 5 %, Ø5 × 12 mm. Tient entre les trous ✅.
- R124, R125 et R123 : Multicomp Pro MCF au carbone, mêmes valeurs et mêmes puissances (½ W, ½ W, ¼ W) ✅.
- Diodes : onsemi 1N4004RL, la même 1N4004 livrée en bande ✅.
- TIP36C, 2N5401 et fusibles : mêmes références que chez Mouser ✅.

## 1. À commander

### 1.1 Indispensable

| Pièce | Pour | Qté | Remarque |
|---|---|---|---|
| **TIP36C**, PNP 100 V 25 A, boîtier **TO-247** (ou TO-218 / TO-3P) | Q82, Sol 01 (en court-circuit) | 2 | 1 + 1 de réserve. **Pas de TO-220**, trop petit |
| **Résistance 0,22 Ω 1 W**, axiale | R153 (coupée) | 4 | 1 + 3 de réserve. **Corps de 15 mm au plus** : 20 mm entre les trous ; l'originale mesure 11 × Ø 6 mm. Vérifier la cote « L » sur la fiche avant de commander. **Pas de 5 W** : 25 mm, ne tient pas à plat |

### 1.2 Réserve bon marché (facultative)

Étage de commande de la Sol 01. Toutes ces pièces ont été mesurées saines en place, mais elles coûtent quelques centimes.

| Pièce | Pour | Qté |
|---|---|---|
| 2N5401, PNP TO-92 | Q71 | 2 |
| 1N4004, DO-41 | Diodes de roue libre D17–D32 et de retour D5–D12 | 5 (10 chez Mouser : moins cher que 5) |
| Résistance 68 Ω ½ W | R124 | 2 |
| Résistance 220 Ω **½ W** (corrigé le 07/11 : le manuel la donne en ½ W, pas ¼ W) | R125 | 2 |
| Résistance 2,7 kΩ ¼ W | R123 (mesurée à 2,08 kΩ en place, cohérent avec une pièce saine) | 2 |

### 1.3 Selon le stock (voir § 2)

| Pièce | Pour | Qté | Condition |
|---|---|---|---|
| **Fusible 5 A temporisé (S-B) 250 V, format 3AG (6,3 × 32 mm)** | F108, à remplacer (dépôt brun), + 2 de réserve | 3 | **À commander** : le sachet ne contient que des 5 A 36 V |
| Fusible 3 A temporisé (S-B) 250 V, format 3AG | Réserve pour F101–F105 | 3 | **À commander** (07/11). 3 A exact, comme l'original (« BUSS MDL 3A ») |
| Tresse à dessouder, 2 à 2,5 mm | Dessoudage | 1 | ✅ En stock (CFH 52235, 2,0 mm, 1,6 m) : ne pas commander |
| Flux sans nettoyage, en stylo | Soudure | 1 | **À commander** : pas de flux séparé en stock |
| Soudure fine au plomb (Sn60/Pb40 ou Sn63/Pb37, 0,5–0,8 mm) | Soudure | 1 | ✅ En stock (CFH Sn60Pb39Cu1, 1,0 mm) : ne pas commander |
| Alcool isopropylique (IPA) | Nettoyage du flux | 1 flacon | **À acheter sur place** (pharmacie, droguerie) |

### 1.4 Hors électronique

- [ ] **Ampoule de flasher** × 2, pour le flasher Sol 26 de la tête. Probablement une #906, mais il faut **d'abord vérifier celle en place**. À prendre chez un revendeur de pièces de flipper, par exemple [Marco Specialties](https://www.marcospecialties.com/).

## 2. Déjà en stock

| Article | Quantité | État | Usage |
|---|---|---|---|
| **TIP102** Reichelt « TIP 102 MBR » (G03-122), TO-220 | 10 | Neufs, vus le 06/11 | **Q86**, et **Q81** au besoin. **Ne pas en racheter** |
| Sachet de fusibles en verre | ≈ 12 | Vérifié le 07/11 : **5 A 36 V** | ❌ Inutilisables pour F108 (l'original est T5AL250V) → T5A 250 V à commander |
| Diodes noires sur bande (marquage partiel « 22 », peut-être des 1N5822) | Plusieurs | Non identifiées | Aucun pour cette réparation |
| Soudure au plomb CFH S-Sn60Pb39Cu1, 1,0 mm, 100 g, flux colophane intégré | 1 bobine | Vue le 07/11 | **À utiliser pour la carte** |
| Soudure sans plomb Sn99,3 Cu0,7 (tube vert) | 1 | Vue le 07/11 | Ne pas utiliser sur cette carte ; ne pas mélanger |
| Tresse à dessouder CFH 52235, 2,0 mm, 1,6 m | 1 (entamée) | Vue le 07/11 | Dessoudage |
| Pompe à dessouder | 1 | Vue le 07/11 | Dégager les trous des TIP36C |
| Outils d'aide au soudage (pointes, grattoirs) | 1 jeu | Vu le 07/11 | Redresser, gratter |
| Flux séparé | 0 | Vérifié le 07/11 | À commander |
| Alcool isopropylique | 0 | Vérifié le 07/11 | À acheter sur place |
| Résistance 0,22 Ω 1 W | 0 | Vérifié le 06/11 | À commander |

## 3. Écarté par les mesures (rien à commander)

| Pièce | Pourquoi |
|---|---|
| TIP107 (Q91–Q98) | Les 8 sont sains (450 mV / OL) |
| Les autres TIP102 (rangées et sorties) | Tous cohérents avec leurs voisins ; seuls Q81 et Q86 s'en écartent |
| 2N5401 (Q59–Q62, Q71–Q74) | Jonctions et C–E identiques sur tous |
| Diodes 1N4004 de la carte | Toutes vérifiées, deux fois |
| C6 / C7 (15 000 µF) | Dessus plat, pas de fuite, soudures saines |
| Diodes des lampes | Aucun court-circuit dans la matrice du plateau (64 paires testées) |
| R160 (1 kΩ), R161 (2,2 kΩ) | Valeurs nominales |
| Les 7 autres 0,22 Ω | 0,4 Ω, comme attendu |

## 4. Prix par distributeur

Prix par pièce en CHF, **relevés les 01 et 02/11/2026** (Mouser relu le 07/11/2026 ; Farnell relevé le 09/11/2026, hors TVA), à recontrôler au moment de commander. « — » = introuvable, « n.v. » = non vérifié.

| Pièce | Mouser | Farnell | Conrad | Reichelt |
|---|---|---|---|---|
| TIP36C, TO-247 | 2.62 · ST · [lien](https://www.mouser.ch/en/ProductDetail/STMicroelectronics/TIP36C?qs=JV7lzlMm3yLzusij15X%2FdA%3D%3D) | 2.49 · ST · [lien](https://ch.farnell.com/fr-CH/stmicroelectronics/tip36c/transistor-pnp-boitier-to-218/dp/9936130) | 1.75 · ST · 46 en stock · [lien](https://www.conrad.ch/fr/p/stmicroelectronics-transistor-bjt-discret-tip36c-to-247-3-1-pnp-155457.html) | **1.17** · ST · [lien](https://www.reichelt.com/ch/fr/shop/produit/transistor_de_puissance_pnp_100v_25a_125w_to-247-21503) |
| 0,22 Ω 1 W | **0.233** (0.147 dès 10) · Yageo KNP100JR-73-0R22 · Ø4,6 × 11,5 mm · **min. 1** · [lien](https://www.mouser.ch/en/ProductDetail/YAGEO/KNP100JR-73-0R22?qs=wcZjbqjoJehe%2FtK%2F9xdtBg%3D%3D) | **0.096** · Multicomp Pro MCKNP01WJ022KA10, bobinée · Ø5 × 12 mm · **min. 1** · [lien](https://ch.farnell.com/fr-CH/multicomp-pro/mcknp01wj022ka10/resistance-bobinee-0r22-5-1w/dp/1903680) | 0.136 · Yageo KNP100JT-73-0R22 · ⚠️ **min. 100, par multiples de 100 : CHF 13.64 minimum** · [lien](https://www.conrad.ch/fr/p/yageo-knp100jt-73-0r22-resistance-bobinee-0-22-sortie-axiale-0411-1-w-5-1-pc-s-tape-3464411.html) | — (5 W seulement, ne tient pas) |
| 2N5401 | 0.145 · Diotec · [lien](https://www.mouser.ch/en/ProductDetail/Diotec-Semiconductor/2N5401?qs=OlC7AqGiEDkcJQvsxuzVvg%3D%3D) | 0.124 · Diotec · ⚠️ **min. 5 : CHF 0.62** · [lien](https://ch.farnell.com/fr-CH/diotec-semiconductor/2n5401/transistor-pnp-150v-0-6a-to-92/dp/4710237) | 0.037 · ⚠️ **min. 100 : CHF 3.70 minimum** · [lien](https://www.conrad.ch/fr/p/diotec-transistor-bjt-discret-2n5401-to-92-pnp-2808997.html) | 0.05 · [lien](https://www.reichelt.com/ch/fr/shop/produit/transistor_bipolaire_pnp_160v_0_6a_0_625w_to-92-2053) |
| 1N4004 | 0.137 (0.058 dès 10) · Diotec · [lien](https://www.mouser.ch/en/ProductDetail/Diotec-Semiconductor/1N4004?qs=OlC7AqGiEDk3eaZusDVIWQ%3D%3D) | 0.202 (0.0875 dès 10) · onsemi 1N4004RL · min. 5 · [lien](https://ch.farnell.com/fr-CH/onsemi/1n4004rl/diode-1a-400v/dp/9556109) | 0.03 · ⚠️ **min. 70 : CHF 2.10 minimum** · [lien](https://www.conrad.ch/fr/p/diotec-diode-de-redressement-si-1n4004-do-204al-400-v-1-a-162248.html) | **0.02** · [lien](https://www.reichelt.com/ch/fr/shop/produit/diode_de_redressement_do41_400_v_1_a-1726) |
| 68 Ω ½ W | 0.29 · Vishay NFR25H, 0,5 W confirmé · [lien](https://www.mouser.ch/en/ProductDetail/Vishay-BC-Components/NFR25H0006809JR500?qs=gQQ%2FpDEpiRKwYWNGueF5Vg%3D%3D) | 0.0531 · Multicomp Pro MCF, carbone 0,5 W · ⚠️ **min. 5 : CHF 0.27** · [lien](https://ch.farnell.com/fr-CH/multicomp-pro/mcf-0-5w-68r/resistance-0-5w-5-68r/dp/9338918) | 0.04 · Weltron 405116 · ⚠️ **min. 70 : CHF 2.80 minimum** · [lien](https://www.conrad.ch/fr/p/resistance-a-couche-carbone-weltron-405116-68-sortie-axiale-0411-0-5-w-1-pc-s-405116.html) | 0.08 · [recherche](https://www.reichelt.com/ch/en/shop/search/metal%20film%20resistor%2068%20ohm) |
| 220 Ω **½ W** | 0.08 · Yageo CFR-50JB-52-220R, carbone 0,5 W · [lien](https://www.mouser.ch/en/ProductDetail/YAGEO/CFR-50JB-52-220R?qs=oypCK0zG326TESPIftbMYg%3D%3D) (Vishay NFR25H à 0.378 : en rupture le 07/11) | 0.0535 · Multicomp Pro MCF, carbone 0,5 W · ⚠️ **min. 5 : CHF 0.27** · [lien](https://ch.farnell.com/fr-CH/multicomp-pro/mcf-0-5w-220r/resistance-0-5w-5-220r/dp/9338594) | ⚠️ seulement du ¼ W relevé (0.02, TRU Components) : **ne convient pas** · [recherche](https://www.conrad.ch/fr/search.html?search=r%C3%A9sistance%20220%20ohm%200%2C25W) | **0.07** · METALL 220, **0,6 W** : convient · [recherche](https://www.reichelt.com/ch/en/shop/search/metal%20film%20resistor%20220%20ohm) |
| 2,7 kΩ ¼ W | 0.112 · Yageo CFR25SJT · [lien](https://www.mouser.ch/en/ProductDetail/YAGEO/CFR25SJT-26-2K7?qs=xZ%2FP%252Ba9zWqYr54wciWJIlQ%3D%3D) | 0.0324 · Multicomp Pro MCF, carbone · ⚠️ **min. 10 : CHF 0.32** · [lien](https://ch.farnell.com/fr-CH/multicomp-pro/mcf-0-25w-2k7/resistance-0-25w-5-2k7/dp/9339361) | — | **0.11** · [recherche](https://www.reichelt.com/ch/en/shop/search/1%2F4W%202%2C7K) |
| Fusible 5 A temporisé, 3AG (6,3 × 32) | 1.24 · Littelfuse 0313005.HXP, verre · [lien](https://www.mouser.ch/en/ProductDetail/Littelfuse/0313005.HXP?qs=8QfiMw8FY5OwXK2QPOUCgQ%3D%3D) (Schurter 0001.2531 : 4.02) | 1.22 (0.978 dès 5) · Littelfuse 0313005.HXP, verre · [lien](https://ch.farnell.com/fr-CH/littelfuse/0313005-hxp/fusible-cartouche-tempo-5a-250v/dp/3515943) | **3.10 le sachet de 10** · Püschel FSUT5,0B · [recherche](https://www.conrad.ch/fr/search.html?search=fusible%206%2C3%20x%2032%20mm%205%20A%20temporis%C3%A9) | 1.70 · céramique · [recherche](https://www.reichelt.com/ch/en/shop/search/Fuse%206.3x32mm%205A%20Slow-blow) |
| Fusible 3 A temporisé, 3AG (6,3 × 32) | 1.10 · Littelfuse 0313003.HXP, **3 A exact**, verre · [lien](https://www.mouser.ch/en/ProductDetail/Littelfuse/0313003.HXP?qs=WtG364jHAdzb9YdwG1OIXA%3D%3D) | 1.23 (0.872 dès 5) · Littelfuse 0313003.HXP · [lien](https://ch.farnell.com/fr-CH/littelfuse/0313003-hxp/fusible-cartouche-tempo-3a-250v/dp/3515939) | **3.10 le sachet de 10**, en 3,15 A · [recherche](https://www.conrad.ch/fr/search.html?search=fusible%206%2C3%20x%2032%20mm%203%2C15%20A%20temporis%C3%A9) | 0.94 (T3A, dès le 09/11) · [recherche](https://www.reichelt.com/ch/en/shop/search/Fuse%206.3x32mm%203A%20Slow-blow) |
| Fusible 7 A temporisé, 3AG | 1.24 · Littelfuse 0313007.HXP · [lien](https://www.mouser.ch/en/ProductDetail/Littelfuse/0313007.HXP?qs=qI%252BDxnNls1%2FxPz%2F3%2FU%2FQaQ%3D%3D) | 1.23 · Littelfuse 0313007.HXP · [lien](https://ch.farnell.com/fr-CH/littelfuse/0313007-hxp/fusible-cartouche-tempo-7a-250v/dp/2762020) | n.v. | n.v. |
| Fusible 8 A rapide, 3AG | 0.443 · Littelfuse 0312008.HXP · [lien](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312008.HXP?qs=OJFHm2hVE4HQD4IUOZg1nA%3D%3D) | 0.606 · même réf. · ⚠️ stock US : 10 à 14 jours ouvrés · [lien](https://ch.farnell.com/fr-CH/littelfuse/0312008-hxp/cartridge-fuse-fast-acting-8a/dp/1149686) | n.v. | n.v. |
| Fusible 3/4 A rapide, 3AG | 0.443 · Littelfuse 0312.750HXP · [lien](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312.750HXP?qs=YKoktUZms5IHRFJHqQyd%252Bw%3D%3D) | 0.589 · même réf. · ⚠️ stock US · [lien](https://ch.farnell.com/fr-CH/littelfuse/0312-750hxp/cartridge-fuse-fast-acting-0-75a/dp/1149676) | n.v. | n.v. |
| Fusible 3/8 A rapide, 3AG | 0.973 · Littelfuse 0312.375HXP · [lien](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312.375HXP?qs=qI%252BDxnNls1%2FlVvJlY8L2IA%3D%3D) | ⚠️ **par 100 seulement : CHF 78.70**, stock US · [lien](https://ch.farnell.com/fr-CH/littelfuse/0312-375hxp/cartridge-fuse-fast-acting-0-375a/dp/1149673) | n.v. | n.v. |
| Tresse à dessouder | 2.15 · Soldered 555022, 2 mm · [lien](https://www.mouser.ch/en/ProductDetail/Soldered/555022?qs=bDnubaabCY%2F8xXsgLHlzZQ%3D%3D) | 5.68 · Multicore NC-AB, 1,88 mm × 1,5 m · [lien](https://ch.farnell.com/fr-CH/multicore-loctite/nc-ab-wick-1-88mm-x-1-5m/braid-desoldering-1-5m-1-88mm/dp/252499) | **2.10** · [recherche](https://www.conrad.ch/fr/search.html?search=tresse%20%C3%A0%20dessouder) | 4.25 · [recherche](https://www.reichelt.com/ch/en/shop/search/desoldering%20braid) |
| Flux en stylo | 6.40 · Chip Quik CQ4LF, 10 ml · [lien](https://www.mouser.ch/en/ProductDetail/Chip-Quik/CQ4LF?qs=sGAEpiMZZMtyU1cDF2RqUKX7eE1PyzPuDUbrgOk06lw%3D) | — (seulement des stylos vides, rechargeables, Bonkote : 78.03 les 5) | — | **5.98** · [recherche](https://www.reichelt.com/ch/en/shop/search/flux%20pen) |
| Soudure au plomb | **11.21** · Chip Quik SMDSW.031, 63/37, 0,8 mm, 28 g · [lien](https://www.mouser.ch/en/ProductDetail/Chip-Quik/SMDSW.031-1oz.period?qs=8BX3xQzFIvnKjoNZf181FQ%3D%3D) | 34.65 · Multicore 60/40, 0,71 mm, 250 g · [lien](https://ch.farnell.com/fr-CH/multicore-loctite/x-39-60en-2c-0-7mm-r-250g/bobine-soudure-x39-250g/dp/289840) | — | — |
| **Frais de port** | 23.00 (gratuit dès CHF 70) · **pas de supplément** (lu au panier) | **11.99** (gratuit dès CHF 50 d'après le panier) · pas de supplément · TVA ajoutée et affichée au panier | 9.95 **+ supplément petite quantité CHF 7.00 si le panier est inférieur à CHF 35 TTC** (testé au panier) | ≈ 9.50 (€ 10.39 affichés au panier vide) · supplément éventuel **non vérifié** (le site refuse mes clics) |
| **Quantité minimale** | 1 par pièce (vérifié sur la 0,22 Ω) | 1 sur le TIP36C, la 0,22 Ω et les fusibles ; **5** sur le 2N5401, la 1N4004, la 68 Ω et la 220 Ω ; **10** sur la 2,7 kΩ (vérifié au panier) | **70 à 100** sur la 0,22 Ω, le 2N5401, la 1N4004 et la 68 Ω ; 1 sur le TIP36C et la 220 Ω | 1 (non testé au panier) |

## 5. Scénarios de commande (CHF, port compris)

« Minimum » = § 1.1 + § 1.2. Distrelec est écarté : il n'a pas de TIP36C. **Les chiffres tiennent compte des quantités minimales et du supplément petite quantité de Conrad** (corrigé le 07/11 : la version précédente les ignorait et donnait Conrad à ≈ CHF 14). Mouser et Farnell : **hors TVA** ; Conrad et Reichelt : TVA comprise.

| Scénario | Minimum | + fusible T5A | + tresse et flux | Ce qui manque |
|---|---|---|---|---|
| **Farnell seul** | **≈ 19.71** (≈ 21.30 avec TVA) | ≈ 20.93 | ≈ 26.61, **sans flux** | Flux (soudure : + 34.65 les 250 g) |
| Mouser seul | ≈ 31.00 | ≈ 32.24 | ≈ 40.79 | Rien (soudure : + 11.21) |
| Conrad seul | ≈ 42.73 | ≈ 45.83 | ≈ 47.93, sans flux | 2,7 kΩ et 220 Ω ½ W (réserve), flux, soudure |
| Reichelt + Conrad (Conrad pour la 0,22 Ω et la tresse) | ≈ 43.20 | ≈ 44.90 | ≈ 52.98 | Soudure |
| Reichelt + Mouser (Mouser pour la 0,22 Ω) | ≈ 36.54 | ≈ 38.24 | ≈ 48.47 | Soudure |

Détail Conrad « minimum » : 2 TIP36C 3.50 + 100 résistances 0,22 Ω 13.64 + 100 × 2N5401 3.70 + 70 × 1N4004 2.10 + 70 × 68 Ω 2.80 + 2 × 220 Ω 0.04 = 25.78, **+ 7.00 de supplément (panier < CHF 35) + 9.95 de port**. En ne prenant que le TIP36C et la 0,22 Ω (sans la réserve) : 17.14 + 16.95 = **34.09**, mais sans aucune réserve.

**Recommandation (09/11) : Farnell, avec le flux acheté en magasin.**
- Détail du calcul « minimum » : 7.72 de pièces + 11.99 de port = 19.71.
- **Mêmes 12 lignes** (pièces de la carte et fusibles) : **CHF 33.81 hors TVA, port compris, chez Farnell, contre 46.96 chez Mouser.** L'écart vient surtout du port (11.99 contre 23.00) et des fusibles temporisés.
- Panier Farnell réel du 09/11 : **CHF 36.54 TVA comprise** (« Variante Farnell », en fin de fichier).
- **Introuvables chez Farnell** :
  - le stylo de flux, à prendre en magasin comme la soudure ;
  - le fusible 3/8 A rapide, vendu par 100 seulement. Ce n'est qu'une réserve pour la carte d'affichage.
- **Mouser reste la solution en un seul colis, flux compris** : CHF 55.31 hors TVA (« Liste de courses finale »).
- Les deux vendent les mêmes fusibles Littelfuse 313, l'équivalent exact des Bussmann MDL d'origine.
- Les deux vendent la 0,22 Ω **à la pièce**, dans une taille qui tient entre les trous : Ø4,6 × 11,5 mm chez Mouser, Ø5 × 12 mm chez Farnell.
- Reichelt n'apporte rien : il n'a pas la 0,22 Ω 1 W, et un second distributeur ajoute son port.
- Conrad ne redevient intéressant que si l'on veut vraiment 100 résistances 0,22 Ω.
- Pour la soudure au plomb et le flux : magasin local plutôt qu'un second envoi.

## 6. Avant de passer commande

- [x] Sachet de fusibles : 5 A 36 V, inutilisables pour F108 (07/11).
- [x] Stock : tresse, soudure au plomb et pompe OK ; flux et IPA manquants (07/11).
- [x] Test des lampes de la caisse : 7 OL, 8 OL, 9 ≈ 890 mV ; aucun court-circuit (07/11, journal S3-L4).
- [x] Corps de la 0,22 Ω 1 W de Mouser : Ø4,6 × 11,5 mm (fiche Mouser, 07/11), donc 15 mm au plus.
- [ ] Seulement s'il faut un jour remplacer Q71 : vérifier le brochage E-B-C du 2N5401 Diotec sur sa fiche avant de souder.
- [x] Panier Mouser monté le 07/11 : 14 lignes, toutes en stock, minimum 1 pièce partout, pas de supplément petite quantité. La 220 Ω Vishay, en rupture, est remplacée par une Yageo.
- [x] Panier Farnell monté le 09/11 : 12 lignes en stock, CHF 36.54 TVA et port compris. Ni flux, ni fusible 3/8 A à l'unité.
- [ ] Choisir : Farnell (moins cher, flux en magasin) ou Mouser (un seul colis, flux compris).
- [ ] Si Mouser, à la caisse : voir si la TVA (8,1 %) s'ajoute au total, et vérifier que les prix n'ont pas bougé.

## Sources

- **Reichelt** (relevé le 02/11/2026) : prix TTC (TVA suisse 8,1 %), sans douane pour la Suisse. [Frais de port](https://www.reichelt.com/ch/en/shop/service/-12_28).
- **Mouser** (relevé le 01/11/2026) : prix pour 1 pièce ; HT ou TTC à contrôler au panier ; droits et douane payés par Mouser.
- **Conrad** (relevé le 01/11/2026, quantités minimales et supplément testés le 07/11/2026) : prix TTC. Panier de test avec un TIP36C : 1.75 + supplément de petite quantité 7.00 + port 9.95 = 18.70. Le supplément disparaît à partir de CHF 35 de marchandises (testé : présent à 33.25, absent à 35.00). Panier vidé ensuite ; rien commandé. [Frais de port](https://help.conrad.ch/hc/fr-ch/articles/360001281777-A-combien-s-%C3%A9l%C3%A8vent-les-frais-de-port-standard-chez-Conrad).
- **Reichelt** (07/11/2026) : impossible de tester le panier (le site refuse les clics automatisés). Les conditions générales ne mentionnent ni minimum ni supplément ; le port affiché au panier vide est de € 10.39.
- **Mouser** (fiches produit relues le 07/11/2026) : « Minimum 1, Multiples 1 » sur toutes les pièces du panier ; le panier de test (une pièce) n'a ajouté aucun supplément. Prix dégressifs, par exemple pour la 0,22 Ω : 0.233 (1), 0.147 (10), 0.11 (25).
- **Panier Mouser** (07/11/2026, navigateur intégré) : les 14 lignes de la liste de courses finale ajoutées une à une, toutes « Dispatches Now ». Marchandise 32.31 + port UPS 23.00 = 55.31 CHF, conditions DDP, TVA non affichée. Lien de partage créé (Access ID e7b74b3e08) et relu : il affiche les 14 lignes. Rien commandé.
- **Farnell** (09/11/2026, navigateur intégré, site ch.farnell.com) :
  - Prix en CHF hors TVA.
  - Port : standard CHF 11.99, express 14.99. D'après le panier et les fiches produit, le standard est gratuit dès CHF 50 ; la page d'aide ([Angaben zur Lieferung](https://ch.farnell.com/help-schnelle-lieferung)) dit encore CHF 75.
  - Panier de 12 lignes monté puis relu : 21.82 + 11.99 de port + 2.74 de TVA = 36.54. Le 8 A et le 3/4 A partent de l'entrepôt américain, sans port supplémentaire au panier.
  - Rien commandé, aucun compte créé.
- **Yageo KNP100JR-73-0R22** : cotes lues sur la fiche Mouser le 07/11/2026, Ø4,6 × 11,5 mm (la fiche du fabricant était inaccessible le 06/11).
- **Compatibilité** : liste des pièces A-12697-3 (manuel, p. 2-8) et schéma de l'étage Sol 01–04, tous deux dans `docs/`.

### Digi-Key (vérifié le 06/11, 0,22 Ω 1 W seulement)

- Stackpole RSF1JTR220 : Ø4,5 × 11 mm, CHF 0,22 — Yageo KNP100JR-73-0R22 : Ø4,6 × 11,5 mm, CHF 0,24 (cote L confirmée, convient).
- Port CH : CHF 23 sous CHF 70, gratuit dès CHF 70 (DDP). Pour notre petite commande, ≈ CHF 38 → moins intéressant que Mouser seul.
- Source : résumé automatique de la page filtre Digi-Key, à revérifier avant commande.

## 🛒 Liste de courses finale — Mouser (07/11/2026)

Une seule commande chez **mouser.ch**. **Panier monté et vérifié le 07/11/2026** dans le navigateur intégré : 14 lignes, toutes en stock (« Dispatches Now »), minimum 1 pièce partout, aucun supplément. Droits et douane payés par Mouser (DDP).

**Panier tout fait :** [lien de partage Mouser](https://www.mouser.ch/en/Tools/SavedCart/Share?AccessID=e7b74b3e08) (Access ID `e7b74b3e08`). La page affiche les 14 lignes ; cocher « Select All », puis « Buy selected items » pour les mettre dans ton propre panier (ce bouton n'a pas été testé).

| ✓ | Qté | Article | Réf. fabricant | Réf. Mouser | Prix (CHF) | Lien |
|---|---|---|---|---|---|---|
| [ ] | 2 | Transistor TIP36C, TO-247 (Q82) | STMicroelectronics **TIP36C** | 511-TIP36C | 2 × 2.62 = 5.24 | [ouvrir](https://www.mouser.ch/en/ProductDetail/STMicroelectronics/TIP36C?qs=JV7lzlMm3yLzusij15X%2FdA%3D%3D) |
| [ ] | 4 | Résistance 0,22 Ω 1 W, Ø4,6 × 11,5 mm (R153) | Yageo **KNP100JR-73-0R22** | 603-KNP100JR-73-0R22 | 4 × 0.233 = 0.93 | [ouvrir](https://www.mouser.ch/en/ProductDetail/YAGEO/KNP100JR-73-0R22?qs=wcZjbqjoJehe%2FtK%2F9xdtBg%3D%3D) |
| [ ] | 2 | Transistor 2N5401, TO-92 (réserve Q71) | Diotec **2N5401** | 637-2N5401 | 2 × 0.145 = 0.29 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Diotec-Semiconductor/2N5401?qs=OlC7AqGiEDkcJQvsxuzVvg%3D%3D) |
| [ ] | 10 | Diode 1N4004 (réserve) | Diotec **1N4004** | 637-1N4004 | 10 × 0.058 = 0.58 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Diotec-Semiconductor/1N4004?qs=OlC7AqGiEDk3eaZusDVIWQ%3D%3D) |
| [ ] | 2 | Résistance 68 Ω ½ W (réserve R124) | Vishay **NFR25H0006809JR500** | 594-NFR25H0006809JR5 | 2 × 0.29 = 0.58 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Vishay-BC-Components/NFR25H0006809JR500?qs=gQQ%2FpDEpiRKwYWNGueF5Vg%3D%3D) |
| [ ] | 2 | Résistance 220 Ω ½ W, carbone (réserve R125) | Yageo **CFR-50JB-52-220R** | 603-CFR-50JB-52-220R | 2 × 0.08 = 0.16 | [ouvrir](https://www.mouser.ch/en/ProductDetail/YAGEO/CFR-50JB-52-220R?qs=oypCK0zG326TESPIftbMYg%3D%3D) |
| [ ] | 2 | Résistance 2,7 kΩ ¼ W (réserve R123) | Yageo **CFR25SJT-26-2K7** | 603-CFR25SJT-26-2K7 | 2 × 0.112 = 0.22 | [ouvrir](https://www.mouser.ch/en/ProductDetail/YAGEO/CFR25SJT-26-2K7?qs=xZ%2FP%252Ba9zWqYr54wciWJIlQ%3D%3D) |
| [ ] | 5 | Fusible 5 A temporisé 250 V, 6,3 × 32 mm (F108 + réserve) | Littelfuse **0313005.HXP** | 576-0313005.HXP | 5 × 1.24 = 6.20 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0313005.HXP?qs=8QfiMw8FY5OwXK2QPOUCgQ%3D%3D) |
| [ ] | 5 | Fusible 3 A temporisé 250 V, 6,3 × 32 mm (réserve) | Littelfuse **0313003.HXP** | 576-0313003.HXP | 5 × 1.10 = 5.50 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0313003.HXP?qs=WtG364jHAdzb9YdwG1OIXA%3D%3D) |
| [ ] | 2 | Fusible 7 A temporisé 250 V, 6,3 × 32 mm (réserve F112) | Littelfuse **0313007.HXP** | 576-0313007.HXP | 2 × 1.24 = 2.48 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0313007.HXP?qs=qI%252BDxnNls1%2FxPz%2F3%2FU%2FQaQ%3D%3D) |
| [ ] | 2 | Fusible 8 A **rapide**, 6,3 × 32 mm, 250 V (réserve F114 ; l'original est 32 V) | Littelfuse **0312008.HXP** | 576-0312008.HXP | 2 × 0.443 = 0.89 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312008.HXP?qs=OJFHm2hVE4HQD4IUOZg1nA%3D%3D) |
| [ ] | 2 | Fusible 3/4 A **rapide** 250 V, 6,3 × 32 mm (réserve F115) | Littelfuse **0312.750HXP** | 576-0312.750HXP | 2 × 0.443 = 0.89 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312.750HXP?qs=YKoktUZms5IHRFJHqQyd%252Bw%3D%3D) |
| [ ] | 2 | Fusible 3/8 A **rapide** 250 V, 6,3 × 32 mm (réserve F601–F602) | Littelfuse **0312.375HXP** | 576-0312.375HXP | 2 × 0.973 = 1.95 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312.375HXP?qs=qI%252BDxnNls1%2FlVvJlY8L2IA%3D%3D) |
| [ ] | 1 | Flux sans nettoyage en stylo, 10 ml | Chip Quik **CQ4LF** | 910-CQ4LF | 6.40 | [ouvrir](https://www.mouser.ch/en/ProductDetail/Chip-Quik/CQ4LF?qs=sGAEpiMZZMtyU1cDF2RqUKX7eE1PyzPuDUbrgOk06lw%3D) |
| | | **Marchandise** | | | **32.31** | |
| | | Port UPS (gratuit dès CHF 70) | | | 23.00 | |
| | | **Total du panier** (TVA non affichée) | | | **55.31** | |

**Lignes ❓ résolues le 07/11 :** les quatre fusibles existent chez Mouser sous leur référence Littelfuse exacte, en stock, dans la même série que les autres (313 = temporisé, 312 = rapide, 3AG verre). Calibres et types contrôlés contre la liste des fusibles du manuel (p. 1-52).

**Deux remarques sur le panier :**
- **220 Ω :** la Vishay NFR25H prévue d'abord était en rupture (« Backordered »). Remplacée par la Yageo CFR-50JB : même valeur, même puissance (½ W), au carbone.
- **68 Ω :** le texte court du panier dit « 1/3W », mais la fiche technique Mouser indique bien « 500 mW (1/2 W) ».

**À la caisse :** la TVA n'apparaît pas au panier. Si elle s'ajoute (8,1 %), le total passe à ≈ **CHF 59.80**. Il manque CHF 37.69 de marchandise pour le port gratuit : ça ne vaut le coup que s'il y a autre chose à commander.

**Pas chez Mouser :**
- [ ] Alcool isopropylique (pharmacie ou droguerie, 99 % si possible).
- [ ] Ampoule de flasher × 2 (après vérification de celle en place ; revendeur de pièces de flipper).

**Ne pas commander (en stock) :** TIP102, soudure au plomb, tresse, pompe à dessouder.

## 🛒 Variante Farnell (09/11/2026)

Les mêmes pièces chez **ch.farnell.com**. **Panier monté et relu le 09/11/2026** dans le navigateur intégré, avec les 12 lignes que Farnell a en stock. Prix hors TVA ; le panier ajoute la TVA (8,1 %) et affiche le total. Livraison standard **CHF 11.99**, gratuite dès CHF 50 de marchandises.

| ✓ | Qté | Article | Réf. fabricant | Code Farnell | Prix (CHF) | Lien |
|---|---|---|---|---|---|---|
| [ ] | 2 | Transistor TIP36C, TO-247 (Q82) | STMicroelectronics **TIP36C** | 9936130 | 2 × 2.49 = 4.98 | [ouvrir](https://ch.farnell.com/fr-CH/stmicroelectronics/tip36c/transistor-pnp-boitier-to-218/dp/9936130) |
| [ ] | 4 | Résistance 0,22 Ω 1 W bobinée, Ø5 × 12 mm (R153) | Multicomp Pro **MCKNP01WJ022KA10** | 1903680 | 4 × 0.096 = 0.38 | [ouvrir](https://ch.farnell.com/fr-CH/multicomp-pro/mcknp01wj022ka10/resistance-bobinee-0r22-5-1w/dp/1903680) |
| [ ] | 5 | Transistor 2N5401, TO-92 (réserve Q71). Minimum 5 | Diotec **2N5401** | 4710237 | 5 × 0.124 = 0.62 | [ouvrir](https://ch.farnell.com/fr-CH/diotec-semiconductor/2n5401/transistor-pnp-150v-0-6a-to-92/dp/4710237) |
| [ ] | 10 | Diode 1N4004 (réserve) | onsemi **1N4004RL** | 9556109 | 10 × 0.0875 = 0.88 | [ouvrir](https://ch.farnell.com/fr-CH/onsemi/1n4004rl/diode-1a-400v/dp/9556109) |
| [ ] | 5 | Résistance 68 Ω ½ W, carbone (réserve R124). Minimum 5 | Multicomp Pro **MCF 0.5W 68R** | 9338918 | 5 × 0.0531 = 0.27 | [ouvrir](https://ch.farnell.com/fr-CH/multicomp-pro/mcf-0-5w-68r/resistance-0-5w-5-68r/dp/9338918) |
| [ ] | 5 | Résistance 220 Ω ½ W, carbone (réserve R125). Minimum 5 | Multicomp Pro **MCF 0.5W 220R** | 9338594 | 5 × 0.0535 = 0.27 | [ouvrir](https://ch.farnell.com/fr-CH/multicomp-pro/mcf-0-5w-220r/resistance-0-5w-5-220r/dp/9338594) |
| [ ] | 10 | Résistance 2,7 kΩ ¼ W, carbone (réserve R123). Minimum 10 | Multicomp Pro **MCF 0.25W 2K7** | 9339361 | 10 × 0.0324 = 0.32 | [ouvrir](https://ch.farnell.com/fr-CH/multicomp-pro/mcf-0-25w-2k7/resistance-0-25w-5-2k7/dp/9339361) |
| [ ] | 5 | Fusible 5 A temporisé 250 V, 6,3 × 32 mm (F108 + réserve) | Littelfuse **0313005.HXP** | 3515943 | 5 × 0.978 = 4.89 | [ouvrir](https://ch.farnell.com/fr-CH/littelfuse/0313005-hxp/fusible-cartouche-tempo-5a-250v/dp/3515943) |
| [ ] | 5 | Fusible 3 A temporisé 250 V, 6,3 × 32 mm (réserve) | Littelfuse **0313003.HXP** | 3515939 | 5 × 0.872 = 4.36 | [ouvrir](https://ch.farnell.com/fr-CH/littelfuse/0313003-hxp/fusible-cartouche-tempo-3a-250v/dp/3515939) |
| [ ] | 2 | Fusible 7 A temporisé 250 V, 6,3 × 32 mm (réserve F112) | Littelfuse **0313007.HXP** | 2762020 | 2 × 1.23 = 2.46 | [ouvrir](https://ch.farnell.com/fr-CH/littelfuse/0313007-hxp/fusible-cartouche-tempo-7a-250v/dp/2762020) |
| [ ] | 2 | Fusible 8 A **rapide** 250 V, 6,3 × 32 mm (réserve F114). ⚠️ Stock US | Littelfuse **0312008.HXP** | 1149686 | 2 × 0.606 = 1.21 | [ouvrir](https://ch.farnell.com/fr-CH/littelfuse/0312008-hxp/cartridge-fuse-fast-acting-8a/dp/1149686) |
| [ ] | 2 | Fusible 3/4 A **rapide** 250 V, 6,3 × 32 mm (réserve F115). ⚠️ Stock US | Littelfuse **0312.750HXP** | 1149676 | 2 × 0.589 = 1.18 | [ouvrir](https://ch.farnell.com/fr-CH/littelfuse/0312-750hxp/cartridge-fuse-fast-acting-0-75a/dp/1149676) |
| | | **Marchandise** | | | **21.82** | |
| | | Livraison standard (gratuite dès CHF 50) | | | 11.99 | |
| | | TVA 8,1 % | | | 2.74 | |
| | | **Total du panier, TVA comprise** | | | **36.54** | |

*Arrondis : le panier calcule sur les prix non arrondis (21.816 + 11.99 + 2.738 de TVA = 36.544), d'où 36.54 et non 36.55.*

**Introuvables chez Farnell (09/11) :**
- **Stylo de flux.** Farnell n'a pas le Chip Quik CQ4LF, ni aucun stylo prêt à l'emploi : seulement des stylos vides, rechargeables (Bonkote, CHF 78.03 les 5). À prendre en magasin.
- **Fusible 3/8 A rapide** (réserve F601–F602). Le Littelfuse 0312.375HXP n'est vendu que **par 100** (CHF 78.70), et aucun autre 3/8 A rapide n'est vendu à l'unité. Ce n'est qu'une réserve pour la carte d'affichage : il peut attendre.

**Comparaison avec Mouser (CHF) :**

| | Mouser | Farnell |
|---|---|---|
| Les 12 lignes communes | 23.96 | 21.82 |
| Port | 23.00 | 11.99 |
| **Total hors TVA, pour les mêmes 12 lignes** | **46.96** | **33.81** |
| Avec la TVA (8,1 %) | ≈ 50.76 (TVA non affichée chez Mouser) | **36.54** (affichée au panier) |
| Flux et fusibles 3/8 A | + 8.35, soit 55.31 hors TVA | introuvables |

**À savoir avant de commander :**
- **Délais.** Dix lignes partent du stock européen (livraison standard en 2 à 3 jours ouvrés). Le 8 A et le 3/4 A partent de l'entrepôt américain : 10 à 14 jours ouvrés, sans doute dans un colis séparé. Le panier ne compte pourtant qu'un seul port.
- **Minimums.** Le 2N5401, la 68 Ω et la 220 Ω se vendent par 5, la 2,7 kΩ par 10 : plus de réserve que chez Mouser, pour quelques centimes.
- **Port gratuit.** Il manque CHF 28.18 de marchandises pour l'avoir.
- **Panier.** Il reste ouvert dans le navigateur intégré, onglet Farnell. Ailleurs, on le refait avec les liens du tableau.

