# Liste d'achats — réparation de la Power Driver (A-12697-3)

> Préparée le 01/11/2026 pour la séance au banc. Seul **Q82** est certainement défectueux ; le reste est une réserve bon marché pour ne pas bloquer la séance si un test révèle une autre pièce abîmée.
>
> Trois distributeurs qui livrent en Suisse, en CHF : **Distrelec** (suisse, livraison rapide), **Mouser** et **Conrad** (section 7). Choisir un seul distributeur pour tout regrouper et amortir les frais de port.
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

## 7. Troisième distributeur : Conrad.ch (vérifié le 01/11/2026)

Relevé à la main dans le navigateur intégré. Prix **TTC**, plus frais de port ; livraison annoncée le 5 novembre pour les pièces en stock. Conrad vend souvent les petites pièces à l'unité, très bon marché, mais **ne couvre pas toute la liste**.

| Pièce | Qté | Conrad |
|---|---|---|
| **TIP36C** (indispensable) | 2 | **Trouvé** : [STMicroelectronics TIP36C, TO-247-3, PNP](https://www.conrad.ch/fr/search.html?search=TIP36C) — **CHF 1.75** pièce — 46 en stock. Moins cher que chez Mouser (2.62), mais stock limité. |
| TIP102 | 4 | **Introuvable** (la recherche renvoie des fers à souder et des forets). Conrad a des TIP120 / TIP121, qui ne sont pas équivalents. |
| TIP107 | 2 | **Introuvable.** |
| 2N5401 | 2 | **Trouvé** : [Diotec 2N5401, TO-92, PNP](https://www.conrad.ch/fr/search.html?search=2N5401) — **CHF 0.037** — 872 en stock. |
| 1N4004 | 5 | **Trouvé** : [Diotec 1N4004, DO-204AL (= DO-41), 400 V 1 A](https://www.conrad.ch/fr/search.html?search=1N4004) — **CHF 0.03** — 20 387 en stock. |
| Résistance 68 Ω ½ W | 2 | **Trouvé** : Weltron 405116, couche carbone, axiale, 0,5 W — **CHF 0.04** — 1 510 en stock ([recherche](https://www.conrad.ch/fr/search.html?search=r%C3%A9sistance%2068%20ohm%200%2C5W%20traversante)). |
| Résistance 220 Ω ¼ W | 2 | **Trouvé** : TRU Components TC-MF0W4FF2200A50203, couche métallique, axiale, 0,25 W — **CHF 0.02** — 5 206 en stock ([recherche](https://www.conrad.ch/fr/search.html?search=r%C3%A9sistance%20220%20ohm%200%2C25W)). |
| Résistance 2,7 kΩ ¼ W | 2 | **Non trouvée** avec ma recherche (elle a renvoyé des 27 kΩ). À chercher à la main, ou prendre chez Mouser. |
| Résistance 0,22 Ω 1 W | 4 | **Trouvé** : Yageo KNP100JT-73-0R22, bobinée axiale, 1 W 5 % — **CHF 0.136** (prix remisé) — 300 en stock ([recherche](https://www.conrad.ch/fr/search.html?search=r%C3%A9sistance%200%2C22%20ohm%201W)). |
| Fusible T5A 6,3 × 32 | 3 | **Trouvé** : Püschel **FSUT5,0B**, 6,3 × 32 mm, 5 A 250 V temporisé, **sachet de 10 pour CHF 3.10** — 52 en stock. 1 sachet suffit, et il y a de la marge. |
| Fusible T3A 6,3 × 32 | 3 | **Trouvé (3,15 A)** : Püschel **FSUT3,15B**, 6,3 × 32 mm, 3,15 A 250 V temporisé, **sachet de 10 pour CHF 3.10** — 40 en stock. Même remarque que chez Mouser : pas de « 3 A » exact. |
| Flux | 1 | **Pas de stylo no-clean trouvé** ; seulement du flux liquide au litre (Stannol EF350, CHF 24.95) : trop. |
| Tresse à dessouder | 1 | **Trouvé** : Stannol Solder Ex, 2,5 mm × 1,6 m, flux imprégné — **CHF 2.10** — 1 021 en stock (aussi : Toolcraft ZD-180, 3 mm, CHF 1.65). |
| Soudure au plomb | 1 | **Pas trouvée** : seulement du sans plomb (Sn99,3Cu0,7). Pas adapté si l'on veut du Sn60/Pb40 ou Sn63/Pb37. |

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
| Frais de port / seuil de gratuité pour la Suisse | Non vérifié (site bloqué par le CAPTCHA) | **CHF 23.00** (UPS Worldwide Express Saver), lus au panier ; **gratuit « sur la plupart des commandes » dès CHF 70** ; droits et douane payés par Mouser (DDP) |

### Frais de port (relevés le 01/11/2026)

| Distributeur | Frais de port | Gratuit dès | Source |
|---|---|---|---|
| **Mouser** | CHF 23.00 | CHF 70 (sur la plupart des commandes) | Panier mouser.ch (une pièce mise au panier, puis retirée ; rien commandé) |
| **Conrad** | CHF 9.95 (particulier) ; CHF 15.95 (professionnel) | CHF 200 TTC | [Aide Conrad](https://help.conrad.ch/hc/fr-ch/articles/360001281777-A-combien-s-%C3%A9l%C3%A8vent-les-frais-de-port-standard-chez-Conrad) |
| **Distrelec** | Non vérifié | Non vérifié | Page bloquée |

### Coût total, port compris

| Scénario | Marchandises | Port | **Total** |
|---|---|---|---|
| Tout chez Mouser | ≈ 60.18 | 23.00 | **≈ 83.18** |
| Tout chez Mouser, panier complété pour atteindre CHF 70 | ≥ 70.00 | 0 | **≈ 70.00** |
| Conrad (ce qu'il a) + Mouser (le reste : TIP102, TIP107, 2,7 kΩ, flux, soudure) | 12.69 + 26.71 | 9.95 + 23.00 | **≈ 72.35** |
| Conrad seul (liste incomplète, 5 pièces manquantes) | 12.69 | 9.95 | ≈ 22.64 |

Total Conrad, pour ce qui y est disponible (TIP36C, 2N5401, 1N4004, résistances 68 Ω / 220 Ω / 0,22 Ω, un sachet de chaque fusible, tresse) : **≈ CHF 12.69 TTC**, hors port. Il manque **TIP102, TIP107, résistances 2,7 kΩ, flux et soudure au plomb**.

## Recommandation

**Port compris, le plus avantageux est de tout commander chez Mouser en dépassant CHF 70** : le port (CHF 23) devient gratuit, pour environ CHF 70 en tout. Le panier complet fait ≈ CHF 60 : il manque environ 10 CHF, qu'on peut employer à des pièces de réserve utiles (par exemple quelques TIP36C ou TIP102 de plus, ou un second stylo de flux). Mouser seul, sous CHF 70, coûte ≈ CHF 83 port compris. Panacher Conrad et Mouser (≈ CHF 72) ne fait pas mieux et oblige à deux commandes.

**Tout commander chez Mouser.** Il a le **TIP36C en TO-247-3** (CHF 2.62, 3 528 en stock), indispensable et absent chez Distrelec, et tout le reste de la liste est en stock au même endroit : un seul envoi. À vérifier au panier : les frais de port vers la Suisse et si les prix sont HT ou TTC. Ce qui coûte le plus, ce sont les fusibles et la soudure ; si l'on a déjà de la soudure ou des fusibles de rechange, la commande tombe autour de 17 à 30 CHF (hors port).

---

**À vérifier au moment de commander :** la tension (au moins celle indiquée), le boîtier (TO-247 / TO-218 pour le TIP36C, TO-220 pour TIP102 et TIP107), la puissance de la résistance 68 Ω (≥ ½ W), et la taille des fusibles (6,3 × 32 mm, pas 5 × 20 mm).
