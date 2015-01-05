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



    #################################
    #   Récupération des données    #
    #################################
    # Les datasets doivent être dans le dossier datasets, et au formats *.fsa.res
    # les dataset sont ensuite stocké dans un dic qui associe le nom du dataset à une liste
    #   cette liste contient tous les couples (input, output) du dataset

    affichage(1)

    dataset_dic = {}
    file_dataset_cleaning = codecs.open("datasets_cleaning.txt", "w", "utf-8")
    for dataset_name in glob.glob("datasets/*"):
        file_dataset = codecs.open(dataset_name, "r", "utf-8")
        tmp_lst = []
        for lines in file_dataset.readlines():
            tmp_couple = (lines.split(",")[1].split(",")[0],lines.split(",")[2])
            tmp_lst.append(tmp_couple)
        dataset_dic[dataset_name.split("/")[-1].split(".")[-2]] = tmp_lst
        file_dataset.close()
    file_dataset_cleaning.close()

    affichage(0)

    