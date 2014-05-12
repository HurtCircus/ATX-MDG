# drug dictionary as a list and data structure holding drugs
# coding utf-8

drug_data_list_of_dicts = [
{"drug" : "Acetaminophen (APAP) (Tylenol)",
 "name" : "[b]Acetaminophen (APAP) (Tylenol)[/b]",
 "adult dosage" : "M-09, M-16",
 "pedi dosage" : "PM-03, PM-06, PM-07",
 "indications" : "Fever with or without seizures or Pain.",
 "contraindications" : "Use in caution with children afflicted with arthritic or rheumatoid conditions.  Use in caution with known thrombocytopenia and/or Liver",
 "adverse effects" : "N/V, abdominal pain",
 "class" : "Analgesic, Antipyretic",
 "pharmacokinetics" : "Absorption is rapid, peak 1-2h, duration 3-4h, half-life 1-3h. APAP is processed in the Liver",
 "action" : "Equivalent to aspirin in both analgesic and antipyretic effects.  Unlike aspirin, acetaminophen has little effect on platelet function, no effect on homeostasis, and is not known to produce gastric bleeding.  Acetaminophen is not an NSAID, as it has no anti-inflammatory properties. Its function was largely a mystery until the early 1990's when it was found that it acted on a variant of cyclooxygenase called COX3 that is only expressed in the central nervous system. Because it does not work on COX1 and COX2 (like ASA) it does not cause the downstream effects on platelets or the immune system.",
 "is_selected" : False},
{"drug" : "Adenosine",
 "name" : "[b]Adenosine[/b]",
 "adult dosage" : "12mg rapid IV repeat x1 (Max 24mg) - 10mL flush after each dose",
 "pedi dosage" : "N/A",
 "indications" : "Symptomatic (poor perfusion) narrow complex tachycardia w/ pulse ",
 "contraindications" : "Known hypersensitivity.  Sick Sinus Syndrome. Second or third degree AV block. Use with caution in patients with severe asthma.",
 "adverse effects" : "Flushing, CP, HA, N/V, hypotension",
 "class" : "Antidysrhythmic",
 "pharmacokinetics" : "Immediate onset and peak, half-life 10s",
 "action" : "Slows AV node conduction, interrupts reentry pathways. Adenosine works in a variety of receptors grouped into a group called P1 receptors. The true mechanism is somewhat unclear. Adenosine works through the activation of cAMP and coupled G-proteins to cause its cardiac effects.",
 "is_selected" : False},
{"drug" : "Albuterol",
 "name" : "[b]Albuterol[/b]",
 "adult dosage" : "M-02, R-04, SO-01, T-04 ",
 "pedi dosage" : "PM-01, PR-03",
 "indications" : "",
 "contraindications" : "",
 "adverse effects" : "",
 "class" : "",
 "pharmacokinetics" : "",
 "action" : "",
 "is_selected" : False},
{"drug" : "Amiodarone",
 "name" : "[b]Amiodarone[/b]",
 "adult dosage" : "C-05, CA-03",
 "pedi dosage" : "PC-03, PCA-03",
 "indications" : "",
 "contraindications" : "",
 "adverse effects" : "",
 "class" : "",
 "pharmacokinetics" : "",
 "action" : "",
 "is_selected" : False},
{"drug" : "Fentanyl Citrate",
 "name" : "[b]Fentanyl Citrate[/b]",
 "adult dosage" : "[b]Burns:[/b] 1mcg/kg IV q 5 mins (Max Total 400mcg)\
with SBP > 100mmHg\n\
[b]Other[/b]: 1mcg/kg IV/IM/IN may repeat 0.5mcg/kg q 5 mins (Max Total 300mcg) \
with SBP > 100mmHg",
 "pedi dosage" : "N/A",
 "indications" : "",
 "contraindications" : "",
 "adverse effects" : "",
 "class" : "",
 "pharmacokinetics" : "",
 "action" : "",
 "is_selected" : False},
{"drug" : "Enalprilat (Vasotec)",
 "name" : "[b]Enalaprilat (Vasotec)[/b]",
 "adult dosage" : "1.25mg IV if SBP >= 140mmHg",
 "pedi dosage" : "N/A",
 "indications" : "",
 "contraindications" : "",
 "adverse effects" : "",
 "class" : "",
 "pharmacokinetics" : "",
 "action" : "",
 "is_selected" : False},
{"drug" : "Calcium Chloride",
 "name" : "[b]Calcium Chloride[/b]",
 "adult dosage" : "1g IV over 10 minutes",
 "pedi dosage" : "N/A",
 "indications" : "",
 "contraindications" : "",
 "adverse effects" : "",
 "class" : "",
 "pharmacokinetics" : "",
 "action" : "",
 "is_selected" : False},
{"drug" : "Ondansetron (Zofran)",
 "name" : "[b]Ondansetron (Zofran)[/b]",
 "adult dosage" : "4mg IV/IM or 4mg PO (ODT)",
 "pedi dosage" : "N/A",
 "indications" : "",
 "contraindications" : "",
 "adverse effects" : "",
 "class" : "",
 "pharmacokinetics" : "",
 "action" : "",
 "is_selected" : False}]

drug_data = {}
for drug_record in drug_data_list_of_dicts:
    drug_data[drug_record["drug"]] = {}
    drug_data[drug_record["drug"]] = \
            dict({"drug" : drug_record["drug"],
                  "name": drug_record["name"],
                  "adult dosage": drug_record["adult dosage"],
                  "pedi dosage" : drug_record["pedi dosage"],
                  "indications" : drug_record["indications"],
                  "contraindications" : drug_record["contraindications"],
                  "adverse effects" : drug_record["adverse effects"],
                  "class" : drug_record["class"],
                  "pharmacokinetics" : drug_record["pharmacokinetics"],
                  "action" : drug_record["action"],
                  "is_selected": drug_record["is_selected"]})
            
drugs = []
for drug in sorted(drug_data):
    drugs.append(drug_data[drug]["drug"])
    
drug_detail = []
for detail in sorted(drug_data):
    drug_detail.append(drug_data[str(detail)]["name"])
    drug_detail.append(drug_data[str(detail)]["adult dosage"])
    drug_detail.append(drug_data[str(detail)]["pedi dosage"])
    drug_detail.append(drug_data[str(detail)]["indications"])
    drug_detail.append(drug_data[str(detail)]["contraindications"])
    drug_detail.append(drug_data[str(detail)]["adverse effects"])
    drug_detail.append(drug_data[str(detail)]["class"])
    drug_detail.append(drug_data[str(detail)]["pharmacokinetics"])
    drug_detail.append(drug_data[str(detail)]["action"])
    
detail_text = ""
for detail in sorted(drug_data):
    detail_text += str(drug_data[detail]["adult dosage"])
    
print detail_text
