#parse gene_absence_presence.csv
def parse_file(file_path):
    CF = []
    liste1 = []
    liste2 = []

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split(',')
            if len(columns) >= 14:
                col2 = columns[-2].strip('"')
                col3 = columns[-1].strip('"')
                if col2 and col3:
                    CF.append(columns[2].strip('"'))
                    liste1.append(col3)
                    liste2.append(col2)

    return CF, liste1, liste2


#obtenir listes des produits dans les gff d'origine selon l'ordre des gènes décrits dans le csv
def parse_gene_product(file_path1, CF, liste):
    listCF = []
    gene_product_map = {}

    with open(file_path1, 'r') as file1:
        for line1 in file1:
            if line1.startswith('gnl'):
                columns1 = line1.strip().split('\t')
                if len(columns1) >= 9 and columns1[2] == 'CDS':
                    last_column1 = columns1[-1]
                    if ';' in last_column1:
                        products1 = last_column1.split(';')
                        last_product1 = products1[-1]
                        product = products1[-2]
                        if '|' in last_product1:
                            gene_name1 = last_product1.split('|')[-1]
                            product_column1 = columns1[8]
                        if product.startswith('product='):
                            get_product = product.split("=")[1]

                            if gene_name1 not in gene_product_map:
                                gene_product_map[gene_name1] = get_product

    for gene_name in liste:
        if gene_name in gene_product_map:
            listCF.append(gene_product_map[gene_name])

    return listCF


#comparer deux listes pour trouver le nombre de correspondances
def compare_lists(info1, info2, listoriginal):
    count_match = 0
    count_total = 0
    count_hyp = 0
    count_others = 0
    for i in range(len(info1)):
        if info1[i].lower() == info2[i].lower() or ('transposase' in info1[i].lower() and 'transposase' in info2[i].lower()):
            count_match += 1
        elif 'hypothetical' in info1[i].lower() or 'hypothetical' in info2[i].lower():
            count_hyp += 1
        elif 'transporter' in info1[i].lower() or 'transporter' in info2[i].lower()\
                or 'phage' in info1[i].lower() or 'phage' in info2[i].lower()\
                or 'permease' in info1[i].lower() or 'permease' in info2[i].lower()\
                or 'helicase' in info1[i].lower() or 'helicase' in info2[i].lower()\
                or 'cyclohydrolase' in info1[i].lower() or 'cyclohydrolase' in info2[i].lower()\
                or 'synthetase' in info1[i].lower() or 'synthetase' in info2[i].lower()\
                or 'phosphorylase' in info1[i].lower() or 'phosphorylase' in info2[i].lower()\
                or 'phosphoesterase' in info1[i].lower() or 'phosphoesterase' in info2[i].lower()\
                or 'protease' in info1[i].lower() or 'protease' in info2[i].lower()\
                or 'aminotransferase' in info1[i].lower() or 'aminotransferase' in info2[i].lower()\
                or 'reductase' in info1[i].lower() or 'reductase' in info2[i].lower()\
                or 'synthase' in info1[i].lower() or 'synthase' in info2[i].lower()\
                or 'binding' in info1[i].lower() or 'binding' in info2[i].lower()\
                or 'peroxidase' in info1[i].lower() or 'peroxidase' in info2[i].lower()\
                or 'ribonuclease' in info1[i].lower() or 'ribonuclease' in info2[i].lower()\
                or 'kinase' in info1[i].lower() or 'kinase' in info2[i].lower()\
                or 'monooxygenase' in info1[i].lower() or 'monooxygenase' in info2[i].lower()\
                or 'methyltransferase' in info1[i].lower() or 'methyltransferase' in info2[i].lower()\
                or 'monooxygenase' in info1[i].lower() or 'monooxygenase' in info2[i].lower()\
                or 'membrane' in info1[i].lower() or 'membrane' in info2[i].lower()\
                or 'ligase' in info1[i].lower() or 'ligase' in info2[i].lower()\
                or 'tautomerase' in info1[i].lower() or 'tautomerase' in info2[i].lower()\
                or 'integrase' in info1[i].lower() or 'integrase' in info2[i].lower()\
                or 'transferase' in info1[i].lower() or 'transferase' in info2[i].lower()\
                or 'translocase' in info1[i].lower() or 'translocase' in info2[i].lower()\
                or 'dehydrogenase' in info1[i].lower() or 'dehydrogenase' in info2[i].lower()\
                or 'rhodanese' in info1[i].lower() or 'rhodanese' in info2[i].lower()\
                or 'ribosomal' in info1[i].lower() or 'ribosomal' in info2[i].lower()\
                or 'peptidase' in info1[i].lower() or 'peptidase' in info2[i].lower()\
                or 'topoisomerase' in info1[i].lower() or 'topoisomerase' in info2[i].lower()\
                or 'dehydratase' in info1[i].lower() or 'dehydratase' in info2[i].lower()\
                or 'stress' in info1[i].lower() or 'stress' in info2[i].lower()\
                or 'pump' in info1[i].lower() or 'pump' in info2[i].lower()\
                or 'hydrolase' in info1[i].lower() or 'hydrolase' in info2[i].lower()\
                or 'transcriptional' in info1[i].lower() or 'transcriptional' in info2[i].lower()\
                or 'phosphatase' in info1[i].lower() or 'phosphatase' in info2[i].lower()\
                or 'regulator' in info1[i].lower() or 'regulator' in info2[i].lower()\
                or 'oxidase' in info1[i].lower() or 'oxidase' in info2[i].lower()\
                or 'deaminase' in info1[i].lower() or 'deaminase' in info2[i].lower()\
                or 'nucleotidase' in info1[i].lower() or 'nucleotidase' in info2[i].lower()\
                or 'transglycosylase' in info1[i].lower() or 'transglycosylase' in info2[i].lower()\
                or 'excinuclease' in info1[i].lower() or 'excinuclease' in info2[i].lower()\
                or 'domain-containing' in info1[i].lower() or 'domain-containing' in info2[i].lower()\
                or 'excinuclease' in info1[i].lower() or 'excinuclease' in info2[i].lower()\
                or 'mobilization' in info1[i].lower() or 'mobilization' in info2[i].lower()\
                or 'formamidopyrimidine' in info1[i].lower() or 'formamidopyrimidine' in info2[i].lower()\
                or 'polymerase' in info1[i].lower() or 'polymerase' in info2[i].lower()\
                or 'repair' in info1[i].lower() or 'repair' in info2[i].lower()\
                or 'aldolase' in info1[i].lower() or 'aldolase' in info2[i].lower()\
                or 'deaminase' in info1[i].lower() or 'deaminase' in info2[i].lower()\
                or 'competence' in info1[i].lower() or 'competence' in info2[i].lower()\
                or 'polysaccharide' in info1[i].lower() or 'polysaccharide' in info2[i].lower()\
                or 'shock' in info1[i].lower() or 'shock' in info2[i].lower()\
                or 'deaminase' in info1[i].lower() or 'deaminase' in info2[i].lower()\
                or 'carboxylase' in info1[i].lower() or 'carboxylase' in info2[i].lower()\
                or 'resistance' in info1[i].lower() or 'resistance' in info2[i].lower()\
                or 'mutase' in info1[i].lower() or 'mutase' in info2[i].lower()\
                or 'asparaginase' in info1[i].lower() or 'asparaginase' in info2[i].lower()\
                or 'division' in info1[i].lower() or 'division' in info2[i].lower()\
                or 'isomerase' in info1[i].lower() or 'isomerase' in info2[i].lower()\
                or 'racemase' in info1[i].lower() or 'racemase' in info2[i].lower()\
                or 'glycosylase' in info1[i].lower() or 'glycosylase' in info2[i].lower()\
                or 'recombinase' in info1[i].lower() or 'recombinase' in info2[i].lower()\
                or 'thioesterase' in info1[i].lower() or 'thioesterase' in info2[i].lower()\
                or 'partition' in info1[i].lower() or 'partition' in info2[i].lower()\
                or 'bacteriocin' in info1[i].lower() or 'bacteriocin' in info2[i].lower()\
                or 'hemolysin' in info1[i].lower() or 'hemolysin' in info2[i].lower()\
                or 'amidase' in info1[i].lower() or 'amidase' in info2[i].lower()\
                or 'sortase' in info1[i].lower() or 'sortase' in info2[i].lower()\
                or 'hydratase' in info1[i].lower() or 'hydratase' in info2[i].lower()\
                or 'deacylase' in info1[i].lower() or 'deacylase' in info2[i].lower()\
                or 'glucosidase' in info1[i].lower() or 'glucosidase' in info2[i].lower()\
                or 'enzyme' in info1[i].lower() or 'enzyme' in info2[i].lower()\
                or 'phosphate' in info1[i].lower() or 'phosphate' in info2[i].lower()\
                or 'resolvase' in info1[i].lower() or 'resolvase' in info2[i].lower()\
                or 'deiminase' in info1[i].lower() or 'deiminase' in info2[i].lower()\
                or 'desulfurase' in info1[i].lower() or 'desulfurase' in info2[i].lower()\
                or 'antiporter' in info1[i].lower() or 'antiporter' in info2[i].lower()\
                or 'nuclease' in info1[i].lower() or 'nuclease' in info2[i].lower()\
                or 'phosphodiesterase' in info1[i].lower() or 'phosphodiesterase' in info2[i].lower()\
                or 'recombination' in info1[i].lower() or 'recombination' in info2[i].lower()\
                or 'homeostasis' in info1[i].lower() or 'homeostasis' in info2[i].lower()\
                or 'translocating' in info1[i].lower() or 'translocating' in info2[i].lower()\
                or 'phospholipase' in info1[i].lower() or 'phospholipase' in info2[i].lower()\
                or 'chaperon' in info1[i].lower() or 'chaperon' in info2[i].lower()\
                or 'replication' in info1[i].lower() or 'replication' in info2[i].lower()\
                or 'mechanosensitive' in info1[i].lower() or 'mechanosensitive' in info2[i].lower()\
                or 'ribosylhomocystein' in info1[i].lower() or 'ribosylhomocystein' in info2[i].lower()\
                or 'epimerase' in info1[i].lower() or 'epimerase' in info2[i].lower()\
                or 'cluster' in info1[i].lower() or 'cluster' in info2[i].lower()\
                or 'thioredoxin' in info1[i].lower() or 'thioredoxin' in info2[i].lower():
            count_others += 1
        else:
            print(info1[i],"---",info2[i], "---", listoriginal[i])
            print("-------")
        count_total += 1
    print(count_hyp)
    return count_match, count_total, count_others


#################################
#############PRINT##############
#################################
file_csv = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR1699337hyb/gene_presence_absence.csv"
file_comp1 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR1699337hyb/SRR1699337hyb.gff"
file_comp2 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR1699337hyb/Lactococcus_lactis_SRR1699337hyb.gff"
CF, liste1, liste2 = parse_file(file_csv)
CF = parse_liste(CF)
liste1.pop(0)
liste2.pop(0)
print(liste1)
print(liste2)
print(CF)
info1 = parse_gene_product(file_comp1, CF, liste1) #bactopia
info2 = parse_gene_product(file_comp2, CF, liste2) #asap
print(info1)
print(info2)
count_match, count_total, count_others = compare_lists(info1, info2, CF)
print("Nombre de correspondances :", count_match)
print("Annotations approximatives :", count_others)
print("Nombre total d'éléments :", count_total)
