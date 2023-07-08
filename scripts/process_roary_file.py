import csv

#comparer les sorties d'un même génome analysé par les 3 pipelines
#relève les catégories fonctionnelles/les gènes communs à chaque pipelines
def get_info_gene(input_file, nom_souche1, nom_souche2, nom_souche3):
    common_genes = 0
    specific_strain_bactopia = 0
    specific_strain_asa3p = 0
    specific_strain_nullarbor = 0
    specific_bactopia_asa3p_genes = 0
    specific_bactopia_nullarbor_genes = 0
    specific_asa3p_nullarbor_genes = 0

    list_CF_specific_bactopia = []
    list_CF_specific_asap = []
    list_CF_specific_nullarbor = []

    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            asap = row[nom_souche1]
            bactopia = row[nom_souche2]
            nullarbor = row[nom_souche3]
            isolates = row["No. isolates"].split(";")
            if isolates == ['3']:
                common_genes = common_genes + 1
            elif isolates == ['2']:
                if len(bactopia) > 1 and len(asap) > 1:
                    specific_bactopia_asa3p_genes = specific_bactopia_asa3p_genes + 1
                elif len(bactopia) > 1 and len(nullarbor) > 1:
                    specific_bactopia_nullarbor_genes = specific_bactopia_nullarbor_genes + 1
                elif len(nullarbor) > 1 and len(asap) > 1:
                    specific_asa3p_nullarbor_genes = specific_asa3p_nullarbor_genes + 1
            elif isolates == ['1']:
                if len(bactopia) > 1:
                    specific_strain_bactopia = specific_strain_bactopia + 1
                    list_CF_specific_bactopia.append(row["Annotation"])
                elif len(asap) > 1:
                    specific_strain_asa3p = specific_strain_asa3p + 1
                    list_CF_specific_asap.append(row["Annotation"])
                elif len(nullarbor) > 1:
                    specific_strain_nullarbor = specific_strain_nullarbor + 1
                    list_CF_specific_nullarbor.append(row["Annotation"])
            else:
                print("pbbbb")

    return list_CF_specific_asap, list_CF_specific_bactopia, list_CF_specific_nullarbor


#comparer les sorties d'un même génome analysé par les 2 des 3 pipelines
#relève les catégories fonctionnelles/les gènes communs à chaque pipelines
def get_info_gene_2files(input_file, nom_souche1, nom_souche2):
    common_genes = 0
    specific_strain_outil1 = 0
    specific_strain_outil2 = 0
    list_CF_specific_tool1 = []
    list_CF_specific_tool2 = []

    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            outil1 = row[nom_souche1]
            outil2 = row[nom_souche2]
            isolates = row["No. isolates"].split(";")
            if isolates == ['2']:
                common_genes = common_genes + 1
            elif isolates == ['1']:
                if len(outil1) > 1:
                    specific_strain_outil1 = specific_strain_outil1 + 1
                    list_CF_specific_tool1.append(row["Annotation"])
                elif len(outil2) > 1:
                    specific_strain_outil2 = specific_strain_outil2 + 1
                    list_CF_specific_tool2.append(row["Annotation"])
            else:
                print("pbbbb")

    return list_CF_specific_tool1, list_CF_specific_tool2


#compter le nombre d'annotation transposase/hypothetical d'un coté et les autres d'un autre
def count_occurrences(data):
    transposase_hypothetical_count = 0
    other_count = 0
    for item in data:
        if 'transposase' in item.lower() or 'hypothetical' in item.lower():
            transposase_hypothetical_count += 1
        else:
            other_count += 1
    return transposase_hypothetical_count, other_count


###############
# PRINT
###############

# comparaison annotations prokka
SRR5329951_results = get_info_gene(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR5329951/gene_presence_absence.csv",
    "Lactococcus_lactis_SRR5329951", "SRR5329951_badq", "SRR5329951")  # asap, bactopia, nullarbor
SRR1699337hyb_results = get_info_gene_2files(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR1699337hyb/gene_presence_absence.csv",
    "Lactococcus_lactis_SRR1699337hyb", "SRR1699337hyb")  # asap, bactopia
SRR6482979_results = get_info_gene_2files(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR6482979/gene_presence_absence.csv",
    "Lactococcus_lactis_SRR6482979", "SRR6482979")  # asap, nullarbor
SRR8182677_results = get_info_gene_2files(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR8182677/gene_presence_absence.csv",
    "Lactococcus_lactis_SRR8182677", "SRR8182677_goodq")  # asap, bactopia
SRR16993378_results = get_info_gene_2files(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR16993378/gene_presence_absence.csv",
    "Lactococcus_lactis_SRR16993378", "SRR16993378")  # asap, bactopia
SRR16993379_results = get_info_gene(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR16993379/gene_presence_absence.csv",
    "Lactococcus_lactis_SRR16993379", "SRR16993379_illumina", "SRR16993379")  # asap, bactopia, nullarbor

# comparaison annotations bakta/prokka pour bactopia
# outil1 = prokka, outil2 = bakta
hybrid_bakta_results = get_info_gene_2files(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/bakta/hybrid/gene_presence_absence.csv",
    "SRR1699337hyb_simple", "SRR1699337hyb_hyb_bactopia")
SRR5329951_bakta_results = get_info_gene_2files(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/bakta/SRR5329951/gene_presence_absence.csv",
    "SRR5329951_badq", "SRR5329951_bakta")
SRR8182677_bakta_results = get_info_gene_2files(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/bakta/SRR8182677/gene_presence_absence.csv",
    "SRR8182677_goodq", "SRR8182677_bakta")
SRR16993378_bakta_results = get_info_gene_2files(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/bakta/SRR16993378/gene_presence_absence.csv",
    "SRR16993378", "SRR16993378_bakta")
SRR16993379_bakta_results = get_info_gene_2files(
    "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/bakta/SRR16993379/gene_presence_absence.csv",
    "SRR16993379_illumina", "SRR16993379_bakta")

# 3 outils
all_mixed_annotation_specific_bactopia = [SRR5329951_results[1], \
                                          SRR1699337hyb_results[1], \
                                          SRR8182677_results[1], \
                                          SRR16993378_results[1], \
                                          SRR16993379_results[1]]
all_mixed_annotation_specific_asa3p = [SRR5329951_results[0], \
                                       SRR1699337hyb_results[0], \
                                       SRR6482979_results[0], \
                                       SRR8182677_results[0], \
                                       SRR16993378_results[0], \
                                       SRR16993379_results[0]]
all_mixed_annotation_specific_nullarbor = [SRR5329951_results[2], \
                                           SRR6482979_results[1], \
                                           SRR16993379_results[2]]

