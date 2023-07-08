#obtenir % dans chaque gff : nullarbor, bactopia et asa3p
def get_hyp(file):
    total_count = 0
    hypothetical_count = 0
    with open(file, "r") as fichier:
        for ligne in fichier:
            if ligne.startswith("gnl"):
            # if ligne.startswith("Contig"):
                colonnes = ligne.split("\t")
                if colonnes[2] == "CDS":
                    dernier_colonne = colonnes[-1].strip()
                    mention_product = None
                    for mention in dernier_colonne.split(";"):
                        if mention.startswith("product="):
                            mention_product = mention
                            break
                    if mention_product:
                        total_count += 1
                        if "hypothetical" in mention_product:
                            hypothetical_count += 1

    percentage = (hypothetical_count / total_count) * 100 if total_count != 0 else 0
    print("Total count:", total_count)
    print("Hypothetical count:", hypothetical_count)
    print("Percentage:", percentage)
    print("--------------")
    return percentage

#bactopia
f1 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR5329951/SRR5329951_badq.gff"
f2 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR1699337hyb/SRR1699337hyb.gff"
f3 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR8182677/SRR8182677_goodq.gff"
f4 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR16993378/SRR16993378.gff"
f5 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR16993379/SRR16993379_illumina.gff"
# get_hyp(f1)
# get_hyp(f2)
# get_hyp(f3)
# get_hyp(f4)
# get_hyp(f5)

#asa3p
f6 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR1699337hyb/Lactococcus_lactis_SRR1699337hyb.gff"
f7 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR5329951/Lactococcus_lactis_SRR5329951.gff"
f8 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR6482979/Lactococcus_lactis_SRR6482979.gff"
f9 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR8182677/Lactococcus_lactis_SRR8182677.gff"
f10 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR16993378/Lactococcus_lactis_SRR16993378.gff"
f11 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR16993379/Lactococcus_lactis_SRR16993379.gff"

# get_hyp(f6)
# get_hyp(f7)
# get_hyp(f8)
# get_hyp(f9)
# get_hyp(f10)
# get_hyp(f11)

f12 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR5329951/SRR5329951.gff"
f13 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR6482979/SRR6482979.gff"
f14 = "/Users/fionahak/Documents/StageM1/stagem1_scripts/analyses_gff_quast_roary/roary_comp/roary_comp_SRR16993379/SRR16993379.gff"

# get_hyp(f12)
# get_hyp(f13)
# get_hyp(f14)

