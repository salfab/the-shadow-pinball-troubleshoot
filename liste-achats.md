# Liste d'achats — réparation de la Power Driver (A-12697-3)

> **État au 17/11/2026 : tout est commandé**, chez Reichelt et chez Farnell, soit **≈ CHF 72.02** en deux colis. Reste à attendre les colis et à vérifier les pièces à la réception (§ 3).
>
> **Pièces défectueuses, confirmées par mesure :** Q82 (TIP36C, Sol 01), Q86 (TIP102, rangée de lampes) et R153 (0,22 Ω 1 W, coupée). Mesures : `journal-diagnostic-the-shadow.md`, § 4, lignes S3-*.
>
> Les comparatifs de prix entre Mouser, Farnell, Conrad et Reichelt, et les listes A, B et C d'avant la commande, ne sont plus dans ce fichier. Ils restent dans l'historique git (version du commit `d6abc1e`).

## 1. Commandes passées (17/11/2026)

Documents de commande : `docs/commandes/` (PDF Reichelt, relevé Farnell).

### 1.1 Reichelt : commande I-939651, CHF 44.52

Sous-total 35.02 + port DPD 9.50 = **CHF 44.52**, TVA 8,1 % comprise (3.34), payé par carte. Les 14 lignes du panier monté les 15 et 16/11, sans changement. Livraison annoncée : 3 à 4 jours ouvrés.

| ✓ | Qté | Réf. Reichelt | Article | Pour | Prix pièce | Lien |
|---|---|---|---|---|---|---|
| [ ] | 5 | **TIP 36C STM** | Transistor TIP36C, PNP 100 V 25 A, TO-247 | Q82 + 4 de réserve | 1.17 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/transistor_de_puissance_pnp_100v_25a_125w_to-247-21503) |
| [ ] | 5 | **2N 5401** | Transistor 2N5401 CDIL, TO-92 | Réserve Q71 | 0.05 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/transistor_bipolaire_pnp_160v_0_6a_0_625w_to-92-2053) |
| [ ] | 10 | **METALL 68,0** | Résistance 68 Ω 0,6 W, couche métallique | Réserve R124 | 0.04 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/resistance_a_film_metallique_68_0_ohms-11938) |
| [ ] | 10 | **METALL 220** | Résistance 220 Ω 0,6 W, couche métallique | Réserve R125 | 0.03 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/resistance_a_film_metallique_de_220_ohms-11627) |
| [ ] | 10 | **METALL 2,70K** | Résistance 2,7 kΩ 0,6 W, couche métallique (Yageo) | Réserve R123 | 0.03 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/resistance_a_film_metallique_de_2_70_kohms-11599) |
| [ ] | 5 | **LM 339 DIL** | Comparateur LM339, DIP-14, sans marque | Réserve U15 | 0.21 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/comparateur_quadrilatere_pdip-14_lm339-10475) |
| [ ] | 5 | **SN 74LS74AN TEX** | Double bascule D 74LS74, DIP-14, Texas Instruments | Réserve U11 | 0.60 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/flip-flop_type_d_double_4_75_5_25_v_dil-14-217311) |
| [ ] | 2 | **GS 14P** | Support tulipe DIP-14, contacts tournés dorés | U15 et U11 | 0.21 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/socle_de_ic_14_laiton_etame-8207) |
| [ ] | 1 | **GS 20P** | Support tulipe DIP-20, contacts tournés dorés | U5 | 0.31 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/socle_de_ic_20_laiton_etame-8213) |
| [ ] | 5 | **KU-TR 5,0A** | Fusible 5 A temporisé, 6,3 × 32 mm, céramique | F108 + réserve | 1.33 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/fusible_g_6_3_x_32_mm_retarde_5_000_a-119403) |
| [ ] | 10 | **LITT 0313003.HXP** | Fusible 3 A temporisé 250 V, 6,3 × 32 mm, verre | Réserve F101–F105 | 0.65 | [ouvrir](https://www.reichelt.com/ch/en/shop/product/fuse_6_3x32mm_3a_slow-blow_313-242005) |
| [ ] | 2 | **LITT 0313007.HXP** | Fusible 7 A temporisé 250 V, verre | Réserve F112 | 1.28 | [ouvrir](https://www.reichelt.com/ch/en/shop/product/fuse_6_3x32mm_7a_slow-blow_313-242006) |
| [ ] | 2 | **ESKA 632.026** | Fusible 8 A rapide, 6,3 × 32 mm, verre | Réserve F114 | 0.72 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/fusible_fin_6_3_x_32_mm_rapide_f_8_a_-278900) |
| [ ] | 1 | **STANNOL X32-10I** | Stylo de flux sans nettoyage, sans halogène, 10 ml | Soudure | 6.01 | [ouvrir](https://www.reichelt.com/ch/fr/shop/produit/crayon_a_flux_stannol_x32-10i_10_ml-96335) |

Sur les CHF 35.02 de pièces, environ **CHF 26.60 sont des réserves**. Seuls un TIP36C (Q82), un fusible 5 A (F108) et le stylo de flux (≈ 8.50) servent à coup sûr.

### 1.2 Farnell : CHF 27.50

Marchandise 13.45 HT + livraison standard 11.99 + TVA 2.06 = **CHF 27.50**. Pas encore expédié le 17/11.

| ✓ | Qté | Code Farnell | Article | Pour | Prix HT pièce | Lien |
|---|---|---|---|---|---|---|
| [ ] | 10 | 1735024 | Vishay **AC01000002207JA100**, 0,22 Ω 1 W 5 %, bobinée, Ø4,3 × 11 mm | R153 + 9 de réserve | 0.81 | [ouvrir](https://ch.farnell.com/fr-CH/search?st=1735024) |
| [ ] | 2 | 1749430 | STMicroelectronics **TIP107**, Darlington PNP 100 V 8 A, TO-220 | Réserve Q91–Q98 | 1.43 | [ouvrir](https://ch.farnell.com/fr-CH/stmicroelectronics/tip107/trans-pnp-darl-100v-8a-to-220/dp/1749430) |
| [ ] | 1 | (non relevé) | TIP36C, PNP 100 V 25 A, TO-247 | Réserve Q82 | ≈ 2.49 (déduit du total) | |

Les prix par ligne ne sont pas dans la page de la commande : ceux du TIP36C et de la ligne AC01 sont déduits du total, qui colle avec les prix du catalogue (10 × 0.81 + 2 × 1.43 + 2.49 = 13.45).

Pourquoi Farnell pour la 0,22 Ω : la Vitrohm de Reichelt a glissé du 16/11 au 7/12, alors que la Vishay AC01 est en stock et, **comme l'originale, de 1 W**. Pourquoi des TIP107 en réserve : les colonnes de lampes (+18 V) n'ont aucune protection, et Reichelt n'en a plus avant le 2/6/2027.

### 1.3 Total

| Fournisseur | CHF |
|---|---|
| Reichelt | 44.52 |
| Farnell | 27.50 |
| **Total** | **72.02** |

## 2. Compatibilité avec la carte

Pièces comparées à la **liste des pièces A-12697-3** (manuel, p. 2-8 : `docs/manuel-the-shadow/2-8_PD_liste-pieces.png`), au **schéma** de l'étage Sol 01–04 (`docs/schema-power-driver/f3_etage-HP_Q71-Q82_sol01-04.png`) et, pour les fusibles, à la **liste des fusibles** (manuel, p. 1-52 : `docs/manuel-the-shadow/1-52_fusibles.png`).

| Repère | D'origine | Pièce commandée ou en stock | Verdict |
|---|---|---|---|
| Q82 | TIP36C PNP (5191-12179-00) | ST TIP36C, TO-247 | ✅ Même référence. Brochage B-C-E ; poser la face métallique du même côté que l'ancien. **Pas de TO-220** |
| Q86 et Q81 | TIP 102 (5162-12635-00) | TIP 102 Reichelt, **10 en stock** | ✅ Même référence |
| R153 | 0,22 Ω 1 W 5 % (5010-12427-00), 11 × Ø6 mm | Vishay AC01, 1 W 5 %, Ø4,3 × 11 mm | ✅ Même puissance, tient entre les trous (20 mm). R153 est la résistance d'émetteur de la rangée de lampes de Q86 (protégée par F114, 8 A) |
| Q71 | 2N5401 PNP (5194-09055-00) | CDIL 2N5401 | ✅ Même référence. ⚠️ **Vérifier le brochage E-B-C** avant de souder |
| D5–D12, D17–D32 | 1N4004 1 A (5070-09054-00) | **1N4007** du tiroir (24) | ✅ Même série 1N400x, même courant, même boîtier DO-41 ; 1000 V au lieu de 400 V. Pas de 1N4004 commandée |
| R124 | 68 Ω ½ W | METALL 68,0, 0,6 W, 1 % | ✅ La liste des pièces imprime mal la valeur (on lit « 68 K »), le schéma dit « 68 OHM 1/2 W » : c'est aussi la seule valeur qui laisse conduire le TIP36C |
| R125 | 220 Ω **½ W** (5010-09361-00) | METALL 220, 0,6 W | ✅ |
| R123 | 2,7 kΩ ¼ W (5010-08997-00) | METALL 2,70K, 0,6 W | ✅ |
| U15 | LM339 (sur la carte : Rohm BA10339, équivalent, soudé sans support) | LM339 DIP-14 sans marque | ✅ Même brochage |
| U11 | 74LS74 | TI SN74LS74AN | ✅ Même référence, famille LS (pas de 74HC74) |
| U5 | 74LS374 | Aucune réserve (voir § 4) | Support DIP-20 commandé |
| Supports U5, U11, U15 | Aucun : puces soudées | GS 14P et GS 20P, contacts tournés, écartement 7,62 mm | ✅ |
| F108 (groupe F106–F111) | 5 A 250 V temporisé (5731-09651-00), 3AG | KU-TR 5,0A, céramique | ✅ Même format 6,3 × 32 mm ; la céramique tient mieux un court-circuit. À remplacer par précaution (dépôt brun) |
| F101–F105 | 3 A 250 V temporisé (5731-10356-00) | Littelfuse 0313003.HXP | ✅ 3 A exact |
| F112, F114 | 7 A 250 V temporisé ; 8 A **32 V** rapide | Littelfuse 0313007.HXP ; ESKA 632.026 | ✅ Même calibre et même type. Le 8 A est en 250 V au lieu de 32 V : sans inconvénient |
| Q91–Q98 | TIP107 | ST TIP107 (réserve) | ✅ Même référence |

## 3. À la réception des colis

- [ ] Relire les marquages de chaque pièce contre les § 1.1 et 1.2, et vérifier les quantités.
- [ ] **2N5401 CDIL** : vérifier le brochage E-B-C avant de le souder.
- [ ] **TIP36C** : face métallique orientée comme l'ancien ; TO-247, pas de TO-220.
- [ ] **TIP107** : bien PNP, marquage STMicroelectronics.
- [ ] **Vishay AC01** : mesurer le corps (Ø4,3 × 11 mm) et la valeur (0,22 Ω).
- [ ] Flux : **jamais de flux de plomberie** (eau à souder, pâte à braser pour raccords) : souvent acide, il ronge les pistes. Le stylo Stannol est sans nettoyage et sans halogène.
- [ ] Noter les numéros de suivi et les dates de réception dans le carnet.

## 4. Pas commandé

| Article | Pourquoi |
|---|---|
| **74LS374** (réserve U5) | Ni Reichelt ni Farnell n'en vendent (Reichelt n'a qu'un 74HCT374, autre famille). Chez Mouser : Texas Instruments SN74LS374N, réf. 595-SN74LS374N, ≈ CHF 1.12 [ouvrir](https://www.mouser.ch/en/ProductDetail/Texas-Instruments/SN74LS374N?qs=5h8QSfodyRhdi57F6aDgtA%3D%3D). Mouser prend CHF 23 de port sous CHF 70 : à grouper avec les fusibles ci-dessous |
| Fusibles rapides **3/4 A** (F115) et **3/8 A** (F601–F602) | Introuvables à l'unité en 6,3 × 32 mm chez Reichelt ; Farnell ne vend le 3/8 A que par 100. Chez Mouser : Littelfuse 0312.750HXP (576-0312.750HXP, ≈ 0.45) [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312.750HXP?qs=YKoktUZms5IHRFJHqQyd%252Bw%3D%3D) et 0312.375HXP (576-0312.375HXP, ≈ 0.97) [ouvrir](https://www.mouser.ch/en/ProductDetail/Littelfuse/0312.375HXP?qs=qI%252BDxnNls1%2FlVvJlY8L2IA%3D%3D). Simples réserves, sans urgence |
| Diodes 1N4004 | Les 24 1N4007 du tiroir les remplacent |
| Vitrohm 0,22 Ω 3 W de Reichelt | Remplacée par la Vishay AC01 de Farnell |
| Ampoule de flasher × 2 | À acheter chez un revendeur de pièces de flipper (par exemple [Marco Specialties](https://www.marcospecialties.com/)) après avoir **vérifié celle en place** (probablement une #906) |
| Alcool isopropylique (99 % si possible) | À acheter sur place (pharmacie ou droguerie), pour nettoyer le flux |

## 5. Déjà en stock

| Article | Quantité | État | Usage |
|---|---|---|---|
| **TIP102** Reichelt « TIP 102 MBR » (G03-122), TO-220 | 10 | Neufs, vus le 06/11 | **Q86**, et **Q81** au besoin. Ne pas en racheter |
| Diodes **1N4007** | 24 | Signalées le 16/11 (tiroir) | Remplacent les 1N4004 de la carte |
| Soudure au plomb CFH S-Sn60Pb39Cu1, 1,0 mm, 100 g, flux colophane intégré | 1 bobine | Vue le 07/11 | **À utiliser pour la carte** |
| Soudure sans plomb Sn99,3 Cu0,7 (tube vert) | 1 | Vue le 07/11 | Ne pas utiliser sur cette carte ; ne pas mélanger |
| Tresse à dessouder CFH 52235, 2,0 mm, 1,6 m | 1 (entamée) | Vue le 07/11 | Dessoudage |
| Pompe à dessouder | 1 | Vue le 07/11 | Dégager les trous des TIP36C |
| Outils d'aide au soudage (pointes, grattoirs) | 1 jeu | Vu le 07/11 | Redresser, gratter |
| Sachet de fusibles en verre | ≈ 12 | Vérifié le 07/11 : **5 A 36 V** | ❌ Inutilisables pour F108 (l'original est T5AL250V) |
| Diodes noires sur bande (marquage « 22 », peut-être des 1N5822) | Plusieurs | Non identifiées | Aucun pour cette réparation |

## 6. Écarté par les mesures (rien à commander)

| Pièce | Pourquoi |
|---|---|
| TIP107 (Q91–Q98) | Les 8 sont sains (450 mV / OL). Deux de réserve commandés par précaution |
| Les autres TIP102 (rangées et sorties) | Tous cohérents avec leurs voisins ; seuls Q81 et Q86 s'en écartent |
| 2N5401 (Q59–Q62, Q71–Q74) | Jonctions et C–E identiques sur tous |
| Diodes 1N4004 de la carte | Toutes vérifiées, deux fois |
| C6 / C7 (15 000 µF) | Dessus plat, pas de fuite, soudures saines |
| Diodes des lampes | Aucun court-circuit dans la matrice du plateau (64 paires testées) |
| R160 (1 kΩ), R161 (2,2 kΩ) | Valeurs nominales |
| Les 7 autres 0,22 Ω | 0,4 Ω, comme attendu |

## 7. Ce que les recherches ont appris (pour une prochaine commande)

- **Flux :** Farnell Suisse n'en vend aucun d'utilisable (rayon vide ; la pâte Duratool D01850 est à 80 % de vaseline et 20 % de chlorure de zinc, un flux de plomberie corrosif). Reichelt a le stylo Stannol à ≈ 6 ; Galaxus le même à 18 et une colophane Termopasty à 4.70.
- **Ports :** Reichelt 9.50 (DPD, sans douane ni TVA à l'import), Farnell 11.99 (gratuit dès CHF 50 HT), Mouser 23.00 (gratuit dès CHF 70), Conrad 9.95 plus 7.00 de supplément sous CHF 35, Galaxus 4.90 sous CHF 50.
- **Quantités minimales :** Reichelt et Mouser vendent à l'unité ; Farnell par 5 ou 10 sur les petites résistances et le 2N5401 ; Conrad par 70 à 100.
- **Prix dégressifs Reichelt :** dès 10 pièces, les résistances de réserve coûtent moins cher que 5 ; les fusibles 3 A, 0.65 au lieu de 0.94.
- **Compatibilité :** la liste des pièces A-12697-3 imprime mal la valeur de R124 (voir § 2) ; le 8 A d'origine est en 32 V, un 250 V convient.
- **Paniers :** ceux du navigateur intégré se perdent quand l'application redémarre ; refaire le panier avec les références, ou enregistrer le panier dans le compte.

## Sources

- Commandes : `docs/commandes/reichelt-I-939651_2026-11-17.pdf` (confirmation Reichelt) et `docs/commandes/farnell_2026-11-17.md` (relevé de la page de commande Farnell).
- Liste des pièces A-12697-3 (manuel, p. 2-8) et schéma de l'étage Sol 01–04 : `docs/`.
- Cotes de la Vishay AC01 : fiche Farnell, relue le 16/11/2026 (Ø4,3 × 11 mm, bobinée cimentée, -55 à 250 °C).
- Règles de port : [Reichelt](https://www.reichelt.com/ch/en/shop/service/-12_28), [Conrad](https://help.conrad.ch/hc/fr-ch/articles/360001281777-A-combien-s-%C3%A9l%C3%A8vent-les-frais-de-port-standard-chez-Conrad).
