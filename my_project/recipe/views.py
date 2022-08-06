from multiprocessing import context
from turtle import title
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests  
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .process import html_to_pdf 

from . import models
from .forms import ProcessFormSet, RecipeForm, IngredientForm, IngredientFormSet 
#from my_project import recipe

# Create your views here.
''' Objects transmitted into the context'''

recipes = [{
        'title' : 'burger',
        'description' : 'combine ingredients',
        'cook_time' : '30' 
    },{
        'title' : 'Pizza',
        'description' : 'combine ingredients',
        'cook_time' : '40' 
    },{
        'title' : 'Pizza',
        'description' : 'combine ingredients',
        'date_posted' : '50' }]

recipes = models.Recipe.objects.all()
ingredients_app = models.Ingredient.objects.all()
familles_app = models.Famille.objects.all()
contraintes = models.Contraintes.objects.all()
ingredients_recette = models.IngredientRecipe.objects.all()


#Creating a class based view
#class GeneratePdf(View):
 #    def get(self, request, pk, *args, **kwargs):
        #récuperer l'ID de la recette 
  #      print(pk)
        #génerer la page html de ses détails  
        # getting the template
   #     pdf = html_to_pdf('result.html')
         
         # rendering the template
    #    return HttpResponse(pdf, content_type='application/pdf')

'''Function to generate PDFs'''   
def generatePdf(request, pk):        #récuperer l'ID de la recette 
    #print(pk)
    #génerer la page html de ses détails  
    # getting the template

    recipe = models.Recipe.objects.filter(id = pk)[0]

    def total_calorie() : 
        '''
        Calculer les totaux des différents attributs des ingrédients présents dans la recette. Les stocker dans un dicionnaire
        '''

        ingredients = models.IngredientRecipe.objects.filter(recipe = recipe)
        quantite_total = 0

        total_calorique = 0 
        total_calorique_kcal = 0 
        total_glucide = 0
        total_sodium = 0

        total_proteins = 0 
        total_fibres = 0 
        total_eau= 0
        total_lipide = 0
        total_sucres = 0
        total_fructose = 0 
        total_galactose = 0 
        total_glucose= 0
        total_lactose = 0
        total_maltose= 0 
        total_saccharose = 0 
        total_amidon= 0

        total_fibresAlimentaires = 0
        total_polyols= 0 
        total_cendres = 0 
        total_alcool= 0
        
        total_acidesOrganiques = 0
        total_AGsatures = 0 
        total_AGmonoinsature = 0 
        total_AGpolyinsature = 0
        total_AGbutyrique = 0
        total_AGcaproique = 0 
        total_AGcaprylique = 0 
        total_AGcaprique = 0

        total_AGlaurique = 0 
        total_AGmyristique = 0
        total_AGpalmitique = 0
        total_AGbstearique = 0 
        total_AGoleique = 0 
        
        total_AGlinoleique = 0 
        total_AGalphalinolenique = 0

        total_AGepa = 0
        total_AGdha = 0

        total_cholesterol = 0 
        total_selchlorure = 0
        total_calcium = 0 
        total_cuivre = 0
        total_fer = 0 
        total_iode = 0 
        total_magnesium = 0
        total_manganese = 0
        total_phosphore = 0
        total_potassium= 0 
        total_selenium = 0 
        total_zinc = 0
        total_retinol= 0
        total_betacarotene = 0

        total_vitamineD = 0
        total_vitamineE = 0 

        total_VitamineK1 = 0 
        total_vitamineK2 = 0

        total_vitamineB1 = 0
        total_vitamineB2 = 0 
        total_vitamineB3 = 0
        total_VitamineB5 = 0 
        total_vitamineB6 = 0
        total_VitamineB9 = 0 
        total_vitamineB12 = 0


        total_fibresAlimentaires = 0
        total_sels_ajoutes = 0
        total_sucres_ajoutes = 0

        Total_graisses_ajoutes = 0
        Total_fruitslegumineuse = 0

        quantite_total = 0.001
        if ingredients.__len__ == 0 :
            quantite_total = 1
            print(ingredients)
            print(" est vide")

        else :
            print(ingredients)
        for ingredient in ingredients : 

            if ingredient.ingredient.forme.name=='sels' :
                total_sels_ajoutes = total_sels_ajoutes + ingredient.quantity 

            if ingredient.ingredient.forme.name=='sucres,miels et assimilés' :
                total_sucres_ajoutes = total_sucres_ajoutes + ingredient.quantity 

            if ingredient.ingredient.famille.name =='matières grasses' :
                Total_graisses_ajoutes = Total_graisses_ajoutes + ingredient.quantity 

            if ingredient.ingredient.famille.name =='fruits, légumes, légumineuses et oléagineux' :
                Total_fruitslegumineuse = Total_fruitslegumineuse + ingredient.quantity 

 
            if isinstance(ingredient.ingredient.energie_kJ, float):
                total_calorique  = total_calorique + ingredient.quantity * (ingredient.ingredient.energie_kJ/100)

            if isinstance(ingredient.ingredient.energie_kcal, float):
                total_calorique_kcal  = total_calorique_kcal + ingredient.quantity * (ingredient.ingredient.energie_kcal/100)
            
            if isinstance(ingredient.ingredient.glucide , float):
                total_glucide  = total_glucide + ingredient.quantity * (ingredient.ingredient.glucide/100)

            if isinstance(ingredient.ingredient.sodium , float):
                total_sodium  = total_sodium + ingredient.quantity * (ingredient.ingredient.sodium/100)


            if isinstance(ingredient.ingredient.energie_kJ, float):
                total_proteins  = total_proteins + ingredient.quantity * (ingredient.ingredient.energie_kJ/100)

            if isinstance(ingredient.ingredient.fibres, float):
                total_fibres  = total_fibres + ingredient.quantity * (ingredient.ingredient.fibres/100)
            
            if isinstance(ingredient.ingredient.eau , float):
                total_eau  = total_eau + ingredient.quantity * (ingredient.ingredient.eau/100)

            if isinstance(ingredient.ingredient.lipide , float):
                total_lipide  = total_lipide + ingredient.quantity * (ingredient.ingredient.lipide/100)



            if isinstance(ingredient.ingredient.sucres, float):
                total_sucres  = total_sucres + ingredient.quantity * (ingredient.ingredient.sucres/100)

            if isinstance(ingredient.ingredient.fructose, float):
                total_fructose  = total_fructose + ingredient.quantity * (ingredient.ingredient.fructose/100)
            
            if isinstance(ingredient.ingredient.galactose , float):
                total_galactose  = total_galactose + ingredient.quantity * (ingredient.ingredient.galactose/100)

            if isinstance(ingredient.ingredient.glucose , float):
                total_glucose  = total_glucose + ingredient.quantity * (ingredient.ingredient.glucose/100)

            if isinstance(ingredient.ingredient.lactose, float):
                total_lactose  = total_lactose + ingredient.quantity * (ingredient.ingredient.lactose/100)

            if isinstance(ingredient.ingredient.maltose, float):
                total_maltose  = total_maltose + ingredient.quantity * (ingredient.ingredient.maltose/100)

            if isinstance(ingredient.ingredient.saccharose, float):
                total_saccharose  = total_saccharose + ingredient.quantity * (ingredient.ingredient.saccharose/100)
            
            if isinstance(ingredient.ingredient.amidon , float):
                total_amidon  = total_amidon + ingredient.quantity * (ingredient.ingredient.amidon/100)

            if isinstance(ingredient.ingredient.fibresALimentraires , float):
                total_fibresAlimentaires  = total_fibresAlimentaires + ingredient.quantity * (ingredient.ingredient.fibresALimentraires/100)

            if isinstance(ingredient.ingredient.polyols, float):
                total_polyols  = total_polyols + ingredient.quantity * (ingredient.ingredient.polyols/100)


            if isinstance(ingredient.ingredient.cendres , float):
                total_cendres  = total_cendres + ingredient.quantity * (ingredient.ingredient.cendres/100)

            if isinstance(ingredient.ingredient.alcool , float):
                total_alcool  = total_alcool + ingredient.quantity * (ingredient.ingredient.alcool/100)

            if isinstance(ingredient.ingredient.acidesOrganiques, float):
                total_acidesOrganiques  = total_acidesOrganiques + ingredient.quantity * (ingredient.ingredient.acidesOrganiques/100)


            if isinstance(ingredient.ingredient.AGsatures, float):
                total_AGsatures  = total_AGsatures + ingredient.quantity * (ingredient.ingredient.AGsatures/100)

            if isinstance(ingredient.ingredient.AGmonoinsature, float):
                total_AGmonoinsature  = total_AGmonoinsature + ingredient.quantity * (ingredient.ingredient.AGmonoinsature/100)

            if isinstance(ingredient.ingredient.AGpolyinsature, float):
                total_AGpolyinsature  = total_AGpolyinsature + ingredient.quantity * (ingredient.ingredient.AGpolyinsature/100)
            
            if isinstance(ingredient.ingredient.AGbutyrique , float):
                total_AGbutyrique  = total_AGbutyrique + ingredient.quantity * (ingredient.ingredient.AGbutyrique/100)

            if isinstance(ingredient.ingredient.AGcaproique , float):
                total_AGcaproique  = total_AGcaproique + ingredient.quantity * (ingredient.ingredient.AGcaproique/100)

            if isinstance(ingredient.ingredient.AGcaprylique, float):
                total_AGcaprylique  = total_AGcaprylique + ingredient.quantity * (ingredient.ingredient.AGcaprylique/100)

            if isinstance(ingredient.ingredient.AGcaprique , float):
                total_AGcaprique  = total_AGcaprique + ingredient.quantity * (ingredient.ingredient.AGcaprique/100)

            if isinstance(ingredient.ingredient.AGlaurique , float):
                total_AGlaurique  = total_AGlaurique + ingredient.quantity * (ingredient.ingredient.AGlaurique/100)

            if isinstance(ingredient.ingredient.AGmyristique, float):
                total_AGmyristique  = total_AGmyristique + ingredient.quantity * (ingredient.ingredient.AGmyristique/100)

            if isinstance(ingredient.ingredient.AGpalmitique , float):
                total_AGpalmitique  = total_AGpalmitique + ingredient.quantity * (ingredient.ingredient.AGpalmitique/100)

            if isinstance(ingredient.ingredient.AGbstearique, float):
                total_AGbstearique  = total_AGbstearique + ingredient.quantity * (ingredient.ingredient.AGbstearique/100)

            if isinstance(ingredient.ingredient.AGoleique , float):
                total_AGoleique  = total_AGoleique + ingredient.quantity * (ingredient.ingredient.AGoleique/100)

            if isinstance(ingredient.ingredient.AGlinoleique , float):
                total_AGlinoleique  = total_AGlinoleique + ingredient.quantity * (ingredient.ingredient.AGlinoleique/100)

            if isinstance(ingredient.ingredient.AGalphalinolenique , float):
                total_AGalphalinolenique  = total_AGalphalinolenique + ingredient.quantity * (ingredient.ingredient.sodium/100)

            if isinstance(ingredient.ingredient.AGepa, float):
                total_AGepa  = total_AGepa + ingredient.quantity * (ingredient.ingredient.AGepa/100)

            if isinstance(ingredient.ingredient.AGdha, float):
                total_AGdha  = total_AGdha + ingredient.quantity * (ingredient.ingredient.AGdha/100)

            if isinstance(ingredient.ingredient.cholesterol, float):
                total_cholesterol  = total_cholesterol + ingredient.quantity * (ingredient.ingredient.cholesterol/100)

            if isinstance(ingredient.ingredient.selchlorure , float):
                total_selchlorure  = total_selchlorure + ingredient.quantity * (ingredient.ingredient.selchlorure/100)

            if isinstance(ingredient.ingredient.calcium, float):
                total_calcium  = total_calcium + ingredient.quantity * (ingredient.ingredient.calcium/100)

            if isinstance(ingredient.ingredient.cuivre, float):
                total_cuivre  = total_cuivre + ingredient.quantity * (ingredient.ingredient.cuivre/100)

            if isinstance(ingredient.ingredient.fer , float):
                total_fer  = total_fer + ingredient.quantity * (ingredient.ingredient.fer/100)

            if isinstance(ingredient.ingredient.iode , float):
                total_iode  = total_iode + ingredient.quantity * (ingredient.ingredient.iode/100)

            if isinstance(ingredient.ingredient.magnesium, float):
                total_magnesium  = total_magnesium + ingredient.quantity * (ingredient.ingredient.magnesium/100)



            if isinstance(ingredient.ingredient.manganese, float):
                total_manganese  = total_manganese + ingredient.quantity * (ingredient.ingredient.manganese/100)

            if isinstance(ingredient.ingredient.phosphore , float):
                total_phosphore  = total_phosphore + ingredient.quantity * (ingredient.ingredient.phosphore/100)

            if isinstance(ingredient.ingredient.potassium, float):
                total_potassium  = total_potassium + ingredient.quantity * (ingredient.ingredient.potassium/100)

            if isinstance(ingredient.ingredient.selenium , float):
                total_selenium  = total_selenium + ingredient.quantity * (ingredient.ingredient.selenium/100)

            if isinstance(ingredient.ingredient.zinc , float):
                total_zinc  = total_zinc + ingredient.quantity * (ingredient.ingredient.zinc/100)

            if isinstance(ingredient.ingredient.retinol, float):
                total_retinol  = total_retinol + ingredient.quantity * (ingredient.ingredient.retinol/100)

            if isinstance(ingredient.ingredient.betaCarotene , float):
                total_betacarotene  = total_betacarotene + ingredient.quantity * (ingredient.ingredient.betaCarotene/100)

            if isinstance(ingredient.ingredient.vitamineD , float):
                total_vitamineD  = total_vitamineD + ingredient.quantity * (ingredient.ingredient.vitamineD/100)

            if isinstance(ingredient.ingredient.vitamineE, float):
                total_vitamineE  = total_vitamineE + ingredient.quantity * (ingredient.ingredient.vitamineE/100)
            if isinstance(ingredient.ingredient.VitamineK1 , float):
                total_VitamineK1  = total_VitamineK1 + ingredient.quantity * (ingredient.ingredient.VitamineK1/100)

            if isinstance(ingredient.ingredient.vitamineK2 , float):
                total_vitamineK2  = total_vitamineK2 + ingredient.quantity * (ingredient.ingredient.vitamineK2/100)

            if isinstance(ingredient.ingredient.vitamineB1, float):
                total_vitamineB1  = total_vitamineB1 + ingredient.quantity * (ingredient.ingredient.vitamineB1/100)

            
            if isinstance(ingredient.ingredient.vitamineB2, float):
                total_vitamineB2  = total_vitamineB2 + ingredient.quantity * (ingredient.ingredient.vitamineB2/100)

#####vitamineB2

            if isinstance(ingredient.ingredient.VitamineB3 , float):
                total_vitamineB3  = total_vitamineB3 + ingredient.quantity * (ingredient.ingredient.VitamineB3/100)

            if isinstance(ingredient.ingredient.vitamineB5 , float):
                total_VitamineB5  = total_VitamineB5 + ingredient.quantity * (ingredient.ingredient.vitamineB5/100)

            if isinstance(ingredient.ingredient.vitamineB9, float):
                total_vitamineB6  = total_vitamineB6 + ingredient.quantity * (ingredient.ingredient.vitamineB6/100)
            if isinstance(ingredient.ingredient.glucide , float):
                total_VitamineB9  = total_VitamineB9 + ingredient.quantity * (ingredient.ingredient.vitamineB9/100)
#Changing V to V
            if isinstance(ingredient.ingredient.VitamineB12 , float):
                total_vitamineB12  = total_vitamineB12 + ingredient.quantity * (ingredient.ingredient.VitamineB12/100)

                
            if isinstance(ingredient.quantity, float):
                quantite_total  = quantite_total + ingredient.quantity 
 


        return {"total_calorique" : total_calorique / quantite_total, "total_calorique_kcal" : total_calorique_kcal/quantite_total,
                "total_glucide" : total_glucide / quantite_total, "total_sodium" : total_sodium / quantite_total, 
                "total_proteins" : total_proteins / quantite_total, "total_fibres" : total_fibres / quantite_total, 
                "total_eau" : total_eau / quantite_total, "total_sodium" : total_sodium / quantite_total, 
                "total_lipide" : total_lipide / quantite_total, "total_sucres" : total_sucres / quantite_total, 
                "total_fructose" : total_fructose / quantite_total, "total_galactose" : total_galactose / quantite_total, 
                "total_glucose" : total_glucose / quantite_total, "total_lactose" : total_lactose / quantite_total, 
                "total_maltose" : total_maltose / quantite_total, "total_saccharose" : total_saccharose / quantite_total, 
                "total_amidon" : total_amidon / quantite_total, "total_fibresAlimentaires" : total_fibresAlimentaires / quantite_total, 
                "total_polyols" : total_polyols / quantite_total, "total_cendres" : total_cendres / quantite_total, 
                "total_alcool" : total_alcool / quantite_total, "total_acidesOrganiques" : total_acidesOrganiques / quantite_total, 
                "total_AGsatures" : total_AGsatures / quantite_total, "total_AGmonoinsature" : total_AGmonoinsature / quantite_total, 
                "total_AGpolyinsature" : total_AGpolyinsature / quantite_total, "total_AGbutyrique" : total_AGbutyrique / quantite_total, 
                "total_AGcaproique" : total_AGcaproique / quantite_total, "total_AGcaprylique" : total_AGcaprylique / quantite_total, 
                "total_AGcaprique" : total_AGcaprique / quantite_total, "total_AGlaurique" : total_AGlaurique / quantite_total, 
        
                "total_AGmyristique" : total_AGmyristique / quantite_total, "total_AGpalmitique" : total_AGpalmitique / quantite_total, 

                "total_AGbstearique" : total_AGbstearique / quantite_total, "total_AGoleique" : total_AGoleique / quantite_total, 

                "total_AGlinoleique" : total_AGlinoleique / quantite_total, "total_AGalphalinolenique" : total_AGalphalinolenique / quantite_total, 

                        
                "total_AGepa" : total_AGepa / quantite_total, "total_AGdha" : total_AGdha / quantite_total, "total_cholesterol" : total_cholesterol / quantite_total, 

                "total_selchlorure" : total_selchlorure / quantite_total, "total_cuivre" : total_cuivre / quantite_total, 

                "total_fer" : total_fer / quantite_total, "total_iode" : total_iode / quantite_total, 

                "total_magnesium" : total_magnesium / quantite_total, "total_manganese" : total_manganese / quantite_total, "total_calcium" : total_calcium / quantite_total, 

                "total_phosphore" : total_phosphore / quantite_total, "total_potassium" : total_potassium / quantite_total, 

                "total_selenium" : total_selenium / quantite_total, "total_zinc" : total_zinc / quantite_total, 
                
                "total_retinol" : total_retinol / quantite_total, "total_betacarotene" : total_betacarotene / quantite_total, 

                "total_vitamineD" : total_vitamineD / quantite_total, "total_vitamineE" : total_vitamineE / quantite_total, 

                "total_VitamineK1" : total_VitamineK1 / quantite_total, "total_vitamineK2" : total_vitamineK2 / quantite_total, 

                    
                "total_vitamineB1" : total_vitamineB1 / quantite_total, "total_vitamineB2" : total_vitamineB2 / quantite_total, 

                "total_vitamineB3" : total_vitamineB3 / quantite_total, "total_VitamineB5" : total_VitamineB5 / quantite_total, 

                "total_vitamineB6" : total_vitamineB6 / quantite_total, "total_VitamineB9" : total_VitamineB9 / quantite_total,  

                "total_VitamineB12" : total_vitamineB12 / quantite_total,   "total_sels_ajoutes" : total_sels_ajoutes / quantite_total , "total_sucres_ajoutes" : total_sucres_ajoutes / quantite_total, "total_graisses_ajoutes" : Total_graisses_ajoutes / quantite_total, "total_fruitslegumineuse" : Total_fruitslegumineuse / quantite_total ,

                "Quantite_totale" : quantite_total}


    def score_calorie_kj(total_calorique) : 
        '''Calculer un score selon le total obtenu'''
        score = (total_calorique - 0.1) // 335
        if score < 10 : 
            return score
        else :
            return 10 


    def score_sodium(total_sodium) : 
        score = (total_sodium - 0.1) // 90
        if score < 10 : 
            return score
        else :
            return 10 

    def score_glucide(total_glucide) : 
        ''' Calculer score de glucide '''
        score = (total_glucide - 0.01) // 4.5
        if score < 10 : 
            return score
        else :
            return 10 

    def score_agsature(total_agsature) : 
        ''' Calculer score d'acides gras saturés '''
        score = (total_agsature - 0.1) // 1
        if score < 10 : 
            return score
        else :
            return 10 

    def score_protein(total_protein) : 
        ''' Calculer score de protein '''
        score = (total_protein - 0.01) // 1.6
        if score < 5 : 
            return score
        else :
            return 5 

    def score_fibre(total_fibre) : 
        ''' Calculer score de fibres '''
        score = (total_fibre - 0.01) // 0.9
        if score < 5 : 
            return score
        else :
            return 5 


    def score_fln(total_graisse, total_fruitslegumes) : 
        ''' Calculer score de fruit légumes et légumineuse '''
        score = total_graisse + total_fruitslegumes
        return score

    def score_A(pts_kj, pts_glucide, pts_agsatures, pts_sodium) : 
        ''' Calculer score A '''
        score =  pts_kj + pts_glucide + pts_agsatures + pts_sodium
        return score

    def nutriscore(scoreA, pts_fln, pts_prot, pts_fib):
        ''' Attribuer un nutriscore selon les scores calculés'''
        if (scoreA < 11 and scoreA > 0) or (scoreA >= 11 and pts_fln == 5) : 
            return scoreA - (pts_prot + pts_fln)

        else :
            return scoreA - (pts_fln + pts_fib)

    def nutriscoreLettre(nutriscore):
        if nutriscore < 0 : 
            return "Nutriscore A"
        elif nutriscore < 3 :
            return "Nutriscore B"
        elif nutriscore < 11 :
            return "Nutriscore C"  
        elif nutriscore < 19 :
            return "Nutriscore D"
        else :
            return "Nutriscore E"



    def allegation(total_cal, total_graisse, total_graisse_saturee, total_sucres,
     total_sucres_ajoutes, total_sel, total_sel_ajoute, total_fibre, total_protein, total_graisses_monoinsatures, 
     total_graisses_polyinsatures, total_selenium,  total_magnesium, total_phosphore, total_calcium, 
     total_cuivre, total_fer, total_manganese, total_potassium, total_zinc, total_vitamineD, total_vitamineE,
      total_vitamineK, total_vitamineB1,  total_vitamineB2, total_vitamineB3, total_vitamineB5, total_vitamineB6, 
      total_vitamineB9, total_vitamineB12, total_AGepa, total_dha  ) : 
        '''faire une allégation selon les valeurs des différents totaux'''
        allegations = []
        allegations_minerales = []

        total_cal = 0.001

        if total_cal < 170 : 
            allegations.append('Faible en valeur énergétique' )
        elif total_cal < 17 : 
            allegations.append('Sans apport energetique')

        #ajouter acide gras trans  
        if total_graisse < 3 :
            allegations.append ('faible teneur en matières grasses')
        
        elif total_graisse < 0.5 :
            allegations.append ('sans matières grasses' )
        
        #à voir avec le client    
        if total_graisse_saturee < 1.5 :
            allegations.append ('faible teneur en graisses saturees')

        elif total_graisse_saturee < 0.1 :
            allegations.append ('faible teneur en graisses saturees')    
        
        if total_sucres_ajoutes < 5 :
            allegations.append ('faible teneur en sucres')

        elif total_sucres_ajoutes < 0.5 :
            allegations.append ('sans sucres')

        #à voir avec le client 
        #if total_sucres_ajoutes < 0.5 :
        #    allegations.append ({'sans sucres ajoutes' : total_sucres})    
        
        if total_sel + total_sel_ajoute < 0.12 :
            allegations.append ('pauvre en sel')   

        elif total_sel + total_sel_ajoute < 0.04 :
            allegations.append ('tres pauvre en sel')    
        
        elif total_sel + total_sel_ajoute< 0.005 :
            allegations.append ('sans sodium')   

        #if total_sel + total_sel_ajoute< 0.005 :
        #    allegations.append ({'sans sodium ajouté' : total_sel})  

        #a voir avec le client
        if total_fibre > 3 :
            allegations.append ('source de fibres')    

        elif total_fibre > 6 :
            allegations.append ('riche en fibres')

        #a voir avec le client
        if total_protein * 4 / total_cal > 12 :
            allegations.append ('source de proteins')

        elif total_protein * 4 / total_cal > 20 :
            allegations.append ('riche en proteins')


        ### 22, 23, 24 
        total_acide_alphalinolenique, total_acide_eicosapentaenoique, total_acide_docosahexenoique = 0, 0, 0
        if total_acide_alphalinolenique > 0.3 or (total_acide_eicosapentaenoique + total_acide_docosahexenoique > 0.04) : 
            allegations.append ('source d acide gras omega3')

        elif total_acide_alphalinolenique > 0.3 or (total_acide_eicosapentaenoique + total_acide_docosahexenoique > 40) : 
            allegations.append ('riche en acide gras omega3')

        energie_graisses_monoinsatures, perc_graisses_monoinsatures = 0, 0
        if (perc_graisses_monoinsatures > 0.45 and energie_graisses_monoinsatures > 0.2 * total_cal) : 
            allegations.append ('riche en graisse monoinsaturees')

        perc_graisses_polyinsatures, energie_graisses_polyinsatures = 0, 0
        if (perc_graisses_polyinsatures > 0.45 and energie_graisses_polyinsatures > 0.2 * total_cal) : 
            allegations.append ('riche en graisse polyinsaturees')


        if total_selenium > 8.25 : 
            allegations.append('source de selenium')
        elif total_selenium > 16.5 : 
            allegations.append('riche en selenium')

        if total_magnesium > 0.056 : 
            allegations.append('source de magnesium')
        elif total_magnesium > 0.112 : 
            allegations.append('riche en magnesium')

        if total_phosphore > 0.105 : 
            allegations.append('source de phosphore')
        elif total_phosphore > 0.210 : 
            allegations.append('riche en phosphore')

        if total_calcium > 120 : 
            allegations.append('source de calcium')
        elif total_calcium > 240 : 
            allegations.append('riche en selenium')

        if total_cuivre > 0.15 : 
            allegations.append('source de cuivre')
        elif total_cuivre > 0.30 : 
            allegations.append('riche en cuivre')

        if total_fer > 2.1 : 
            allegations.append('source de fer')
        elif total_fer > 4.2 : 
            allegations.append('riche en fer')

        if total_manganese > 0.3 : 
            allegations.append('source de manganese')
        elif total_manganese > 0.6 : 
            allegations.append('riche en manganese')

        if total_potassium > 300 : 
            allegations.append('source de potassium')
        elif total_potassium > 600 : 
            allegations.append('riche en potassium')    

        if total_zinc > 1.5 : 
            allegations.append('source de zinc')
        elif total_zinc > 3 : 
            allegations.append(['riche en zinc'])

        if total_vitamineD > 0.75 : 
            allegations.append(['source de vitamine D'])
        elif total_vitamineD > 1.5 : 
            allegations.append(['riche en vitamine D'])

        if total_vitamineE > 1.8 : 
            allegations.append(['source de vitamine E'])
        elif total_vitamineE > 1.8 : 
            allegations.append(['riche en vitamine E'])
            
        if total_vitamineK > 1.8 : 
            allegations.append(['source de vitamine K'])
        elif total_vitamineK > 1.8 : 
            allegations.append(['riche en vitamine K'])            
            
        if total_vitamineB1 > 0.165 : 
            allegations.append(['source de vitamine B1'])
        elif total_vitamineB1 > 0.33 : 
            allegations.append(['riche en vitamine B1'])     

        if total_vitamineB2 > 0.21 : 
            allegations.append(['source de vitamine B2'])
        elif total_vitamineB2 > 0.42 : 
            allegations.append(['riche en vitamine B2'])     


        if total_vitamineB3 > 2.4 : 
            allegations.append(['source de vitamine B2'])
        elif total_vitamineB3 > 4.2 : 
            allegations.append(['riche en vitamine B2'])     

        if total_vitamineB5 > 0.9 : 
            allegations.append(['source de vitamine B5'])
        elif total_vitamineB5 > 1.8 : 
            allegations.append(['riche en vitamine B5'])     

        if total_vitamineB6 > 0.21 : 
            allegations.append(['source de vitamine B6'])
        elif total_vitamineB6 > 0.42 : 
            allegations.append(['riche en vitamine B6'])

        if total_vitamineB9 > 30 : 
            allegations.append(['source de vitamine B9'])
        elif total_vitamineB9 > 60 : 
            allegations.append(['riche en vitamine B9'])

        if total_vitamineB12 > 0.375 : 
            allegations.append(['source de vitamine B12'])
        elif total_vitamineB12 > 0.75: 
            allegations.append(['riche en vitamine B12'])

        return allegations


#############################################################################################################################
#
# Declare necessary data 
#
#######################################################################################################
    nutriscore_couleur = {"Nutriscore A" : "Vert", "Nutriscore B" : "Vert_clair", "Nutriscore C" : "Jaune", "Nutriscore D" : "Orange Clair", "Nutriscore E" : "Orange Foncé", }
    ingredient_Recipe = models.IngredientRecipe.objects.filter(recipe = recipe)
    ingredients = models.IngredientRecipe.objects.filter(recipe = recipe)



    total_calorique = 0 
    for ingredient in ingredients : 
        if isinstance(ingredient.ingredient.energie_kJ, float):
            total_calorique  = total_calorique + ingredient.quantity * (ingredient.ingredient.energie_kJ/100)

    context = {'object' : recipe, 'ingredients' : ingredients}

    #context['total_calorie'] = total_calorie()
    #context['Score_calorie'] = score_calorie_kj()
    context['Attribut_test'] = RecipeDetailView.function_test()
    process_Recipe = models.ProcessRecipe.objects.filter(recipe = recipe)


    '''for i in range(len(ingredient_Recipe)) : 
        if ingredient_Recipe[i].recipe.famille == models.Famille.objects.get(name = 'viandes, œufs, poissons et assimilés'):
            score_fln = score_fln + ingredient_Recipe[i].quantity
    '''



    context['ingredients'] = ingredient_Recipe
    context['process'] = process_Recipe

    totaux = total_calorie()

###########################################################################################
#
#   Envoi des quantites calculees au front end
#
############################################################################################

    context['total_calorie'] = totaux["total_calorique"]
    context['quantite_totale'] = totaux["Quantite_totale"]
    context['inv_quantite_totale'] = 1/totaux["Quantite_totale"]
    context['total_calorie_kcal'] = totaux["total_calorique_kcal"]


    context['total_glucide'] = round(totaux["total_glucide"],2)
    context['total_sodium'] = totaux["total_sodium"]

    context['total_protein'] = totaux['total_proteins']
    context['total_fibre'] = round(totaux["total_fibres"],5)
    context['total_eau'] = round(totaux["total_eau"],2)
    context['total_lipide'] = round(totaux["total_lipide"],2)

    context['total_sucres'] = totaux['total_sucres']
    context['total_fructose'] = round(totaux["total_fructose"],5)
    context['total_galactose'] = round(totaux["total_galactose"],2)
    context['total_glucose'] = round(totaux["total_glucose"],2)
    context['total_lactose'] = totaux['total_lactose']
    context['total_maltose'] = round(totaux["total_maltose"],5)
    context['total_saccharose'] = round(totaux["total_saccharose"],2)
    context['total_amidon'] = round(totaux["total_amidon"],2)
    context['total_fibresAlimentaires'] = round(totaux["total_fibresAlimentaires"],2)

    context['total_polyols'] = totaux['total_polyols']
    context['total_cendres'] = round(totaux["total_cendres"],5)
    context['total_alcool'] = round(totaux["total_alcool"],2)
    context['total_acidesOrganiques'] = round(totaux["total_acidesOrganiques"],2)
    context['total_AGsatures'] = totaux['total_AGsatures']
    context['total_AGmonoinsature'] = round(totaux["total_AGmonoinsature"],5)
    context['total_AGpolyinsature'] = round(totaux["total_AGpolyinsature"],2)
    context['total_AGbutyrique'] = round(totaux["total_AGbutyrique"],2)
    context['total_AGcaproique'] = round(totaux["total_AGcaproique"],2)
    context['total_AGcaprylique'] = totaux['total_AGcaprylique']

    context['total_AGlaurique'] = round(totaux["total_AGlaurique"],5)
    context['total_AGmyristique'] = round(totaux["total_AGmyristique"],2)
    context['total_AGbutyrique'] = round(totaux["total_AGbutyrique"],2)
    context['total_AGpalmitique'] = round(totaux["total_AGpalmitique"],2)
    context['total_AGbstearique'] = round(totaux["total_AGbstearique"],2)
    context['total_AGoleique'] = round(totaux["total_AGoleique"],2)
    context['total_AGlinoleique'] = round(totaux["total_AGlinoleique"],2)
    context['total_AGalphalinolenique'] = round(totaux["total_AGalphalinolenique"],2)

    context['total_AGepa'] = round(totaux["total_AGepa"],5)
    context['total_AGdha'] = round(totaux["total_AGdha"],2)

    context['total_cholesterol'] = round(totaux["total_cholesterol"],2)
    context['total_selchlorure'] = round(totaux["total_selchlorure"],2)
    context['total_calcium'] = round(totaux["total_calcium"],2)
    context['total_cuivre'] = round(totaux["total_cuivre"],2)
    context['total_fer'] = round(totaux["total_fer"],2)
    context['total_iode'] = totaux['total_iode']
    context['total_magnesium'] = round(totaux["total_magnesium"],2)
    context['total_manganese'] = round(totaux["total_manganese"],2)
    context['total_phosphore'] = round(totaux["total_phosphore"],2)
    context['total_potassium'] = round(totaux["total_potassium"],2)
    context['total_selenium'] = round(totaux["total_selenium"],2)
    context['total_zinc'] = round(totaux["total_zinc"],2)
    context['total_retinol'] = round(totaux["total_retinol"],2)
    context['total_betacarotene'] = round(totaux["total_betacarotene"],2)



    context['total_phosphore'] = round (totaux["total_phosphore"], 3)
    context['total_selenium'] = round(totaux["total_zinc"],5)
    context['total_VitamineK1'] = round(totaux["total_VitamineK1"],2)
    context['total_vitamineK2'] = totaux["total_vitamineK2"]
    context['total_vitamineB1'] = totaux['total_vitamineB1']
    context['total_vitamineB2'] = round (totaux["total_vitamineB2"], 3)
    context['total_vitamineB3'] = round(totaux["total_vitamineB3"],5)

    context['total_VitamineB5'] = totaux['total_VitamineB5']
    context['total_VitamineB9'] = round (totaux["total_VitamineB9"], 3)
    context['total_VitamineB12'] = round(totaux["total_VitamineB12"],5)


    context['total_sels_ajoutes'] = totaux['total_sels_ajoutes']
    context['total_sucres_ajoutes'] = round (totaux["total_sucres_ajoutes"], 3)
    context['Total_graisses_ajoutes'] = totaux['total_graisses_ajoutes']
    context['Total_fruitslegumineuse'] = round (totaux["total_fruitslegumineuse"], 3)



    #get the total_fln quantite des ingredients appartenant a fruits, légumes ou légumineuses
    #context['total_fln'] = totaux['total_protein']

###############################################################################################
#            Calcul des scores en fonction des totaux
#
###############################################################################################
    score_kj = score_calorie_kj(totaux["total_calorique"])
    score_sodium = score_sodium(totaux["total_sodium"])
    score_glucide = score_glucide(totaux["total_glucide"])
    score_agsatures = score_agsature(totaux["total_AGsatures"])
    score_protein = score_protein(totaux["total_proteins"])
    score_fibre = score_fibre(totaux["total_fibres"])
    score_fln = score_fln(totaux["total_graisses_ajoutes"], totaux["total_fruitslegumineuse"])

    scoreA = score_A(score_kj, score_glucide, score_agsatures, score_sodium)
    nutriscore = nutriscore(scoreA, score_fln, score_protein, score_fibre)  

    context['Score_sodium'] = score_sodium
    context['Score_glucide'] = score_glucide
    context['score_AGsatures'] = score_agsatures
    context['score_protein'] = score_protein
    context['score_fibre'] = score_fibre
    context['score_fln'] = score_fln
    context['score_A'] = scoreA
    context['Score_calorie_kcal'] = 0        


    context['nutriscore'] = nutriscoreLettre(nutriscore)
    context['couleur'] = nutriscore_couleur[context['nutriscore']]
    context['allegation'] = allegation(totaux["total_calorique"], totaux["total_graisses_ajoutes"], totaux["total_AGsatures"], totaux["total_sucres"],
                            totaux["total_sucres_ajoutes"], totaux["total_sodium"], totaux["total_sels_ajoutes"], totaux["total_fibres"], totaux["total_proteins"], totaux["total_AGmonoinsature"], totaux["total_AGpolyinsature"], 
                            totaux["total_selenium"], totaux["total_magnesium"], totaux["total_phosphore"], totaux["total_calcium"], totaux["total_cuivre"], totaux["total_fer"], totaux["total_manganese"], totaux["total_potassium"], totaux["total_zinc"], 
                            totaux["total_vitamineD"], totaux["total_vitamineE"], totaux["total_VitamineK1"], totaux["total_VitamineB5"],  totaux["total_vitamineB2"], totaux["total_vitamineB3"], totaux["total_vitamineB2"], totaux["total_vitamineB6"], totaux["total_VitamineB9"],
                            totaux["total_VitamineB12"], totaux["total_AGepa"], totaux["total_AGdha"] )

    #context.pop('self', None)
    #context['self'] = recipe_cont
    pdf = html_to_pdf("recipe/recipe_detail_pdf.html", context_dict = context)

    # rendering the template
    return HttpResponse(pdf, content_type='application/pdf')


def home(request):
    context = {'title' : 'homme'}
    return render(request, "recipe/home.html", context)
    #return HttpResponse("<h1> Welcome to ORI </h1>")ß

'''def recettes(request):
    context = {'recipes' : recipes, 'title' : 'Recettes'}
    return render(request, "recipe/recettes.html", context)
    #return HttpResponse("<h1> Welcome to ORI </h1>")'''

def ingredients(request):
    context = {'ingredients' : ingredients_app, 'title' : 'Ingrédients'}
    return render(request, "recipe/ingredients.html", context)

def familles(request):
    context = {'familles' : familles_app, 'ingredients' : ingredients_app ,'title' : 'Ingrédients'}
    return render(request, "recipe/familles.html", context)

def contraintes(request):
    context = {'contraintes' : contraintes, 'title' : 'Ingrédients'}
    return render(request, "recipe/contraintes.html", context)





def create_recipe2(request) : 
    #form = form()
        #def form_valid(self, form):
        #form.instance.author = self.request.user
        #return super().form_valid(form)
    print(request)

    Formset_Params = {
    'ingredients_recipe-TOTAL_FORMS' : '1',
    'ingredients_recipe-INITIAL_FORMS' : '0',
    'ingredients_recipe-MIN_NUM_FORMS' : '1', 
    }    
    if request.method ==  "GET":
        form = RecipeForm()
        formset = IngredientFormSet(Formset_Params)
        #formset = IngredientFormSet()
        #return render(request, 'recipe/create_recipe.html', {"form" : form, "formset" : formset})
        return render(request, 'recipe/create_recipe.html', {"form" : form, "formset" : formset})

    elif request.method == "POST" :
        if 'terminerBttn' in request.POST:
            print(print(request.POST.get('title')))
            form = RecipeForm(request.POST)
            formset = IngredientFormSet(request.POST)
            form.instance.author = request.user
            if form.is_valid():
                recipe = form.save()
                pk = recipe.id
                formset = IngredientFormSet(request.POST, instance=recipe)
                
                if formset.is_valid():
                    formset.save()
            return redirect("create_recipe_process", pk)
        
    else :
        return render(request, 'recipe/create_recipe.html', {"form" : form, "formset" : formset})


def create_process(request, pk) : 
    Formset_Params = {
    "process_recipe-TOTAL_FORMS" : '1',
    "process_recipe-INITIAL_FORMS" : '1',
    "process_recipe-MIN_NUM_FORMS" : '1', 
    }    
    if request.method ==  "GET":
        print(" GET ")
        recipe_instance = models.Recipe.objects.get(id=pk)
        mainform = RecipeForm( instance=recipe_instance)
#        formset = ProcessFormSet(Formset_Params)
        formset = ProcessFormSet()

        return render(request, 'recipe/process.html', {"form" : mainform, "formset" : formset, "pk":pk})
    
    elif request.method == "POST" :
        print(" POST ")
        form = RecipeForm(request.POST)
        #if form.is_valid():
        print(print(request.POST.get('title')))
        print(" form is valid ")
        recipe_instance = models.Recipe.objects.get(id=pk)
        formset = ProcessFormSet(request.POST, instance=recipe_instance)
            
        if formset.is_valid():
            print(" form of formset is valid ")
            formset.save()
        #else :
            #print(" Form is invalid") 
                
        return redirect("recettes-recipe")
    else :
        return redirect("recettes-recipe" )

def update_recipe2(request, pk) : 
    Formset_Params = {
    'ingredients_recipe-TOTAL_FORMS' : '1',
    'ingredients_recipe-INITIAL_FORMS' : '0',
    'ingredients_recipe-MIN_NUM_FORMS' : '1', 
    } 

    recipe_instance = models.Recipe.objects.get(id=pk)   
    if request.method ==  "GET":

        mainform = RecipeForm(instance=recipe_instance)
        formset = IngredientFormSet(instance=recipe_instance, )
        print(formset)
        return render(request, 'recipe/update_recipe.html', {"form" : mainform, "formset" : formset , "pk" : pk})

    elif request.method == "POST" :
        print(request.POST.get('title'))
        form = RecipeForm(request.POST, request.FILES,recipe_instance)
        form.instance.author = request.user
        #if form.is_valid():
        #    print(request.POST)
        recipe_instance.title = request.POST.get('title')
        recipe_instance.save(update_fields=['title'])

        formset = IngredientFormSet(request.POST, instance=recipe_instance)
        #formset = IngredientFormSet(request.POST)

            
        #if formset.is_valid():
        formset.save()
        print(formset)
                
        return redirect("update_recipe_process" , pk)
        
    else :
        return render(request, 'recipe/update_recipe.html', {"form" : form})



def update_process(request, pk) : 
    Formset_Params = {
    "process_recipe-TOTAL_FORMS" : '1',
    "process_recipe-INITIAL_FORMS" : '1',
    "process_recipe-MIN_NUM_FORMS" : '1', 
    }    
    recipe_instance = models.Recipe.objects.get(id=pk)
    if request.method ==  "GET":
        print(" GET ")

        mainform = RecipeForm(instance=recipe_instance)
        formset = ProcessFormSet(instance=recipe_instance)
        print(formset)
        return render(request, 'recipe/update_process.html', {"form" : mainform, "formset" : formset, "pk":pk})
    
    elif request.method == "POST" :
        print(request)
        recipe_instance = models.Recipe.objects.get(id=pk)
        form = RecipeForm(request.POST, recipe_instance)
        #if form.is_valid():
        #    print(request.POST)
        #    print(" form is valid ")
        formset = ProcessFormSet(request.POST, instance=recipe_instance)
        #formset = ProcessFormSet(request.POST)
            
        #if formset.is_valid():
        print(" form of formset is valid ")
        formset.save()
        print(formset)
           
        #else :
        #    print(" Form is invalid") 
                
        return redirect("recettes-recipe")
    else :
        return redirect("recettes-recipe" )






def admin_recipe(request) :
    recipes = models.Recipe.objects.all()
    context = {"recipes" : recipes }
    return render(request, 'recipe/recettes_admin.html', context)


class RecipeListView(ListView):
    model = models.Recipe 
    template_name = 'recipe/recettes.html'
    context_object_name = 'recipes'





class RecipeDetailView(DetailView):
    model = models.Recipe

    def function_test():
        return "Test Function"
    
    def total_calorie(self) : 
        '''
        Calculer les totaux des différents attributs des ingrédients présents dans la recette. Les stocker dans un dicionnaire
        '''
        ingredients = models.IngredientRecipe.objects.filter(recipe = self.object)
        quantite_total = 0

        total_calorique = 0 
        total_calorique_kcal = 0 
        total_glucide = 0
        total_sodium = 0

        total_proteins = 0 
        total_fibres = 0 
        total_eau= 0
        total_lipide = 0

        total_sucres = 0
        total_fructose = 0 
        total_galactose = 0 
        total_glucose= 0
        total_lactose = 0
        total_maltose= 0 
        total_saccharose = 0 
        total_amidon= 0

        total_fibresAlimentaires = 0
        total_polyols= 0 
        total_cendres = 0 
        total_alcool= 0
        
        total_acidesOrganiques = 0
        total_AGsatures = 0 
        total_AGmonoinsature = 0 
        total_AGpolyinsature = 0
        total_AGbutyrique = 0
        total_AGcaproique = 0 
        total_AGcaprylique = 0 
        total_AGcaprique = 0

        total_AGlaurique = 0 
        total_AGmyristique = 0
        total_AGpalmitique = 0
        total_AGbstearique = 0 
        total_AGoleique = 0 
        
        total_AGlinoleique = 0 
        total_AGalphalinolenique = 0

        total_AGepa = 0
        total_AGdha = 0

        total_cholesterol = 0 
        total_selchlorure = 0
        total_calcium = 0 
        total_cuivre = 0
        total_fer = 0 
        total_iode = 0 
        total_magnesium = 0
        total_manganese = 0
        total_phosphore = 0
        total_potassium= 0 
        total_selenium = 0 
        total_zinc = 0
        total_retinol= 0
        total_betacarotene = 0

        total_vitamineD = 0
        total_vitamineE = 0 
        total_VitamineK1 = 0 
        total_vitamineK2 = 0
        total_vitamineB1 = 0
        total_vitamineB2 = 0 
        total_vitamineB3 = 0
        total_VitamineB5 = 0 
        total_vitamineB6 = 0
        total_VitamineB9 = 0 
        total_vitamineB12 = 0


        total_fibresAlimentaires = 0
        total_sels_ajoutes = 0
        total_sucres_ajoutes = 0

        Total_graisses_ajoutes = 0
        Total_fruitslegumineuse = 0

        quantite_total = 0.001
        if ingredients.__len__ == 0 :
            quantite_total = 1
            print(ingredients)
            print(" est vide")

        else :
            print(ingredients)
        for ingredient in ingredients : 

            if ingredient.ingredient.forme.name=='sels' :
                total_sels_ajoutes = total_sels_ajoutes + ingredient.quantity 

            if ingredient.ingredient.forme.name=='sucres,miels et assimilés' :
                total_sucres_ajoutes = total_sucres_ajoutes + ingredient.quantity 

            if ingredient.ingredient.famille.name =='matières grasses' :
                Total_graisses_ajoutes = Total_graisses_ajoutes + ingredient.quantity 

            if ingredient.ingredient.famille.name =='fruits, légumes, légumineuses et oléagineux' :
                Total_fruitslegumineuse = Total_fruitslegumineuse + ingredient.quantity 

 
            if isinstance(ingredient.ingredient.energie_kJ, float):
                total_calorique  = total_calorique + ingredient.quantity * (ingredient.ingredient.energie_kJ/100)

            if isinstance(ingredient.ingredient.energie_kcal, float):
                total_calorique_kcal  = total_calorique_kcal + ingredient.quantity * (ingredient.ingredient.energie_kcal/100)
            
            if isinstance(ingredient.ingredient.glucide , float):
                total_glucide  = total_glucide + ingredient.quantity * (ingredient.ingredient.glucide/100)

            if isinstance(ingredient.ingredient.sodium , float):
                total_sodium  = total_sodium + ingredient.quantity * (ingredient.ingredient.sodium/100)


            if isinstance(ingredient.ingredient.energie_kJ, float):
                total_proteins  = total_proteins + ingredient.quantity * (ingredient.ingredient.energie_kJ/100)

            if isinstance(ingredient.ingredient.fibres, float):
                total_fibres  = total_fibres + ingredient.quantity * (ingredient.ingredient.fibres/100)
            
            if isinstance(ingredient.ingredient.eau , float):
                total_eau  = total_eau + ingredient.quantity * (ingredient.ingredient.eau/100)

            if isinstance(ingredient.ingredient.lipide , float):
                total_lipide  = total_lipide + ingredient.quantity * (ingredient.ingredient.lipide/100)



            if isinstance(ingredient.ingredient.sucres, float):
                total_sucres  = total_sucres + ingredient.quantity * (ingredient.ingredient.sucres/100)

            if isinstance(ingredient.ingredient.fructose, float):
                total_fructose  = total_fructose + ingredient.quantity * (ingredient.ingredient.fructose/100)
            
            if isinstance(ingredient.ingredient.galactose , float):
                total_galactose  = total_galactose + ingredient.quantity * (ingredient.ingredient.galactose/100)

            if isinstance(ingredient.ingredient.glucose , float):
                total_glucose  = total_glucose + ingredient.quantity * (ingredient.ingredient.glucose/100)

            if isinstance(ingredient.ingredient.lactose, float):
                total_lactose  = total_lactose + ingredient.quantity * (ingredient.ingredient.lactose/100)

            if isinstance(ingredient.ingredient.maltose, float):
                total_maltose  = total_maltose + ingredient.quantity * (ingredient.ingredient.maltose/100)

            if isinstance(ingredient.ingredient.saccharose, float):
                total_saccharose  = total_saccharose + ingredient.quantity * (ingredient.ingredient.saccharose/100)
            
            if isinstance(ingredient.ingredient.amidon , float):
                total_amidon  = total_amidon + ingredient.quantity * (ingredient.ingredient.amidon/100)

            if isinstance(ingredient.ingredient.fibresALimentraires , float):
                total_fibresAlimentaires  = total_fibresAlimentaires + ingredient.quantity * (ingredient.ingredient.fibresALimentraires/100)

            if isinstance(ingredient.ingredient.polyols, float):
                total_polyols  = total_polyols + ingredient.quantity * (ingredient.ingredient.polyols/100)


            if isinstance(ingredient.ingredient.cendres , float):
                total_cendres  = total_cendres + ingredient.quantity * (ingredient.ingredient.cendres/100)

            if isinstance(ingredient.ingredient.alcool , float):
                total_alcool  = total_alcool + ingredient.quantity * (ingredient.ingredient.alcool/100)

            if isinstance(ingredient.ingredient.acidesOrganiques, float):
                total_acidesOrganiques  = total_acidesOrganiques + ingredient.quantity * (ingredient.ingredient.acidesOrganiques/100)


            if isinstance(ingredient.ingredient.AGsatures, float):
                total_AGsatures  = total_AGsatures + ingredient.quantity * (ingredient.ingredient.AGsatures/100)

            if isinstance(ingredient.ingredient.AGmonoinsature, float):
                total_AGmonoinsature  = total_AGmonoinsature + ingredient.quantity * (ingredient.ingredient.AGmonoinsature/100)

            if isinstance(ingredient.ingredient.AGpolyinsature, float):
                total_AGpolyinsature  = total_AGpolyinsature + ingredient.quantity * (ingredient.ingredient.AGpolyinsature/100)
            
            if isinstance(ingredient.ingredient.AGbutyrique , float):
                total_AGbutyrique  = total_AGbutyrique + ingredient.quantity * (ingredient.ingredient.AGbutyrique/100)

            if isinstance(ingredient.ingredient.AGcaproique , float):
                total_AGcaproique  = total_AGcaproique + ingredient.quantity * (ingredient.ingredient.AGcaproique/100)

            if isinstance(ingredient.ingredient.AGcaprylique, float):
                total_AGcaprylique  = total_AGcaprylique + ingredient.quantity * (ingredient.ingredient.AGcaprylique/100)

            if isinstance(ingredient.ingredient.AGcaprique , float):
                total_AGcaprique  = total_AGcaprique + ingredient.quantity * (ingredient.ingredient.AGcaprique/100)

            if isinstance(ingredient.ingredient.AGlaurique , float):
                total_AGlaurique  = total_AGlaurique + ingredient.quantity * (ingredient.ingredient.AGlaurique/100)

            if isinstance(ingredient.ingredient.AGmyristique, float):
                total_AGmyristique  = total_AGmyristique + ingredient.quantity * (ingredient.ingredient.AGmyristique/100)

            if isinstance(ingredient.ingredient.AGpalmitique , float):
                total_AGpalmitique  = total_AGpalmitique + ingredient.quantity * (ingredient.ingredient.AGpalmitique/100)

            if isinstance(ingredient.ingredient.AGbstearique, float):
                total_AGbstearique  = total_AGbstearique + ingredient.quantity * (ingredient.ingredient.AGbstearique/100)

            if isinstance(ingredient.ingredient.AGoleique , float):
                total_AGoleique  = total_AGoleique + ingredient.quantity * (ingredient.ingredient.AGoleique/100)

            if isinstance(ingredient.ingredient.AGlinoleique , float):
                total_AGlinoleique  = total_AGlinoleique + ingredient.quantity * (ingredient.ingredient.AGlinoleique/100)

            if isinstance(ingredient.ingredient.AGalphalinolenique , float):
                total_AGalphalinolenique  = total_AGalphalinolenique + ingredient.quantity * (ingredient.ingredient.sodium/100)

            if isinstance(ingredient.ingredient.AGepa, float):
                total_AGepa  = total_AGepa + ingredient.quantity * (ingredient.ingredient.AGepa/100)

            if isinstance(ingredient.ingredient.AGdha, float):
                total_AGdha  = total_AGdha + ingredient.quantity * (ingredient.ingredient.AGdha/100)

            if isinstance(ingredient.ingredient.cholesterol, float):
                total_cholesterol  = total_cholesterol + ingredient.quantity * (ingredient.ingredient.cholesterol/100)

            if isinstance(ingredient.ingredient.selchlorure , float):
                total_selchlorure  = total_selchlorure + ingredient.quantity * (ingredient.ingredient.selchlorure/100)

            if isinstance(ingredient.ingredient.calcium, float):
                total_calcium  = total_calcium + ingredient.quantity * (ingredient.ingredient.calcium/100)

            if isinstance(ingredient.ingredient.cuivre, float):
                total_cuivre  = total_cuivre + ingredient.quantity * (ingredient.ingredient.cuivre/100)

            if isinstance(ingredient.ingredient.fer , float):
                total_fer  = total_fer + ingredient.quantity * (ingredient.ingredient.fer/100)

            if isinstance(ingredient.ingredient.iode , float):
                total_iode  = total_iode + ingredient.quantity * (ingredient.ingredient.iode/100)

            if isinstance(ingredient.ingredient.magnesium, float):
                total_magnesium  = total_magnesium + ingredient.quantity * (ingredient.ingredient.magnesium/100)



            if isinstance(ingredient.ingredient.manganese, float):
                total_manganese  = total_manganese + ingredient.quantity * (ingredient.ingredient.manganese/100)

            if isinstance(ingredient.ingredient.phosphore , float):
                total_phosphore  = total_phosphore + ingredient.quantity * (ingredient.ingredient.phosphore/100)

            if isinstance(ingredient.ingredient.potassium, float):
                total_potassium  = total_potassium + ingredient.quantity * (ingredient.ingredient.potassium/100)

            if isinstance(ingredient.ingredient.selenium , float):
                total_selenium  = total_selenium + ingredient.quantity * (ingredient.ingredient.selenium/100)

            if isinstance(ingredient.ingredient.zinc , float):
                total_zinc  = total_zinc + ingredient.quantity * (ingredient.ingredient.zinc/100)

            if isinstance(ingredient.ingredient.retinol, float):
                total_retinol  = total_retinol + ingredient.quantity * (ingredient.ingredient.retinol/100)

            if isinstance(ingredient.ingredient.betaCarotene , float):
                total_betacarotene  = total_betacarotene + ingredient.quantity * (ingredient.ingredient.betaCarotene/100)

            if isinstance(ingredient.ingredient.vitamineD , float):
                total_vitamineD  = total_vitamineD + ingredient.quantity * (ingredient.ingredient.vitamineD/100)

            if isinstance(ingredient.ingredient.vitamineE, float):
                total_vitamineE  = total_vitamineE + ingredient.quantity * (ingredient.ingredient.vitamineE/100)
            if isinstance(ingredient.ingredient.VitamineK1 , float):
                total_VitamineK1  = total_VitamineK1 + ingredient.quantity * (ingredient.ingredient.VitamineK1/100)

            if isinstance(ingredient.ingredient.vitamineK2 , float):
                total_vitamineK2  = total_vitamineK2 + ingredient.quantity * (ingredient.ingredient.vitamineK2/100)

            if isinstance(ingredient.ingredient.vitamineB1, float):
                total_vitamineB1  = total_vitamineB1 + ingredient.quantity * (ingredient.ingredient.vitamineB1/100)

            
            if isinstance(ingredient.ingredient.vitamineB2, float):
                total_vitamineB2  = total_vitamineB2 + ingredient.quantity * (ingredient.ingredient.vitamineB2/100)

#####vitamineB2

            if isinstance(ingredient.ingredient.VitamineB3 , float):
                total_vitamineB3  = total_vitamineB3 + ingredient.quantity * (ingredient.ingredient.VitamineB3/100)

            if isinstance(ingredient.ingredient.vitamineB5 , float):
                total_VitamineB5  = total_VitamineB5 + ingredient.quantity * (ingredient.ingredient.vitamineB5/100)

            if isinstance(ingredient.ingredient.vitamineB9, float):
                total_vitamineB6  = total_vitamineB6 + ingredient.quantity * (ingredient.ingredient.vitamineB6/100)
            if isinstance(ingredient.ingredient.glucide , float):
                total_VitamineB9  = total_VitamineB9 + ingredient.quantity * (ingredient.ingredient.vitamineB9/100)
#Changing V to V
            if isinstance(ingredient.ingredient.VitamineB12 , float):
                total_vitamineB12  = total_vitamineB12 + ingredient.quantity * (ingredient.ingredient.VitamineB12/100)

                
            if isinstance(ingredient.quantity, float):
                quantite_total  = quantite_total + ingredient.quantity 
 
            total_AG_trans = total_AGsatures +  total_AGbutyrique + total_AGcaproique + total_AGcaprylique + total_AGcaprique + total_AGlaurique
            + total_AGmyristique + total_AGpalmitique + total_AGbstearique + total_AGoleique + total_AGlinoleique + total_AGalphalinolenique
            + total_AGepa + total_AGdha

            total_AG_insatures = total_AGmonoinsature + total_AGpolyinsature

            total_AG = total_AG_trans + total_AG_insatures + total_AGsatures
            total_VitamineK = total_VitamineK1 + total_vitamineK2

        return {"total_calorique" : total_calorique / quantite_total, "total_calorique_kcal" : total_calorique_kcal/quantite_total,
                "total_glucide" : total_glucide / quantite_total, "total_sodium" : total_sodium / quantite_total, 
                "total_proteins" : total_proteins / quantite_total, "total_fibres" : total_fibres / quantite_total, 
                "total_eau" : total_eau / quantite_total, "total_sodium" : total_sodium / quantite_total, 
                "total_lipide" : total_lipide / quantite_total, "total_sucres" : total_sucres / quantite_total, 
                "total_fructose" : total_fructose / quantite_total, "total_galactose" : total_galactose / quantite_total, 
                "total_glucose" : total_glucose / quantite_total, "total_lactose" : total_lactose / quantite_total, 
                "total_maltose" : total_maltose / quantite_total, "total_saccharose" : total_saccharose / quantite_total, 
                "total_amidon" : total_amidon / quantite_total, "total_fibresAlimentaires" : total_fibresAlimentaires / quantite_total, 
                "total_polyols" : total_polyols / quantite_total, "total_cendres" : total_cendres / quantite_total, 
                "total_alcool" : total_alcool / quantite_total, "total_acidesOrganiques" : total_acidesOrganiques / quantite_total, 
                "total_AGsatures" : total_AGsatures / quantite_total, "total_AGmonoinsature" : total_AGmonoinsature / quantite_total, 
                "total_AGpolyinsature" : total_AGpolyinsature / quantite_total, "total_AGbutyrique" : total_AGbutyrique / quantite_total, 
                "total_AGcaproique" : total_AGcaproique / quantite_total, "total_AGcaprylique" : total_AGcaprylique / quantite_total, 
                "total_AGcaprique" : total_AGcaprique / quantite_total, "total_AGlaurique" : total_AGlaurique / quantite_total, 
        
                "total_AGmyristique" : total_AGmyristique / quantite_total, "total_AGpalmitique" : total_AGpalmitique / quantite_total, 

                "total_AGbstearique" : total_AGbstearique / quantite_total, "total_AGoleique" : total_AGoleique / quantite_total, 

                "total_AGlinoleique" : total_AGlinoleique / quantite_total, "total_AGalphalinolenique" : total_AGalphalinolenique / quantite_total, 

                        
                "total_AGepa" : total_AGepa / quantite_total, "total_AGdha" : total_AGdha / quantite_total, "total_cholesterol" : total_cholesterol / quantite_total, 

                "total_selchlorure" : total_selchlorure / quantite_total, "total_cuivre" : total_cuivre / quantite_total, 

                "total_fer" : total_fer / quantite_total, "total_iode" : total_iode / quantite_total, 

                "total_magnesium" : total_magnesium / quantite_total, "total_manganese" : total_manganese / quantite_total, "total_calcium" : total_calcium / quantite_total, 

                "total_phosphore" : total_phosphore / quantite_total, "total_potassium" : total_potassium / quantite_total, 

                "total_selenium" : total_selenium / quantite_total, "total_zinc" : total_zinc / quantite_total, 
                
                "total_retinol" : total_retinol / quantite_total, "total_betacarotene" : total_betacarotene / quantite_total, 

                "total_vitamineD" : total_vitamineD / quantite_total, "total_vitamineE" : total_vitamineE / quantite_total, 

                "total_VitamineK1" : total_VitamineK1 / quantite_total, "total_vitamineK2" : total_vitamineK2 / quantite_total, 


                "total_vitamineK" : total_VitamineK / quantite_total, 

                    
                "total_vitamineB1" : total_vitamineB1 / quantite_total, "total_vitamineB2" : total_vitamineB2 / quantite_total, 

                "total_vitamineB3" : total_vitamineB3 / quantite_total, "total_VitamineB5" : total_VitamineB5 / quantite_total, 

                "total_vitamineB6" : total_vitamineB6 / quantite_total, "total_VitamineB9" : total_VitamineB9 / quantite_total,  

                "total_VitamineB12" : total_vitamineB12 / quantite_total,   "total_sels_ajoutes" : total_sels_ajoutes / quantite_total , 
                 
                "total_sucres_ajoutes" : total_sucres_ajoutes / quantite_total, "total_graisses_ajoutes" : Total_graisses_ajoutes / quantite_total, "total_fruitslegumineuse" : Total_fruitslegumineuse / quantite_total ,
                "total_AG" : total_AG, "total_AG_insatures" : total_AG_insatures, "total_AG_trans" : total_AG_trans, "Quantite_totale" : quantite_total}


    def score_calorie_kj(self, total_calorique) : 
        '''Calculer un score selon le total obtenu'''
        score = (total_calorique - 0.1) // 335
        if score < 10 : 
            return score
        else :
            return 10 


    def score_sodium(self, total_sodium) : 
        score = (total_sodium - 0.1) // 90
        if score < 10 : 
            return score
        else :
            return 10 

    def score_glucide(self, total_glucide) : 
        ''' Calculer score de glucide '''
        score = (total_glucide - 0.01) // 4.5
        if score < 10 : 
            return score
        else :
            return 10 

    def score_agsature(self, total_agsature) : 
        ''' Calculer score d'acides gras saturés '''
        score = (total_agsature - 0.1) // 1
        if score < 10 : 
            return score
        else :
            return 10 

    def score_protein(self, total_protein) : 
        ''' Calculer score de protein '''
        score = (total_protein - 0.01) // 1.6
        if score < 5 : 
            return score
        else :
            return 5 

    def score_fibre(self, total_fibre) : 
        ''' Calculer score de fibres '''
        score = (total_fibre - 0.01) // 0.9
        if score < 5 : 
            return score
        else :
            return 5 


    def score_fln(self,total_graisse, total_fruitslegumes) : 
        ''' Calculer score de fruit légumes et légumineuse '''
        score = total_graisse + total_fruitslegumes
        return score

    def score_A(self, pts_kj, pts_glucide, pts_agsatures, pts_sodium) : 
        ''' Calculer score A '''
        score =  pts_kj + pts_glucide + pts_agsatures + pts_sodium
        return score

    def nutriscore(self, scoreA, pts_fln, pts_prot, pts_fib):
        ''' Attribuer un nutriscore selon les scores calculés'''
        if (scoreA < 11 and scoreA > 0) or (scoreA >= 11 and pts_fln == 5) : 
            return scoreA - (pts_prot + pts_fln)

        else :
            return scoreA - (pts_fln + pts_fib)

    def nutriscoreLettre(self, nutriscore):
        if nutriscore < 0 : 
            return "Nutriscore A"
        elif nutriscore < 3 :
            return "Nutriscore B"
        elif nutriscore < 11 :
            return "Nutriscore C"  
        elif nutriscore < 19 :
            return "Nutriscore D"
        else :
            return "Nutriscore E"
    
####################################################################################################################    
#
#           Calcul des allegations 
#
####################################################################################################################
    def allegation(self, total_cal, total_graisse, total_ag_saturee,
     total_ag_trans, total_ag, total_sucres, total_sucres_ajoutes, total_sel, total_sel_ajoute, 
     total_fibre, total_protein, total_graisses_monoinsatures, total_graisses_polyinsatures,
     total_selenium,  total_magnesium, total_phosphore, total_calcium, total_cuivre, total_fer, 
     total_manganese, total_potassium, total_zinc, total_vitamineD, total_vitamineE,
     total_vitamineK, total_vitamineB1,  total_vitamineB2, total_vitamineB3, total_vitamineB5, 
     total_vitamineB6, total_vitamineB9, total_vitamineB12, total_AGepa, total_dha, total_AGalphalinolenique  ) : 
        '''faire une allégation selon les valeurs des différents totaux'''
        allegations = []
        allegations_minerales = []

        total_cal = 0.001

        if total_cal < 170 : 
            allegations.append('Faible en valeur énergétique' )
        elif total_cal < 17 : 
            allegations.append('Sans apport energetique')

        #ajouter acide gras trans  
        if total_graisse < 3 :
            allegations.append ('faible teneur en matières grasses')
        
        elif total_graisse < 0.5 :
            allegations.append ('sans matières grasses' )
        
        #à voir avec le client    
        if total_ag_saturee + total_ag_trans < 1.5 :
            allegations.append ('faible teneur en graisses saturees')

        elif total_ag_saturee + total_ag_trans < 0.1 :
            allegations.append ('faible teneur en graisses saturees')    
        
        if total_sucres_ajoutes < 5 :
            allegations.append ('faible teneur en sucres')

        elif total_sucres_ajoutes < 0.5 :
            allegations.append ('sans sucres')

        #à voir avec le client 
        #if total_sucres_ajoutes < 0.5 :
        #    allegations.append ({'sans sucres ajoutes' : total_sucres})    
        
        if total_sel + total_sel_ajoute < 0.12 :
            allegations.append ('pauvre en sel')   

        elif total_sel + total_sel_ajoute < 0.04 :
            allegations.append ('tres pauvre en sel')    
        
        elif total_sel + total_sel_ajoute< 0.005 :
            allegations.append ('sans sodium')   

        #if total_sel + total_sel_ajoute< 0.005 :
        #    allegations.append ({'sans sodium ajouté' : total_sel})  

        #a voir avec le client
        if total_fibre > 3 :
            allegations.append ('source de fibres')    

        elif total_fibre > 6 :
            allegations.append ('riche en fibres')

        #a voir avec le client
        if total_cal > 0 : 
            if total_protein * 4 / total_cal > 0.12 :
                allegations.append ('source de proteins')

            elif total_protein * 4 / total_cal > 0.20 :
                allegations.append ('riche en proteins')


        ### 22, 23, 24 
        if total_AGalphalinolenique > 0.3 or (total_AGepa + total_dha > 40) : 
            allegations.append ('source d acide gras omega3')

        elif total_AGalphalinolenique > 0.6 or (total_AGepa + total_dha > 80) : 
            allegations.append ('riche en acide gras omega3')

        total_acide_gras = total_graisses_monoinsatures + total_graisses_polyinsatures + total_ag_saturee

        if total_acide_gras > 0 :

            if (total_graisses_monoinsatures / total_acide_gras > 0.45 and total_graisses_monoinsatures * 37 > 0.2 * total_cal) : 
                allegations.append ('riche en graisse monoinsaturees')

            if (total_graisses_polyinsatures / total_acide_gras  > 0.45 and total_graisses_polyinsatures > 0.2 * total_cal) : 
                allegations.append ('riche en graisse polyinsaturees')

            if ( total_graisses_polyinsatures + total_graisses_monoinsatures / total_acide_gras ) > 0.7  : 
                allegations.append ('riche en graisse insaturees')






        if total_selenium > 8.25 : 
            allegations.append('source de selenium')
        elif total_selenium > 16.5 : 
            allegations.append('riche en selenium')

        if total_magnesium > 0.056 : 
            allegations.append('source de magnesium')
        elif total_magnesium > 0.112 : 
            allegations.append('riche en magnesium')

        if total_phosphore > 0.105 : 
            allegations.append('source de phosphore')
        elif total_phosphore > 0.210 : 
            allegations.append('riche en phosphore')

        if total_calcium > 120 : 
            allegations.append('source de calcium')
        elif total_calcium > 240 : 
            allegations.append('riche en selenium')

        if total_cuivre > 0.15 : 
            allegations.append('source de cuivre')
        elif total_cuivre > 0.30 : 
            allegations.append('riche en cuivre')

        if total_fer > 2.1 : 
            allegations.append('source de fer')
        elif total_fer > 4.2 : 
            allegations.append('riche en fer')

        if total_manganese > 0.3 : 
            allegations.append('source de manganese')
        elif total_manganese > 0.6 : 
            allegations.append('riche en manganese')

        if total_potassium > 300 : 
            allegations.append('source de potassium')
        elif total_potassium > 600 : 
            allegations.append('riche en potassium')    

        if total_zinc > 1.5 : 
            allegations.append('source de zinc')
        elif total_zinc > 3 : 
            allegations.append(['riche en zinc'])

        if total_vitamineD > 0.75 : 
            allegations.append(['source de vitamine D'])
        elif total_vitamineD > 1.5 : 
            allegations.append(['riche en vitamine D'])

        if total_vitamineE > 1.8 : 
            allegations.append(['source de vitamine E'])
        elif total_vitamineE > 1.8 : 
            allegations.append(['riche en vitamine E'])
            
        if total_vitamineK > 1.8 : 
            allegations.append(['source de vitamine K'])
        elif total_vitamineK > 1.8 : 
            allegations.append(['riche en vitamine K'])            
            
        if total_vitamineB1 > 0.165 : 
            allegations.append(['source de vitamine B1'])
        elif total_vitamineB1 > 0.33 : 
            allegations.append(['riche en vitamine B1'])     

        if total_vitamineB2 > 0.21 : 
            allegations.append(['source de vitamine B2'])
        elif total_vitamineB2 > 0.42 : 
            allegations.append(['riche en vitamine B2'])     


        if total_vitamineB3 > 2.4 : 
            allegations.append(['source de vitamine B2'])
        elif total_vitamineB3 > 4.2 : 
            allegations.append(['riche en vitamine B2'])     

        if total_vitamineB5 > 0.9 : 
            allegations.append(['source de vitamine B5'])
        elif total_vitamineB5 > 1.8 : 
            allegations.append(['riche en vitamine B5'])     

        if total_vitamineB6 > 0.21 : 
            allegations.append(['source de vitamine B6'])
        elif total_vitamineB6 > 0.42 : 
            allegations.append(['riche en vitamine B6'])

        if total_vitamineB9 > 30 : 
            allegations.append(['source de vitamine B9'])
        elif total_vitamineB9 > 60 : 
            allegations.append(['riche en vitamine B9'])

        if total_vitamineB12 > 0.375 : 
            allegations.append(['source de vitamine B12'])
        elif total_vitamineB12 > 0.75: 
            allegations.append(['riche en vitamine B12'])

        return allegations



    def get_context_data(self, **kwargs):

        nutriscore_couleur = {"Nutriscore A" : "Vert", "Nutriscore B" : "Vert_clair", "Nutriscore C" : "Jaune", "Nutriscore D" : "Orange Clair", "Nutriscore E" : "Orange Foncé", }

        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        #context['ingredients'] = models.IngredientRecipe.objects.all()

        #Calculer score fln
        ingredient_Recipe = models.IngredientRecipe.objects.filter(recipe = self.object)
        process_Recipe = models.ProcessRecipe.objects.filter(recipe = self.object)


        '''for i in range(len(ingredient_Recipe)) : 
            if ingredient_Recipe[i].recipe.famille == models.Famille.objects.get(name = 'viandes, œufs, poissons et assimilés'):
                score_fln = score_fln + ingredient_Recipe[i].quantity
        '''



        context['ingredients'] = ingredient_Recipe
        context['process'] = process_Recipe

        totaux = self.total_calorie()

###########################################################################################
#
#   Envoi des quantites calculees au front end
#
############################################################################################

        context['total_calorie'] = totaux["total_calorique"]
        context['quantite_totale'] = totaux["Quantite_totale"]
        context['inv_quantite_totale'] = 1/totaux["Quantite_totale"]
        context['total_calorie_kcal'] = totaux["total_calorique_kcal"]


        context['total_glucide'] = round(totaux["total_glucide"],2)
        context['total_sodium'] = totaux["total_sodium"]

        context['total_protein'] = totaux['total_proteins']
        context['total_fibre'] = round(totaux["total_fibres"],5)
        context['total_eau'] = round(totaux["total_eau"],2)
        context['total_lipide'] = round(totaux["total_lipide"],2)

        context['total_sucres'] = totaux['total_sucres']
        context['total_fructose'] = round(totaux["total_fructose"],5)
        context['total_galactose'] = round(totaux["total_galactose"],2)
        context['total_glucose'] = round(totaux["total_glucose"],2)
        context['total_lactose'] = totaux['total_lactose']
        context['total_maltose'] = round(totaux["total_maltose"],5)
        context['total_saccharose'] = round(totaux["total_saccharose"],2)
        context['total_amidon'] = round(totaux["total_amidon"],2)
        context['total_fibresAlimentaires'] = round(totaux["total_fibresAlimentaires"],2)

        context['total_polyols'] = totaux['total_polyols']
        context['total_cendres'] = round(totaux["total_cendres"],5)
        context['total_alcool'] = round(totaux["total_alcool"],2)
        context['total_acidesOrganiques'] = round(totaux["total_acidesOrganiques"],2)
        context['total_AGsatures'] = totaux['total_AGsatures']
        context['total_AGmonoinsature'] = round(totaux["total_AGmonoinsature"],5)
        context['total_AGpolyinsature'] = round(totaux["total_AGpolyinsature"],2)
        context['total_AGbutyrique'] = round(totaux["total_AGbutyrique"],2)
        context['total_AGcaproique'] = round(totaux["total_AGcaproique"],2)
        context['total_AGcaprylique'] = totaux['total_AGcaprylique']

        context['total_AGlaurique'] = round(totaux["total_AGlaurique"],5)
        context['total_AGmyristique'] = round(totaux["total_AGmyristique"],2)
        context['total_AGbutyrique'] = round(totaux["total_AGbutyrique"],2)
        context['total_AGpalmitique'] = round(totaux["total_AGpalmitique"],2)
        context['total_AGbstearique'] = round(totaux["total_AGbstearique"],2)
        context['total_AGoleique'] = round(totaux["total_AGoleique"],2)
        context['total_AGlinoleique'] = round(totaux["total_AGlinoleique"],2)
        context['total_AGalphalinolenique'] = round(totaux["total_AGalphalinolenique"],2)

        context['total_AGepa'] = round(totaux["total_AGepa"],5)
        context['total_AGdha'] = round(totaux["total_AGdha"],2)

        context['total_cholesterol'] = round(totaux["total_cholesterol"],2)
        context['total_selchlorure'] = round(totaux["total_selchlorure"],2)
        context['total_calcium'] = round(totaux["total_calcium"],2)
        context['total_cuivre'] = round(totaux["total_cuivre"],2)
        context['total_fer'] = round(totaux["total_fer"],2)
        context['total_iode'] = totaux['total_iode']
        context['total_magnesium'] = round(totaux["total_magnesium"],2)
        context['total_manganese'] = round(totaux["total_manganese"],2)
        context['total_phosphore'] = round(totaux["total_phosphore"],2)
        context['total_potassium'] = round(totaux["total_potassium"],2)
        context['total_selenium'] = round(totaux["total_selenium"],2)
        context['total_zinc'] = round(totaux["total_zinc"],2)
        context['total_retinol'] = round(totaux["total_retinol"],2)
        context['total_betacarotene'] = round(totaux["total_betacarotene"],2)
    


        context['total_phosphore'] = round (totaux["total_phosphore"], 3)
        context['total_selenium'] = round(totaux["total_zinc"],5)
        context['total_VitamineK1'] = round(totaux["total_VitamineK1"],2)
        context['total_vitamineK2'] = totaux["total_vitamineK2"]
        context['total_vitamineB1'] = totaux['total_vitamineB1']
        context['total_vitamineB2'] = round (totaux["total_vitamineB2"], 3)
        context['total_vitamineB3'] = round(totaux["total_vitamineB3"],5)
    
        context['total_VitamineB5'] = totaux['total_VitamineB5']
        context['total_VitamineB9'] = round (totaux["total_VitamineB9"], 3)
        context['total_VitamineB12'] = round(totaux["total_VitamineB12"],5)
    

        context['total_sels_ajoutes'] = totaux['total_sels_ajoutes']
        context['total_sucres_ajoutes'] = round (totaux["total_sucres_ajoutes"], 3)
        context['Total_graisses_ajoutes'] = totaux['total_graisses_ajoutes']
        context['Total_fruitslegumineuse'] = round (totaux["total_fruitslegumineuse"], 3)

    

        #get the total_fln quantite des ingredients appartenant a fruits, légumes ou légumineuses
        #context['total_fln'] = totaux['total_protein']


        score_kj = self.score_calorie_kj(totaux["total_calorique"])
        score_sodium = self.score_sodium(totaux["total_sodium"])
        score_glucide = self.score_glucide(totaux["total_glucide"])
        score_agsatures = self.score_agsature(totaux["total_AGsatures"])
        score_protein = self.score_protein(totaux["total_proteins"])
        score_fibre = self.score_fibre(totaux["total_fibres"])
        score_fln = self.score_fln(totaux["total_graisses_ajoutes"], totaux["total_fruitslegumineuse"])

        scoreA = self.score_A(score_kj, score_glucide, score_agsatures, score_sodium)
        nutriscore = self.nutriscore(scoreA, score_fln, score_protein, score_fibre)  

        context['Score_sodium'] = score_sodium
        context['Score_glucide'] = score_glucide
        context['score_AGsatures'] = score_agsatures
        context['score_protein'] = score_protein
        context['score_fibre'] = score_fibre
        context['score_fln'] = score_fln
        context['score_A'] = scoreA
        context['Score_calorie_kcal'] = 0        


        context['nutriscore'] = self.nutriscoreLettre(nutriscore)
        context['couleur'] = nutriscore_couleur[context['nutriscore']]
        context['allegation'] = self.allegation(totaux["total_calorique"], totaux["total_graisses_ajoutes"], totaux["total_AGsatures"], totaux["total_AG_trans"],  totaux["total_AG"], totaux["total_sucres"],
                                totaux["total_sucres_ajoutes"], totaux["total_sodium"], totaux["total_sels_ajoutes"], totaux["total_fibres"], totaux["total_proteins"], totaux["total_AGmonoinsature"], totaux["total_AGpolyinsature"], 
                                totaux["total_selenium"], totaux["total_magnesium"], totaux["total_phosphore"], totaux["total_calcium"], totaux["total_cuivre"], totaux["total_fer"], totaux["total_manganese"], totaux["total_potassium"], totaux["total_zinc"], 
                                totaux["total_vitamineD"], totaux["total_vitamineE"], totaux["total_vitamineK"], totaux["total_vitamineB1"],  totaux["total_vitamineB2"], totaux["total_vitamineB3"], totaux["total_VitamineB5"], totaux["total_vitamineB6"], totaux["total_VitamineB9"],
                                totaux["total_VitamineB12"], totaux["total_AGepa"], totaux["total_AGdha"], totaux["total_AGalphalinolenique"] )

    
        return context

    



    
class RecipeCreateView(CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'cook_time']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
#class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):


    
    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recettes-recipe')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    
    
''' LES INGREDIENTS'''
class IngredientListView(ListView):
    model = models.Ingredient 
    template_name = 'ingredients/ingredients.html'
    context_object_name = 'ingredients_app'
    paginate_by = 100


class IngredientDetailView(DetailView):
    model = models.Ingredient
    template_name = 'ingredients/ingredient_detail.html'
    
class IngredientCreateView(CreateView):
    model = models.Ingredient
    template_name = 'ingredients/ingredient_form.html'
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class IngredientUpdateView(UpdateView):
    model = models.Ingredient
    template_name = 'ingredients/ingredient_form.html'
    fields = '__all__'

    
class IngredientDeleteView(DeleteView):
    model = models.Ingredient
    template_name = 'ingredients/ingredient_confirm_delete.html'
    success_url = reverse_lazy('ingredients-recipe')
    
    

    '''def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author'''

    
    
    
''' Les familles'''
class FamilleListView(ListView):
    model = models.Famille 
    template_name = 'familles/familles.html'
    context_object_name = 'familles_app'
    paginate_by = 100


class FamilleDetailView(DetailView):
    model = models.Famille
    template_name = 'familles/famille_detail.html'
    
class FamilleCreateView(CreateView):
    model = models.Famille
    template_name = 'familles/famille_form.html'
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class FamilleUpdateView(UpdateView):
    model = models.Famille
    template_name = 'familles/famille_form.html'
    fields = '__all__'

    
class FamilleDeleteView(DeleteView):
    model = models.Famille
    template_name = 'familles/famille_confirm_delete.html'
    success_url = reverse_lazy('familles-recipe')
    
    

    '''def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author'''



def test_cascade(request):
    ingredientsObj = models.Ingredient.objects.all()
    famillesObj = models.Famille.objects.all()
    context  = { 'familles' : famillesObj,'ingredients' : ingredientsObj}
    return render(request, 'recipe/test_cascade.html', context)


def ingredient_create_view(request):
    form = IngredientForm()
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'recipe/test_cascade.html', {'form': form})

# AJAX
def load_ingredient(request):
    print(request)
    forme_id = request.GET.get('forme_id')
    print("forme_id", forme_id)
    forme = models.Forme.objects.get(id = forme_id)
    print("forme", forme)
    ingredients = forme.forme_ingredient.all().order_by('name')
    print("ingredients", ingredients)
    return render(request, 'recipe/ingredient_dropdown_list_options.html', {'ingredients_famille': ingredients})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def load_forme(request):
    famille_id = request.GET.get('famille_id')
    famille = models.Famille.objects.get(pk = famille_id)
    formes = famille.forme_famille.all().order_by('name')
    return render(request, 'recipe/forme_dropdown_list_options.html', {'formes_famille': formes})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)



    