-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 24 nov. 2025 à 08:31
-- Version du serveur :  5.7.31
-- Version de PHP : 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `nsi_eleve3`
--

-- --------------------------------------------------------

--
-- Structure de la table `action`
--

DROP TABLE IF EXISTS `action`;
CREATE TABLE IF NOT EXISTS `action` (
  `id_action` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `description` varchar(255) NOT NULL,
  `lienscript` varchar(100) NOT NULL,
  PRIMARY KEY (`id_action`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `action`
--

INSERT INTO `action` (`id_action`, `nom`, `description`, `lienscript`) VALUES
(1, 'Afficher météo', 'Affiche la météo de la ville demandée', 'scripts/meteo.py'),
(2, 'Afficher heure', 'Retourne l’heure locale', 'scripts/heure.py'),
(3, 'Afficher aide', 'Montre la liste des commandes disponibles', 'scripts/aide.py'),
(4, 'Raconter blague', 'Renvoie une blague au hasard', 'scripts/blague.py'),
(5, 'Infos ville', 'Affiche la population et des infos sur une ville', 'scripts/ville.py'),
(6, 'Infos utilisateur', 'Affiche les infos d’un utilisateur', 'scripts/userinfo.py'),
(7, 'Liste commandes', 'Affiche toutes les commandes disponibles', 'scripts/commande.py'),
(8, 'Dire bonjour', 'Envoie un message de salutation', 'scripts/salut.py'),
(9, 'Afficher actualités', 'Affiche les dernières actualités', 'scripts/news.py');

-- --------------------------------------------------------

--
-- Structure de la table `association`
--

DROP TABLE IF EXISTS `association`;
CREATE TABLE IF NOT EXISTS `association` (
  `id_motcle` int(11) NOT NULL,
  `id_categorie` int(11) NOT NULL,
  PRIMARY KEY (`id_motcle`,`id_categorie`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `attribution`
--

DROP TABLE IF EXISTS `attribution`;
CREATE TABLE IF NOT EXISTS `attribution` (
  `id_categorie` int(11) NOT NULL,
  `id_action` int(11) NOT NULL,
  PRIMARY KEY (`id_categorie`,`id_action`),
  KEY `id_action` (`id_action`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `attribution`
--

INSERT INTO `attribution` (`id_categorie`, `id_action`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9);

-- --------------------------------------------------------

--
-- Structure de la table `catégorie`
--

DROP TABLE IF EXISTS `catégorie`;
CREATE TABLE IF NOT EXISTS `catégorie` (
  `id_categorie` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id_categorie`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `catégorie`
--

INSERT INTO `catégorie` (`id_categorie`, `nom`, `description`) VALUES
(1, 'Météo', 'Toutes les fonctionnalités liées à la météo'),
(2, 'Heure', 'Affichage de l’heure et du temps'),
(3, 'Aide', 'Aide, assistance et support utilisateur'),
(4, 'Humour', 'Blagues et contenu amusant'),
(5, 'Ville', 'Informations sur les villes'),
(6, 'Utilisateur', 'Gestion des utilisateurs'),
(7, 'Commande', 'Gestion et liste des commandes'),
(8, 'Salutation', 'Messages de bienvenue'),
(9, 'Actualité', 'News et informations récentes');

-- --------------------------------------------------------

--
-- Structure de la table `commande`
--

DROP TABLE IF EXISTS `commande`;
CREATE TABLE IF NOT EXISTS `commande` (
  `id_commande` int(11) NOT NULL,
  `commande` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id_commande`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `commande`
--

INSERT INTO `commande` (`id_commande`, `commande`, `description`) VALUES
(2, 'heure', 'Donner l\'heure locale'),
(3, 'aide', 'Afficher l\'aide ou la liste des commandes'),
(1, 'meteo', 'Récupérer la météo d\'une ville'),
(4, 'addition', 'Réalise une addition'),
(5, 'villes', 'Recherche des informations sue les villes');

-- --------------------------------------------------------

--
-- Structure de la table `motcle`
--

DROP TABLE IF EXISTS `motcle`;
CREATE TABLE IF NOT EXISTS `motcle` (
  `id_motcle` int(11) NOT NULL,
  `motcle` varchar(15) NOT NULL,
  `commande` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id_motcle`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `motcle`
--

INSERT INTO `motcle` (`id_motcle`, `motcle`, `commande`, `description`) VALUES
(2, 'meteo', 1, 'variation sans accent'),
(3, 'temps', 1, 'synonyme lié à la météo'),
(1, 'météo', 1, 'mot déclencheur pour météo'),
(4, 'heure', 2, 'mot déclencheur pour l\'heure'),
(5, 'clock', 2, 'variation anglaise'),
(6, 'help', 3, 'mot pour aide'),
(7, 'aide', 3, 'mot français utilisé pour demander de l\'aide'),
(8, 'assistant', 3, 'mot déclencheur pour demander de l\'aide'),
(9, 'blague', 4, 'mot déclencheur pour raconter une blague'),
(10, 'joke', 4, 'variation anglaise pour une blague'),
(11, 'ville', 5, 'mot lié aux données de la table ville'),
(12, 'population', 5, 'demande d\'informations sur population'),
(13, 'carte', 5, 'mot lié à la recherche de villes'),
(14, 'utilisateur', 6, 'mot déclencheur pour gestion utilisateur'),
(15, 'profil', 6, 'synonyme lié aux utilisateurs'),
(16, 'commande', 7, 'mot déclencheur pour gestion des commandes'),
(17, 'achat', 7, 'mot lié aux achats'),
(18, 'bonjour', 8, 'mot déclencheur pour salutation'),
(19, 'salut', 8, 'variation informelle'),
(20, 'news', 9, 'mot pour actualités'),
(21, 'actualité', 9, 'mot français pour news');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `id_utilisateur` int(11) NOT NULL,
  `nom` varchar(15) DEFAULT NULL,
  `prenom` varchar(15) DEFAULT NULL,
  `surnom` varchar(25) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `mot_de_passe` varchar(50) DEFAULT NULL,
  `date_utilisation` date DEFAULT NULL,
  `commande` int(11) NOT NULL,
  PRIMARY KEY (`id_utilisateur`),
  KEY `commande` (`commande`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`id_utilisateur`, `nom`, `prenom`, `surnom`, `mail`, `mot_de_passe`, `date_utilisation`, `commande`) VALUES
(1, 'Idriss', 'Atil', 'cr7legoat', 'atilidriss@gmail.com', 'motdepasse_exemple', '2024-01-01', 3),
(2, 'Dupont', 'Marie', 'mdupont', 'marie@example.com', 'dupontjosef65', '2024-02-01', 1),
(3, 'Lemoine', 'Paul', 'tartempion_95', 'paul.lemoine@example.com', 'azerty1234', '2024-03-01', 2),
(4, 'Martin', 'Lucie', 'grumpy_cat', 'lucie.martin@example.com', 'password123', '2024-04-01', 4),
(5, 'Durand', 'Pierre', 'pierre_the_terrible', 'pierre.durand@example.com', 'ilovepizza123', '2024-05-01', 1),
(6, 'Petit', 'Sophie', 'sophie_les_pates', 'sophie.petit@example.com', '12345qwert', '2024-06-01', 5),
(7, 'Moreau', 'Julien', 'soda_fantome', 'julien.moreau@example.com', 'motdepasse123', '2024-07-01', 2),
(8, 'Roux', 'Claire', 'claire_qui_rigole', 'claire.roux@example.com', '1234toto', '2024-08-01', 3),
(9, 'Benoit', 'Alexandre', 'super_héros_de_lombre', 'alexandre.benoit@example.com', 'qwerty12345', '2024-09-01', 1),
(10, 'Dufresne', 'Isabelle', 'la_chieuse', 'isabelle.dufresne@example.com', 'motdepasseIsabelle1', '2024-10-01', 4),
(11, 'Lemoine', 'Alexis', 'chasseur_de_croissants', 'alexis.lemoine@example.com', 'croissant1234', '2024-11-01', 2),
(12, 'Boucher', 'Chloé', 'les_pommes_de_terre', 'chloe.boucher@example.com', 'potatoesrock42', '2024-12-01', 1),
(13, 'Gerard', 'Jean', 'king_burger', 'jean.gerard@example.com', 'mangermacdo123', '2025-01-01', 3),
(14, 'Bonnet', 'Julie', 'mama_bear', 'julie.bonnet@example.com', 'bearhug42', '2025-02-01', 5),
(15, 'Faure', 'Géraldine', 'super_nana_01', 'geraldine.faure@example.com', '12345supernana', '2025-03-01', 4),
(16, 'Leclerc', 'Maxime', 'max_power_up', 'maxime.leclerc@example.com', 'powermax456', '2025-04-01', 2),
(17, 'Thomas', 'Sylvain', 'darth_vador_94', 'sylvain.thomas@example.com', 'force12345', '2025-05-01', 1),
(18, 'Nicolas', 'Lise', 'princesse_mignon', 'lise.nicolas@example.com', 'cuteprincess2024', '2025-06-01', 3),
(19, 'Deschamps', 'Bernard', 'le_chef_de_lombre', 'bernard.deschamps@example.com', 'chefbernard2024', '2025-07-01', 2),
(20, 'Lemoine', 'Fanny', 'fanny_le_fantome', 'fanny.lemoine@example.com', 'motdepasseFanny1', '2025-08-01', 4);

-- --------------------------------------------------------

--
-- Structure de la table `ville`
--

DROP TABLE IF EXISTS `ville`;
CREATE TABLE IF NOT EXISTS `ville` (
  `id_ville` int(11) NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `pays` varchar(30) DEFAULT NULL,
  `nb_population` int(11) DEFAULT NULL,
  `date_constrcution` date DEFAULT NULL,
  PRIMARY KEY (`id_ville`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `ville`
--

INSERT INTO `ville` (`id_ville`, `nom`, `pays`, `nb_population`, `date_constrcution`) VALUES
(2, 'Marseille', 'France', 870000, '0600-01-01'),
(1, 'Paris', 'France', 2148000, '0520-01-01'),
(3, 'Lyon', 'France', 522000, '0043-01-01'),
(4, 'Toulouse', 'France', 498000, '0300-01-01'),
(5, 'Nice', 'France', 342000, '0350-01-01'),
(6, 'Nantes', 'France', 320000, '0050-01-01'),
(7, 'Montpellier', 'France', 300000, '0985-01-01'),
(8, 'Strasbourg', 'France', 290000, '0048-01-01'),
(9, 'Bordeaux', 'France', 260000, '0200-01-01'),
(10, 'Lille', 'France', 234000, '1066-01-01'),
(11, 'Rennes', 'France', 220000, '0100-01-01'),
(12, 'Reims', 'France', 184000, '0080-01-01'),
(13, 'Toulon', 'France', 176000, '0597-01-01'),
(14, 'Saint-Étienne', 'France', 170000, '1291-01-01'),
(15, 'Le Havre', 'France', 169000, '1517-01-01'),
(16, 'Grenoble', 'France', 158000, '0011-01-01'),
(17, 'Dijon', 'France', 155000, '0980-01-01'),
(18, 'Angers', 'France', 155000, '0047-01-01'),
(19, 'Nîmes', 'France', 150000, '0000-01-01'),
(20, 'Clermont-Ferrand', 'France', 143000, '0050-01-01'),
(21, 'Villeurbanne', 'France', 150000, '1200-01-01'),
(22, 'Saint-Denis', 'France', 113000, '0660-01-01'),
(23, 'Aix-en-Provence', 'France', 145000, '0122-01-01'),
(24, 'Besançon', 'France', 118000, '0080-01-01'),
(25, 'Limoges', 'France', 132000, '0020-01-01'),
(26, 'Tours', 'France', 136000, '0100-01-01'),
(27, 'Metz', 'France', 118000, '0030-01-01'),
(28, 'Perpignan', 'France', 120000, '0990-01-01'),
(29, 'Caen', 'France', 106000, '1100-01-01'),
(30, 'Orléans', 'France', 116000, '0000-01-01'),
(31, 'Mulhouse', 'France', 109000, '0800-01-01'),
(32, 'Rouen', 'France', 111000, '0200-01-01'),
(33, 'Boulogne-Billancourt', 'France', 120000, '1300-01-01'),
(34, 'Argenteuil', 'France', 110000, '0690-01-01'),
(35, 'Montreuil', 'France', 110000, '1100-01-01'),
(36, 'Nancy', 'France', 105000, '0700-01-01'),
(37, 'Avignon', 'France', 92000, '0043-01-01'),
(38, 'Poitiers', 'France', 90000, '0050-01-01'),
(39, 'Amiens', 'France', 135000, '0000-01-01'),
(40, 'Annecy', 'France', 140000, '1100-01-01'),
(41, 'Pau', 'France', 77000, '0900-01-01'),
(42, 'Valence', 'France', 64000, '0020-01-01'),
(43, 'La Rochelle', 'France', 76000, '1000-01-01'),
(44, 'Chambéry', 'France', 59000, '1100-01-01'),
(45, 'Béziers', 'France', 78000, '0060-01-01'),
(46, 'Troyes', 'France', 61000, '0047-01-01'),
(47, 'Narbonne', 'France', 55000, '0118-01-01'),
(48, 'Colmar', 'France', 70000, '0800-01-01'),
(49, 'Chartres', 'France', 39000, '0000-01-01'),
(50, 'Gap', 'France', 40000, '0122-01-01'),
(51, 'Albi', 'France', 50000, '0104-01-01'),
(52, 'Brive-la-Gaillarde', 'France', 48000, '0050-01-01');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
