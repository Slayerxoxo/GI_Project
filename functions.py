#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Authors:
    Coraline MARIE, Carl Goubeau et Emmanuel Turbé

:Date:
    2015/1/5
"""
import re
import sys
import os
import codecs
import math


###############################
#     Organistion du code     #
###############################


###    color    ###
#    mise en forme du texte
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


###    affichage    ###
#    affiche dans la console des textes sur l'exécution du programme
def affichage(num):
    if num == 404:
        print(color.RED + "\nERREUR" + color.END)
    elif num == 0:
        print("                                 " + color.GREEN + " > done" + color.END)
    elif num == 1:
        print(color.BOLD + "\n\nRECUPERATION DES DATASETS :" + color.END)
    elif num == 2:
        print(color.BOLD + "\n\nTEST SUR LE FORMAT DES DATASETS :" + color.END)
    elif num == 3:
        print(color.GREEN + "--> aucun problème sur les datasets\n" + color.END)
    elif num == 4:
        print(color.BOLD + "\n\nTEST SUR LA POSITION DES TONIQUES :" + color.END)




##############################
#     Test sur le format     #
##############################

def test_format_funct(dataset_dic):
    nb_dataset_errones = 0
    for dataset_name in dataset_dic.keys():
        for (element_input,element_output) in dataset_dic[dataset_name]:
            if element_input[0] != "w" or element_output[0] != "s" :
                affichage(404)
                print ("\n fichier : " + dataset_name)
                nb_dataset_errones += 1
    if nb_dataset_errones == 0 :
        affichage(3)


#################################
# Test sur la pos de la tonique #
#################################

def test_pos_tonique_funct(dataset_dic):
    affichage(4)
    tmp_dic = {}
    for dataset_name in dataset_dic.keys():
        for (element_input,element_output) in dataset_dic[dataset_name]:
            for pos in range(0,len(element_output)):
                if element_output[pos] == "2":
                    if (pos/2) in tmp_dic.keys():
                        tmp_dic[pos/2] += 1
                    else:
                        tmp_dic[pos/2] = 1
    for element in tmp_dic.keys():
        print tmp_dic[element], " de tonique en position ",element
    affichage(0)