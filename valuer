import csv



def forme(fusion_csv):
    with open(fusion_csv) as file:
        x = csv.reader(file)
        c ="date_reference|semaine_injection|region_residence|libelle_region|departement_residence|libelle_departement|population_insee|classe_age|libelle_classe_age|type_vaccin|effectif_1_inj|effectif_termine|effectif_cumu_1_inj|effectif_cumu_termine|taux_1_inj|taux_termine|taux_cumu_1_inj,taux_cumu_termine|date,effectif_rappel|effectif_cumu_rappel|effectif_rappel_parmi_eligible|effectif_eligible_au_rappel|taux_rappel|taux_cumu_rappel|taux_cumu_rappeleli".split("|")
        s = ""
        l=[list() for loop in range(2)]
        for i in x:
            i=i[0].split(";")
            if not "date_reference" in i and len(i)>19:
                l[0].append(i[5])
                l[1].append(i[18])
        return l




a=forme("fusion.csv")
for i in range(len(a[0])):
    print(a[0][i],a[1][i])
