# e-commerce-ai-system


1. **`application/`** : Contient les services et les cas d'utilisation de l'application. Cette couche gère la logique métier et les interactions entre les différentes couches, sans être directement dépendante des détails d'implémentation des frameworks ou des entités.

   - **`services/`** : Devrait contenir les services qui orchestrent les différentes opérations nécessaires pour réaliser les cas d'utilisation.
   - **`use_case/`** : Contient les cas d'utilisation spécifiques qui encapsulent la logique métier de haut niveau.

2. **`domain/`** : Représente le cœur de ton application, avec les entités et les interfaces de repository. C'est la couche la plus indépendante, qui ne dépend d'aucun autre code ou framework.

   - **`entities/`** : Contient les définitions des entités de ton domaine, représentant les objets métier principaux.
   - **`repositories/`** : Définit les interfaces pour l'accès aux données, souvent en interaction avec les services ou la base de données.

3. **`infrastructure/`** : Gère les détails d'implémentation spécifiques, comme l'accès aux données ou l'intégration avec des frameworks externes.

   - **`adapters/`** : Contient les adaptateurs pour l'accès aux sources de données ou pour l'intégration avec d'autres systèmes. 
   - **`frameworks/`** : Contient les implémentations spécifiques aux frameworks et bibliothèques externes, comme TensorFlow dans ton cas.

4. **`presentation/`** : Gère l'interaction avec l'utilisateur ou l'interface API. C'est la couche responsable de l'affichage des données et de la réception des entrées utilisateur.
