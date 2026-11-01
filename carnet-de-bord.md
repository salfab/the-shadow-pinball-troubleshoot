# Carnet de bord — réparation d'un Bally *The Shadow* (1994)

> Récit chronologique des séances, destiné à devenir un article de blog une fois la réparation terminée.
> Le suivi technique détaillé (mesures, hypothèses, checklist) est dans `journal-diagnostic-the-shadow.md` ; les photos sont dans `photos/`, la documentation dans `docs/`.

## Le point de départ

- **La machine** : Bally *The Shadow*, 1994, système WPC-S. La carte de puissance (Power Driver A-12697-3) commande les bobines, les flashers et les lampes.
- **L'historique**, tel que je m'en souvenais :
  - un court-circuit, peut-être au mini-playfield, sur un flasher ou un mini drop target ;
  - le fusible F103 qui fondait ;
  - un transistor grillé, puis une diode de la carte brûlée, que j'ai remplacée en corrigeant le court-circuit ;
  - ensuite, plusieurs transistors qui chauffaient, avec des « points lumineux » en bas à droite de la carte.
- **Le symptôme** : dès l'allumage, la bobine du lanceur automatique (Sol 01, Ball Launch) restait alimentée et tenait le plongeur.
- **L'objectif** : avant de rebrancher une carte réparée, s'assurer que rien dans la machine ne la détruira de nouveau.

## Séance 1 — dimanche 25 octobre 2026 (12 h 40 – 19 h 55)

### La méthode

- Rassembler la documentation : manuel de *The Shadow*, schéma de la Power Driver, manuel de théorie WPC.
- Ouvrir un journal de diagnostic.
- Règles retenues :
  - tout faire hors tension, cordon débranché ;
  - une mesure à la fois, avec son interprétation prévue à l'avance ;
  - ne jamais tenir un souvenir pour un fait.

### Trouver le court-circuit (≈ 13 h – 14 h 30)

1. **Le bip inattendu.** Carte encore branchée, le multimètre sonnait entre TP6 (+50 V) et la masse. En ohms, on lisait 4,5 Ω : la valeur d'une bobine dont l'autre bout touche la masse. Ce n'était donc pas un court-circuit direct.
2. **Couper en deux.** Le fusible F105 résistait. On a plutôt débranché le connecteur J130, qui relie les bobines Sol 1 à 8 à la carte. Le chemin a disparu (10 kΩ, la résistance de décharge R260 seule). Le défaut était donc **sur la carte**, et pas un fil du faisceau à la masse.
3. **Trouver la sortie.** Broche par broche sur l'embase J130 : la broche 1 (Sol 01) était à 0,5 Ω de la masse, les autres saines. **Le transistor de sortie Q82 (TIP36C) était en court-circuit.**
4. **Les diodes de protection.** Testées en mode diode, D25 à D32 étaient saines et bien orientées. Un premier essai avait été fait pointes inversées : les valeurs montaient lentement, parce que le multimètre chargeait le condensateur du 50 V.
5. **Les marquages.** Q82 est le TIP36C ST d'origine (code date 9431), comme ses voisins. Q71 à Q74 sont des 2N5401 National d'origine, et Q81 a le même aspect que les autres TIP102. Aucune pièce de mauvais type : c'est le transistor d'usine qui a lâché.

### La surprise des fusibles (≈ 14 h 40 – 17 h 10)

1. **F105**, enfin retiré : un 313 de 3 A temporisé, propre. Conforme au manuel.
2. **Première énigme.** La Sol 01 n'était pas reliée à F105, alors que le manuel l'y place, mais à F104, un Bussmann MDL 3 A temporisé, propre. Le Knocker (Sol 07) aussi.
3. **Faut-il remettre sous tension pour vérifier ?** Non : F104 et F105 retirés, aucune liaison ne restait entre le fil de la Sol 01 et le 50 V. Une mesure hors tension suffisait et ne risquait rien.
4. **Sous le plateau.**
   - La bobine Sol 01 (AE-23-800) fait 4 Ω, elle est saine.
   - Elle n'a pas de diode. C'est normal sur WPC : pour les sorties 1 à 16, la diode de protection est sur la carte.
5. **Défaut électrique ou erreur du manuel ?**
   - Les lignes de F104 et F105 sont bien séparées : pas de court-circuit entre elles.
   - La fiche J107 porte les couleurs du manuel.
   - Sur la carte, F104 arrive sur la broche 2 (Rouge-Marron) et F105 sur la broche 3 (Rouge-Noir), exactement comme sur le schéma.
   - Conclusion : **c'est le tableau des fusibles du manuel qui inverse F104 et F105.** La machine est conforme.

### Vérifier les bobines une par une (≈ 17 h 30 – 19 h)

- **Une astuce** : fiche J107 rebranchée et fusibles retirés, les clips vides des fusibles deviennent des points de mesure qui tiennent seuls la pointe du multimètre.

| Groupe | Résultat |
|---|---|
| Sol 1–8 (J130) | Toutes sur F104 sauf la Sol 08 (F105). 4 Ω pour les trois AE-23-800, 7 Ω pour les quatre AE-25-1000, 32 Ω pour la bobine spéciale de la Sol 02 |
| Sol 9–16 (J127) | Toutes sur F105 ; les paires de même modèle sont identiques (11/11, 14/14, 7,5/7,5 Ω) |
| Sol 24–25 + tieback (J126, J122) | 7,7 Ω et 10,9 Ω ; les deux fils de tieback sont bien raccordés (0,5 Ω) |

Aucune bobine trop basse, donc aucune ne peut griller un transistor.

### Ce qui reste ouvert en fin de séance

- **Pourquoi Q82 a lâché.** Ce n'est pas prouvé. Côté machine, rien ne l'explique. La Sol 01 ne collait qu'*après* l'épisode F103, d'où une piste : la commande de Q82 (Q81, Q71, logique) aurait été abîmée par cet épisode.
- **Les diodes de tieback elles-mêmes** (D5 à D12). M12 n'a vérifié que les fils du faisceau ; les diodes seront testées sur l'établi.
- **Les « points lumineux ».** Ils étaient en fait au-dessus de J133 et J137, sur les transistors qui pilotent les lampes. C'est une piste distincte, à suivre côté câblage des lampes et sur l'établi.
- **Les contrôles restants avant de rebrancher** : courts-circuits entre lignes d'alimentation (M13), vers les lampes, les contacts et la logique, les flippers. Ensuite viendront la réparation de la carte et la remise sous tension progressive.

### Corrections en cours de route (pour l'honnêteté du récit)

- L'assistant avait annoncé, en se fiant au manuel, que F105 arrivait sur la broche 2 de J107. Le schéma, relu de près, disait l'inverse, et la mesure lui a donné raison.
- Il avait aussi annoncé une diode sur la bobine Sol 01 : erreur, ce n'est pas le cas sur WPC pour les sorties 1 à 16.
- Un premier tableau de 16 mesures était plus lourd que nécessaire. Il a été allégé à 5 mesures, en expliquant à chaque fois à quoi servait la série.

### Ce que j'en retiens

- **Mesurer plutôt que croire le manuel** : le tableau des fusibles et celui des solénoïdes contiennent des erreurs.
- **Diviser pour localiser**, hors tension : carte branchée, on débranche un connecteur à la fois et on regarde si le défaut disparaît.
- **Quelques pièges du multimètre :**
  - à travers une diode, la valeur en ohms dépend du calibre ;
  - un condensateur fait monter la lecture ;
  - le sens des pointes compte.
- **Un fusible temporisé peut tenir plusieurs secondes à deux ou trois fois son calibre.** Une bobine collée a donc le temps de chauffer avant qu'il ne fonde.
- **Des photos annotées** pour repérer chaque composant : beaucoup plus simple que les seuls repères du schéma.

### Photos de la séance

- `photos/2026-10-25_O5_zone-J127-J130.jpg`, `..._O6_Q80-Q81-Q82.jpg`, `..._O6_Q82-D32-J130.jpg` : étage de la Sol 01.
- `photos/2026-10-25_O8_Q81-Q82-D32-fiche-J130.jpg`, `..._O9_vue-generale-PD.jpg` : vue générale de la carte.
- `photos/2026-10-25_O11_bobine-AE-23-800.jpg`, `..._O12_bobine-Sol01-cosses.jpg`, `..._O13_bobine-Sol08-cosses.jpg` : bobines sous le plateau.
- `photos/2026-10-25_O14_J107-fils.jpg`, `..._O15_fiche-J107.jpg` : connecteur J107.
- Images annotées : `photos/2026-10-25_annotee_*.jpg`, `photos/plan-PD_*.png`.

## Entre les deux séances

- Tout le projet est sauvegardé sur un dépôt GitHub privé : journal, carnet, photos, documentation, ainsi que la mémoire et les conversations avec Claude. Un script, `sauvegarde.ps1`, met la sauvegarde à jour.

## Séance 2 — dimanche 1er novembre 2026 (8 h 10 – 13 h 50)

### Une résistance qui varie (≈ 8 h 10 – 8 h 50)

- Entre TP7 (+20 V des flashers) et TP5 (masse), le multimètre bipait, affichait 39 Ω, puis montait au-delà de 171 kΩ. J'ai eu peur d'un court-circuit entre le 20 V et la masse.
- **Explication** : C11, le condensateur de 15 000 µF du 20 V, se chargeait avec le courant du multimètre. Un vrai court-circuit resterait bas et stable. Fausse alerte.

### Fin du contrôle des alimentations des bobines (≈ 8 h 50 – 9 h 15)

- Avec F103 retiré à son tour, les trois lignes 50 V des bobines se sont révélées isolées : entre elles, du 20 V et de la masse.
- C'était vrai même en faisant glisser à la main la palette du Mini Kicker, celle « façon Arkanoid » du mini-plateau.
- **Un souvenir revenu** : la machine redémarrait toujours peu après la sortie de la balle du mini-plateau. Noté, à surveiller à la remise sous tension.

### La matrice des lampes (≈ 9 h 20 – 10 h 45)

- **Première surprise** : sur *The Shadow*, J133 et J137 ne servent pas. Les lampes du plateau passent par J135 pour les rangées et J138 pour les colonnes.
- **Deuxième surprise** : les rangées 1 à 3 ont les mêmes couleurs que les alimentations des bobines (Rouge-Marron, Rouge-Noir, Rouge-Orange).
- **L'astuce** : depuis une colonne, le multimètre atteint toutes les rangées à travers les lampes et leurs diodes. Il suffit donc de sonder une seule fiche.
- **Une fausse piste** : une valeur montait de 1,2 à 1,6 V sur toutes les broches. Elle venait de l'embase de la carte, c'est-à-dire des transistors des colonnes et des condensateurs du +18 V, pas des fils. Sur la fiche, côté fils : OL.
- **Résultat** : aucun fil des lampes ne touche la masse, le 50 V des bobines ou le 20 V des flashers.
- **Question encore ouverte** : quelle pièce a brillé autrefois ?
  - La photo de la première séance, regardée en pleine résolution, ne montre aucune brûlure.
  - Les huit résistances bleues de 0,22 Ω des rangées sont les meilleures candidates.
  - On tranchera sur l'établi.

### L'éclairage général (≈ 10 h 50 – 11 h 50)

- **Mesure clé** : chaque fusible de GI est à 0,4 Ω de la masse, à travers le transformateur. Les mesures déjà faites couvraient donc aussi les fils de GI.
- **Photos de la zone** : les connecteurs sont sains.
- **Fusibles** : deux d'entre eux sont d'un autre modèle, avec un fil droit et une perle verte. Leur marquage, T5AL250V, les rend conformes.

### Les flashers (≈ 12 h – 13 h 15)

- Un flasher en court-circuit détruirait son transistor sur la carte. J'ai mesuré les 8 flashers du plateau et les 5 de la tête : aucun court-circuit.
- À revoir à l'allumage : le flasher Sol 26 de la tête (circuit ouvert) et trois flashers à la résistance élevée.

### Les lignes des flippers (≈ 13 h 20 – 13 h 45)

- Les fils 50 V des flippers ne touchent ni les lampes ni le 20 V.

### Bilan de la séance

- Côté machine, tout ce qui pouvait abîmer la Power Driver réparée a été vérifié.
- **Prochaine étape** : la carte sur l'établi (Q82 et sa commande, les pilotes de lampes, la zone qui a brillé), puis la remise sous tension progressive.

### Corrections en cours de route

- L'assistant avait situé les « points lumineux » au-dessus de J133 et J137 sans savoir que ces connecteurs ne servent pas sur ce jeu.
- À la première séance, il avait décrit les résistances bleues comme « montées debout ». Elles sont en fait montées à plat.
- Son premier contrôle des lampes ne couvrait pas les lignes des flippers (F101, F102). Il l'a ajouté en fin de séance.

### Ce que j'en retiens

- **Une valeur qui monte toute seule**, c'est un condensateur qui se charge, pas une panne.
- **Fiche ou embase** : pour tester les fils, on mesure la fiche débranchée, côté fils.
- **Le manuel du jeu fait foi** : un jeu n'utilise pas forcément tous les connecteurs du schéma de la carte.
- **La valeur plutôt que le bip** : elle dit ce qu'il y a sur le chemin (0,4 Ω, un fil ; quelques ohms, une bobine ou des ampoules ; 10 kΩ, une résistance).
- **Lire un fusible** : T5AL250V veut dire temporisé, 5 A, faible pouvoir de coupure, 250 V.

### Photos de la séance

- Zone de la GI : `photos/2026-11-01_G2_*.jpg`.
- Résistances des rangées : `photos/2026-11-01_annotee_resistances-0R22-rangees.jpg`.
- Plans annotés : `photos/plan-PD_TP7-TP5-C11*.png`, `plan-PD_lampes_*.png`, `plan-PD_C6-C7_18V_embase-J138.png`, `plan-PD_GI_F106-F110_TP5.png`, `plan-PD_J124-J125-J106-TP7.png`.

### Liste d'achats : vérification chez Mouser (≈ 23 h)

- Playwright était bloqué en « Access Denied » par Mouser, mais le navigateur intégré de l'application passe sans problème : la vérification à la main fonctionne.
- Le **TIP36C** (Q82) existe chez Mouser en **TO-247-3**, à CHF 2.62 et en stock ; Distrelec n'en a pas. Tout le reste de la liste est aussi en stock chez Mouser : total ≈ CHF 60 hors port (≈ 17 sans fusibles ni consommables).
- Restent à confirmer au moment de commander : le fusible 3 A (seul le 3,15 A trouvé), la puissance de la résistance 68 Ω, les frais de port et le HT/TTC.
