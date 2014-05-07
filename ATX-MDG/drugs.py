# drug dictionary as a list and data structure holding drugs

drug_data_list_of_dicts = [
{"drug" : "Adenosine",
 "name" : "[b]Adenosine[/b]",
 "adult dosage" : "12mg rapid IV repeat x1 (Max 24mg) - 10mL flush after each dose",
 "is_selected" : False},
{"drug" : "Fentanyl Citrate",
 "name" : "[b]Fentanyl Citrate[/b]",
 "adult dosage" : "[b]Burns:[/b] 1mcg/kg IV q 5 mins (Max Total 400mcg)\n\
with SBP > 100mmHg\n\
[b]Other[/b]: 1mcg/kg IV/IM/IN may repeat 0.5mcg/kg q 5 mins (Max Total 300mcg) \
with SBP > 100mmHg",
 "is_selected" : False},
{"drug" : "Enalprilat (Vasotec)",
 "name" : "[b]Enalaprilat (Vasotec)[/b]",
 "adult dosage" : "1.25mg IV if SBP >= 140mmHg",
 "is_selected" : False},
{"drug" : "Calcium Chloride",
 "name" : "[b]Calcium Chloride[/b]",
 "adult dosage" : "1g IV over 10 minutes",
 "is_selected" : False},
{"drug" : "Ondansetron (Zofran)",
 "name" : "[b]Ondansetron (Zofran)[/b]",
 "adult dosage" : "4mg IV/IM or 4mg PO (ODT)",
 "is_selected" : False}]

drug_data = {}
for drug_record in drug_data_list_of_dicts:
    drug_data[drug_record["drug"]] = {}
    drug_data[drug_record["drug"]] = \
            dict({"drug" : drug_record["drug"],
                  "name": drug_record["name"],
                  "adult dosage": drug_record["adult dosage"],
                  "is_selected": drug_record["is_selected"]})
            
drugs = []
for drug in sorted(drug_data):
    drugs.append(drug_data[drug]["drug"])
    
drug_detail = []
for detail in sorted(drug_data):
    drug_detail.append(drug_data[str(detail)]["name"])
    drug_detail.append(drug_data[str(detail)]["adult dosage"])
    
print drug_detail
