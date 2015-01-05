#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Authors:
    Coraline MARIE, Carl Goubeau et Emmanuel Turbé

:Date:
    2015/1/5
"""

import sys
import os
import codecs
import re
import glob

from functions import *

##########################################################################################################
#                                          LANCEMENT DU SCRIPT                                           #
#															                                             #
# python main_script.py                                                                                  #
#                                                                                                        #                                                                              #
##########################################################################################################

#                           IDEES
# - vérifier que tous les dataset obeissent bien aux consignes
# - faire des stats :
# 	- % de position de la tonique par rapport à la taille de la phrase
# 	- % de l'existence de la seconde tonique en fonction de la taille de la phrase
# 	- % position de la seconde tonique quand il y en a une
# 	- % d'apparition de la seconde tonique
# 	- % combien y a t'il en moyenne de tonique et de seconde tonique dans le phrase


if __name__ == "__main__":


    ###############################
    #   Variables de traitement   #
    ###############################
    # True pour lancer la fonction False sinon
    test_format = True
    test_pos_tonique = True



    #################################
    #   Récupération des données    #
    #################################
    # Les datasets doivent être dans le dossier datasets, et au formats *.fsa.res
    # les dataset sont ensuite stocké dans un dic qui associe le nom du dataset à une liste
    #   cette liste contient tous les couples (input, output) du dataset

    affichage(1)

    dataset_dic = {}
    for dataset_name in glob.glob("datasets/*"):
        file_dataset = codecs.open(dataset_name, "r", "utf-8")
        tmp_lst = []
        for lines in file_dataset.readlines():
            tmp_couple = (lines.split(",")[1].split(",")[0],lines.split(",")[2])
            tmp_lst.append(tmp_couple)
        dataset_dic[dataset_name.split("/")[-1].split(".")[-3]] = tmp_lst
        file_dataset.close()


    affichage(0)


    ################################
    #    Tests sur les données     #
    ################################

    ### TEST FORMAT ###
    # Vérification que tous les datasets sont bien de la forme input = w..., output = s...

    if test_format == True:
        affichage(2)
        test_format_funct(dataset_dic)
        affichage(0)

    ### TEST SUR LA POSITION DE LA TONIQUE ###
    # On cherche à déterminer ou est située la tonique dans un mot

    if test_pos_tonique == True:
        test_pos_tonique_funct(dataset_dic)

