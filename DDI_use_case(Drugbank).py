#!/usr/bin/env python
# coding: utf-8


from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import sys

# Select DDI of Hydroxychloroquine between all drugs of covid

#DB01611     Hydroxychloroquine
#DB01593     Zinc
#DB00608     Chloroquine


query1 = """
select distinct ?Drug1CUI ?drugLabel1 ?Drug1 ?Drug2CUI ?drugLabel2 ?Drug2 ?Impact ?Effect
 where {
        ?DrugDrugInteraction a <http://covid-19.tib.eu/vocab/DrugDrugInteraction>.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasImpact> ?Impact.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasEffect> ?Effect.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/affects> ?Drug1.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/isAffected> ?Drug2.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug1CUI> ?Drug1CUI.
        ?Annotation1 <http://covid-19.tib.eu/vocab/hasAnnotation> ?Drug1CUI.
        ?Annotation1 <http://covid-19.tib.eu/vocab/annotates> ?Publication1.
        ?COVIDAnnotation1 a <http://covid-19.tib.eu/vocab/COVID_Annotation>.
        ?COVIDAnnotation1 <http://covid-19.tib.eu/vocab/annotates> ?Publication1.
        ?Drug1CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel1.

        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug2CUI> ?Drug2CUI.        
        ?Annotation2 <http://covid-19.tib.eu/vocab/hasAnnotation> ?Drug2CUI.        
        ?Annotation2 <http://covid-19.tib.eu/vocab/annotates> ?Publication2.        
        ?COVIDAnnotation2 a <http://covid-19.tib.eu/vocab/COVID_Annotation>.
        ?COVIDAnnotation2 <http://covid-19.tib.eu/vocab/annotates> ?Publication2.
        ?Drug2CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel2.
        FILTER (?drugLabel1 != ?drugLabel2)
        Filter (?Drug2 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>,
                <http://covid-19.tib.eu/vocab/DB00608>))
}
"""


# # Antihypertensive: Beta-blockers

#DB01611     Hydroxychloroquine
#DB01593    Zinc
#DB00608     Chloroquine

#'DB00335'  #atenolol
#'DB01197'  Captopril
#'DB01193'  Acebutolol
#'DB00571'  Propranolol
#'DB00195'  betaxolol 
#'DB00612'  bisoprolol 
#DB00999    hydrochlorothiazide
#DB00264   Metoprolol
#DB01203   nadolol 
#DB00960   pindolol 
#DB00489   Sotalol
#DB00373  timolol 
query2 = """select distinct ?Drug1CUI ?drugLabel1 ?Drug1 ?Drug2CUI ?drugLabel2 ?Drug2 ?Impact ?Effect
 where {
        ?DrugDrugInteraction a <http://covid-19.tib.eu/vocab/DrugDrugInteraction>.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasImpact> ?Impact.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasEffect> ?Effect.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/affects> ?Drug1.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/isAffected> ?Drug2.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug1CUI> ?Drug1CUI.
        ?Drug1CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel1.

        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug2CUI> ?Drug2CUI.        
        ?Drug2CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel2.
        FILTER (?drugLabel1 != ?drugLabel2)
        Filter (?Drug1 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>, <http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB00335>, <http://covid-19.tib.eu/vocab/DB01193>, <http://covid-19.tib.eu/vocab/DB00571>,
<http://covid-19.tib.eu/vocab/DB00195>, <http://covid-19.tib.eu/vocab/DB00612>, <http://covid-19.tib.eu/vocab/DB00264>,
<http://covid-19.tib.eu/vocab/DB01203>, <http://covid-19.tib.eu/vocab/DB00960>, <http://covid-19.tib.eu/vocab/DB00489>,
<http://covid-19.tib.eu/vocab/DB00373>))

        Filter (?Drug2 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>, <http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB00335>, <http://covid-19.tib.eu/vocab/DB01193>, <http://covid-19.tib.eu/vocab/DB00571>,
<http://covid-19.tib.eu/vocab/DB00195>, <http://covid-19.tib.eu/vocab/DB00612>, <http://covid-19.tib.eu/vocab/DB00264>,
<http://covid-19.tib.eu/vocab/DB01203>, <http://covid-19.tib.eu/vocab/DB00960>, <http://covid-19.tib.eu/vocab/DB00489>,
<http://covid-19.tib.eu/vocab/DB00373>))
}"""


# # Antihypertensive: Angiotensin converting enzyme (ACE) inhibitors

#DB01611     Hydroxychloroquine
#DB01593    Zinc
#DB00608     Chloroquine

#'DB00542'  #benazepril 
#'DB01197'  Captopril
#'DB00584'  #enalapril
#'DB00492'  Fosinopril
#'DB00722'  lisinopril 
#'DB00691'  moexipril  
#'DB00790'  perindopril  
#DB00881    quinapril 
#DB00178   ramipril 
#DB00519   trandolapril  

query3 = """select distinct ?Drug1CUI ?drugLabel1 ?Drug1 ?Drug2CUI ?drugLabel2 ?Drug2 ?Impact ?Effect
 where {
        ?DrugDrugInteraction a <http://covid-19.tib.eu/vocab/DrugDrugInteraction>.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasImpact> ?Impact.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasEffect> ?Effect.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/affects> ?Drug1.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/isAffected> ?Drug2.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug1CUI> ?Drug1CUI.
        ?Drug1CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel1.

        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug2CUI> ?Drug2CUI.        
        ?Drug2CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel2.
        FILTER (?drugLabel1 != ?drugLabel2)
        Filter (?Drug1 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>, <http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB00542>, <http://covid-19.tib.eu/vocab/DB01197>, <http://covid-19.tib.eu/vocab/DB00584>,
<http://covid-19.tib.eu/vocab/DB00492>, <http://covid-19.tib.eu/vocab/DB00722>, <http://covid-19.tib.eu/vocab/DB00691>,
<http://covid-19.tib.eu/vocab/DB00790>, <http://covid-19.tib.eu/vocab/DB00881>, <http://covid-19.tib.eu/vocab/DB00178>,
<http://covid-19.tib.eu/vocab/DB00519>))

        Filter (?Drug2 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>, <http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB00542>, <http://covid-19.tib.eu/vocab/DB01197>, <http://covid-19.tib.eu/vocab/DB00584>,
<http://covid-19.tib.eu/vocab/DB00492>, <http://covid-19.tib.eu/vocab/DB00722>, <http://covid-19.tib.eu/vocab/DB00691>,
<http://covid-19.tib.eu/vocab/DB00790>, <http://covid-19.tib.eu/vocab/DB00881>, <http://covid-19.tib.eu/vocab/DB00178>,
<http://covid-19.tib.eu/vocab/DB00519>))
}"""


# # Statins

#DB01611    Hydroxychloroquine
#DB01593    Zinc
#DB00608     Chloroquine

#DB01076  atorvastatin
#DB01095  fluvastatin
#DB00227  lovastatin
#DB08860  pitavastatin
#DB00175  pravastatin
#DB01098  rosuvastatin
#DB00641  simvastatin

query4 = """select distinct ?Drug1CUI ?drugLabel1 ?Drug1 ?Drug2CUI ?drugLabel2 ?Drug2 ?Impact ?Effect
 where {
        ?DrugDrugInteraction a <http://covid-19.tib.eu/vocab/DrugDrugInteraction>.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasImpact> ?Impact.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasEffect> ?Effect.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/affects> ?Drug1.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/isAffected> ?Drug2.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug1CUI> ?Drug1CUI.
        ?Drug1CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel1.

        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug2CUI> ?Drug2CUI.        
        ?Drug2CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel2.
        FILTER (?drugLabel1 != ?drugLabel2)
        Filter (?Drug1 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>,<http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB01076>, <http://covid-19.tib.eu/vocab/DB01095>, <http://covid-19.tib.eu/vocab/DB00227>,
<http://covid-19.tib.eu/vocab/DB08860>, <http://covid-19.tib.eu/vocab/DB00175>, <http://covid-19.tib.eu/vocab/DB01098>,
<http://covid-19.tib.eu/vocab/DB00641>))

        Filter (?Drug2 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>,<http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB01076>, <http://covid-19.tib.eu/vocab/DB01095>, <http://covid-19.tib.eu/vocab/DB00227>,
<http://covid-19.tib.eu/vocab/DB08860>, <http://covid-19.tib.eu/vocab/DB00175>, <http://covid-19.tib.eu/vocab/DB01098>,
<http://covid-19.tib.eu/vocab/DB00641>))
}"""


# # Type 2 diabetes

#DB01611    Hydroxychloroquine
#DB01593    Zinc
#DB00608     Chloroquine

#DB00331  Metformin
#DB01016  Glyburide
#DB01067  Glipizide
#DB00222  Glimepiride
#DB00912  Repaglinide
#DB00731  Nateglinide
#DB00412  Rosiglitazone
#DB01132  Pioglitazone
#DB01261  Sitagliptin
#DB06335  Saxagliptin
#DB08882  Linagliptin
#DB01276  Exenatide
#DB06655  Liraglutide
#DB13928  Semaglutide
#DB08907  Canagliflozin
#DB06292  Dapagliflozin
#DB09038  Empagliflozin
#DB00047  Insulin glargine
#DB01307  Insulin detemir

query5 = """select distinct ?Drug1CUI ?drugLabel1 ?Drug1 ?Drug2CUI ?drugLabel2 ?Drug2 ?Impact ?Effect
 where {
        ?DrugDrugInteraction a <http://covid-19.tib.eu/vocab/DrugDrugInteraction>.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasImpact> ?Impact.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasEffect> ?Effect.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/affects> ?Drug1.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/isAffected> ?Drug2.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug1CUI> ?Drug1CUI.
        ?Drug1CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel1.

        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug2CUI> ?Drug2CUI.        
        ?Drug2CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel2.
        FILTER (?drugLabel1 != ?drugLabel2)
        Filter (?Drug1 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>,<http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB00331>, <http://covid-19.tib.eu/vocab/DB01016>, <http://covid-19.tib.eu/vocab/DB01067>,
<http://covid-19.tib.eu/vocab/DB00222>, <http://covid-19.tib.eu/vocab/DB00912>, <http://covid-19.tib.eu/vocab/DB00731>,
<http://covid-19.tib.eu/vocab/DB00412>, <http://covid-19.tib.eu/vocab/DB01132>, <http://covid-19.tib.eu/vocab/DB01261>,
<http://covid-19.tib.eu/vocab/DB06335>, <http://covid-19.tib.eu/vocab/DB08882>, <http://covid-19.tib.eu/vocab/DB01276>,
<http://covid-19.tib.eu/vocab/DB06655>, <http://covid-19.tib.eu/vocab/DB13928>, <http://covid-19.tib.eu/vocab/DB08907>,
<http://covid-19.tib.eu/vocab/DB06292>, <http://covid-19.tib.eu/vocab/DB09038>, <http://covid-19.tib.eu/vocab/DB00047>,
<http://covid-19.tib.eu/vocab/DB01307>))

        Filter (?Drug2 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>,<http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB00331>, <http://covid-19.tib.eu/vocab/DB01016>, <http://covid-19.tib.eu/vocab/DB01067>,
<http://covid-19.tib.eu/vocab/DB00222>, <http://covid-19.tib.eu/vocab/DB00912>, <http://covid-19.tib.eu/vocab/DB00731>,
<http://covid-19.tib.eu/vocab/DB00412>, <http://covid-19.tib.eu/vocab/DB01132>, <http://covid-19.tib.eu/vocab/DB01261>,
<http://covid-19.tib.eu/vocab/DB06335>, <http://covid-19.tib.eu/vocab/DB08882>, <http://covid-19.tib.eu/vocab/DB01276>,
<http://covid-19.tib.eu/vocab/DB06655>, <http://covid-19.tib.eu/vocab/DB13928>, <http://covid-19.tib.eu/vocab/DB08907>,
<http://covid-19.tib.eu/vocab/DB06292>, <http://covid-19.tib.eu/vocab/DB09038>, <http://covid-19.tib.eu/vocab/DB00047>,
<http://covid-19.tib.eu/vocab/DB01307>))
}"""


# # pneumonia

#DB01611    Hydroxychloroquine
#DB01593    Zinc
#DB00608     Chloroquine

#DB00207  Azithromycin
#DB01211  Clarithromycin
#DB00537  ciprofloxacin
#DB11404  Enrofloxacin
#DB01137  Levofloxacin
#DB00254  Doxycycline
#DB00759  Tetracycline


query6 = """select distinct ?Drug1CUI ?drugLabel1 ?Drug1 ?Drug2CUI ?drugLabel2 ?Drug2 ?Impact ?Effect
 where {
        ?DrugDrugInteraction a <http://covid-19.tib.eu/vocab/DrugDrugInteraction>.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasImpact> ?Impact.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasEffect> ?Effect.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/affects> ?Drug1.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/isAffected> ?Drug2.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug1CUI> ?Drug1CUI.
        ?Drug1CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel1.

        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug2CUI> ?Drug2CUI.        
        ?Drug2CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel2.
        FILTER (?drugLabel1 != ?drugLabel2)
        Filter (?Drug1 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>,<http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB00207>, <http://covid-19.tib.eu/vocab/DB01211>, <http://covid-19.tib.eu/vocab/DB00537>,
<http://covid-19.tib.eu/vocab/DB11404>, <http://covid-19.tib.eu/vocab/DB01137>, <http://covid-19.tib.eu/vocab/DB00254>,
<http://covid-19.tib.eu/vocab/DB00759>))

        Filter (?Drug2 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>,<http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB00207>, <http://covid-19.tib.eu/vocab/DB01211>, <http://covid-19.tib.eu/vocab/DB00537>,
<http://covid-19.tib.eu/vocab/DB11404>, <http://covid-19.tib.eu/vocab/DB01137>, <http://covid-19.tib.eu/vocab/DB00254>,
<http://covid-19.tib.eu/vocab/DB00759>))
}"""


# # Asthma

#DB01611    Hydroxychloroquine
#DB01593    Zinc
#DB00608     Chloroquine

#DB00277  Theophylline
#DB00332  Ipratropium
#DB00043  Omalizumab
#DB06612  Mepolizumab
#DB12023  Benralizumab
#DB06602  Reslizumab
#DB13867  Fluticasone
#DB01222  Budesonide
#DB00764  Mometasone
#DB00394  Beclomethasone dipropionate
#DB01410  Ciclesonide
#DB00471  Montelukast
#DB00549  Zafirlukast
#DB00744  Zileuton
#DB00938  Salmeterol
#DB13139  Levosalbutamol
#DB00332  Ipratropium
#DB00635  Prednisone
#DB00959  Methylprednisolone
#DB00043  Omalizumab

query7 = """select distinct ?Drug1CUI ?drugLabel1 ?Drug1 ?Drug2CUI ?drugLabel2 ?Drug2 ?Impact ?Effect
 where {
        ?DrugDrugInteraction a <http://covid-19.tib.eu/vocab/DrugDrugInteraction>.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasImpact> ?Impact.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasEffect> ?Effect.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/affects> ?Drug1.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/isAffected> ?Drug2.
        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug1CUI> ?Drug1CUI.
        ?Drug1CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel1.

        ?DrugDrugInteraction <http://covid-19.tib.eu/vocab/hasDrug2CUI> ?Drug2CUI.        
        ?Drug2CUI <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel2.
        FILTER (?drugLabel1 != ?drugLabel2)
        Filter (?Drug1 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>,<http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB00277>, <http://covid-19.tib.eu/vocab/DB00332>, <http://covid-19.tib.eu/vocab/DB00043>,
<http://covid-19.tib.eu/vocab/DB06612>, <http://covid-19.tib.eu/vocab/DB12023>, <http://covid-19.tib.eu/vocab/DB06602>,
<http://covid-19.tib.eu/vocab/DB13867>, <http://covid-19.tib.eu/vocab/DB01222>, <http://covid-19.tib.eu/vocab/DB00764>,
<http://covid-19.tib.eu/vocab/DB00394>, <http://covid-19.tib.eu/vocab/DB01410>, <http://covid-19.tib.eu/vocab/DB00471>,
<http://covid-19.tib.eu/vocab/DB00549>, <http://covid-19.tib.eu/vocab/DB00744>, <http://covid-19.tib.eu/vocab/DB00938>,
<http://covid-19.tib.eu/vocab/DB13139>, <http://covid-19.tib.eu/vocab/DB00332>, <http://covid-19.tib.eu/vocab/DB00635>,
<http://covid-19.tib.eu/vocab/DB00959>, <http://covid-19.tib.eu/vocab/DB00043>))

        Filter (?Drug2 in (<http://covid-19.tib.eu/vocab/DB01611>, <http://covid-19.tib.eu/vocab/DB01593>,<http://covid-19.tib.eu/vocab/DB00608>,
<http://covid-19.tib.eu/vocab/DB00277>, <http://covid-19.tib.eu/vocab/DB00332>, <http://covid-19.tib.eu/vocab/DB00043>,
<http://covid-19.tib.eu/vocab/DB06612>, <http://covid-19.tib.eu/vocab/DB12023>, <http://covid-19.tib.eu/vocab/DB06602>,
<http://covid-19.tib.eu/vocab/DB13867>, <http://covid-19.tib.eu/vocab/DB01222>, <http://covid-19.tib.eu/vocab/DB00764>,
<http://covid-19.tib.eu/vocab/DB00394>, <http://covid-19.tib.eu/vocab/DB01410>, <http://covid-19.tib.eu/vocab/DB00471>,
<http://covid-19.tib.eu/vocab/DB00549>, <http://covid-19.tib.eu/vocab/DB00744>, <http://covid-19.tib.eu/vocab/DB00938>,
<http://covid-19.tib.eu/vocab/DB13139>, <http://covid-19.tib.eu/vocab/DB00332>, <http://covid-19.tib.eu/vocab/DB00635>,
<http://covid-19.tib.eu/vocab/DB00959>, <http://covid-19.tib.eu/vocab/DB00043>))
}"""


def get_use_case(case):
    if case==1:
        query = query1
        use_case=''
    elif case==2:
        query = query2
        use_case='with Hypertensive drugs\nBeta-blockers'
    elif case==3:
        query = query3
        use_case='with Hypertensive drugs\nAngiotensin converting enzyme'
    elif case==4:
        query = query4
        use_case='with Statins drugs'
    elif case==5:
        query = query5
        use_case='with Type 2 diabetes drugs'
    elif case==6:
        query = query6
        use_case='with Pneumonia drugs'
    else:  #case==7
        query = query7
        use_case='with Asthma drugs'
    return query, use_case


def get_ddi(query, sparql):
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    dd = {'Drug1CUI': [], 'drugLabel1': [], 'Drug1': [], 'Drug2CUI': [], 'drugLabel2': [], 'Drug2': [], 'Impact': [],
          'Effect': []}

    for r in results['results']['bindings']:
        dd['Drug1CUI'].append(r['Drug1CUI']['value'])
        dd['drugLabel1'].append(r['drugLabel1']['value'])
        dd['Drug1'].append(r['Drug1']['value'])
        dd['Drug2CUI'].append(r['Drug2CUI']['value'])
        dd['drugLabel2'].append(r['drugLabel2']['value'])
        dd['Drug2'].append(r['Drug2']['value'])
        dd['Impact'].append(r['Impact']['value'])
        dd['Effect'].append(r['Effect']['value'])

    set_DDIs = pd.DataFrame(dd)
    set_DDIs['Effect'] = set_DDIs['Effect'].str.replace('http://covid-19.tib.eu/Effect/', '')
    set_DDIs['Impact'] = set_DDIs['Impact'].str.replace('http://covid-19.tib.eu/Impact/', '')
    set_DDIs['Drug1CUI'] = set_DDIs['Drug1CUI'].str.replace('http://covid-19.tib.eu/vocab/', '')
    set_DDIs['Drug2CUI'] = set_DDIs['Drug2CUI'].str.replace('http://covid-19.tib.eu/vocab/', '')
    set_DDIs['Drug1'] = set_DDIs['Drug1'].str.replace('http://covid-19.tib.eu/vocab/', '')
    set_DDIs['Drug2'] = set_DDIs['Drug2'].str.replace('http://covid-19.tib.eu/vocab/', '')

    # # Combine column 'effect' and 'Impact'

    set_DDIs['effect_impact'] = set_DDIs[['Effect', 'Impact']].apply(lambda x: '_'.join(x), axis=1)
    set_DDIs = set_DDIs[['drugLabel1', 'drugLabel2', 'effect_impact']]
    set_DDIs.head()

    # ==== Add drug Zinc isolate ====
    interaction = pd.DataFrame(columns=['drugLabel1', 'drugLabel2', 'effect_impact'])
    interaction.drugLabel1 = ['Zinc']
    interaction.drugLabel2 = ['Zinc']
    interaction.effect_impact = [set_DDIs.effect_impact[0]]
    set_DDIs = pd.concat([set_DDIs, interaction])
    return set_DDIs


def Add_color_to_edges(set_DDIs):
    effect_impact = list(pd.value_counts(set_DDIs.effect_impact).index)

    col = colors.cnames
    color=list(col.values())
    #--------------remove colors-------------
    index=color.index('#FFEBCD')
    color.pop(index)
    index=color.index('#FF7F50')
    color.pop(index)
    index=color.index('#DEB887')
    color.pop(index)
    index=color.index('#FFF8DC')
    color.pop(index)
    index=color.index('#DC143C')
    color.pop(index)
    #--------------remove colors-------------
    ColorLegend = {}

    for i in range(len(effect_impact)):
        set_DDIs.loc[set_DDIs.effect_impact == effect_impact[i], "edge_color"] = color[i+7]
        ColorLegend[effect_impact[i]]=color[i+7]

    set_DDIs.reset_index(inplace=True)
    set_DDIs = set_DDIs.drop(columns=['index'])
    return set_DDIs, ColorLegend


def create_graph(set_DDIs):
    g = nx.DiGraph()
    # Add edges and edge attributes
    for i, elrow in set_DDIs.iterrows():
        g.add_edge(elrow[0], elrow[1], attr_dict=elrow[3], create_using=nx.DiGraph())

    # Define data structure (list) of edge colors for plotting
    edge_colors = [e[2]['attr_dict'] for e in g.edges(data=True)]
    return g, edge_colors


def Size_of_nodes(g, set_DDIs):
    list_node = list(g.nodes)
    d2 = list(set_DDIs.drugLabel2.unique())
    d2_size = []
    for i in range(len(list_node)):
        n2 = list_node[i]
        if n2 in d2:
            d2_size.append(g.degree(n2) * 80)
        else:
            d2_size.append(80)
    return d2_size


def draw_networkx(g, ColorLegend, edge_colors, d2_size, use_case):
    if len(use_case)>1:
        f = plt.figure(figsize=(16, 8))
    else:
        f = plt.figure(figsize=(70, 70))
    ax = f.add_subplot(1,1,1)

    for label in ColorLegend:
        ax.plot([0],[0], color=ColorLegend[label], label=label)

    nx.draw_circular(g, with_labels=True, node_color='skyblue', edge_color=edge_colors, node_size=d2_size, width=1.5,
           font_size=10, font_weight="bold", alpha=1.0, ax=ax)

    plt.axis('off')
    plt.title('Use Case: Hydroxychloroquine, Zinc and Chloroquine '+use_case, fontsize= 20, ha='center')

    #f.set_facecolor('W')

    plt.legend(loc='upper center', ncol=4).get_frame().set_alpha(0.2)#upper center

    f.tight_layout()
    use_case = use_case.replace('\n','_')
    if len(use_case)>1:
        plt.savefig(use_case+'.png', dpi = 300)
    else:
        plt.savefig('covid_drugs.png', dpi=300)

def main(*args):
    endpoint = "https://f0ffbb86.ngrok.io/sparql"
    sparql = SPARQLWrapper(endpoint)

    query, use_case = get_use_case(int(args[0]))
    set_DDIs = get_ddi(query, sparql)
    set_DDIs, ColorLegend = Add_color_to_edges(set_DDIs)
    g, edge_colors = create_graph(set_DDIs)
    d2_size = Size_of_nodes(g, set_DDIs)
    draw_networkx(g, ColorLegend, edge_colors, d2_size, use_case)


if __name__ == "__main__":
    main(*sys.argv[1:])