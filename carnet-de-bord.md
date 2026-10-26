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

## Séance 1 — samedi 25 octobre 2026 (12 h 40 – 19 h 55)

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
