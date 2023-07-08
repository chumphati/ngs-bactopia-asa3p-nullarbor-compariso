#comparer deux sorties quast entre elles
def get_info_quast_2tools(file1, file2):
    columns_file1 = set()
    columns_file2 = []
    all_id_gene_file1 = []
    all_id_gene_file2 = set()
    nb_common_columns_all = 0
    specific_strain_file2 = 0

    with open(file1, "r") as f:
        next(f)
        next(f)
        next(f)
        for line in f:
            columns = line.strip().split("\t")
            columns_file1.add(columns[0])

    with open(file2, "r") as f:
        next(f)
        next(f)
        next(f)
        for line in f:
            columns = line.strip().split("\t")
            all_id_gene_file2.add(columns[0])
            if columns[0] in columns_file1:
                nb_common_columns_all += 1
            else:
                specific_strain_file2 += 1
                columns_file2.append(columns[0])

    for elements in columns_file1:
        if elements not in all_id_gene_file2:
            all_id_gene_file1.append(elements)

    #partiel ou pas ?
    type_file1 = []
    contig_file1 = []
    with open(file1, "r") as f:
        next(f)
        next(f)
        next(f)
        for line in f:
            columns = line.strip().split("\t")
            type = columns[4]
            if columns[0] in all_id_gene_file1:
                type_file1.append(type)
                contig_file1.append(columns[5])

    type_file2 = []
    contig_file2 = []
    with open(file2, "r") as f:
        next(f)
        next(f)
        next(f)
        for line in f:
            columns = line.strip().split("\t")
            type = columns[4]
            if columns[0] in columns_file2:
                type_file2.append(type)
                contig_file2.append(columns[5])

    specific_strain_asap = len(columns_file1) - nb_common_columns_all

    #type = partiel ou complet, contig = positions début et fin dans le contig
    return type_file2, type_file1, contig_file2, contig_file1

#comparer les sorties quast des trois pipelines
def get_info_quast_3tools(file_asap, file_bactopia, file_nullarbor):
    columns_asap = set()
    columns_bactopia = set()
    columns_nullarbor = set()
    specific_asap = []
    specific_bactopia = []
    specific_nullarbor = []

    with open(file_asap, "r") as file:
        next(file)
        next(file)
        for line in file:
            columns = line.strip().split("\t")
            columns_asap.add(columns[0])

    with open(file_bactopia, "r") as file:
        next(file)
        next(file)
        for line in file:
            columns = line.strip().split("\t")
            columns_bactopia.add(columns[0])

    with open(file_nullarbor, "r") as file:
        next(file)
        next(file)
        for line in file:
            columns = line.strip().split("\t")
            columns_nullarbor.add(columns[0])

    for elementsasap in columns_asap:
        if elementsasap not in columns_bactopia and elementsasap not in columns_nullarbor:
            specific_asap.append(elementsasap)

    for elementbac in columns_bactopia:
        if elementbac not in columns_asap and elementbac not in columns_nullarbor:
            specific_bactopia.append(elementbac)

    for elementnull in columns_nullarbor:
        if elementnull not in columns_bactopia and elementnull not in columns_asap:
            specific_nullarbor.append(elementnull)

    # partiel ou pas ?
    type_asap = []
    with open(file_asap, "r") as file:
        next(file)
        next(file)
        for line in file:
            columns = line.strip().split("\t")
            type = columns[4]
            if columns[0] in specific_asap:
                type_asap.append(type)

    type_bactopia = []
    contig_bactopia = []
    with open(file_bactopia, "r") as file:
        next(file)
        next(file)
        for line in file:
            columns = line.strip().split("\t")
            type = columns[4]
            if columns[0] in specific_bactopia:
                type_bactopia.append(type)
                contig_bactopia.append(columns[5])

    type_nullarbor = []
    with open(file_nullarbor, "r") as file:
        next(file)
        next(file)
        for line in file:
            columns = line.strip().split("\t")
            type = columns[4]
            if columns[0] in specific_nullarbor:
                type_nullarbor.append(type)

    common_columns = columns_asap.intersection(columns_bactopia, columns_nullarbor)
    count_common_columns_asap_bactopia_nullarbor = len(common_columns)

    specific_strain_asap = len(columns_asap.difference(columns_bactopia, columns_nullarbor))
    specific_strain_bactopia = len(columns_bactopia.difference(columns_asap, columns_nullarbor))
    specific_strain_nullarbor = len(columns_nullarbor.difference(columns_asap, columns_bactopia))

    count_common_asap_bactopia = len(columns_asap.intersection(columns_bactopia) - common_columns)
    count_common_nullarbor_bactopia = len(columns_bactopia.intersection(columns_nullarbor) - common_columns)
    count_common_nullarbor_asap = len(columns_asap.intersection(columns_nullarbor) - common_columns)

    return type_asap, type_bactopia, type_nullarbor, contig_bactopia

#obtenir le % des occurences des gènes partiels et complets
def calcul_percent_list(types):
    occurrences = {}
    for type in types:
        if type in occurrences:
            occurrences[type] += 1
        else:
            occurrences[type] = 1
    total_occurrences = len(types)
    percentage_occurrences = {}
    for type, count in occurrences.items():
        percentage = (count / total_occurrences) * 100
        percentage_occurrences[type] = percentage

    for type, percentage in percentage_occurrences.items():
        print(f"{type}: {percentage}%")

#obtenir le nombre des occurences des gènes partiels et complets
def calcul_occurrences(types):
    occurrences = {}
    for type in types:
        if type in occurrences:
            occurrences[type] += 1
        else:
            occurrences[type] = 1
    print(occurrences)


###############
#PRINT
###############

# comparaison annotations prokka
SRR1699337hyb_quast = get_info_quast_2tools("/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR1699337hyb/results/genome_stats/Lactococcus_lactis_SRR1699337hyb-gff_genomic_features_gene.txt","/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR1699337hyb/results/genome_stats/SRR1699337hyb-gff_genomic_features_gene.txt") #asap, bactopia
SRR6482979_quast = get_info_quast_2tools("/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR6482979/results/genome_stats/Lactococcus_lactis_SRR6482979-gff_genomic_features_gene.txt","/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR6482979/results/genome_stats/SRR6482979-gff_genomic_features_gene.txt") #asap, nullarbor
SRR8182677_quast = get_info_quast_2tools("/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR8182677/results/genome_stats/Lactococcus_lactis_SRR8182677-gff_genomic_features_any.txt","/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR8182677/results/genome_stats/SRR8182677_goodq-gff_genomic_features_any.txt") #asap, bactopia
SRR16993378_quast = get_info_quast_2tools("/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR16993378/results/genome_stats/Lactococcus_lactis_SRR16993378-gff_genomic_features_gene.txt","/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR16993378/results/genome_stats/SRR16993378-gff_genomic_features_gene.txt") #asap, bactopia
SRR16993379_quast = get_info_quast_3tools("/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR16993379/results/genome_stats/Lactococcus_lactis_SRR16993379-gff_genomic_features_gene.txt","/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR16993379/results/genome_stats/SRR16993379_illumina-gff_genomic_features_gene.txt","/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/quast_comp_SRR16993379/results/genome_stats/SRR16993379-gff_genomic_features_gene.txt")

# comparaison annotations bakta/prokka pour bactopia
# outil1 = prokka, outil2 = bakta
hybrid_quast_bakta = get_info_quast_2tools("/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/bakta/hybrid/results/genome_stats/SRR1699337hyb-gff_genomic_features_gene.txt","/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/bakta/hybrid/results/genome_stats/SRR1699337hyb_bakta-gff_genomic_features_gene.txt")
SRR8182677_quast_bakta = get_info_quast_2tools("/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/bakta/SRR8182677/results/genome_stats/SRR8182677_goodq-gff_genomic_features_gene.txt","/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/bakta/SRR8182677/results/genome_stats/SRR8182677_bakta-gff_genomic_features_gene.txt")
SRR16993378_quast_bakta = get_info_quast_2tools("/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/bakta/SRR16993378/results/genome_stats/SRR16993378-gff_genomic_features_gene.txt","/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/bakta/SRR16993378/results/genome_stats/SRR16993378_bakta-gff_genomic_features_gene.txt")
SRR16993379_quast_bakta = get_info_quast_2tools("/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/bakta/SRR16993379/results/genome_stats/SRR16993379_illumina-gff_genomic_features_gene.txt","/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/quast_comp_test/bakta/SRR16993379/results/genome_stats/SRR16993379_bakta-gff_genomic_features_gene.txt")

print(len(SRR16993379_quast_bakta))
print(len(SRR8182677_quast_bakta))

########################################
#stats sur les trois outils
print("SRR8182677")
print("asap ------")
asap = calcul_percent_list(SRR8182677_quast[1])
print("bactopia ------")
bactopia = calcul_percent_list(SRR8182677_quast[0])
print("contigs complet:")
print(SRR8182677_quast[2])
print("--------------------\n")

print("ONT")
print("asap ------")
asap = calcul_percent_list(SRR16993378_quast[1])
print("bactopia ------")
bactopia = calcul_percent_list(SRR16993378_quast[0])
print("contigs complet:")
print(SRR16993378_quast[2])
print("--------------------\n")

print("SRR6482979")
print("asap ------")
asap = calcul_percent_list(SRR6482979_quast[1])
print("nullarbor ------")
bactopia = calcul_percent_list(SRR6482979_quast[0])
print("--------------------\n")

print("SRR16993379")
print("asap ------")
asap = calcul_percent_list(SRR16993379_quast[0])
print("bactopia ------")
bactopia = calcul_percent_list(SRR16993379_quast[1])
print("contigs complet:")
print(SRR16993379_quast[3])
print("nullarbor ------")
nullarbor = calcul_percent_list(SRR16993379_quast[2])
print("--------------------\n")
#######################################

########################################
# Statistiques sur les trois outils
print("SRR8182677")
print("asap ------")
asap = calcul_occurrences(SRR8182677_quast[1])
print("bactopia ------")
bactopia = calcul_occurrences(SRR8182677_quast[0])
print("contigs complets:")
# print(SRR8182677_quast[2])
print("--------------------\n")

print("ONT")
print("asap ------")
asap = calcul_occurrences(SRR16993378_quast[1])
print("bactopia ------")
bactopia = calcul_occurrences(SRR16993378_quast[0])
# print("contigs complets:")
print(SRR16993378_quast[2])
print("--------------------\n")

print("SRR6482979")
print("asap ------")
asap = calcul_occurrences(SRR6482979_quast[1])
print("nullarbor ------")
bactopia = calcul_occurrences(SRR6482979_quast[0])
print("--------------------\n")

print("SRR16993379")
print("asap ------")
asap = calcul_occurrences(SRR16993379_quast[0])
print("bactopia ------")
bactopia = calcul_occurrences(SRR16993379_quast[1])
print("contigs complets:")
# print(SRR16993379_quast[3])
print("nullarbor ------")
nullarbor = calcul_occurrences(SRR16993379_quast[2])
print("--------------------\n")

#hybride = 0
