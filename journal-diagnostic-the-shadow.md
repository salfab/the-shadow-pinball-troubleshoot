# Journal de diagnostic — Bally *The Shadow* (1994)

> **Pour reprendre dans une nouvelle conversation** : fournir ce fichier (et le dossier `docs/` voisin), puis donner le dernier résultat obtenu.
> Récit chronologique des séances, pour un futur article de blog : `carnet-de-bord.md` (à compléter à chaque séance).
> Dernière mise à jour : 01/11/2026 (séance 2 en cours) · Fait : M14 (C11, normal), M13, L1, L2 (matrice lampes isolée de la masse et du 50 V) · L2-20 V : OL, faisceau des lampes du plateau validé · GI : G1–G3 bons · F1 (flashers du plateau et de la tête) : aucun court-circuit · F2 (lignes des flippers) : OL · **Contrôles côté machine terminés.** État en fin de séance 2 : cordon débranché ; J107, J106 branchés ; J130, J127, J126, J122, J135, J138, J124, J125 débranchés ; F103, F104, F105 retirés ; panneau afficheur toujours déposé ; **ne pas remettre sous tension**. Prochaine étape : **réparation de la PD au banc** (Q82, Q81, Q71, R123–R125, diodes D5–D24, pilotes de lampes Q83–Q98 et résistances 0,22 Ω, soudures), puis phase E (remise sous tension progressive).

## 0. Règles de travail

- Chaque information est classée : **[MESURÉ]** · **[OBSERVÉ]** (constat direct de l'utilisateur) · **[SOUVENIR]** (incertain) · **[HYPOTHÈSE]** · **[DOC]** (vérifié dans la documentation).
- Les hypothèses de l'utilisateur ne sont jamais des diagnostics confirmés.
- Une seule manipulation ou mesure à la fois : où, comment, interprétation ; attendre le résultat.
- Contrôles hors tension d'abord ; tenir compte des condensateurs. **Aucune remise sous tension** avant la fin de la checklist §7 et une évaluation des risques.
- Ne rien inventer : demander une photo, une mesure ou un document si nécessaire.
- **Vocabulaire** : « fiche » = connecteur au bout du faisceau (contacts femelles, avec les fils) ; « embase » = rangée de broches mâles soudée sur la carte. Préciser toujours « fiche … du faisceau » ou « embase … de la carte ».
- **Toute mention d'un composant, connecteur, fusible ou point de test de la carte s'accompagne d'une image annotée** (demande de l'utilisateur, 25/10/2026) : photo de l'utilisateur annotée, ou plan d'implantation p. 2-9 **tourné de 90° dans le sens horaire** pour correspondre à la carte montée dans le fronton (J130 en bas, J101 à droite, fusibles F101–F105 verticaux, F101 à gauche et F105 à droite) : `docs/manuel-the-shadow/2-9_PD_implantation_orientee-comme-montee.png`. Images annotées rangées dans `photos/`.

## 1. Résumé de la situation

- Machine : Bally *The Shadow* (1994), modèle 50032, système WPC-S (Security). Cartes : CPU Security, **Power Driver (PD) A-12697-x** (le manuel décrit la -3 ; étiquette « A-12697-3 » sur la carte, O9), Fliptronic II, son DCS, contrôleur DMD. **[DOC]**
- Symptôme actuel : dès l'allumage, la bobine **Sol 01 « Ball Launch »** (lanceur automatique, début du couloir de lancement) reste alimentée ; le plongeur est maintenu par l'électroaimant. **[OBSERVÉ]**
- Objectif : avant de reconnecter une PD réparée, vérifier que le câblage et les composants du flipper ne peuvent pas la détruire de nouveau.
- **État de la machine en fin de séance (25/10/2026, 19 h)** : cordon secteur débranché ; PD en place ; fiche J107 branchée ; fiches **J130, J127, J126, J122 débranchées** ; **F104 et F105 retirés** (F103 en place) ; ne pas remettre sous tension dans cet état.
- État actuel : PD (partiellement réparée) branchée dans le flipper au 25/10/2026, J130 débranché depuis M3 ; F104 et F105 retirés ; panneau haut-parleur et afficheur (DMD) en cours de dépose pour l'accès au fronton (photo `photos/2026-10-25_panneau-afficheur-avant-depose.jpg`). Contenu exact de la réparation : **à préciser**.
- **Constat clé (M2 à M4)** : le +50 V rejoignait la masse par ≈ 4,5 Ω à travers une bobine du groupe Sol 1–8 et une sortie de la PD. Le chemin disparaît quand J130 est débranché : défaut côté PD ; aucun autre chemin bas entre le 50 V et la masse dans les branches dont le fusible est en place et intact (F101–F104 : à vérifier), en l'état. M4 : la broche J130-1 de la PD (Sol 01, Q82) est à ≈ 0 Ω de la masse, ce qui explique directement le symptôme O1. Question ouverte : **pourquoi** cette sortie a lâché (§5.4).
- **Bilan au 25/10/2026 (réponse aux questions de l'utilisateur)** :
  - *Faisceau* : prouvé hors tension et au repos — aucune ligne 50 V ni fil de commande de bobine à la masse (M3) ; bobines Sol 01–16, 24, 25 saines (M8, M10–M12) ; tieback raccordé (M12) ; fil de la Sol 01 sans contact avec les autres lignes 50 V (M7). Pas encore couvert : contacts entre lignes d'alimentation et fils de commande des autres sorties (M13), courts-circuits vers lampes, contacts, GI et logique (phase C), câblage de la matrice lampes (lié à E5), flippers, défauts intermittents (fil qui ne touche qu'en mouvement ou à chaud : jamais exclus à 100 % par des mesures statiques, d'où l'inspection visuelle et la remise sous tension progressive).
  - *Symptôme Sol 01* : cause directe prouvée sur la carte (Q82 en court-circuit, M3–M4), pas dans le faisceau.
  - *Pourquoi Q82 a lâché* : **non prouvé**. Écartés : bobine, diode, fil à la masse ou touchant un autre 50 V, fusible, mauvaise pièce (Q82 d'origine). Restent : usure (K8), commande en amont restée active (K4 : Q81, Q71, U5, logique), défaut intermittent du câblage. Prochains tests : Q82, Q81, Q71, R123–R125 au banc ; M13 ; à la remise sous tension progressive, vérifier, bobines non alimentées, qu'aucune sortie n'est commandée au démarrage et qu'une commande de test ne produit qu'une impulsion brève. Si tout est normal : usure retenue par élimination.
- **Fusibles des bobines** : le manuel inverse F104 et F105. Réel : F104 → Rouge-Marron (Sol 01, 07…), F105 → Rouge-Noir (Sol 08…), conforme au schéma de la PD (M9a).
- **Chaîne Sol 01 côté machine : saine** (bobine ≈ 4 Ω sans diode, normal en WPC ; câblage sans masse ni contact avec un autre 50 V ; D32 saine ; fusible F104 conforme). Seul Q82 est en défaut. Cause de sa panne non trouvée côté machine : usure (K8) ou commande en amont (K4).

## 2. Pannes et réparations connues (non vérifiées)

| # | Événement | Statut | Commentaire technique |
|---|---|---|---|
| E1 | Court-circuit initial, peut-être en haut du plateau (mini-playfield ou drop target) | [SOUVENIR] | Zone à risque documentée : fils de la bobine Mini Kicker (Sol 15), montée sur un chariot mobile → usure par frottement (PinWiki).  **Souvenir précisé (25/10/2026)** : le court-circuit concernait « un flasher ou un mini drop target », sans certitude. |
| E2 | F103 sautait | [SOUVENIR] | [DOC] F103 = 50 V « continuous duty » → J107-1 **Rouge-Orange** → Sol 24 Mini Drop Bank (mini-playfield) + Sol 25 Single Drop Up + ligne « tieback ». Cohérent avec E1, mais cohérence ≠ preuve. Circuit **distinct** de celui de la Sol 01 (F105).  **M7** : la Sol 01 est en réalité sur **F104**. Si le fusible qui sautait était F104 (confusion possible avec F103), le lien avec la Sol 01 collée devient direct . (Correction après M9a : le Mini Kicker, Sol 15, est a priori sur le Rouge-Noir, donc sur F105 et non F104 ; à confirmer par la cartographie.)  **Chronologie (souvenir, 25/10/2026)** : la Sol 01 ne collait pas avant cet épisode, seulement après. |
| E3 | Un transistor a grillé | [SOUVENIR] | Repère inconnu. |
| E4 | Une diode de la PD a brûlé, remplacée ; un court-circuit identifié a été corrigé | [SOUVENIR] | Repère de la diode, nature et lieu du court-circuit inconnus.  La réparation sera visible sur la carte au banc : la diode concernée sera identifiée à ce moment-là. |
| E5 | Plusieurs transistors semblaient surchauffer ; points lumineux « en bas à droite » de la carte | [SOUVENIR] | Carte montée dans le fronton : en bas à droite = zone J130 (étages Sol 1–8, Q63–Q82) et matrice lampes (J133–J138, Q83–Q98). Les LED d'état de la PD ne sont pas dans cette zone (manuel p. 1-51). À clarifier (photo).  **Précision de l'utilisateur (25/10/2026)** : les transistors qui semblaient s'illuminer étaient **au-dessus de J133 et J137**, soit la zone des pilotes de la matrice lampes (Q83–Q98 et leurs résistances), pas l'étage de la Sol 01 (aucune trace de brûlure autour de Q82, O6, O8). Piste distincte : un défaut dans le câblage des lampes pourrait les détruire de nouveau. |
| E6 | Plusieurs composants remplacés, sans certitude d'avoir tout réparé | [SOUVENIR] | Liste à établir. |

## 3. Données techniques de référence [DOC]

### 3.1 Chaîne de commande de la Sol 01 (Ball Launch)

```
Commande :  CPU ─(J113)─ U5 74LS374 ─R135─ Q71 2N5401 ─R124─ Q81 TIP102 ─ Q82 TIP36C (collecteur à la masse)
                         sorties coupées par BLANKING                         │ émetteur
Puissance : +50 V ─F104 3 A─ J107-2 ─Rouge-Marron─ [BOBINE Sol 01] ─Violet-Marron─ J130-1
            (F112 7 A → BR3 → C8 100 µF + R260 10 kΩ, TP6)        D32 1N4004 (sur la PD) : J130-1 → +50 V
```

- La bobine est alimentée dès que son fil **Violet-Marron** est relié à la masse : normalement par Q82, sinon par n'importe quel défaut (transistor en court-circuit, fil à la masse…).
- **Blanking** : au démarrage, la CPU maintient désactivées les sorties des 74LS374 (broche OC reliée à BLANKING, J113-31) ; R134 (4,7 kΩ) bloque alors Q71, donc Q81 et Q82. Une bobine active **dès la mise sous tension** oriente vers un défaut **en aval de U5** (Q82, Q81, Q71, pont de soudure) ou vers le **câblage**, plutôt que vers la logique (U5, CPU, logiciel).
- LED de la CPU (manuel p. 1-51) : à l'allumage D19 et D21 allumées, D20 éteinte ; en fonctionnement D19 éteinte, D20 clignote, D21 allumée.
- Bobine AE-23-800 : résistance attendue **≈ 3,5 Ω** (valeur fournisseur pour un 23 AWG / 800 spires, indicative). Meilleure référence : comparer avec **Sol 07 Knocker** et **Sol 08 Wall Target Up** (AE-23-800 aussi selon le manuel).
- Bobine collée : courant de l'ordre de 50 V / 3,5 Ω ≈ 14 A (moins en pratique, l'alimentation chute), très au-delà de F104 (3 A temporisé ; le manuel indique F105 à tort, voir §3.2), qui devrait fondre rapidement. Une bobine maintenue longtemps sans que F105 fonde serait suspecte (fusible non conforme ? transistor en conduction partielle, donc échauffement ?).
- Étages Sol 1–8 sur la PD (schéma A-12697-1, feuille 3) : sortie J130 → 2N5401 / TIP102 / TIP36C / diode de roue libre 1N4004.
- **En WPC, les bobines des sorties 1–16 n'ont pas de diode** : la diode de roue libre (« tieback diode ») est sur la PD (D17–D32). Manuel p. 3-8 et théorie WPC p. 3-11 ; constaté sur la Sol 01 (O12). Ne pas en ajouter une à l'envers lors d'un remplacement de bobine.

| Broche J130 | Sol | 2N5401 | TIP102 | TIP36C | Diode |
|---|---|---|---|---|---|
| 1 | 01 | Q71 | Q81 | Q82 | D32 |
| 2 | 02 | Q74 | Q79 | Q80 | D31 |
| 4 | 03 | Q72 | Q77 | Q78 | D30 |
| 5 | 04 | Q73 | Q75 | Q76 | D29 |
| 6 | 05 | Q61 | Q63 | Q64 | D25 |
| 7 | 06 | Q60 | Q65 | Q66 | D26 |
| 8 | 07 | Q62 | Q67 | Q68 | D27 |
| 9 | 08 | Q59 | Q69 | Q70 | D28 |

- D'après le schéma (feuille 3), les sorties Sol 1–8 sortent aussi, en parallèle de J130 (9 broches, « PLFD » = plateau), sur **J132** (5 broches, « B.B. » = fronton) et **J131** (5 broches, « CAB » = caisse). À vérifier : ces embases sont-elles utilisées sur *The Shadow* (Knocker Sol 07 dans la caisse ?) et des connecteurs y sont-ils branchés ?
- Les cathodes des diodes de roue libre D25–D32 sont reliées au réseau « 50V » de la feuille 3 : bus 50 V de TP6 ou 50 V après F105 ? Non confirmé sur le schéma (scan sans renvoi lisible) ; M5bis le dira.

### 3.2 Fusibles PD (manuel p. 1-52 ; T = temporisé)

| Fusible | Circuit | Calibre |
|---|---|---|
| F101 / F102 | +50 V général (flipper gauche / droit) | 3 A 250 V T |
| **F103** | Sol #25–#28 : 50 V J107-1 Rouge-Orange (Sol 24, Sol 25, tieback) | 3 A 250 V T |
| F104 | Manuel : Sol #9–#16, J107-3 Rouge-Noir. **Réel (schéma + M9a) : J107-2 Rouge-Marron** → Sol 01, Sol 07 mesurées (et a priori les autres bobines Rouge-Marron) | 3 A 250 V T |
| **F105** | Manuel : Sol #1–#8, J107-2 Rouge-Marron. **Réel (schéma + M9a) : J107-3 Rouge-Noir** → Sol 08 mesurée (et a priori les bobines Rouge-Noir, Sol 9–16 selon le manuel) | 3 A 250 V T |
| F106–F110 | GI #5 à #1 | 5 A 250 V T |
| F111 | Flashers, secondaire (→ BR4, 20 V) | 5 A 250 V T |
| F112 | Solénoïdes, secondaire (→ BR3, tout le 50 V) | 7 A 250 V T |
| F113 | +5 V logique | 5 A 250 V T |
| F114 | +18 V matrice lampes | 8 A 32 V |
| F115 | +12 V matrice contacts | 3/4 A 250 V (rapide selon p. 1-52 ; « S-B » dans la liste de pièces) |
| F116 | +12 V secondaire | 3 A 250 V T |
| F901–F904 | Fliptronic II (flippers) | 3 A 250 V T |

### 3.3 Solénoïdes (manuel p. 2-42, 3-6, 3-27 à 3-29)

⚠️ **Colonne « Fus. » : F104 et F105 sont inversés dans le manuel.** D'après le schéma de la PD (`docs/schema-power-driver/f1_J107_brochage-F103-F104-F105.png`) et la mesure M9a : F104 → J107-2 Rouge-Marron, F105 → J107-3 Rouge-Noir. Les bobines sur Rouge-Marron sont donc protégées par F104, celles sur Rouge-Noir par F105. Exception mesurée au tableau : la Sol 08 est sur le Rouge-Noir (M6, O13). Répartition complète à établir par la cartographie.

⚠️ PinWiki signale que le tableau des solénoïdes du manuel contient des erreurs de câblage (table corrigée par « Zaza », publiée en image). Toujours confirmer par la couleur du fil et la continuité.

| Sol | Fonction | Type | Alimentation | Fus. | Transistor | Sortie PD – fil | Bobine |
|---|---|---|---|---|---|---|---|
| 01 | **Ball Launch** | Haute puissance | Manuel : J107-2 Rouge-Marron 50 V. **[MESURÉ] faux : pas sur F105** (M6, M6bis), alimentée par l'un de F101–F104 | Manuel : F105 ; **réel : F104** (M7, confirmé) | Q82 | J130-1 Violet-Marron | AE-23-800 |
| 02 | Lockup Kickout | HP | idem | F105 | Q80 | J130-2 Violet-Rouge | A-14189 |
| 03 | Left Diverter Left | HP | idem | F105 | Q78 | J130-4 Violet-Orange | AE-25-1000 |
| 04 | Left Diverter Right | HP | idem | F105 | Q76 | J130-5 Violet-Jaune | AE-25-1000 |
| 05 | Right Diverter Right | HP | idem | F105 | Q64 | J130-6 Violet-Vert | AE-25-1000 |
| 06 | Right Diverter Left | HP | idem | F105 | Q66 | J130-7 Violet-Bleu | AE-25-1000 |
| 07 | Knocker | HP | Manuel : idem. **[MESURÉ]** J130-8 non relié au clip de F105 par une bobine (M6) ; relié au clip du haut de F104 par ≈ 4 Ω (M7) | Manuel : F105 ; **réel : F104** (M7) | Q68 | J130-8 Violet-Noir | AE-23-800 |
| 08 | Wall Target Up | HP | idem | F105 | Q70 | J130-9 Violet-Gris | AE-23-800 |
| 09 | Left Slingshot | Basse puissance | J107-3 Rouge-Noir 50 V | F104 | Q58 | J127-1 Marron-Noir | AE-26-1200 |
| 10 | Right Slingshot | BP | idem | F104 | Q56 | J127-3 Marron-Rouge | AE-26-1200 |
| 11 | Right Eject | BP | idem | F104 | Q54 | J127-4 Marron-Orange | AE-27-1200 |
| 12 | Left Eject | BP | idem | F104 | Q52 | J127-5 Marron-Jaune | AE-26-1500 |
| 13 | Ball Release | BP | idem | F104 | Q50 | J127-6 Marron-Vert | AE-26-1500 |
| 14 | Ball Popper | BP | idem | F104 | Q48 | J127-7 Marron-Bleu | AE-25-1000 |
| 15 | Mini Kicker (chariot mobile) | BP | idem | F104 | Q46 | J127-8 Marron-Violet | AE-25-1000 |
| 16 | Wall Target Down | BP | idem | F104 | Q44 | J127-9 Marron-Gris | SM-30-1100-DC |
| 17 | Mini Playfield Flasher | Flasher | J107-6 / J106-5 Rouge-Blanc 20 V | F111 | Q42 | J126-1 / J125-1 Noir-Marron | #89 / #906 |
| 18 | Left Side Flasher | Flasher | idem | F111 | Q40 | J126-2 / J125-2 Noir-Rouge | #89 / #906 |
| 19 | Mini Motor Right | via carte moteur A-16120 | J116-2 Gris-Jaune +12 V | — | Q38 | J126-3 Noir-Orange | moteur 14-8014 |
| 20 | Mini Motor Left | idem | idem | — | Q36 | J126-4 Noir-Jaune | idem |
| 21 | Right Side Flasher | Flasher | J107-6 Rouge-Blanc 20 V | F111 | Q28 | J126-5 Bleu-Vert | #906 / #89 |
| 22 | Right Ramp Flasher | Flasher | idem | F111 | Q30 | J126-6 Bleu-Noir | #906 / #89 |
| 23 | Left Ramp Flasher | Flasher | idem | F111 | Q34 | J126-7 Bleu-Violet | #906 / #89 |
| 24 | **Mini Drop Bank** (mini-playfield) | bobine sur sortie « flasher » | J107-1 Rouge-Orange 50 V | F103 | Q32 | J126-8 Bleu-Gris | AE-25-1000 |
| 25 | **Single Drop Up** | GP (bobine) | J107-1 Rouge-Orange 50 V | F103 | Q26 | J122-1 Bleu-Marron | AE-26-1200 |
| 26–28 | Back Flashers G / C / D | GP (flashers) | J107-6 / J106-5 20 V | F111 | Q24 / Q22 / Q20 | J122-2/3/4 et J124-2/3/5 | #906 |
| 35 | Magnet | Fliptronic II | J907-8,9 Rouge-Gris 50 V | à vérifier | — | J902-3 Jaune-Gris | 20-9247 |
| 36 | Single Drop Down | Fliptronic II | idem | à vérifier | — | J902-1 Orange-Gris | SM1-26-600 |

### 3.4 « Tieback » (Sol 24 et 25)

- Sur la PD, les sorties Q28/Q30/Q34/Q32 (J126) ont les diodes **D9/D10/D12/D11**, et les sorties Q26/Q24/Q22/Q20 (J122) les diodes **D8/D7/D6/D5**. Leurs cathodes communes sortent sur **J126-11** et **J122-5** (schéma A-12697-1, feuille 3).
- Le faisceau doit relier J122-5 (« loop ») et J126-11 (« end ») au **Rouge-Orange 50 V** (J107-1). Sans cette liaison, les TIP102 de Sol 24 (Q32) et Sol 25 (Q26) ne sont plus protégés contre la surtension à la coupure des bobines (défaillance documentée sur d'autres WPC, par exemple *Terminator 2*).
- Conséquence : si le Rouge-Orange touche la masse, les flashers 20 V (Sol 21–23, 26–28) peuvent débiter à travers ces diodes vers le court-circuit (voir **H-hist**, §6).

### 3.5 PD : LED, points de test, condensateurs

- LED (p. 1-51) : LED1 +12 V contacts, LED2 et LED3 capteur de tension secteur, LED4 +5 V, LED5 +20 V flashers, LED6 +18 V lampes, LED7 +12 V puissance. Toutes normalement allumées, sauf LED3 (normalement éteinte).
- Points de test : TP1 +12 V, TP2 +5 V, TP3 +12 V, TP5 masse, TP6 +50 V, TP7 +20 V, TP8 +18 V.
- Condensateurs : C5, C6, C7, C11, C30 = 15 000 µF 25 V (basse tension mais énergie élevée : ne jamais les court-circuiter) ; C8 = 100 µF sur le 50 V, déchargé par R260 (10 kΩ). PD débranchée, le faisceau des bobines ne contient pas de gros condensateur ; la Fliptronic II et le contrôleur DMD (+62 V, −113/−125 V) en contiennent.

## 4. Observations et mesures

| ID | Date | Conditions | Point de mesure | Attendu | Résultat | Interprétation |
|---|---|---|---|---|---|---|
| O1 | avant le 25/10/2026 | PD connectée, sous tension | Sol 01 | Bobine au repos | Bobine alimentée dès l'allumage, plongeur maintenu | [OBSERVÉ] symptôme principal |
| O2 | 25/10/2026 | PD branchée dans le flipper ; hors tension (à confirmer) ; fusibles dans l'état trouvé | TP6 (+50 V) ↔ GND, mode continuité | Pas de bip (≈ 10 kΩ, R260 seule) | Le multimètre sonne | [OBSERVÉ] Résistance faible entre le bus 50 V et la masse, ou bip bref de charge de C8. À quantifier (M2) ; chemins possibles au §5.3 |
| M1 | — | Hors tension, PD débranchée | J130-1 ↔ masse (J116-3) et ↔ terre | 0 V, puis OL | *couverte par M3* | — |
| M2 | 25/10/2026 | Hors tension (à confirmer), PD branchée, rien retiré ; résistance des pointes et sens non précisés | TP6 ↔ TP5 en ohms ; puis TP6 ↔ vis reliée à la masse | ≈ 10 kΩ (R260) | **4,5 Ω** ; **4,6 Ω** sur la vis | [MESURÉ] Chemin réel et résistif entre le 50 V et la masse, de la valeur d'une bobine de faible résistance (ou de plusieurs en parallèle) dont l'autre extrémité est à la masse. Pas un court-circuit direct (< 1 Ω attendu). Sens sans incidence : une jonction donnerait des centaines d'ohms. TP5 et la vis sont bien à la même masse |
| O3 | 25/10/2026 | Hors tension | F105 | Retrait sans effort | Fusible difficile à extraire, non retiré | [OBSERVÉ] Clips serrés, ou fusible et clips ayant chauffé ? Ne pas forcer : risque de clips desserrés ou de soudures fissurées. Après O7 (embouts propres, verre clair) : pas de trace de chauffe ; clips probablement juste serrés, donc bon contact. Tension des clips à revérifier au remontage |
| M3 | — | Hors tension, PD branchée, **J130 débranché** (remplace le retrait de F105) ; connecteur posé sur un isolant | TP6 ↔ TP5 | OL sur 200 Ω si le seul chemin passait par une sortie Sol 1–8 de la PD | **10 kΩ** | [MESURÉ] R260 seule : le seul chemin bas passait par une sortie Sol 1–8 de la PD (ou par le contact du connecteur J130 lui-même). Aucun fil de commande Sol 1–8 à la masse dans le faisceau ; aucune autre branche (F101–F104, sous réserve que leurs fusibles soient en place et intacts) ni le bus 50 V de la PD à la masse, en l'état. F105 conduit (le chemin de M2 le traversait) |
| M4 | — | Hors tension, J130 débranché | Chaque broche de l'embase J130 de la PD (1, 2, 4–9) ↔ TP5, pointe rouge sur la broche | OL sur 200 Ω (≥ 10 kΩ en automatique) ; ≈ 0 Ω pour une sortie en court-circuit | Broche 1 : **0,5 Ω** (pointes comprises) ; broches 2, 4, 5, 7, 8, 9 : 173, 194, 160, 188, 155, 177 kΩ (unités confirmées) ; broche 6 : hors calibre sur 200 kΩ, 0,98 MΩ sur le calibre 2 MΩ | [MESURÉ] Ligne de commande Sol 01 reliée franchement à la masse sur la PD (Q82 E-C, pont de soudure ou piste). D32 hors de cause (en court-circuit, elle relierait la broche au 50 V : ≈ 10 kΩ). Recoupement : 4,5 − 0,5 ≈ 4,0 Ω pour F105 + fils + bobine Sol 01, plausible pour une AE-23-800 avec son câblage. Autres sorties Sol 02–08 : ni court-circuit ni fuite notable ; 150–200 kΩ correspond au chemin diode de roue libre → bus 50 V → R260, qu'un ohmmètre affiche comme une forte valeur variable (faible courant de test, qui change avec le calibre : ne comparer que sur un même calibre). Broche 6 (Sol 05, D25) un peu plus haute que les autres sur 200 kΩ : dispersion ou diode différente, non concluant → M5 |
| O4 | — | Hors tension, J130 débranché | Marquages et aspect de Q82, Q81, Q71 et de leurs voisins | TIP36C, TIP102, 2N5401 ; pas de brûlure | *en attente* | — |
| M5 | — | Hors tension, J130 débranché | Mode diode : chaque broche de l'embase J130 de la PD (pointe rouge) ↔ TP6 (pointe noire), soit les diodes D25–D32 | ≈ 0,4–0,6 V, valeurs voisines | Lectures qui montent depuis ≈ 0,6 V ; valeurs finales : broche 1 ≈ 1,5 V, autres ≈ 1,8–1,9 V. Sens des pointes non confirmé | Signature de C8 (100 µF, 50 V) chargé par le multimètre : aucune diode ne conduit dans ce sens. Cohérent avec des **pointes inversées** (rouge sur TP6) : chemin TP6 → C8 et R260 → masse → jonction collecteur-base du TIP36C → R 220 Ω → broche ; la broche 1 n'a pas cette jonction (Q82 en court-circuit), d'où ≈ 0,3–0,4 V de moins. Si c'est le cas : aucune diode D25–D32 en court-circuit ni inversée (K7 écartée) ; une diode coupée reste indétectable dans ce sens. **Autre explication** si F105 était déjà retiré pendant M5 et si les cathodes des diodes sont reliées au 50 V après F105 (non confirmé sur le schéma) : pointes dans le bon sens, mais diodes isolées de TP6 ; la broche 1 n'a alors qu'un chemin continu, Q82 → masse → R260 (≈ 1,5 V), les autres tendent vers la tension à vide du multimètre → M5bis |
| O8 | 25/10/2026 | Hors tension, J130 débranché | Photo de Q81, Q82, D32 et de la fiche J130 du faisceau (`photos/2026-10-25_O8_…`) | TIP102 marqué comme ses voisins | Q81 : boîtier TO-220 **sans marquage visible**, face moulée à deux nervures, d'aspect différent des TIP102 ST d'origine vus ailleurs sur la carte (« ST 94xx MALAYSIA TIP102 »). Fiche J130 : dépôts bruns sur le bord supérieur, du côté des positions 9 à 5 (fil Violet-Bleu = position 7 repéré), pas sur la position 1 | [OBSERVÉ] Q81 peut-être remplacé lors d'une réparation : type à vérifier (comparaison avec Q79, test sur banc). Dépôts de la fiche : résidu ou saleté plutôt que chauffe due à la Sol 01 (pas sur la position 1) ; à examiner côté contacts en phase C |
| O9 | 25/10/2026 | Hors tension | Vue générale de la PD (`photos/2026-10-25_O9_vue-generale-PD.jpg`, version annotée `photos/2026-10-25_annotee_Q71-Q79-Q81-Q82.jpg`) | — | Étiquette « A-12697-3 ». Sous R134–R141 : 4 transistors TO-92 marqués « 2N 5401 EBC », logo National, identiques au groupe Q59–Q62 ; le probable Q71 (en haut à gauche du groupe, par analogie avec la disposition Q59/Q61/Q60/Q62) ne laisse voir que le logo et « 2N », le reste caché. Q77, Q79 et Q81 (TIP102 des Sol 03, 02, 01) ont le même aspect, montés à plat, sans marquage visible sous cet angle. R125 : rouge-rouge-marron = 220 Ω, conforme | [OBSERVÉ] Q71–Q74 d'origine selon toute vraisemblance (H6 très peu probable pour Q71 ; le 2N5551 existe aussi chez National, d'où la réserve sur le marquage caché). Q81 identique à ses voisins : le soupçon de remplacement (O8) s'affaiblit. Le type réel de Q81 et Q71 sera confirmé sur banc |
| O7 | 25/10/2026 | Hors tension | F105 retiré par l'utilisateur (difficile à extraire, O3) | 3 A temporisé, intact | Marquage **« 313 3A 250V »** ; verre clair, embouts propres ; continuité non mesurée (le courant de M2 le traversait) | [OBSERVÉ] Série Littelfuse 313 = fusible 3AG **temporisé** (Slo-Blo) : 3 A 250 V, conforme au manuel. **K5 écartée.** Un temporisé à 2–3 fois son calibre (bobine collée, 50 V qui chute sous la charge) peut tenir plusieurs secondes, parfois davantage : cohérent avec une bobine maintenue sans fusion de F105, mais la bobine Sol 01 a alors dissipé plusieurs centaines de watts et ses fils et contacts (J107-2, J130-1) ont transporté plusieurs ampères → R1, K2 et contacts à contrôler avec soin. À laisser retiré jusqu'à la réparation de la PD |
| M5bis | — | Idem M5, F105 retiré, **pointe rouge sur la broche 2** (référence) ; pointe noire sur TP6, puis, si la lecture monte encore, sur chacun des deux clips vides de F105 | Broches ↔ TP6 (point supposé, à confirmer), mode diode | Valeur fixe immédiate ≈ 0,4–0,6 V | **Broche 1 : 428 mV ; broches 2 et 4–9 : 480 à 514 mV** | [MESURÉ] Les huit diodes D25–D32 conduisent dans le bon sens, avec une tension normale : présentes, bien orientées, ni coupées ni en court-circuit. Avec M5 (sens inverse : aucune conduction), contrôle complet. **K7 écartée.** D32 un peu plus basse : en partie le chemin parallèle par Q82 en court-circuit et R260 (quelques dizaines de µA détournés), peut-être aussi une diode d'une autre série (la diode remplacée de E4 ?). Pas un défaut |
| O5 | 25/10/2026 | Hors tension, J130 débranché, J127 branché | Photo de la zone J127–J130 (étages Sol 9–16 à gauche, Sol 02 et 05–08 au centre et à droite) | — | TIP36C ST « Morocco », codes date 9422 à 9431, sur Q66, Q68, Q70, Q80 (et un autre en colonne droite) ; TIP102 ST « Malaysia » 94xx dans la zone Sol 9–16 ; aucune brûlure visible dans le champ. Q82 et Q81 au bord inférieur droit, marquages illisibles ; Q71 hors champ. Résistances bleues montées debout à droite de Q80 et de Q82, différentes des résistances beiges du reste de la carte | [OBSERVÉ] Pièces visibles d'origine (1994), cohérentes entre elles. Numérotation de l'embase J130 conforme (9 à gauche, 1 à droite). Si la photo suit l'orientation de montage, le coin inférieur droit (Q82, D32, J130-1) est la zone des « points lumineux » (E5). Résistances bleues : voir O6 (matrice lampes, hors circuit Sol 01) |
| O6 | 25/10/2026 | Hors tension, J130 débranché | Photos rapprochées de Q80, Q81, Q82, D32, J130 | — | **Q82 : ST TIP36C, code date 9431, « Morocco »**, identique à Q66 et Q68 (9431) ; Q80 et Q70 : ST TIP36C 9422. Aucune brûlure visible autour de Q82, D32 et de l'embase J130 (côté composants). D32 : diode noire type 1N4004, sens impossible à vérifier sur photo. Q81 : seule sa semelle métallique est visible, marquage caché. Q71 hors champ. Détrompeur de J130 en position 3 (▼ sérigraphié). Résistances bleues à droite de Q82 : zone matrice lampes (R15x, Q84, J133/J134) | [OBSERVÉ] Q82 est du bon type et très probablement d'origine (jamais remplacé) : H6 écartée pour Q82, c'est le transistor d'usine qui a lâché. Reste à lire Q81 et Q71 ; sens de D32 à contrôler par M5 (broche 1) |
| M6 (1er essai) | 25/10/2026 | Hors tension, J130 débranché, F105 retiré | Clips de F105 : le clip **du bas** sonne avec TP6 (côté alimentation) ; le clip **du haut** est donc côté J107-2 (Rouge-Marron, bobines Sol 1–8). Puis « 10 kΩ avec la pin 1 », points exacts non précisés | Clip du haut ↔ fiche J130 position 1 : ≈ 3,5–4,5 Ω | 10 kΩ | 10 kΩ = signature de R260 (50 V ↔ masse) : la mesure est très probablement passée par le côté TP6 (clip du bas), la broche 1 de la carte étant à la masse par Q82. Attendu, sans information sur la bobine. À refaire avec le clip du haut et le contact de la fiche débranchée. Si ces points-là donnent 10 kΩ, anomalie (M2 montrait ≈ 4 Ω à travers la bobine) |
| M6 | 25/10/2026 | Hors tension, J130 débranché, F105 retiré, F101–F104 en place | Clip du haut de F105 (côté J107-2, Rouge-Marron) ↔ contacts de la fiche J130 débranchée : positions 1 (Sol 01), 8 (Sol 07), 9 (Sol 08) | Trois valeurs voisines ≈ 3,5–4,5 Ω | **Position 9 : 4,2 Ω ; positions 1 et 8 : OL** sur 200 Ω. Sur le calibre 20 MΩ : une valeur s'affiche pour les positions 1 et 8 ; celle de la position 1 monte lentement | [MESURÉ] Sol 08 normale (AE-23-800 + câblage) ; confirme que le clip du haut alimente bien des bobines Sol 1–8. Sol 07 (Knocker, dans la caisse) : OL pas forcément anormal, il peut être câblé par J131 (« CAB ») plutôt que J130. **Sol 01 : OL inattendu**, puisque M2 montrait ≈ 4 Ω à travers la bobine reliée à J130-1. Explications possibles : (a) erreur de position (à vérifier par la couleur du fil) ; (b) pointe sans contact dans l'alvéole ; (c) contact de la fiche en position 1 ouvert (il a transporté plusieurs ampères ; manipulé au débranchement) ; (d) bobine Sol 01 alimentée par un autre fusible que F105 (le tableau du manuel contient des erreurs, PinWiki) → M6bis. Les valeurs en MΩ ne sont pas des bobines (quelques ohms) mais des fuites ou des chemins à travers diodes et condensateurs. Une lecture qui monte lentement sur 20 MΩ = un gros condensateur chargé par le très faible courant de mesure, a priori C8 (100 µF) : le fil de la position 1 semble rejoindre le bus 50 V ou la masse par un autre chemin que F105, ce qui va dans le sens de (d) |
| M6 (reprise) | 25/10/2026 | Idem M6 | Idem M6 | Idem M6 | L'utilisateur signale que les mesures précédentes n'étaient **pas prises au bon endroit** sur la fiche J130. Position 9 refaite : **≈ 4,5 Ω**. Positions 1 et 8 : rien sur 200 Ω ; **≈ 2,5 MΩ** sur le calibre 20 MΩ, même valeur pour les deux | [MESURÉ] Sol 08 ≈ 4,2–4,5 Ω, normale. **Les fils des positions 1 (Sol 01) et 8 (Sol 07) ne rejoignent pas le clip du haut de F105 par une bobine** (une bobine ferait quelques ohms). Les 2,5 MΩ, identiques pour les deux, évoquent un chemin commun à travers une diode parcourue par le très faible courant de ce calibre (par exemple bobine → autre fusible → bus 50 V → R260 → masse → Q82 → D32 → clip du haut, si les cathodes D25–D32 sont sur le 50 V après F105). Contredit le manuel (Sol 1–8 sur F105, Rouge-Marron) : erreur de tableau ou câblage modifié. Couleurs des fils à confirmer → M6bis |
| M6bis | 25/10/2026 | Hors tension, J130 débranché, F105 retiré, F101–F104 en place | Couleurs de la fiche J130 ; contact Violet-Marron (position 1) ↔ clip du bas de F105 (côté TP6) | ≈ 4 Ω si la Sol 01 passe par F101–F104 | Couleurs **confirmées** (1 Violet-Marron, 8 Violet-Noir, 9 Violet-Gris) ; **≈ 4 Ω** | [MESURÉ] **La bobine Sol 01 est alimentée par l'un des fusibles F101–F104, pas par F105** : le tableau du manuel est faux sur ce point, ou le câblage a été modifié. Bobine + câblage ≈ 4 Ω, du même ordre que la Sol 08 (≈ 4,5 Ω) : pas d'indice net de spires en court-circuit (à préciser aux cosses). Le chemin de M2 passait donc par un autre fusible que F105 → H-hist2 renforcée |
| M7 | 25/10/2026 | Hors tension, J130 débranché, F105 et **F104 retirés** (l'utilisateur a retiré F104 au lieu de débrancher J107) | Contacts Violet-Marron (Sol 01) et Violet-Noir (Sol 07, Knocker) de la fiche J130 ↔ clip du haut de F104 | ≈ 4 Ω sur le fusible qui alimente la Sol 01 | **Sol 01 ≈ 4 Ω ; Sol 07 ≈ 4 Ω** | [MESURÉ] **Les bobines Sol 01 et Sol 07 sont alimentées par F104** (ligne « LO POWER PULSE », J107-3 Rouge-Noir selon le manuel, qui la réserve aux Sol 9–16). **Confirmé** : avec F104 et F105 retirés, Violet-Marron ↔ TP6 = **OL** ; F104 est le seul fusible qui alimente la Sol 01. H-hist2 (F103) non confirmée telle quelle. Le chemin de M2 passait par F104 |
| O10 | 25/10/2026 | Hors tension | F104 retiré | 3 A temporisé | Marquage **« BUSS MDL 3A »** ; verre clair, embouts propres | [OBSERVÉ] Bussmann MDL = fusible 3AG (6,3 × 32 mm) **temporisé** : 3 A, conforme au manuel. C'est F104 qui portait le courant de la Sol 01 collée : le comportement décrit pour F105 (O7 : un temporisé peut tenir plusieurs secondes à 2–3 fois son calibre) s'applique à F104. K5 écartée aussi pour F104. Aucune trace de chauffe |
| O11 | 25/10/2026 | Hors tension, plateau levé | Photo d'une bobine sous le plateau (`photos/2026-10-25_O11_bobine-AE-23-800.jpg`) | Bobine Sol 01 | Bobine **AE-23-800** (logo Williams), montée en biais dans une équerre avec son plongeur. Fil violet sur une cosse, gros fil rouge sur l'autre (rayure non lisible). Enveloppe sans brûlure visible. **Diode non visible** sur la photo (floue) | [OBSERVÉ] Identité à confirmer : deux AE-23-800 sous le plateau (Sol 01 Ball Launch, couloir de lancement ; Sol 08 Wall Target Up). Rayure du fil violet : marron → Sol 01 ; gris → Sol 08. Rayure du fil rouge : noir attendu (F104). Diode à vérifier sur une photo nette des cosses |
| M8 | 25/10/2026 | Hors tension, bobine isolée (F104, F105 retirés, J130 débranché) | Résistance entre les deux cosses de la bobine AE-23-800 de O11 | ≈ 3,5–4 Ω | **≈ 4 Ω** (pointes déduites ou non : non précisé) | [MESURÉ] Valeur normale pour une AE-23-800 : pas de spires en court-circuit. Ne renseigne pas sur la diode (à 4 Ω, la tension de mesure est trop faible pour la faire conduire). Identité de la bobine (Sol 01 ou Sol 08) encore à confirmer par la rayure du fil violet |
| O12 | 25/10/2026 | Hors tension, plateau levé | Cosses de la bobine de O11/M8 (photo nette `photos/2026-10-25_O12_bobine-Sol01-cosses.jpg`) | Diode sur la bobine (supposition erronée, voir interprétation) | Fils : **Violet-Marron** (commande) et **Rouge-Marron** (alimentation). **Aucune diode** entre les cosses. Soudures des cosses propres, fils du bobinage bien engagés, enveloppe intacte de ce côté | [OBSERVÉ] C'est bien la **Sol 01**. Absence de diode **normale** en WPC pour les sorties 1–16 : la diode de roue libre est sur la PD (D32 pour la Sol 01, saine, M5/M5bis) ; les schémas du manuel (p. 3-8) et de la théorie WPC (p. 3-11) dessinent la bobine sans diode. **K1 écartée.** Incohérence : le Rouge-Marron est la couleur que le manuel attribue à F105, or la Sol 01 est alimentée par le fusible repéré F104 (M7) → Q9 |
| O13 | 25/10/2026 | Hors tension, plateau levé | Photo de « l'autre AE-23-800 » (`photos/2026-10-25_O13_bobine-Sol08-cosses.jpg`) | Sol 08 : Violet-Gris + fil d'alimentation | AE-23-800, **pas de diode** (normal en WPC), soudures propres. Fil violet sur une cosse (rayure non visible) ; sur l'autre, fil **rouge à marques noires** (Rouge-Noir probable), peut-être un second fil rouge en chaîne | [OBSERVÉ] À confirmer : rayure grise du violet (Sol 08) ; marques noires imprimées sur l'isolant (Rouge-Noir) et non ruban ou gaine (réparation). Si Rouge-Noir : Sol 08 (Rouge-Noir) sur F105 et Sol 01 (Rouge-Marron) sur F104, soit l'inverse du brochage du manuel ; et les Sol 1–8 ne sont pas toutes sur la même couleur → §5.5 |
| O14 | 25/10/2026 | Hors tension, J107 encore branché | Photo de J107 et de la rangée F101–F105 (`photos/2026-10-25_O14_J107-fils.jpg`, annotée : `photos/2026-10-25_annotee_J107-F104-F105.jpg`) | Manuel : 1 Rouge-Orange (F103), 2 Rouge-Marron (F105), 3 Rouge-Noir (F104), 4 détrompeur, 6 Rouge-Blanc (20 V flashers) | Lecture provisoire sur photo : position 1 fil à marque orange, position 2 trace brune dans l'alvéole, position 3 fil rouge à bague noire, positions 4 et 5 vides, position 6 fil rouge à marques blanches. Rangée de fusibles de gauche à droite : F101, F102, F103 en place, F104 et F105 retirés | [OBSERVÉ] Fiche J107 apparemment conforme au manuel (à confirmer fiche débranchée). Si c'est le cas, l'inversion F104/F105 se trouverait côté carte (A3 ou A4) → M9 |
| O15 | 25/10/2026 | Hors tension, J107 débranché | Fiche J107 en main, côté entrée des fils (`photos/2026-10-25_O15_fiche-J107.jpg`) | 1 Rouge-Orange, 2 Rouge-Marron, 3 Rouge-Noir, 6 Rouge-Blanc | Fils rouges marqués par anneaux de couleur (pas de rayure continue) : anneau blanc, anneau noir, marques orange ou brunes. Vue inversée par rapport à la carte : de gauche à droite, blanc (position 6), vide (5), vide (4, détrompeur), noir (3), marque brune (2), rouge à marque orange plus haut (1) | [OBSERVÉ] Fiche J107 **conforme au brochage du manuel** (orange/brun à distinguer de visu entre 1 et 2). L'inversion F104/F105 n'est donc pas dans la fiche : elle est sur la carte (A3, A4) ou dans le faisceau entre J107 et les bobines → continuité carte puis fiche J107 ↔ fiche J130 |
| M9a | 25/10/2026 | Hors tension, J107 débranché, F104 et F105 retirés | Continuité clip du haut de F104 / F105 ↔ broches de l'embase J107 de la PD | Schéma relu de près : F104 (« LO POWER PULSE ») → broche 2, F105 (« HI POWER PULSE ») → broche 3 | **Fusible 4 (F104) → broche 2 ; fusible 5 (F105) → broche 3** | [MESURÉ] **Carte conforme à son schéma.** Avec la fiche conforme au manuel (O15 : 2 Rouge-Marron, 3 Rouge-Noir), F104 protège le Rouge-Marron et F105 le Rouge-Noir. Erreur dans le tableau des fusibles du manuel (p. 1-52) et dans ses schémas simplifiés (p. 3-8), pas dans la machine. (Lors de la préparation de M9, l'assistant avait annoncé l'inverse en se fiant au manuel ; corrigé après relecture du schéma.) |
| M10 | 25/10/2026 | Hors tension ; fiche J107 rebranchée, F104 et F105 retirés ; fiche J130 débranchée | Clip du haut de F104 (Rouge-Marron) ou de F105 (Rouge-Noir) ↔ contacts de la fiche J130 | Une valeur de bobine dans une seule colonne | Position 1 (Sol 01) : **4 Ω** sur F104 ; position 2 (Sol 02 Lockup Kickout) : **32 Ω** sur F104 ; position 7 (Sol 06 Right Diverter Left) : **7 Ω** sur F104 ; position 9 (Sol 08) : **4 Ω** sur F105. Positions 4, 5, 6 (Sol 03, 04, 05) : **sur F104** (valeurs non communiquées) ; position 8 (Sol 07) : 4 Ω sur F104 en M7 ; position 7 : l'utilisateur la classe ensuite « pas encore connue », à confirmer. Bilan provisoire : Sol 01–07 sur F104 (Rouge-Marron), Sol 08 sur F105 (Rouge-Noir) | [MESURÉ] Aucune valeur basse dangereuse (repère indicatif : moins de 2,5–3 Ω, ou nettement moins que les bobines jumelles). Sol 02 : bobine spéciale A-14189 sans donnée d'enroulement dans le manuel ; 32 Ω est élevé mais une résistance trop forte ne menace pas la carte (moins de courant), au pire une bobine faible : lire l'étiquette de la bobine à l'occasion. Sol 06 : 7 Ω plausible pour une AE-25-1000 ; Sol 03–05 (même modèle) à mesurer |
| M10 (complet) | 25/10/2026 | Idem M10 | Idem | — | Correction de l'utilisateur : **Sol 01 4 Ω, Sol 02 32 Ω, Sol 03 7 Ω, Sol 04 7 Ω, Sol 05 7 Ω, Sol 06 7 Ω, Sol 07 4 Ω : toutes sur F104** ; **Sol 08 4 Ω sur F105** (seule) | [MESURÉ] **Groupe Sol 1–8 validé côté bobines** : trois AE-23-800 identiques (4 Ω), quatre AE-25-1000 identiques (7 Ω), aucune valeur basse ; Sol 02 (A-14189) à 32 Ω, sans danger. Carte réelle : Sol 01–07 sur Rouge-Marron (F104), Sol 08 sur Rouge-Noir (F105). Reste pour ce groupe : contact éventuel d'un fil de commande avec une autre ligne 50 V (contrôle global prévu en fin de phase B) |
| M11 | 25/10/2026 | Hors tension ; F104, F105 retirés ; J107 branché ; J127 et J130 débranchés | Clip du haut de F105 (Rouge-Noir) ↔ contacts de la fiche J127, de la position 9 à la 1 | Paires égales | Relevé redonné par l'utilisateur dans l'ordre : 1 (Sol 09) **11 Ω** ; 2 détrompeur ; 3 (Sol 10) **11 Ω** ; 4 (Sol 11) **13 Ω** ; 5 (Sol 12) **14 Ω** ; 6 (Sol 13) **14 Ω** ; 7 (Sol 14) **7,5 Ω** ; 8 (Sol 15 Mini Kicker) **7,5 Ω** ; 9 (Sol 16) **16,5 Ω** (premier relevé, à rebours : 11, 10, 13, 14, 15, 7, 7, 16) | [MESURÉ] **Groupe Sol 9–16 validé côté bobines**, toutes sur F105 (Rouge-Noir) : paires identiques (Sol 09/10 : 11/11 Ω ; Sol 12/13 : 14/14 Ω ; Sol 14/15 : 7,5/7,5 Ω, comme les AE-25-1000 des déviateurs), aucune valeur basse. Mini Kicker sain au repos (un frottement intermittent du fil sur le chariot reste possible : à vérifier en déplaçant le chariot lors du contrôle global) |
| M12 | 25/10/2026 | Hors tension ; F103 en place, F104 et F105 retirés ; J107 branché ; J126 et J122 débranchés (J127, J130 aussi) | Clip du bas de F104 (bus 50 V) ↔ fiches J126 et J122 | Sol 24 ≈ 7 Ω ; Sol 25 ≈ 11 Ω ; tieback ≈ 0 Ω | **J126 p8 (Sol 24) 7,7 Ω ; J126 p11 (tieback) 0,5 Ω ; J122 p1 (Sol 25) 10,9 Ω ; J122 p5 (tieback) 0,5 Ω** | [MESURÉ] Ligne Rouge-Orange (F103) saine : Sol 24 (AE-25-1000) et Sol 25 (AE-26-1200) normales ; **les deux fils de tieback sont bien reliés au Rouge-Orange** (0,5 Ω, pointes comprises) : R5 écartée |
| M14 | 01/11/2026 | Hors tension (à confirmer) ; état supposé de fin de séance 1, à confirmer (J107 branché ; J130, J127, J126, J122 débranchés ; F104, F105 retirés ; F103 en place) ; calibre et sens des pointes non précisés | TP7 (+20 V flashers) ↔ TP5 (masse), en ohms (`photos/plan-PD_TP7-TP5-C11_zoom.png`) | Schéma, feuille 1 : C11 (15 000 µF) entre le +20 V et la masse, en parallèle avec LED5 + R194 (1,5 kΩ) ; par J107-6, le fil Rouge-Blanc vers les flashers. Lecture qui part de presque 0 et monte lentement et régulièrement, jusqu'à plusieurs kΩ ou OL | « Une résistance qui varie » : d'abord un **bip** en mode continuité, puis **39 Ω**, puis **171 kΩ** sur le calibre 200 kΩ (sens des pointes non précisé) ; après plusieurs minutes, **continue de monter au-delà de 171 kΩ**. État confirmé : F103 aussi retiré | [OBSERVÉ] Compatible avec la charge de C11 par le multimètre (normal), non confirmé. Un défaut donnerait une valeur basse stable (+20 V ou retour de flasher à la masse), des sauts (contact intermittent) ou un palier intermédiaire stable (fuite) → M14bis. **Conclusion (montée continue) : charge de C11, pas de court-circuit ni de fuite notable entre le +20 V et la masse.** |
| M13 (partiel) | 01/11/2026 | Hors tension ; F103, F104, F105 retirés ; J107 branché | Clips du haut A (F103), B (F104), C (F105) entre eux | OL | **A ↔ B, A ↔ C, B ↔ C : OL** | [MESURÉ] Les trois lignes 50 V (Rouge-Orange, Rouge-Marron, Rouge-Noir) ne se touchent pas. Reste : A, B, C ↔ TP7 ; C ↔ TP5 en déplaçant le Mini Kicker |
| M13 (Mini Kicker) | 01/11/2026 | Idem | C (F105, Rouge-Noir) ↔ masse en mode continuité, en déplaçant la palette du Mini Kicker sur toute sa course | Pas de bip | **Pas de continuité** | [MESURÉ] Pas de court-circuit franc à la masse du fil d'alimentation des Sol 9–16 pendant le mouvement du chariot (une fuite résistive ne serait pas vue en mode continuité). **Souvenir rapporté (E7, non confirmé)** : par le passé, redémarrages intempestifs de la machine, toujours peu après la sortie de la balle du mini-playfield ; l'utilisateur pense que c'était le court-circuit corrigé au début (flasher ou ampoule activé à ce moment-là), avant le remplacement de la diode. À garder en tête pour la remise sous tension (phase E) |
| M13 (fin) | 01/11/2026 | Idem | Clips du haut A, B, C ↔ TP7 (+20 V) | OL | **A, B, C ↔ TP7 : OL** | [MESURÉ] **M13 terminé** : les trois lignes 50 V sont isolées entre elles, isolées du +20 V des flashers et (M3, M13 Mini Kicker) de la masse. Faisceau des bobines exonéré pour les courts-circuits entre alimentations |
| L1 (1er essai) | 01/11/2026 | Hors tension ; F103–F105 retirés ; J107 branché. À confirmer : état de J135, et mesure faite sur l'embase ou sur la fiche J138 | Mode diode, pointe noire sur TP5, pointe rouge sur chaque « pin de J138 » | OL (fiche débranchée, faisceau isolé) | Valeur qui monte, la même quelle que soit la broche : 1200 → 1500 → 1600 mV | [MESURÉ] Signature d'un gros condensateur chargé par le multimètre, commun à toutes les colonnes. **Explication la plus probable :** mesure faite sur les broches de l'embase J138 de la carte. Chaque broche y rejoint le +18 V par les jonctions de son TIP107 (Q91–Q98), et le +18 V porte C6 et C7 (2 × 15 000 µF, `photos/plan-PD_C6-C7_18V_embase-J138.png`). C'est normal, mais ne dit rien du faisceau. Si la mesure a bien été faite sur la fiche : il existe un chemin commun des rangées vers une alimentation (J135 restée branchée, ou fil touchant une alimentation), à rechercher |
| L1bis (rangées) | 01/11/2026 | Fiche J135 débranchée (l'utilisateur mesure sur la fiche) ; polarité non précisée, supposée : pointe noire sur TP5 | Chaque contact de la fiche J135 (rangées 1 à 8) ↔ masse (« terre ») | OL | **Aucun fil connecté à la masse** | [MESURÉ] Aucune rangée du plateau ne touche la masse. Renforce l'explication de L1 (1er essai) : un chemin commun du faisceau vers un condensateur se retrouverait aussi sur les rangées. La montée venait donc très probablement de la carte (embase J138, ou fiche encore enfichée). L1 reste à faire sur la fiche J138 (colonnes ↔ masse, le cas qui détruirait un TIP107) |
| L1 | 01/11/2026 | Fiches J135 et J138 débranchées ; mode diode ; pointe noire sur TP5 | Contacts de la **fiche** J138 (colonnes) ; contre-épreuve sur l'**embase** J138 de la carte | Fiche : OL ; embase : valeur qui monte (+18 V, C6/C7) | **Fiche J138 : OL** ; **embase J138 : 1600 mV** | [MESURÉ] **L1 validée** : aucune colonne du plateau ne touche la masse, et aucune rangée non plus (sinon ≈ 0,5 V à travers une lampe ; L1bis le confirme). La contre-épreuve confirme l'explication du 1er essai : il avait été fait sur l'embase, et le chemin passait par les TIP107 vers le +18 V. Normal |
| L2 | 01/11/2026 | Idem L1 ; F103–F105 retirés, J107 branché | Mode diode : pointe noire dans le clip du haut A (F103), puis B (F104), puis C (F105) ; pointe rouge sur chaque contact de la fiche J138 (1–7, 9) | OL | **OL partout, sur A, B et C** | [MESURÉ] **L2 validée** : aucun fil de colonne ne touche une alimentation de bobines, et aucune rangée non plus (sinon ≈ 0,5 V à travers une lampe). Avec L1 : le faisceau de la matrice du plateau est isolé de la masse et des trois lignes 50 V |
| L2-20 V | 01/11/2026 | Idem L1 | Mode diode : pointe noire sur TP7 (+20 V flashers), pointe rouge sur chaque contact de la fiche J138 | OL | **OL partout** | [MESURÉ] Aucun fil de la matrice ne touche l'alimentation des flashers ni le fil de retour d'un flasher (vu à travers l'ampoule). **Faisceau de la matrice du plateau validé** : isolé de la masse, des lignes 50 V des bobines (F103–F105) et du 20 V. Reste non couvert : contacts rangée–colonne et diodes de lampes en court-circuit (test des lampes à la remise sous tension), GI, lampes de la caisse, lignes des flippers (F101, F102, à examiner avec les flippers) |
| G1 | 01/11/2026 | Hors tension ; fusibles F106–F110 en place ; fiches de la GI branchées | En ohms, calibre 200 Ω : pointe noire sur TP5, pointe rouge sur un clip de chaque fusible F106 à F110 | Valeur basse si la GI est reliée à la masse par le transformateur | **0,4 Ω partout** (soit la résistance des pointes) | [MESURÉ] **Les 5 circuits de GI sont reliés à la masse** par les enroulements du transformateur (J115-1 « GND REF »). Les mesures déjà faites couvrent donc les contacts de la GI avec la matrice des lampes (L1 : OL), avec le 50 V (M3 : 10 kΩ, R260 seule) et avec le 20 V (M14 : charge de C11, sans chemin bas). Reste hors de portée du multimètre : un court-circuit aller ↔ retour d'un même circuit (fusibles ; à surveiller à la remise sous tension) → G2 (examen visuel des connecteurs) |
| G2 | 01/11/2026 | Hors tension | Photos de la zone GI (`photos/2026-11-01_G2_*.jpg`) : J115, J120, J121, J119, fusibles F106–F110 | Pas de connecteur brûlé ; fusibles 5 A 250 V temporisés (manuel, §3.2) | **Connecteurs :** boîtiers intacts, pas de brunissement autour des broches, pas de plastique fondu, juste de la poussière ; isolant d'un fil blanc un peu jauni en J121-11. **Fusibles :** tous intacts (cohérent avec G1). F106, F109, F110 : élément en spirale. **F107 et F108 : fil droit et fin avec une petite perle verte, d'un autre type.** Dépôt brun dans le verre de F108, près d'un embout. Q10 marqué « PH BT138 500E 9430 » (triac Philips de 1994, équivalent du SC141 du schéma) | [OBSERVÉ] Pas de signe de surchauffe des connecteurs de la GI côté composants ; le dessous sera vu au banc. **F107 et F108 peut-être non conformes** (calibre ou type) : un calibre trop fort ne protégerait plus les triacs et les connecteurs ; un fusible rapide ou trop faible fondrait pour rien à l'allumage (ampoules froides). Le dépôt de F108 est probablement un résidu de fabrication (un fusible surchargé noircit ou argente le verre), à confirmer. → G3 : lire le marquage de F107 et F108 |
| G3 | 01/11/2026 | Hors tension | Marquage des fusibles F107 et F108 | 5 A 250 V temporisé | **« T5AL250V »** | [OBSERVÉ] T = temporisé, 5 A, L = faible pouvoir de coupure (normal pour un fusible en verre), 250 V : **conformes**. Le fil droit à perle est une autre construction de fusible temporisé. Au remontage, à titre de précaution : remplacer F108 (dépôt brun) par un T5A neuf et vérifier le serrage de ses clips (un clip lâche chauffe). **GI terminée** : G1, G2, G3 bons |
| F1 (J126) | 01/11/2026 | Hors tension ; J126, J122 débranchés ; J107 branché | En ohms, calibre 200 Ω : pointe noire sur TP7, pointe rouge sur les contacts flashers de la fiche J126 (1, 2, 5, 6, 7 = Sol 17, 18, 21, 22, 23) | Quelques ohms ; ≈ 0,4 Ω (pointes seules) = court-circuit | **Entre 1,4 et 5 Ω** (valeurs individuelles non communiquées) | [MESURÉ] Aucune douille ni aucun fil de flasher en court-circuit sur ces 5 sorties. Les écarts viennent du nombre ou du type d'ampoules, ou d'un contact un peu oxydé : sans danger pour la carte (plus de résistance, moins de courant). Vérifier à l'allumage que chaque flasher éclaire normalement. Reste J122 (2, 3, 4 = Sol 26, 27, 28) |
| F1 (J122) | 01/11/2026 | Idem | Contacts flashers de la fiche J122 : 2 (Sol 26 Left Back), 3 (Sol 27 Center Back), 4 (Sol 28 Right Back) ↔ TP7 | Idem | **5,6 Ω ; 7,5 Ω ; 2 Ω** | [MESURÉ] Pas de court-circuit : **les 8 flashers du plateau sont sans danger pour la carte.** Sol 26 et 27 (5,6 et 7,5 Ω) sont nettement au-dessus d'une ampoule #906 froide (≈ 1,5 Ω) : autre type d'ampoule, LED, ou contact de douille résistant (qui chaufferait en service). **À l'allumage, vérifier l'éclat de Sol 26 et 27** et, s'il est faible, nettoyer leurs douilles. Manuel p. 3-7 : flashers du plateau alimentés par J107-6, flashers de la tête (« insert ») par **J106-5**, avec retours J124-2/3/5 (Sol 26–28) et J125-1/2 (Sol 17, 18) → F1-tête |
| F1-tête | 01/11/2026 | Fiches J124 et J125 débranchées ; J106 branché | En ohms, calibre 200 Ω : pointe noire sur TP7, pointe rouge sur les contacts des fiches J124 et J125 | Quelques ohms ; ≈ 0,4 Ω = court-circuit | **J124-1 : OL** (position sans fil, normal) ; **J124-2 (Sol 26) : OL** ; **J124-3 (Sol 27) : 2 Ω** ; **J124-5 (Sol 28) : 4 Ω** ; **J125-1 (Sol 17) : 2 Ω** ; **J125-2 (Sol 18) : 10 Ω** | [MESURÉ] **Aucun flasher en court-circuit, ni au plateau ni dans la tête : F1 validé.** Le +20 V de la tête arrive bien (J106). À noter pour la remise en état : flasher Sol 26 de la tête ouvert (ampoule absente ou grillée, ou fil coupé) ; Sol 18 de la tête (10 Ω), Sol 26 et 27 du plateau (5,6 et 7,5 Ω) élevés : vérifier leur éclat à l'allumage |
| F2 | 01/11/2026 | Hors tension ; F101, F102 en place (lignes des flippers reliées à TP6) ; F103–F105 retirés ; fiches J135, J138 débranchées | Mode diode : pointe noire sur TP6, pointe rouge sur chaque contact de la fiche J138 ; puis pointe rouge sur TP6, pointe noire sur TP7 | OL | **OL partout** | [MESURÉ] Les lignes 50 V des flippers (et le bus 50 V) ne touchent ni la matrice des lampes ni le 20 V. **Fin des contrôles côté machine** pour ce qui peut détruire la PD : bobines (M3–M13), matrice des lampes (L1, L2), GI (G1–G3), flashers (F1), flippers côté PD (F2) |
| O16 | 01/11/2026 | Photo O9 relue en pleine résolution (`photos/2026-11-01_annotee_resistances-0R22-rangees.jpg`) | Zone des pilotes de lampes (Q83–Q98) et 8 résistances bleues | — | Les 8 résistances bleues sont les **0,22 Ω 1 W des rangées** (R150–R153, R172–R175 ; anneaux rouge-rouge-argent-or). Elles sont **montées à plat**, dans leur sérigraphie : la mention « montées debout » de O5 était erronée. Aucune trace de chauffe visible à cette résolution, ni sur elles ni sur les transistors. Les deux résistances de gauche du groupe R172–R175 sont en partie masquées par les languettes des transistors voisins | [OBSERVÉ] Type 1 W, rien n'indique un remplacement. **On ne sait pas encore quelle pièce a « brillé » (E5).** Le plus souvent, ce sont les 0,22 Ω qui rougissent lors d'une surintensité des rangées ; un transistor en boîtier plastique chauffe ou se fend, mais brille rarement. Ce n'est qu'une hypothèse. À trancher au banc : valeur des 8 résistances, test des 16 transistors, examen des deux faces de la carte |

## 5. Hypothèses

### 5.1 Symptôme : Sol 01 collée

| ID | Hypothèse | Arguments | Test discriminant | Statut |
|---|---|---|---|---|
| H1 | Q82 (TIP36C) en court-circuit émetteur-collecteur | Cause la plus fréquente d'une bobine collée dès l'allumage | Test de Q82 sur la PD, hors tension | **Quasi confirmée** (M4 : J130-1 à ≈ 0 Ω de la masse sur la PD). Reste à départager Q82 et un pont de soudure ou une piste : dessouder une patte de Q82 |
| H2 | Q81 (TIP102), Q71 (2N5401) ou pont de soudure dans l'étage | Mêmes effets ; réparations récentes sur la carte | Test des composants, inspection à la loupe | En attente. Pont de soudure entre les pattes émetteur et collecteur de Q82 (voisines) compatible avec M2–M4 ; Q81 ou Q71 en défaut ne donneraient pas 4,5 Ω hors tension (chute de jonction de Q82, lecture de centaines d'ohms), mais peuvent coexister |
| H3 | Fil Violet-Marron (J130-1 → bobine) à la masse dans le faisceau | Alimenterait la bobine indépendamment de la PD | **M1** | **Écartée en l'état** (M3 : aucun fil Sol 1–8 à la masse, J130 débranché). Défaut intermittent non exclu |
| H4 | Sortie de U5 (74LS374) endommagée ou blanking défaillant | Peu probable si la bobine colle avant la fin du démarrage | Chronologie à l'allumage (LED D19) ; test sur banc plus tard | Inutile pour expliquer O1 (M4) ; reste une cause possible de la destruction de Q82 (§5.4, K4) |
| H5 | Blocage mécanique du plongeur | L'utilisateur décrit un maintien magnétique | Plongeur libre hors tension | Inutile pour expliquer O1 (M4) ; plongeur à contrôler quand même (Phase A) |
| H6 | Pièce de remplacement de mauvais type (même boîtier, même brochage) dans l'étage Sol 01 : 2N5551 (NPN) au lieu de 2N5401 en Q71 ; TIP107 (PNP) au lieu de TIP102 en Q81 ; TIP35C (NPN) au lieu de TIP36C en Q82 ; TIP36 ou TIP36A en Q82 (tenue 40 / 60 V, insuffisante sur le 50 V) | D'après le schéma (feuille 3) : un NPN en Q71 conduit par sa jonction base-collecteur dès que R134 tire sa base au +5 V, donc pendant le blanking et chaque fois que la bobine devrait être au repos, et il commande Q81 ; un TIP107 en Q81 tire la base de Q82 à la masse par sa diode interne collecteur-émetteur ; un TIP35C en Q82, polarisé à l'envers, relie la bobine à la masse par ses jonctions ; un TIP36/36A peut conduire partiellement. Dans chaque cas, Q82 peut conduire dès la mise sous tension, sans commande, avec un fort échauffement. Pertinente seulement si cet étage a été touché lors des réparations | Lecture des marquages de Q71, Q81, Q82 (sans mesure) | **Écartée pour Q82** (O6 : TIP36C ST d'origine). Reste ouverte pour Q81 et Q71 : un TIP107 en Q81 ou un 2N5551 en Q71 aurait fait conduire Q82 en permanence. Q81 sans marquage visible (O8), mais même aspect que Q77 et Q79 (O9) : probablement d'origine. Q71 : 2N5401 National très probable (O9). **Très peu probable**, confirmation sur banc |

### 5.2 Risques pour une PD réparée (à éliminer avant reconnexion)

| ID | Risque | Contrôle prévu | Statut |
|---|---|---|---|
| R1 | Bobine en court-circuit (spires), surtout la Sol 01 si elle a chauffé | Résistance de chaque bobine, comparaison entre bobines identiques | À faire |
| R2 | Diode de bobine inversée ou en court-circuit | Inspection, test | À faire |
| R3 | Fil de commande en contact avec le 50 V ou avec un autre fil de commande | Mesures croisées | À faire |
| R4 | Lignes 50 V (Rouge-Marron, Rouge-Noir, Rouge-Orange, Rouge-Gris Fliptronic) à la masse ou en contact avec le 20 V, 12 V, 5 V, la GI, les matrices lampes ou contacts, notamment au mini-playfield | Mesures d'isolement, inspection | Masse : aucun chemin bas en l'état (M3), sous réserve de l'état des fusibles F101–F104. Autres tensions : à faire |
| R5 | Tieback J122-5 / J126-11 non relié au Rouge-Orange | Continuité | **Écarté** (M12 : 0,5 Ω sur les deux) |
| R6 | Fusibles non conformes (calibre, type), porte-fusibles abîmés | Inventaire | F105 et F104 conformes (O7, O10) ; autres fusibles et état des clips à faire |
| R7 | Dégâts résiduels sur la PD (TIP36C, TIP102, 2N5401, diodes D5–D12 et D17–D32, BR3, ponts de soudure, composants remplacés mal orientés) | Contrôle sur banc | **Confirmé** : sortie Sol 01 en court-circuit (M3, M4). Sorties Sol 02–08 sans court-circuit, diodes D25–D32 saines (M4, M5bis). Reste : Q81, Q71, résistances de l'étage, autres groupes |
| R8 | Dégâts collatéraux ailleurs (CPU et matrice contacts, cartes optos, carte moteur A-16120, Fliptronic II) | À évaluer selon les résultats | À faire |

### 5.3 Bip TP6 ↔ masse, PD branchée (O2)

[DOC] Sur la PD, le bus 50 V (TP6 : BR3 → C8 100 µF 150 V → R260 10 kΩ → F101–F105) ne rejoint la masse que par R260. Les sorties saines ne conduisent pas quand la pointe rouge (+) est sur TP6. Un bip signifie donc une résistance de quelques ohms à quelques dizaines d'ohms (seuil propre au multimètre), sauf bip bref de charge de C8.

| ID | Chemin possible | Lecture M2 attendue | Test suivant |
|---|---|---|---|
| C1 | Aucun défaut : bip bref dû à la charge de C8 | Valeur qui monte puis se stabilise vers 10 kΩ | — |
| C2 | Bobine du groupe Sol 1–8 dont la sortie est à la masse : Q82 (ou Q80, Q78…) en court-circuit, pont de soudure, ou fil Violet-xxx à la masse. Cohérent avec O1 | Résistance d'une bobine (≈ 3–5 Ω pour une AE-23-800 : Sol 01, 07, 08) | Débranchement de J130 (M3) |
| C3 | Même chose sur un autre réseau (F101/F102 flippers, F104 Sol 9–16, F103 Sol 24–25) | Résistance de la bobine concernée | Retrait des fusibles un par un |
| C4 | Fil d'alimentation 50 V à la masse dans le faisceau (Rouge-Orange : voir H-hist ; ou Rouge-Marron, Rouge-Noir, flippers) | ≈ 0 Ω | Retrait des fusibles un par un |
| C5 | Défaut sur le bus 50 V de la PD (C8, BR3, pont de soudure, piste) | ≈ 0 Ω, persiste avec F101–F105 retirés | Contrôle sur banc |

Hors tension, une pièce de mauvais type (H6) ne donne pas à elle seule une lecture basse et stable : ses jonctions ne conduisent qu'avec une chute de tension. Une lecture de quelques ohms désigne plutôt une pièce réellement en court-circuit (H6 peut en revanche avoir détruit Q82) ou un fil.

**Après M2 (4,5 Ω)** : C1 écartée. C4 et C5 peu probables (un court-circuit direct donnerait moins de 1 Ω, sauf liaison elle-même résistive). Restent C2 et C3, éventuellement plusieurs chemins en parallèle (par exemple deux bobines d'environ 9 Ω). Sous tension, ce chemin ferait passer de l'ordre de 50 V / 4,5 Ω ≈ 11 A : **aucune remise sous tension tant qu'il existe**.

**Après M3 (10 kΩ, J130 débranché)** : C2 confirmée, côté PD : le seul chemin passait par une sortie Sol 1–8 de la PD (ou par le contact du connecteur J130 lui-même). C3, C4 et C5 écartées en l'état, sous réserve que F101–F104 soient en place et intacts (une branche dont le fusible est grillé ou absent n'est pas reliée à TP6, donc pas testée). La sortie fautive n'a pas sa diode de roue libre (D25–D32) en court-circuit, sinon TP6 resterait relié à la masse J130 débranché. Ces mesures ne couvrent ni les liaisons vers les autres tensions, ni les bobines (spires, diodes), ni les défauts intermittents.

### 5.4 Pourquoi la sortie Sol 01 a-t-elle lâché ? (cause racine)

Remplacer Q82 sans trouver la cause risque de le détruire de nouveau. Aucune piste n'est prouvée.

| ID | Cause possible | Arguments | Test | Statut |
|---|---|---|---|---|
| K1 | Diode de la bobine Sol 01 montée à l'envers | Supposait une diode sur la bobine | Inspection | **Écartée** : en WPC, les bobines des sorties 1–16 n'ont pas de diode, la protection est D32 sur la PD (saine) ; aucune diode sur la bobine (O12) |
| K2 | Bobine Sol 01 aux spires en court-circuit (courant excessif) | ≈ 4,0 Ω avec fils et fusible : pas d'indice fort. Mais conséquence possible (et non seulement cause) : bobine restée alimentée plusieurs secondes à plusieurs ampères (O7) | Mesure directe aux cosses, comparaison avec Sol 07 et Sol 08 ; aspect de l'enveloppe | M6bis : ≈ 4 Ω (bobine + câblage + fusible) contre ≈ 4,5 Ω pour la Sol 08 ; M8 : ≈ 4 Ω aux cosses ; O12 : c'est bien la Sol 01. **Écartée** |
| K3 | Pièce de mauvais type ou pont de soudure lors d'une réparation (H6, H2) | Réparations antérieures sur la carte | O4 (marquages), inspection des soudures | Q82 d'origine (O6) ; Q81 et Q71 vraisemblablement d'origine (O9) ; restent les soudures côté cuivre et la confirmation sur banc. Peu probable |
| K7 | D32 (diode de roue libre de Q82 sur la PD) montée à l'envers lors d'une réparation : à chaque commande, elle court-circuite le 50 V à travers Q82 | E4 : une diode de la PD a été remplacée, repère inconnu | M5, broche 1 | **Écartée** (M5bis : D32 conduit de la broche 1 vers le 50 V, donc bien orientée) |
| K4 | Sortie commandée trop longtemps : U5, Q71, Q81, blanking, CPU (H4) | Souvenir de transistors qui chauffaient (E5) | Banc (Q81, Q71) ; à la remise sous tension progressive, sorties surveillées bobines débranchées | En attente : **principale piste restante** avec K8 |
| K9 | Lien avec le court-circuit qui faisait fondre F103 (question de l'utilisateur) | D'après le schéma, Q82 n'est pas dans le circuit de F103 : la Sol 01 est sur F104, D32 se referme sur le bus 50 V principal, la commande (U5, Q71, Q81) est en +5 V. Une simple mise à la masse de la ligne Rouge-Orange charge le 50 V et fait fondre F103 (et force le courant des flashers dans les diodes de tieback, H-hist), sans faire passer de courant dans Q82. Deux scénarios rendraient le lien possible : (a) contact entre le fil Violet-Marron (ou la bobine Sol 01) et la ligne F103 : chaque lancement aurait court-circuité cette ligne à travers Q82, d'où F103 fondu et Q82 surchauffé ; (b) court-circuit qui aurait porté le 50 V sur un fil basse tension (lampes, contacts) et abîmé la commande de Q82 (U5, Q71, Q81), qui l'aurait laissé conduire. Un 50 V sur un fil de lampe expliquerait aussi les pilotes de lampes illuminés (E5) | (a) aujourd'hui absent (M7 : Violet-Marron sans contact avec F101–F103, au repos) ; (b) banc (Q81, Q71) et remise sous tension. Questions : où était le court-circuit réparé (quels fils) ? quelle diode a brûlé ? la Sol 01 collait-elle avant ou après ? | **Renforcée** par la chronologie (la Sol 01 ne collait qu'après l'épisode F103, souvenir) ; mécanisme non identifié : scénario (b) à vérifier en priorité au banc (Q81, Q71) et à la remise sous tension (U5, logique) |
| K8 | Défaillance du TIP36C d'origine par usure (bobine de lancement puissante, ≈ 12 A en impulsion, très sollicitée) | Q82 d'origine, de 1994 (O6) ; aucune cause trouvée côté machine | Par élimination ; Q82 testé hors circuit | Plausible |
| K5 | F105 de calibre trop élevé, qui a laissé durer le courant (≈ 10 A) | F105 difficile à retirer (O3) : a-t-il chauffé ? | Lecture du marquage (Q7) | **Écartée** (O7 : F105 313 3A 250V ; O10 : F104 BUSS MDL 3A ; tous deux temporisés, conformes). C'est F104 qui alimentait la Sol 01 |
| K6 | Fil Violet-Marron en contact avec un 50 V : court-circuit franc dès la mise en conduction | — | M6bis, M7 | **Écartée** : avec F104 et F105 retirés, Violet-Marron ↔ TP6 = OL, donc aucun contact avec les réseaux F101–F103 ni le bus ; il ne rejoint le 50 V que par sa bobine (≈ 4 Ω, F104) |

### 5.5 Pourquoi les Sol 01 et 07 sont-elles sur F104 ? (question de l'utilisateur : défaut électrique ou erreur du manuel ?)

Faits mesurés : Sol 01 et Sol 07 sur le réseau de F104, Sol 08 sur celui de F105 (M6, M7) ; Sol 01 ↔ clip côté charge de F105 = OL pendant que Sol 01 ↔ clip côté charge de F104 ≈ 4 Ω. **Les deux réseaux sont donc séparés** : un court-circuit entre les lignes de F104 et de F105 les aurait réunis, et la Sol 01 aurait aussi donné ≈ 4 Ω vers F105. De plus, deux lignes 50 V issues du même bus par deux fusibles identiques sont au même potentiel : un contact entre elles ne ferait passer aucun courant de défaut.

| ID | Explication | Danger pour la PD | Test discriminant |
|---|---|---|---|
| A1 | Tableau ou brochage du manuel faux | Aucun | Par élimination de A2–A4 |
| A2 | Fiche J107 du faisceau re-brochée ou remplacée avec deux positions inversées | Aucun (même tension, fusibles identiques) | Couleur du fil à chaque position de la fiche J107 |
| A3 | Réparation de la PD avec fil de pontage ou piste refaite qui relie F104 et F105 aux mauvaises broches de J107 (historique de réparations, E4–E6) | Indirect : signe d'une réparation à contrôler | Continuité clip côté charge de F104 / F105 ↔ broches de l'embase J107 de la PD ; recherche de fils de pontage, pistes coupées |
| A4 | Révision de carte différente du schéma consulté (A-12697-1 contre carte -3) | Aucun | Comme A3 ; comparaison avec la sérigraphie |
| A5 | Fil d'alimentation de la Sol 01 raccordé à une autre ligne dans le faisceau (modification) | Aucun en soi | Couleur du fil d'alimentation de la Sol 08 et des bobines voisines ; suivi du Rouge-Marron |

Conséquence pratique : quelle que soit l'explication, la répartition réelle des bobines entre fusibles doit être établie par la mesure (checklist, phase B) et non lue dans le manuel.

Après O13 (si la Sol 08 est bien en Rouge-Noir) : les couleurs sont inversées par rapport au brochage du manuel (Rouge-Marron sur F104, Rouge-Noir sur F105) et le groupe Sol 1–8 n'est pas sur une seule couleur. A5 (une seule bobine raccordée ailleurs) devient peu probable ; M9 départagera A1 (manuel), A2 (fiche J107) et A3/A4 (carte).

**Résolu (M9a, O15, relecture du schéma)** : la carte suit son schéma (F104 → J107-2, F105 → J107-3), la fiche J107 suit le brochage du manuel (2 Rouge-Marron, 3 Rouge-Noir). C'est le tableau des fusibles du manuel qui inverse F104 et F105 : **A1 retenue**, aucun défaut électrique. Écart restant, sans danger : Sol 08 sur Rouge-Noir au lieu de Rouge-Marron (tableau des solénoïdes du manuel).

## 6. Hypothèse sur l'historique (non prouvée)

**H-hist** : une mise à la masse du Rouge-Orange 50 V (ou d'un fil lié à Sol 24/25) aurait fait fondre F103 et forcé le courant des flashers à travers les diodes tieback (D5–D12), dont l'une aurait brûlé. Compatible avec E1, E2 et E4 ; rien ne la prouve à ce stade. Elle n'explique pas, à elle seule, la Sol 01 collée (autre fusible, autre étage).

**H-hist2** (25/10/2026, après M6) : si la bobine Sol 01 est en réalité alimentée par **F103** (Rouge-Orange) et non par F105, c'est F103 qui a dû encaisser le courant de la Sol 01 collée par Q82 en court-circuit, ce qui expliquerait le souvenir « F103 sautait » (E2) et l'état impeccable de F105 (O7). Hypothèse non prouvée : à tester (M6bis, puis identification du fusible). **Renforcée par M6bis** : la Sol 01 n'est effectivement pas sur F105 ; reste à savoir si c'est F103 (M7). **M7 : c'est F104, pas F103.** Variante H-hist2' : le fusible qui sautait était F104 (souvenir E2 imprécis) ; F104 alimente la Sol 01 (et toute la ligne Rouge-Marron) ; le Mini Kicker (Sol 15) serait sur F105 (Rouge-Noir), à confirmer. À rapprocher de l'état de F104 (O10).

## 7. Checklist avant reconnexion de la PD

**Phase 0 — Sécurité et état initial**
- [ ] Cordon secteur débranché ; PD entièrement débranchée ; connecteurs photographiés.
- [ ] Inventaire des fusibles (calibre, type, état) comparé au §3.2.

**Phase A0 — Court-circuit 50 V ↔ masse constaté PD branchée (O2) : prioritaire**
- [x] M2 : résistance TP6 ↔ TP5 = 4,5 Ω (4,6 Ω sur la vis de masse).
- [x] M3 : débranchement de J130 → 10 kΩ : le chemin passait par une sortie Sol 1–8 de la PD.
- [x] M4 : broche 1 (Sol 01, Q82) à 0,5 Ω de la masse, pointes comprises ; broches 2 et 4–9 entre 155 et 200 kΩ (normal).

**Phase A — Circuit de la Sol 01**
- [x] M1 : isolement J130-1 (Violet-Marron) ↔ masse : couvert par M3 (masse de la PD et vis de masse au même potentiel, M2).
- [ ] Résistance de la bobine Sol 01 (J130-1 ↔ J107-2), comparée à Sol 07 et Sol 08.
- [ ] Isolement J107-2 (Rouge-Marron) ↔ masse.
- [ ] **Prioritaire** (cause possible de la destruction de Q82, K1) : inspection de la bobine Sol 01 : diode (sens, état), cosses, enveloppe brûlée, fils et connecteurs (J107-2, J130-1) ayant chauffé.
- [ ] Plongeur libre, ressort de rappel efficace.

**Phase B — Toutes les sorties bobines**
- [ ] **Cartographie réelle des alimentations** : pour chaque sortie, vérifier par mesure à quel fusible (clip côté charge) sa bobine est reliée. Le tableau du manuel est faux au moins pour la Sol 01 (sur F104, pas F105) et la Sol 07.
- [ ] Isolement par rapport à la masse, **réseau par réseau** : PD débranchée, chaque alimentation 50 V forme un seul circuit avec ses bobines et leurs fils de commande (environ un réseau par fusible 50 V ; M1 couvre déjà Sol 1–8). Fil par fil seulement si une bobine est coupée ou si un défaut apparaît.
- [ ] Résistances de toutes les bobines, sous forme de tableau (comparaison entre références identiques). **Sol 1–8 : fait (M10). Sol 9–16 : fait (M11). Sol 24–25 : fait (M12).** Restent les flippers et Sol 35–36 (Fliptronic II).
- [ ] Contrôle global, toutes fiches de sorties débranchées et fusibles F103–F105 retirés : clips côté charge F103 ↔ F104 ↔ F105 deux à deux → OL attendu (un fil de commande qui toucherait une autre ligne 50 V donnerait la résistance d'une bobine).
- [ ] Diodes des bobines (sens, état).
- [x] Continuité du tieback : J122-5 et J126-11 reliés au Rouge-Orange (M12, 0,5 Ω).
- [ ] Réseau flashers 20 V (Rouge-Blanc ; Sol 17, 18, 21–23, 26–28) et sorties vers la carte moteur (Sol 19, 20).
- [ ] Fliptronic II : bobines de flippers, Sol 35 Magnet, Sol 36 Single Drop Down.

**Phase C — Courts-circuits entre domaines de tension**
- [ ] Lignes 50 V ↔ 20 V, 12 V, 5 V, GI, rangées et colonnes lampes, matrice contacts.
- [ ] **Matrice lampes (priorité relevée par E5)** : rangées et colonnes (fiches J133–J138 du faisceau) ↔ masse, ↔ lignes 50 V et 20 V, et entre elles hors chemin normal des ampoules ; méthode courte à préparer avec images annotées.
- [ ] Inspection visuelle du faisceau au mini-playfield (Mini Kicker mobile, Mini Drop Bank, carte optos), aux drop targets, aux zones de passage et de charnière.
- [ ] Connecteurs du faisceau côté 50 V et sorties bobines (J102, J107, J130, J127, J126, J122) : alvéoles noircies, détendues ou mal serties. Fiche J130 : dépôts bruns côté positions 9 à 5 (O8) ; regarder la face des contacts, surtout la position 1 (la bobine collée y a fait passer plusieurs ampères), et tester au nettoyage (résidu qui part, ou plastique bruni).

**Phase D — Power Driver (sur banc)**
- [ ] En premier, sans mesure : marquages de Q71, Q81, Q82 et de toutes les pièces remplacées (référence exacte et orientation, H6) → **O4 en cours**.
- [ ] Dessouder une patte de Q82 (émetteur) : si le court-circuit J130-1 ↔ masse disparaît → Q82 ; s'il reste → pont de soudure ou piste. Tester Q82 hors circuit.
- [ ] Q82, Q81, Q71, D32 ; toutes les sorties TIP36C et TIP102 vers la masse.
- [ ] Diodes D5–D12 (tieback : M12 n'a vérifié que les **deux fils** du faisceau qui les relient au 50 V, pas les huit diodes) et D17–D32 (roue libre Sol 1–16) ; **D25–D32 : OK** (M5, M5bis) ; restent D5–D12 et D17–D24. La diode remplacée de E4 est probablement parmi elles : à identifier.
- [ ] **Pilotes de la matrice lampes Q83–Q98 et leurs résistances** (zone au-dessus de J133–J138, E5) : test en mode diode, valeurs des résistances, traces de chauffe.
- [ ] BR3, C8/R260, porte-fusibles ; embases (broches, soudures fissurées) ; ponts de soudure.
- [ ] Zone des « points lumineux » (E5).

**Phase E — Remise sous tension progressive (protocole à définir le moment venu)**
- [ ] Remontage du panneau afficheur : fil de terre vert-jaune du panneau rebranché ; nappe de l'afficheur (bande rouge = broche 1) et connecteur d'alimentation haute tension de l'afficheur rebranchés dans le bon sens, sans décalage d'une broche (un décalage peut détruire l'afficheur ou le contrôleur DMD à l'allumage).
- [ ] Tous les connecteurs débranchés pendant le diagnostic (J130, J107, …) rebranchés dans le bon sens, d'après les photos.
  - 25/10/2026 : nappe de l'afficheur débranchée puis rebranchée par l'utilisateur ; vérifiée sur photo (`photos/2026-10-25_panneau-afficheur-avant-depose.jpg`) : fiche entièrement dans le cadre noir du connecteur, centrée, ergot de détrompage dans l'encoche, bande rouge cohérente. Enfoncement complet à confirmer ; à revérifier au remontage du panneau.
- [ ] Première mise sous tension sans fusibles ni connecteurs bobines ; vérification des tensions et du blanking ; réintroduction progressive.

### Réparation au banc : précautions (l'utilisateur craint de décoller des pistes)

- Station de soudage réglable (≈ 330–350 °C avec de la soudure au plomb, un peu plus pour les grosses pastilles), panne tournevis de 2–3 mm (une panne trop fine oblige à chauffer plus longtemps), flux, tresse à dessouder et pompe ; idéalement un pistolet à dessouder.
- Transistors à remplacer (Q82, et Q81 si besoin) : **couper les pattes au ras du boîtier côté composants**, puis retirer chaque patte séparément au fer et à la pince, sans jamais tirer sur une patte tant que la soudure n'est pas entièrement fondue.
- Rafraîchir d'abord chaque soudure avec un peu de soudure neuve et du flux ; chauffer 3 à 5 s au plus par pastille, laisser refroidir entre deux essais ; ne pas appuyer ni frotter la panne sur la pastille.
- S'entraîner une demi-heure sur une vieille carte électronique avant de toucher la PD.
- Une pastille décollée se répare (fil de pontage vers le point suivant de la piste) ; ce n'est pas irrémédiable.
- Le travail sur la carte peut être confié à un réparateur ; les contrôles côté machine, objectif principal, ne demandent aucune soudure.

## 8. Prochaine étape (reprise de la prochaine séance)

**À faire plus tard, à la demande de l'utilisateur :** expliquer simplement le fonctionnement de la Power Driver (alimentations, étages de sortie). Mis de côté le 01/11 pour se concentrer sur M13.

**Fait (01/11/2026) — M14bis : caractériser la lecture variable TP7 ↔ TP5.** Confirmer d'abord l'état de la machine. Pointe rouge sur TP7, noire sur TP5 ; calibre noté ; mains hors des fils et de la carte. Relever la valeur de départ, la valeur au bout de ≈ 30 s et le sens de variation (monte régulièrement, baisse, saute). Repères : `photos/plan-PD_TP7-TP5-C11_zoom.png`.

1. **M13 — Contrôle global entre lignes d'alimentation** (hors tension ; J107 branché ; fiches J130, J127, J126, J122 débranchées ; F104, F105 retirés ; **retirer aussi F103**). Repères : `photos/plan-PD_M13_clips-F103-F105_TP7.png`. Clips du haut A = F103, B = F104, C = F105 : A ↔ B, A ↔ C, B ↔ C, puis A, B, C ↔ TP7 (+20 V) → OL attendu partout ; facultatif : C ↔ TP5 en déplaçant le chariot du Mini Kicker. Quelques ohms ou moins → un fil d'une ligne touche une autre ligne, à localiser.
2. **Matrice lampes : méthode préparée le 01/11/2026.** Contexte E5 : transistors illuminés dans la zone des pilotes de lampes, au-dessus du groupe J133–J138.
   - **Schéma, feuille 2 :**
     - 8 rangées pilotées par les TIP102 Q83–Q90, avec une résistance d'émetteur de 0,22 Ω 1 W (R150–R153, R172–R175) et une protection contre les surintensités (un LM339 remet à zéro la bascule 74LS74) ;
     - 8 colonnes pilotées par les TIP107 Q91–Q98, alimentées en +18 V et **sans protection** ;
     - le courant va de la colonne à la rangée, en passant par la lampe et sa diode.
   - **Manuel p. 3-29 : sur The Shadow, J133 et J137 ne sont pas utilisés.**
     - **J135 = rangées du plateau** : 1 Rouge-Marron (R1), 2 Rouge-Noir (R2), 3 détrompeur, 4 Rouge-Orange (R3), 5 Rouge-Jaune (R4), 6 Rouge-Vert (R5), 7 Rouge-Bleu (R6), 8 Rouge-Violet (R7), 9 Rouge-Gris (R8).
     - **J138 = colonnes du plateau** : 1 Jaune-Marron (C1), 2 Jaune-Rouge (C2), 3 Jaune-Orange (C3), 4 Jaune-Noir (C4), 5 Jaune-Vert (C5), 6 Jaune-Bleu (C6), 7 Jaune-Violet (C7), 8 détrompeur, 9 Jaune-Gris (C8).
     - Caisse : J134-7/8/9 (rangées 6 à 8) et J136-3 (colonne 8).
     - ⚠️ Les rangées 1 à 3 portent les **mêmes couleurs** que les alimentations de bobines : Rouge-Marron (F104), Rouge-Noir (F105), Rouge-Orange (F103).
   - **Repères :** `photos/plan-PD_lampes_J135-J138-TP5.png`, `photos/plan-PD_lampes_J133-J138_zoom.png`.
   - **Conditions :**
     - hors tension ;
     - fiches J135 et J138 débranchées, après une photo (J133 et J137 sont vides : ne pas s'y tromper au rebranchement) ;
     - J134, J136 et J107 branchés ;
     - F103 à F105 retirés.
   - **L1 :** mode diode, pointe noire sur TP5 (masse), pointe rouge sur chaque contact de la fiche J138 (positions 1 à 7 et 9). OL attendu.
     - ≈ 0 V : la colonne touche la masse (son TIP107 risquerait de griller).
     - ≈ 0,4–0,7 V : une rangée touche la masse ; on la voit à travers une lampe.
   - **L2 :** même geste, pointe noire dans le clip du haut A (F103), puis B (F104), puis C (F105). OL attendu.
     - ≈ 0 V : la colonne touche cette ligne 50 V.
     - ≈ 0,4–0,7 V : une rangée touche cette ligne, vue à travers une lampe.
   - **Principe :** depuis une colonne, le multimètre atteint toutes les rangées à travers les lampes et leurs diodes. Il est donc inutile de sonder J135. Pour les rangées, la couverture dépend des ampoules, mais les 8 colonnes la garantissent.
   - **Non couvert pour l'instant :**
     - courts-circuits rangée–colonne et diodes de lampes en court-circuit : les rangées sont protégées par la carte, et ces défauts se verront au test des lampes à la remise sous tension ;
     - contacts avec la GI ;
     - lampes de la caisse.
   - **Au banc :** Q83–Q98, les résistances de 0,22 Ω et la protection LM339.
   **Statut (01/11/2026) :** L1, L1bis, L2 (A, B, C) et L2-20 V sont OL. Le faisceau de la matrice du plateau est validé.
2bis. **GI : méthode préparée le 01/11/2026.**
   - **Schéma, feuille 1 :** 5 circuits.
     - Chaque circuit part du transformateur par J115, passe par un fusible (F106 à F110), alimente les ampoules par la broche 7 à 11 de J120/J121, puis revient par la broche 1 à 6.
     - Le retour passe par un triac SC141 (Q10, Q12, Q14, Q16, Q18), commandé par un 2N5401 depuis le VCC.
     - J115-1 porte « GND REF » (schéma).
   - **Manuel p. 3-28 :**
     - J115 : fils du transformateur, à 6,8 V alternatifs ; J115-1 est le fil Jaune-Blanc.
     - J120 (plateau) : retours 3 Jaune et 5 Vert ; alimentations 9 Blanc-Jaune et 10 Blanc-Vert.
     - J121 (« insert ») : retours 1 Marron, 2 Orange, 6 Violet ; alimentations 7 Blanc-Marron, 10 Blanc-Vert, 11 Blanc-Violet.
     - J119 (vers A-17051-1) : 1 Blanc-Violet, 3 Violet.
   - **G1 :** en ohms (calibre 200 Ω), pointe noire sur TP5, pointe rouge sur un clip de chaque fusible F106 à F110, fusibles en place (`photos/plan-PD_GI_F106-F110_TP5.png`).
     - Valeur basse (≈ 0,5–2 Ω) : la GI est reliée à la masse par le transformateur. Dans ce cas, un contact GI ↔ matrice aurait été vu en L1, un contact GI ↔ 50 V en M3, un contact GI ↔ 20 V en M14 : tous ces cas sont déjà écartés.
     - OL : ce circuit est flottant et doit être contrôlé directement.
   - **Hors de portée du multimètre :** un court-circuit entre l'aller et le retour d'un même circuit, car les ampoules froides font déjà presque 0 Ω. Ce cas est protégé par les fusibles et sera surveillé à la remise sous tension.
   - **G2 :** examen visuel des connecteurs de la GI (J115, J120, J121, J119, côté carte et côté fiches), souvent brûlés sur les cartes WPC.
3. Flippers et Sol 35–36 (Fliptronic II).
4. Réparation de la PD au banc : Q82 (TIP36C), contrôle de Q81, Q71, R123–R125 ; diodes D5–D12 (tieback) et D17–D24 ; pilotes lampes ; soudures ; zone des « points lumineux ».
5. Phase E : protocole de remise sous tension progressive.

## 9. Questions en suspens

1. La PD est-elle actuellement déposée ? Quels composants ont été remplacés (repères Q…, D…), et par quelles références exactes ?
2. Au dernier allumage : combien de temps la bobine est-elle restée collée ? F105 a-t-il fondu ? Le jeu démarrait-il normalement (écran, sons, LED D20 clignotante) ?
3. Quelle diode a brûlé (repère) et quel court-circuit a été corrigé (où) ?
4. Chronologie : la Sol 01 collait-elle déjà avant les dernières réparations de la carte, ou seulement après ?
5. Photo de la zone des « points lumineux ».
6. O2 et M2 : le cordon était-il débranché pendant les mesures ? Résistance des pointes ?
7. Quels fusibles sont actuellement en place, absents ou grillés ? (F101–F104 conditionnent la portée de M3 ; calibre réel de F105.)
9. (Résolu, M9a) Le Rouge-Marron est alimenté par F104 d'après le schéma de la PD lui-même ; c'est le tableau des fusibles du manuel qui inverse F104 et F105. Sol 08 sur Rouge-Noir (O13) : écart avec le tableau des solénoïdes, a priori une de ses erreurs connues.
8. M5bis : pointe noire sur TP6 ou sur un clip de F105 ? (Si TP6 : les cathodes D25–D32 sont sur le bus de TP6, et M5 avait été fait pointes inversées.)
## 10. Documentation et sources

Photos de la machine dans `photos/` (nommées date_observation_sujet, par exemple `2026-10-25_O6_Q82-D32-J130.jpg`).

Copies locales dans `docs/` : `manuel-the-shadow/` (pages du manuel), `schema-power-driver/` (schéma A-12697-1 et extraits agrandis), `theorie-wpc/` (manuel de théorie WPC).

- Manuel *The Shadow* 16-50032-101 (nov. 1994), version en ligne : https://www.planetarypinball.com/reference/gamemanuals/The_Shadow_Bly/files/assets/basic-html/toc.html
- Schéma Power Driver A-12697-1 (16-9057, rév. 6) : https://pinwiki.com/wiki/index.php/File:WPC_power_drive_board.pdf. La -3 diffère au moins par la zone relais flippers (« NOT USED IN A-12697-3 »).
- Théorie WPC 16-9289 : https://planetarypinball.com/reference/partsmanuals/WMS_Schematic_WPC_16-9289/files/assets/seo/page32.html
- PinWiki *The Shadow* : https://pinwiki.com/wiki/index.php/The_Shadow
- PinWiki, réparation des PD WPC (Leon Borre) : https://pinwiki.com/wiki/index.php/Leon_Borre_Williams_WPC_and_WPC-95_Driver_Board_Repair
- PinWiki *Terminator 2* (tieback) : https://pinwiki.com/wiki/index.php/Terminator_2:_Judgement_Day
- Résistance indicative d'une 23-800 (Marco Specialties) : https://www.marcospecialties.com/pinball-parts/090-5001-00
