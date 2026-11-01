# Liste d'achats — réparation de la Power Driver (A-12697-3)

> Préparée le 01/11/2026 pour la séance au banc. Seul **Q82** est certainement défectueux ; le reste est une réserve bon marché pour ne pas bloquer la séance si un test révèle une autre pièce abîmée.
>
> Deux distributeurs qui livrent en Suisse, en CHF : **Distrelec** (suisse, livraison rapide) et **Mouser**. Choisir un seul distributeur pour tout regrouper et amortir les frais de port.
>
> ⚠️ **Boîtier du TIP36C :** prendre le **TO-247 (ou TO-218 / TO-3P)**, comme l'original : plastique large, trou de fixation. Pas le TO-220, plus petit.
> ⚠️ **Fusibles :** **6,3 × 32 mm**, verre, temporisés (T). Pas 5 × 20 mm.

**Date de vérification : 01/11/2026**

## État de la vérification (à lire d'abord)

La vérification automatique (Playwright, pièce par pièce) a été **interrompue par les protections anti-robots** des deux sites :

- **Mouser** : toutes les pages de recherche et de produit renvoient « Access Denied » (HTTP 403). **Rien n'a pu être vérifié chez Mouser.**
- **Distrelec** : les deux premières pages ont pu être lues, puis le site a affiché un **CAPTCHA** (Radware) qui bloque toutes les pages suivantes, même après une pause de plusieurs minutes. Il n'a pas été contourné.

Seules les lignes marquées **vérifié** ont été vues sur le site. Tout le reste est **non vérifié** : le lien est une simple recherche, à contrôler à la main (prix, stock, boîtier) au moment de commander.

## 1. Indispensable

| ✓ | Pièce | Qté | Distrelec | Mouser |
|---|---|---|---|---|
| [ ] | **TIP36C** — Q82, sortie de la Sol 01 (en court-circuit). PNP 100 V 25 A, **TO-247 / TO-218 / TO-3P** | 2 | **Vérifié : aucun résultat** pour « TIP36C » chez Distrelec. Non disponible. | Non vérifié — [recherche](https://www.mouser.ch/c/?q=TIP36C) |

## 2. Réserve : chaîne de commande de la Sol 01

| ✓ | Pièce | Qté | Distrelec | Mouser |
|---|---|---|---|---|
| [ ] | **TIP102** — Q81, plus 2 pour les pilotes de rangées de lampes (Q83–Q90). NPN Darlington 100 V 8 A, TO-220 | 4 | **Vérifié** : [ST TIP102, sachet de 5 (art. 305-05-942)](https://www.distrelec.ch/fr/darlington-transistor-npn-100-hfe-200-to-200-5pcs-st-tip102/p/30505942) — **CHF 6.85 HT / 7.41 TTC le sachet de 5** (1 sachet suffit) — **445 en stock**, livraison en 1–2 jours ouvrés. Boîtier TO-220 d'après la fiche (le titre indique « TO-200 », c'est une coquille). | Non vérifié — [recherche](https://www.mouser.ch/c/?q=TIP102) |
| [ ] | **2N5401** — Q71. PNP 150 V, TO-92 | 2 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=2N5401) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=2N5401) |
| [ ] | **1N4004** — roue libre (D17–D32) et « tieback » (D5–D12). DO-41 | 5 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=1N4004) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=1N4004) |
| [ ] | **Résistance 68 Ω ½ W** — R124. Traversante | 2 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=resistance%2068%20ohm%200.5W) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=68%20ohm%200.5W%20resistor) |
| [ ] | **Résistance 220 Ω ¼ W** — R125. Traversante | 2 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=resistance%20220%20ohm%200.25W) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=220%20ohm%200.25W%20resistor) |
| [ ] | **Résistance 2,7 kΩ ¼ W** — R123. Traversante | 2 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=resistance%202.7k%200.25W) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=2.7k%200.25W%20resistor) |

## 3. Réserve : zone des lampes qui a « brillé »

| ✓ | Pièce | Qté | Distrelec | Mouser |
|---|---|---|---|---|
| [ ] | **TIP107** — pilotes des colonnes (Q91–Q98). PNP Darlington 100 V 8 A, TO-220 | 2 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=TIP107) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=TIP107) |
| [ ] | **Résistance 0,22 Ω 1 W** — R150–R153, R172–R175 (mesure des rangées). Axiale, couche métallique / oxyde ou bobinée | 4 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=resistance%200.22%20ohm%201W) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=0.22%20ohm%201W%20resistor) |

## 4. Fusibles (6,3 × 32 mm, verre, temporisés)

| ✓ | Pièce | Qté | Distrelec | Mouser |
|---|---|---|---|---|
| [ ] | **T5A 250 V** — remplacement de F108 et réserve GI (F106–F110) | 3 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=fusible%206.3x32%205A%20temporis%C3%A9) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=6.3x32%205A%20slow%20blow%20fuse) |
| [ ] | **T3A 250 V** — réserve pour F101–F105 | 3 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=fusible%206.3x32%203A%20temporis%C3%A9) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=6.3x32%203A%20slow%20blow%20fuse) |

## 5. Consommables de soudure (si pas déjà en stock)

| ✓ | Pièce | Qté | Distrelec | Mouser |
|---|---|---|---|---|
| [ ] | **Flux** sans nettoyage, en stylo ou en seringue | 1 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=flux%20soudure) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=no%20clean%20flux%20pen) |
| [ ] | **Tresse à dessouder** (2 à 2,5 mm) | 1 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=tresse%20%C3%A0%20dessouder) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=desoldering%20braid) |
| [ ] | **Soudure fine au plomb** (Sn60/Pb40 ou Sn63/Pb37, 0,5 à 0,8 mm), petite bobine | 1 | Non vérifié — [recherche](https://www.distrelec.ch/fr/search?q=soudure%20Sn60Pb40%200.8mm) | Non vérifié — [recherche](https://www.mouser.ch/c/?q=Sn63Pb37%20solder%20wire%200.8mm) |

## 6. Ampoule de flasher (hors tableau)

- [ ] **Ampoule de flasher** × 2 — flasher Sol 26 de la tête. Probablement une **#906** (culot à coin) : **vérifier d'abord celle en place** avant de commander. Plutôt chez un revendeur de pièces de flipper (par exemple [Marco Specialties](https://www.marcospecialties.com/), qui livre à l'international), ou chez un revendeur européen de pièces de flipper. Disponibilité d'une #906 chez Distrelec ou Mouser : **non vérifiée** (pages bloquées).

## Totaux estimés et frais de port

| | Distrelec | Mouser |
|---|---|---|
| Total vérifié | CHF 6.85 HT (TIP102 seulement) | Non vérifié |
| Total complet | Non vérifié | Non vérifié |
| Frais de port / seuil de gratuité pour la Suisse | Non vérifié | Non vérifié |

## Recommandation

**Distrelec ne peut pas tout couvrir** : il n'a **aucun TIP36C**, la seule pièce indispensable. Si l'on veut tout acheter au même endroit, **Mouser est le candidat le plus probable**, mais rien n'a pu y être vérifié : contrôler en premier, à la main, qu'il propose un **TIP36C en TO-247 / TO-218 / TO-3P** en stock, puis les fusibles 6,3 × 32 mm temporisés. Si c'est le cas, commander tout chez Mouser ; sinon, chercher le TIP36C ailleurs.

---

**À vérifier au moment de commander :** la tension (au moins celle indiquée), le boîtier (TO-247 / TO-218 pour le TIP36C, TO-220 pour TIP102 et TIP107), et la taille des fusibles (6,3 × 32 mm, pas 5 × 20 mm).
