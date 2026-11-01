# Liste d'achats — réparation de la Power Driver (A-12697-3)

> Préparée le 01/11/2026 pour la séance au banc. Seul **Q82** est certainement défectueux ; le reste est une réserve bon marché pour ne pas bloquer la séance si un test révèle une autre pièce abîmée.
>
> Deux distributeurs qui livrent en Suisse, en CHF : **Distrelec** (suisse, livraison rapide) et **Mouser**. Choisir un seul distributeur pour tout regrouper et amortir les frais de port.
>
> ⚠️ **Boîtier du TIP36C :** prendre le **TO-247 (ou TO-218 / TO-3P)**, comme l'original : plastique large, trou de fixation. Pas le TO-220, plus petit.
> ⚠️ **Fusibles :** **6,3 × 32 mm**, verre, temporisés (T). Pas 5 × 20 mm.

**Date de vérification : 01/11/2026** (Mouser, relevé à la main dans le navigateur intégré ; Distrelec, voir ci-dessous)

## État de la vérification (à lire d'abord)

- **Mouser** : **vérifié le 01/11/2026** dans le navigateur intégré (la vérification automatique par Playwright avait été bloquée en « Access Denied », mais la navigation normale passe). Pour chaque ligne, prix unitaire affiché sur mouser.ch (pour 1 pièce ; dégressif en quantité) et stock au moment du relevé. Le boîtier n'a été confirmé sur la fiche que pour le TIP36C (**TO-247-3**). Les prix sont ceux de la page de résultats : HT ou TTC non précisé sur la page, à contrôler au panier.
- **Distrelec** : seules deux pages avaient pu être lues avant un **CAPTCHA** (Radware), qui n'a pas été contourné. Les lignes Distrelec restent **non vérifiées**, sauf les deux marquées « Vérifié ».

## 1. Indispensable

| ✓ | Pièce | Qté | Distrelec | Mouser |
|---|---|---|---|---|
| [ ] | **TIP36C** — Q82, sortie de la Sol 01 (en court-circuit). PNP 100 V 25 A, **TO-247 / TO-218 / TO-3P** | 2 | **Vérifié : aucun résultat** pour « TIP36C » chez Distrelec. Non disponible. | **Vérifié** : [STMicroelectronics TIP36C (Mouser n° 511-TIP36C)](https://www.mouser.ch/en/ProductDetail/STMicroelectronics/TIP36C?qs=JV7lzlMm3yLzusij15X%2FdA%3D%3D) — **TO-247-3** — **CHF 2.62** pièce — **3 528 en stock**. Alternative : [onsemi TIP36CG](https://www.mouser.ch/en/ProductDetail/onsemi/TIP36CG?qs=xZq1yRCsb1dOFJSHG5v8%252Bg%3D%3D), CHF 3.94, 822 en stock. À éviter : TIP36CW (STMicro), pas en stock (attendu 30/04/2027). |

## 2. Réserve : chaîne de commande de la Sol 01

| ✓ | Pièce | Qté | Distrelec | Mouser |
|---|---|---|---|---|
| [ ] | **TIP102** — Q81, plus 2 pour les pilotes de rangées de lampes (Q83–Q90). NPN Darlington 100 V 8 A, TO-220 | 4 | **Vérifié** : [ST TIP102, sachet de 5 (art. 305-05-942)](https://www.distrelec.ch/fr/darlington-transistor-npn-100-hfe-200-to-200-5pcs-st-tip102/p/30505942) — **CHF 6.85 HT / 7.41 TTC le sachet de 5** (1 sachet suffit) — **445 en stock**, livraison en 1–2 jours ouvrés. Boîtier TO-220 d'après la fiche (le titre indique « TO-200 », c'est une coquille). | **Vérifié** : STMicroelectronics **TIP102** — **CHF 1.59** pièce — 4 875 en stock ([recherche](https://www.mouser.ch/c/?q=TIP102)). Alternative : onsemi TIP102G, CHF 1.80, 6 467 en stock. |
| [ ] | **2N5401** — Q71. PNP 150 V, TO-92 | 2 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=2N5401) | **Vérifié** : **Diotec 2N5401** (TO-92, 150 V, 600 mA) — **CHF 0.145** pièce — 17 932 en stock ([recherche](https://www.mouser.ch/c/?q=2N5401)). Alternative : Rectron 2N5401, CHF 0.333. |
| [ ] | **1N4004** — roue libre (D17–D32) et « tieback » (D5–D12). DO-41 | 5 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=1N4004) | **Vérifié** : **Diotec 1N4004** (DO-41, 400 V, 1 A) — **CHF 0.137** pièce — 194 379 en stock ([recherche](https://www.mouser.ch/c/?q=1N4004)). |
| [ ] | **Résistance 68 Ω ½ W** — R124. Traversante | 2 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=resistance%2068%20ohm%200.5W) | **Vérifié (puissance à confirmer)** : Vishay **NFR25H0006809JR500**, couche métallique 68 Ω 5 % — **CHF 0.29** — 11 443 en stock. Contrôler sur la fiche que la puissance est bien ≥ ½ W avant de commander ([recherche](https://www.mouser.ch/c/?q=68%20ohm%200.5W%20through%20hole%20resistor)). |
| [ ] | **Résistance 220 Ω ¼ W** — R125. Traversante | 2 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=resistance%20220%20ohm%200.25W) | **Vérifié** : KOA Speer **CFS1/4CT52R221J**, couche carbone 220 Ω ¼ W 5 % — **CHF 0.095** — 7 142 en stock ([recherche](https://www.mouser.ch/c/?q=220%20ohm%200.25W%20through%20hole%20resistor)). |
| [ ] | **Résistance 2,7 kΩ ¼ W** — R123. Traversante | 2 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=resistance%202.7k%200.25W) | **Vérifié** : YAGEO **CFR25SJT-26-2K7**, couche carbone 2,7 kΩ ¼ W 5 % — **CHF 0.112** — 10 416 en stock ([recherche](https://www.mouser.ch/c/?q=2.7k%200.25W%20through%20hole%20resistor)). |

## 3. Réserve : zone des lampes qui a « brillé »

| ✓ | Pièce | Qté | Distrelec | Mouser |
|---|---|---|---|---|
| [ ] | **TIP107** — pilotes des colonnes (Q91–Q98). PNP Darlington 100 V 8 A, TO-220 | 2 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=TIP107) | **Vérifié** : STMicroelectronics **TIP107** — **CHF 1.26** pièce — 5 126 en stock ([recherche](https://www.mouser.ch/c/?q=TIP107)). Alternative : onsemi TIP107G, CHF 1.52, 22 196 en stock. |
| [ ] | **Résistance 0,22 Ω 1 W** — R150–R153, R172–R175 (mesure des rangées). Axiale, couche métallique / oxyde ou bobinée | 4 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=resistance%200.22%20ohm%201W) | **Vérifié** : YAGEO **KNP100JR-73-0R22**, bobinée axiale 0,22 Ω 1 W 5 % — **CHF 0.233** — 9 396 en stock ([recherche](https://www.mouser.ch/c/?q=0.22%20ohm%201W%20resistor)). Variante miniature : KNP1WSJR-52-0R22, CHF 0.266. |

## 4. Fusibles (6,3 × 32 mm, verre, temporisés)

| ✓ | Pièce | Qté | Distrelec | Mouser |
|---|---|---|---|---|
| [ ] | **T5A 250 V** — remplacement de F108 et réserve GI (F106–F110) | 3 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=fusible%206.3x32%205A%20temporis%C3%A9) | **Vérifié** : Schurter **SPT 6.3 × 32, 250 V 5 A, réf. 0001.2531** — **CHF 4.02** pièce — 558 en stock ([recherche](https://www.mouser.ch/c/?q=6.3x32%20time%20delay%20fuse%205A%20250V)). Cher, mais bon format. |
| [ ] | **T3A 250 V** — réserve pour F101–F105 | 3 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=fusible%206.3x32%203A%20temporis%C3%A9) | **Vérifié (calibre voisin)** : Schurter **SPT 250 V 3,15 A, réf. 0001.2529** — **CHF 3.78** pièce — 463 en stock. Pas de « 3 A » exact trouvé en 6,3 × 32 : le 3,15 A est la valeur normalisée la plus proche ; **à confirmer sur la fiche** que la taille est bien 6,3 × 32 ([recherche](https://www.mouser.ch/c/?q=6.3x32%20time%20delay%20fuse%203A%20250V)). |

## 5. Consommables de soudure (si pas déjà en stock)

| ✓ | Pièce | Qté | Distrelec | Mouser |
|---|---|---|---|---|
| [ ] | **Flux** sans nettoyage, en stylo ou en seringue | 1 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=flux%20soudure) | **Vérifié** : Chip Quik **CQ4LF**, flux no-clean, stylo 10 ml — **CHF 6.40** — 1 036 en stock ([recherche](https://www.mouser.ch/c/?q=no%20clean%20flux%20pen)). |
| [ ] | **Tresse à dessouder** (2 à 2,5 mm) | 1 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=tresse%20%C3%A0%20dessouder) | **Vérifié** : Soldered **555022**, tresse 2 mm — **CHF 2.15** — 900 en stock ([recherche](https://www.mouser.ch/c/?q=desoldering%20braid)). |
| [ ] | **Soudure fine au plomb** (Sn60/Pb40 ou Sn63/Pb37, 0,5 à 0,8 mm), petite bobine | 1 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=soudure%20Sn60Pb40%200.8mm) | **Vérifié** : Chip Quik **SMDSW.031 1oz**, fil 63/37 no-clean 0,031″ (≈ 0,8 mm), 1 oz (28 g) — **CHF 11.21** — 54 en stock. Version 0,020″ (≈ 0,5 mm) : SMDSW.020, CHF 11.44 ([recherche](https://www.mouser.ch/c/?q=Sn63Pb37%20solder%20wire)). Les autres références 63/37 de Mouser sont des bobines de 1 lb à ~100 CHF : trop. |

## 6. Ampoule de flasher (hors tableau)

- [ ] **Ampoule de flasher** × 2 — flasher Sol 26 de la tête. Probablement une **#906** (culot à coin) : **vérifier d'abord celle en place** avant de commander. Plutôt chez un revendeur de pièces de flipper (par exemple [Marco Specialties](https://www.marcospecialties.com/), qui livre à l'international), ou chez un revendeur européen de pièces de flipper. Disponibilité d'une #906 chez Distrelec ou Mouser : **non vérifiée**.

## Totaux estimés et frais de port

Total Mouser calculé avec les prix unitaires relevés (pièce seule, hors port, HT/TTC à confirmer au panier) :

| Bloc | Détail | CHF |
|---|---|---|
| Indispensable | 2 × TIP36C (2.62) | 5.24 |
| Réserve Sol 01 | 4 × TIP102 (1.59) + 2 × 2N5401 (0.145) + 5 × 1N4004 (0.137) + 2 × 68 Ω (0.29) + 2 × 220 Ω (0.095) + 2 × 2,7 kΩ (0.112) | 8.33 |
| Réserve lampes | 2 × TIP107 (1.26) + 4 × 0,22 Ω (0.233) | 3.45 |
| Fusibles | 3 × T5A (4.02) + 3 × T3,15 A (3.78) | 23.40 |
| Consommables | flux 6.40 + tresse 2.15 + soudure 11.21 | 19.76 |
| **Total Mouser** | | **≈ 60.18** |

(Sans les consommables ni les fusibles : ≈ 17.02.)

| | Distrelec | Mouser |
|---|---|---|
| Total vérifié | CHF 6.85 HT (TIP102 seulement) | ≈ CHF 60.18 (liste complète, prix unitaires) |
| Total complet | Impossible : pas de TIP36C | ≈ CHF 60.18 |
| Frais de port / seuil de gratuité pour la Suisse | Non vérifié | **Non vérifié** (pages d'aide introuvables ; à lire au panier) |

## Recommandation

**Tout commander chez Mouser.** Il a le **TIP36C en TO-247-3** (CHF 2.62, 3 528 en stock), indispensable et absent chez Distrelec, et tout le reste de la liste est en stock au même endroit : un seul envoi. À vérifier au panier : les frais de port vers la Suisse et si les prix sont HT ou TTC. Ce qui coûte le plus, ce sont les fusibles et la soudure ; si l'on a déjà de la soudure ou des fusibles de rechange, la commande tombe autour de 17 à 30 CHF (hors port).

---

**À vérifier au moment de commander :** la tension (au moins celle indiquée), le boîtier (TO-247 / TO-218 pour le TIP36C, TO-220 pour TIP102 et TIP107), la puissance de la résistance 68 Ω (≥ ½ W), et la taille des fusibles (6,3 × 32 mm, pas 5 × 20 mm).
