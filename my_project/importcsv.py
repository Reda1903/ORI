#First define your Django Enviromental variables

from cmath import nan
import os
import math
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")
import django
django.setup()
import pandas as pd
import numpy as np
from recipe.models import * #models

# Import CSV file
df = pd.read_excel('./Table Ciqual.xlsx')
# Do required pre-processing on panda dataframe 
# such as data cleaning, data format settings etc..



familles_opt= ['aides culinaires et ingrédients divers',
 'produits céréaliers',
 'viandes, œufs, poissons et assimilés', 
 'fruits, légumes, légumineuses et oléagineux',
  'produits laitiers et assimilés', 
   'eaux et autres boissons', ]
   
ingredients_opt = ['eaux et autres boissons', 'algues', 'biscuits apéritifs', 'boisson alcoolisées', 
'boissons sans alcool', 'condiments', 'crèmes et spécialités à base de crème', 'denrées destinées à une alimentation particulière', 
'épices', 'fromages et assimilés', 'fruits', 'fruits à coque et graines oléagineuses', 'herbes', 'ingrédients divers'
'laits', 'légumes', 'légumineuses', 'oeufs', 'pains et assimilés', 'pâtes, riz et céréales', 
'produits laitiers frais et assimilés', 'sels'
 ]
#formes_opt = ['']


# Iterater throught panda dataframe and save data in Django model
names= []
for index, row in df.iterrows():
    famille = Famille()
    #print(row['alim_grp_nom_fr'])
    row = row['alim_grp_nom_fr']
    #print(row)

    #if row == "" or row == "nan":
        #row = "Non défini"
      #print(row)

    if row not in names :
      famille.name = row
      names.append(row)
      famille.save()




names= []
for index, row in df.iterrows():
    forme = Forme()

    #print(row['alim_grp_nom_fr'])
    forme.famille = Famille.objects.filter(name = row['alim_grp_nom_fr'])[0]
    row = row['alim_ssgrp_nom_fr']
    #print(row)

    #if row == "" or row == "nan" or row == "-":
        #row = "Non défini"
      #print(row)


    if row not in names :
      forme.name = row
      names.append(row)
      forme.save()


for index, row in df.iterrows():

  #if row['alim_grp_nom_fr'] == 'produits céréaliers':
      # create django model

    ingredient = Ingredient()
      # Normal Fields ( Non-foreign key fields) adding

    
    ingredient.name = row['alim_nom_fr'][:70]
    
    #print(row['alim_grp_nom_fr'])
    #print(row['alim_ssgrp_nom_fr'])
    ingredient.famille = Famille.objects.filter(name = row['alim_grp_nom_fr'])[0]
    ingredient.forme = Forme.objects.filter(name = row['alim_ssgrp_nom_fr'])[0]
    ingredient.energie_kJ = row['Energie. Règlement UE N° 1169/2011 (kJ/100 g)']
    ingredient.energie_kcal = row['Energie, Règlement UE N° 1169/2011 (kcal/100 g)']

    ingredient.sodium = row['Sodium (mg/100 g)']

    ingredient.glucide = row['Glucides (g/100 g)']

    ingredient.proteins = row['Protéines. N x 6.25 (g/100 g)']

    ##A voir
    ingredient.fibres = row['Fibres alimentaires (g/100 g)']

    ingredient.eau = row['Eau (g/100 g)']
    ingredient.lipide = row['Lipides (g/100 g)']
    ingredient.sucres = row['Sucres (g/100 g)']
    ingredient.fructose = row['Fructose (g/100 g)']
    ingredient.galactose = row['Galactose (g/100 g)']
    ingredient.glucose = row['Glucose (g/100 g)']
    ingredient.lactose = row['Lactose (g/100 g)']
    ingredient.maltose = row['Maltose (g/100 g)']
    ingredient.saccharose = row['Saccharose (g/100 g)']
    ingredient.amidon = row['Amidon (g/100 g)']
    ingredient.fibresALimentraires = row['Fibres alimentaires (g/100 g)']
    ingredient.polyols = row['Polyols totaux (g/100 g)']
    ingredient.cendres = row['Cendres (g/100 g)']
    ingredient.alcool = row['Alcool (g/100 g)']

    ingredient.acidesOrganiques = row['Acides organiques (g/100 g)']
    ingredient.AGsatures = row['AG saturés (g/100 g)']
    ingredient.AGmonoinsature = row['AG monoinsaturés (g/100 g)']
    ingredient.AGpolyinsature = row['AG polyinsaturés (g/100 g)']
    ingredient.AGbutyrique = row['AG 4:0, butyrique (g/100 g)']
    ingredient.AGcaproique = row['AG 6:0, caproïque (g/100 g)']
    ingredient.AGcaprylique = row['AG 6:0, caproïque (g/100 g)']
    ingredient.AGcaprique = row['AG 10:0, caprique (g/100 g)']
    ingredient.AGlaurique = row['AG 12:0, laurique (g/100 g)']
    ingredient.AGmyristique = row['AG 14:0, myristique (g/100 g)']
    ingredient.AGpalmitique = row['AG 16:0, palmitique (g/100 g)']
    ingredient.AGbstearique = row['AG 18:0, stéarique (g/100 g)']
    ingredient.AGoleique = row['AG 18:1 9c (n-9), oléique (g/100 g)']
    ingredient.AGlinoleique = row['AG 18:2 9c,12c (n-6), linoléique (g/100 g)']
    ingredient.AGalphalinolenique = row['AG 18:3 c9,c12,c15 (n-3), alpha-linolénique (g/100 g)']
    ###arachidonique
    
    ingredient.AGarachidonique = row['AG 20:4 5c,8c,11c,14c (n-6), arachidonique (g/100 g)']
    ingredient.AGepa = row['AG 20:5 5c,8c,11c,14c,17c (n-3) EPA (g/100 g)']
    ingredient.AGdha = row['AG 22:6 4c,7c,10c,13c,16c,19c (n-3) DHA (g/100 g)']

    ingredient.cholesterol = row['Cholestérol (mg/100 g)']
    ingredient.selchlorure = row['Sel chlorure de sodium (g/100 g)']
    ingredient.calcium = row['Calcium (mg/100 g)']
    ingredient.chlorure = row['Chlorure (mg/100 g)']
    ingredient.cuivre = row['Cuivre (mg/100 g)']
    ingredient.fer = row['Fer (mg/100 g)']
    ingredient.iode = row['Iode (µg/100 g)']
    ingredient.magnesium = row['Magnésium (mg/100 g)']
    ingredient.manganese = row['Manganèse (mg/100 g)']
    ingredient.phosphore = row['Phosphore (mg/100 g)']
    ingredient.potassium = row['Potassium (mg/100 g)']
    ingredient.selenium = row['Sélénium (µg/100 g)']
    ingredient.zinc = row['Zinc (mg/100 g)']

    ingredient.retinol = row['Rétinol (µg/100 g)']
    ingredient.betaCarotene = row['Beta-Carotène (µg/100 g)']
    ingredient.vitamineD = row['Vitamine D (µg/100 g)']
    ingredient.vitamineE = row['Vitamine E (mg/100 g)']
    ingredient.VitamineK1 = row['Vitamine K1 (µg/100 g)']
    ingredient.vitamineK2 = row['Vitamine K2 (µg/100 g)']
    ingredient.vitamineB1 = row['Vitamine B1 ou Thiamine (mg/100 g)']
    ingredient.vitamineB2 = row['Vitamine B2 ou Riboflavine (mg/100 g)']
    ingredient.VitamineB3 = row['Vitamine B3 ou PP ou Niacine (mg/100 g)']
    ingredient.vitamineB5 = row['Vitamine B5 ou Acide pantothénique (mg/100 g)']
    ingredient.vitamineB6 = row['Vitamine B6 (mg/100 g)']
    ingredient.vitamineB9 = row['Vitamine B6 (mg/100 g)']
    ingredient.VitamineB12 = row['Vitamine B12 (µg/100 g)']




    ingredient.save()


'''
    #KJ

    #if ((row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)']) == "-" ) or (row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)'] == "") : 
    #ingredient.energie_kJ = float(0)
    '''''''  
    if isinstance(row['Energie. Règlement UE N° 1169/2011 (kJ/100 g)'],float) :
    #if row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)'] == np.NaN :
      
      
      #ingredient.energie_kJ = 0
      if row['Energie. Règlement UE N° 1169/2011 (kJ/100 g)'] == nan : 
        ingredient.energie_kJ = 1
        print(ingredient.energie_kJ, nan)
      else :
        ingredient.energie_kJ = row['Energie. Règlement UE N° 1169/2011 (kJ/100 g)']
        print(ingredient.energie_kJ) 


    else : 
      my_string = row['Energie. Règlement UE N° 1169/2011 (kJ/100 g)']
      if isinstance(my_string, str) and my_string != "-": 
        my_string = row['Energie. Règlement UE N° 1169/2011 (kJ/100 g)']
        commas_removed = my_string.replace(',', '')
        ingredient.energie_kJ = float(commas_removed)
      
      else :
        ingredient.energie_kJ = float(0) 





    #KCAL
    #if ((row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)']) == "-" ) or (row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)'] == "") : 
    #ingredient.energie_kJ = float(0)
      
    if isinstance(row['Energie, Règlement UE N° 1169/2011 (kcal/100 g)'],float) :
    #if row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)'] == np.NaN :
      
      
      #ingredient.energie_kJ = 0
      if row['Energie, Règlement UE N° 1169/2011 (kcal/100 g)'] == nan : 
        ingredient.energie_kcal = 1
        print(ingredient.energie_kcal, nan)
      else :
        ingredient.energie_kcal = row['Energie, Règlement UE N° 1169/2011 (kcal/100 g)']
        print(ingredient.energie_kcal) 


    else : 
      my_string = row['Energie, Règlement UE N° 1169/2011 (kcal/100 g)']
      if isinstance(my_string, str) and my_string != "-": 
        my_string = row['Energie, Règlement UE N° 1169/2011 (kcal/100 g)']
        commas_removed = my_string.replace(',', '')
        ingredient.energie_kcal = float(commas_removed)
      
      else :
        ingredient.energie_kcal = float(0) 
    #print(ingredient.famille)


    #Sodium
    #if ((row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)']) == "-" ) or (row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)'] == "") : 
    #ingredient.energie_kJ = float(0)
      
    if isinstance(row['Sel chlorure de sodium (g/100 g)'],float) :
    #if row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)'] == np.NaN :
      
      
      #ingredient.energie_kJ = 0
      if row['Sel chlorure de sodium (g/100 g)'] == nan : 
        ingredient.sodium = 1
        print(ingredient.sodium, nan)
      else :
        ingredient.sodium = row['Sel chlorure de sodium (g/100 g)']
        print(ingredient.sodium) 


    else : 
      my_string = row['Sel chlorure de sodium (g/100 g)']
      if isinstance(my_string, str) and my_string != "-": 
        my_string = row['Sel chlorure de sodium (g/100 g)']
        commas_removed = my_string.replace(',', '')
        ingredient.sodium = float(commas_removed)
      
      else :
        ingredient.sodium = float(0) 
    #print(ingredient.famille)


    #Glucides
    #if ((row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)']) == "-" ) or (row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)'] == "") : 
    #ingredient.energie_kJ = float(0)
      
    if isinstance(row['Glucides (g/100 g)'],float) :
    #if row['Energie, Règlement UE N° 1169/2011 (kJ/100 g)'] == np.NaN :
      
      
      #ingredient.energie_kJ = 0
      if row['Glucides (g/100 g)'] == nan : 
        ingredient.glucide = 1
        print(ingredient.glucide, nan)
      else :
        ingredient.glucide = row['Glucides (g/100 g)']
        print(ingredient.sodium) 


    else : 
      my_string = row['Glucides (g/100 g)']
      if isinstance(my_string, str) and my_string != "-"  and my_string != "traces": 
        my_string = row['Glucides (g/100 g)']
        commas_removed = my_string.replace(',', '')
        ingredient.glucide = float(commas_removed)
      
      else :
        ingredient.glucide = float(0)


    #print(ingredient.famille)'''


    
