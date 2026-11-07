# Liste d'achats — réparation de la Power Driver (A-12697-3)

> Version du **06/11/2026**, après les tests de la carte sortie (05 et 06/11). Détail des mesures : `journal-diagnostic-the-shadow.md`, §4, lignes S3-*.
>
> **Pièces défectueuses, confirmées par mesure :** Q82 (TIP36C, Sol 01), Q86 (TIP102, rangée de lampes) et R153 (0,22 Ω 1 W, coupée).

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
| 1N4004, DO-41 | Diodes de roue libre D17–D32 et de retour D5–D12 | 5 |
| Résistance 68 Ω ½ W | R124 | 2 |
| Résistance 220 Ω ¼ W | R125 | 2 |
| Résistance 2,7 kΩ ¼ W | R123 (mesurée à 2,08 kΩ en place, cohérent avec une pièce saine) | 2 |

### 1.3 Selon le stock (voir § 2)

| Pièce | Pour | Qté | Condition |
|---|---|---|---|
| **Fusible T5A 250 V, 6,3 × 32 mm, temporisé** | F108, à remplacer (dépôt brun) | 1 à 3 | Seulement si le sachet du tiroir n'en contient pas |
| Fusible T3,15A (ou T3A) 250 V, 6,3 × 32 mm | Réserve pour F101–F105 | 3 | Facultatif |
| Tresse à dessouder, 2 à 2,5 mm | Dessoudage | 1 | Si la tresse EL 235 n'est plus dans le tiroir |
| Flux sans nettoyage, en stylo | Soudure | 1 | Si pas en stock |
| Soudure fine au plomb (Sn60/Pb40 ou Sn63/Pb37, 0,5–0,8 mm) | Soudure | 1 | Si pas en stock ; introuvable chez Conrad et Reichelt, à prendre dans un magasin local ou chez Mouser |

### 1.4 Hors électronique

- [ ] **Ampoule de flasher** × 2, pour le flasher Sol 26 de la tête. Probablement une #906, mais il faut **d'abord vérifier celle en place**. À prendre chez un revendeur de pièces de flipper, par exemple [Marco Specialties](https://www.marcospecialties.com/).

## 2. Déjà en stock

| Article | Quantité | État | Usage |
|---|---|---|---|
| **TIP102** Reichelt « TIP 102 MBR » (G03-122), TO-220 | 10 | Neufs, vus le 06/11 | **Q86**, et **Q81** au besoin. **Ne pas en racheter** |
| Sachet de fusibles en verre | ≈ 12 | **À vérifier** : longueur (32 mm ?), calibre, T ou F | F108 si ce sont des T5A en 6,3 × 32 mm |
| Diodes noires sur bande (marquage partiel « 22 », peut-être des 1N5822) | Plusieurs | Non identifiées | Aucun pour cette réparation |
| Tresse EL 235, soudure, flux | ? | **À vérifier** | Voir § 1.3 |
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

Prix par pièce en CHF, **relevés les 01 et 02/11/2026**, à recontrôler au moment de commander. « — » = introuvable, « n.v. » = non vérifié.

| Pièce | Mouser | Conrad | Reichelt |
|---|---|---|---|
| TIP36C, TO-247 | 2.62 · ST · [lien](https://www.mouser.ch/en/ProductDetail/STMicroelectronics/TIP36C?qs=JV7lzlMm3yLzusij15X%2FdA%3D%3D) | 1.75 · ST · 46 en stock · [recherche](https://www.conrad.ch/fr/search.html?search=TIP36C) | **1.17** · ST · [lien](https://www.reichelt.com/ch/fr/shop/produit/transistor_de_puissance_pnp_100v_25a_125w_to-247-21503) |
| 0,22 Ω 1 W | **0.233** (0.147 dès 10) · Yageo KNP100JR-73-0R22 · Ø4,6 × 11,5 mm · **min. 1** · [lien](https://www.mouser.ch/en/ProductDetail/YAGEO/KNP100JR-73-0R22?qs=wcZjbqjoJehe%2FtK%2F9xdtBg%3D%3D) | 0.136 · Yageo KNP100JT-73-0R22 · ⚠️ **min. 100, par multiples de 100 : CHF 13.64 minimum** · [lien](https://www.conrad.ch/fr/p/yageo-knp100jt-73-0r22-resistance-bobinee-0-22-sortie-axiale-0411-1-w-5-1-pc-s-tape-3464411.html) | — (5 W seulement, ne tient pas) |
| 2N5401 | 0.145 · [recherche](https://www.mouser.ch/c/?q=2N5401) | 0.037 · ⚠️ **min. 100 : CHF 3.70 minimum** · [lien](https://www.conrad.ch/fr/p/diotec-transistor-bjt-discret-2n5401-to-92-pnp-2808997.html) | 0.05 · [lien](https://www.reichelt.com/ch/fr/shop/produit/transistor_bipolaire_pnp_160v_0_6a_0_625w_to-92-2053) |
| 1N4004 | 0.137 · [recherche](https://www.mouser.ch/c/?q=1N4004) | 0.03 · ⚠️ **min. 70 : CHF 2.10 minimum** · [lien](https://www.conrad.ch/fr/p/diotec-diode-de-redressement-si-1n4004-do-204al-400-v-1-a-162248.html) | **0.02** · [lien](https://www.reichelt.com/ch/fr/shop/produit/diode_de_redressement_do41_400_v_1_a-1726) |
| 68 Ω ½ W | 0.29 · [recherche](https://www.mouser.ch/c/?q=68%20ohm%200.5W%20through%20hole%20resistor) | 0.04 · Weltron 405116 · ⚠️ **min. 70 : CHF 2.80 minimum** · [lien](https://www.conrad.ch/fr/p/resistance-a-couche-carbone-weltron-405116-68-sortie-axiale-0411-0-5-w-1-pc-s-405116.html) | 0.08 · [recherche](https://www.reichelt.com/ch/en/shop/search/metal%20film%20resistor%2068%20ohm) |
| 220 Ω ¼ W | 0.095 · [recherche](https://www.mouser.ch/c/?q=220%20ohm%200.25W%20through%20hole%20resistor) | **0.02** · [recherche](https://www.conrad.ch/fr/search.html?search=r%C3%A9sistance%20220%20ohm%200%2C25W) | 0.07 · [recherche](https://www.reichelt.com/ch/en/shop/search/metal%20film%20resistor%20220%20ohm) |
| 2,7 kΩ ¼ W | 0.112 · [recherche](https://www.mouser.ch/c/?q=2.7k%200.25W%20through%20hole%20resistor) | — | **0.11** · [recherche](https://www.reichelt.com/ch/en/shop/search/1%2F4W%202%2C7K) |
| Fusible T5A 6,3 × 32 | 4.02 · [recherche](https://www.mouser.ch/c/?q=6.3x32%20time%20delay%20fuse%205A%20250V) | **3.10 le sachet de 10** · Püschel FSUT5,0B · [recherche](https://www.conrad.ch/fr/search.html?search=fusible%206%2C3%20x%2032%20mm%205%20A%20temporis%C3%A9) | 1.70 · céramique · [recherche](https://www.reichelt.com/ch/en/shop/search/Fuse%206.3x32mm%205A%20Slow-blow) |
| Fusible T3,15A 6,3 × 32 | 3.78 · [recherche](https://www.mouser.ch/c/?q=6.3x32%20time%20delay%20fuse%203A%20250V) | **3.10 le sachet de 10** · [recherche](https://www.conrad.ch/fr/search.html?search=fusible%206%2C3%20x%2032%20mm%203%2C15%20A%20temporis%C3%A9) | 0.94 (T3A, dès le 09/11) · [recherche](https://www.reichelt.com/ch/en/shop/search/Fuse%206.3x32mm%203A%20Slow-blow) |
| Tresse à dessouder | 2.15 · [recherche](https://www.mouser.ch/c/?q=desoldering%20braid) | **2.10** · [recherche](https://www.conrad.ch/fr/search.html?search=tresse%20%C3%A0%20dessouder) | 4.25 · [recherche](https://www.reichelt.com/ch/en/shop/search/desoldering%20braid) |
| Flux en stylo | 6.40 · [recherche](https://www.mouser.ch/c/?q=no%20clean%20flux%20pen) | — | **5.98** · [recherche](https://www.reichelt.com/ch/en/shop/search/flux%20pen) |
| Soudure au plomb | **11.21** · [recherche](https://www.mouser.ch/c/?q=Sn63Pb37%20solder%20wire) | — | — |
| **Frais de port** | 23.00 (gratuit dès CHF 70) · **pas de supplément** (lu au panier) | 9.95 **+ supplément petite quantité CHF 7.00 si le panier est inférieur à CHF 35 TTC** (testé au panier) | ≈ 9.50 (€ 10.39 affichés au panier vide) · supplément éventuel **non vérifié** (le site refuse mes clics) |
| **Quantité minimale** | 1 par pièce (vérifié sur la 0,22 Ω) | **70 à 100** sur la 0,22 Ω, le 2N5401, la 1N4004 et la 68 Ω ; 1 sur le TIP36C et la 220 Ω | 1 (non testé au panier) |

## 5. Scénarios de commande (CHF, port compris)

« Minimum » = § 1.1 + § 1.2. Distrelec est écarté : il n'a pas de TIP36C. **Les chiffres tiennent compte des quantités minimales et du supplément petite quantité de Conrad** (corrigé le 07/11 : la version précédente les ignorait et donnait Conrad à ≈ CHF 14).

| Scénario | Minimum | + fusible T5A | + tresse et flux | Ce qui manque |
|---|---|---|---|---|
| **Mouser seul** | **≈ 31.15** | ≈ 35.15 | ≈ 43.70 | Rien (soudure : + 11.21) |
| Conrad seul | ≈ 42.73 | ≈ 45.83 | ≈ 47.93, sans flux | 2,7 kΩ (réserve), flux, soudure |
| Reichelt + Conrad (Conrad pour la 0,22 Ω et la tresse) | ≈ 43.20 | ≈ 44.90 | ≈ 52.98 | Soudure |
| Reichelt + Mouser (Mouser pour la 0,22 Ω) | ≈ 36.54 | ≈ 38.24 | ≈ 48.47 | Soudure |

Détail Conrad « minimum » : 2 TIP36C 3.50 + 100 résistances 0,22 Ω 13.64 + 100 × 2N5401 3.70 + 70 × 1N4004 2.10 + 70 × 68 Ω 2.80 + 2 × 220 Ω 0.04 = 25.78, **+ 7.00 de supplément (panier < CHF 35) + 9.95 de port**. En ne prenant que le TIP36C et la 0,22 Ω (sans la réserve) : 17.14 + 16.95 = **34.09**, mais sans aucune réserve.

**Recommandation : Mouser seul.**
- C'est le moins cher dès qu'on compte les minimums de Conrad : ≈ CHF 31, en un seul envoi, avec toute la liste.
- Il vend la 0,22 Ω **à la pièce** (0.233 ; 0.147 dès 10) et la cote est bonne : Ø4,6 × 11,5 mm, donc ≤ 15 mm.
- Reichelt n'apporte rien : il n'a pas la 0,22 Ω 1 W, et un second distributeur ajoute son port.
- Conrad ne redevient intéressant que si l'on veut vraiment 100 résistances 0,22 Ω.
- Pour la soudure au plomb et le flux : magasin local plutôt qu'un second envoi.

## 6. Avant de passer commande

- [ ] Vérifier le sachet de fusibles : longueur, calibre, T ou F.
- [ ] Vérifier le stock de tresse, de flux et de soudure.
- [ ] Faire le test des lampes de la caisse (J134 broches 7, 8, 9 contre J136 broche 3). S'il trouve une diode de lampe en court-circuit, ajouter une 1N4004.
- [ ] Sur la page de la 0,22 Ω 1 W : vérifier que le corps fait 15 mm au plus.
- [ ] Recontrôler les prix et les stocks. Au panier, vérifier la **quantité minimale** de chaque ligne (Conrad : 70 à 100 sur plusieurs pièces) et tout **supplément petite quantité** (Conrad : CHF 7.00 sous CHF 35 ; Mouser : aucun vu ; Reichelt : non vérifié).

## Sources

- **Reichelt** (relevé le 02/11/2026) : prix TTC (TVA suisse 8,1 %), sans douane pour la Suisse. [Frais de port](https://www.reichelt.com/ch/en/shop/service/-12_28).
- **Mouser** (relevé le 01/11/2026) : prix pour 1 pièce ; HT ou TTC à contrôler au panier ; droits et douane payés par Mouser.
- **Conrad** (relevé le 01/11/2026, quantités minimales et supplément testés le 07/11/2026) : prix TTC. Panier de test avec un TIP36C : 1.75 + supplément de petite quantité 7.00 + port 9.95 = 18.70. Le supplément disparaît à partir de CHF 35 de marchandises (testé : présent à 33.25, absent à 35.00). Panier vidé ensuite ; rien commandé.
- **Reichelt** (07/11/2026) : impossible de tester le panier (le site refuse les clics automatisés). Les conditions générales ne mentionnent ni minimum ni supplément ; le port affiché au panier vide est de € 10.39.
- **Mouser** : la fiche de la 0,22 Ω indique « Minimum 1, Multiples 1 » ; le panier de test (une pièce) n'a ajouté aucun supplément. Prix dégressifs : 0.233 (1), 0.147 (10), 0.11 (25). [Frais de port](https://help.conrad.ch/hc/fr-ch/articles/360001281777-A-combien-s-%C3%A9l%C3%A8vent-les-frais-de-port-standard-chez-Conrad).
- **Fiche Yageo KNP100** : inaccessible le 06/11/2026. La page du fabricant renvoie une erreur 404, Mouser ne répondait pas et Conrad bloque les accès automatiques. Les cotes ne sont donc pas vérifiées.

### Digi-Key (vérifié le 06/11, 0,22 Ω 1 W seulement)

- Stackpole RSF1JTR220 : Ø4,5 × 11 mm, CHF 0,22 — Yageo KNP100JR-73-0R22 : Ø4,6 × 11,5 mm, CHF 0,24 (cote L confirmée, convient).
- Port CH : CHF 23 sous CHF 70, gratuit dès CHF 70 (DDP). Pour notre petite commande, ≈ CHF 38 → moins intéressant que Conrad seul.
- Source : résumé automatique de la page filtre Digi-Key, à revérifier avant commande.
