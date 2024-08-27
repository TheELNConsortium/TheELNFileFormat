# AI4Green

## Information

* Repo: https://github.com/AI4Green/AI4Green
* Website: https://ai4green.app/

### Structure of the AI4Green example

This AI4Green export is for a single reaction

Key parts of the reaction dataset are:
- The text field which renders the summary table in HTML
- Automatically generated .RDF (reaction data file) attachment and any additional file attachments

## Concepts used

Here is a correspondance between concepts in AI4Green and how they are translated in the metadata json file in the archive:

| AI4Green concepts          | JSON property  |
|----------------------------|----------------|
| summary_table              | text           ||
| comment                    | comment        |
| description (experimental) | description    |
| mimetype                   | encodingFormat |
| time_of_creation           | dateCreated    ||
| time_of_update             | dateModified   |
| author                     | author         ||
| name                       | name           |


### export.eln
```json
{
    "@context": "https://w3id.org/ro/crate/1.1/context",
    "@graph": [
        {
            "@id": "ro-crate-metadata.json",
            "@type": "CreativeWork",
            "about": {
                "@id": "./"
            },
            "conformsTo": {
                "@id": "https://w3id.org/ro/crate/1.1"
            },
            "schemaVersion": "1.0",
            "dateCreated": "2024-08-27 11:01:48",
            "parentOrganization": {
                "@id": "#university-of-nottingham",
                "@type": "Organization",
                "name": "University of Nottingham",
                "logo": "https://www.nottingham.ac.uk/Brand/LegacyAssets/images-multimedia/2022/Logos/BrandEvolution-NottinghamBlue-Cropped-450x173.png",
                "url": "https://www.nottingham.ac.uk/"
            },
            "sdPublisher": {
                "@type": "Organization",
                "name": "AI4Green",
                "slogan": "AI for Green Chemistry. Electronic Lab Notebook with Machine Learning Support.",
                "url": "https://www.ai4green.app",
                "parentOrganization": "#university-of-nottingham"
            },
            "version": "1.0"
        },
        {
            "@id": "#ro-crate_created",
            "@type": "CreateAction",
            "object": {
                "@id": "./"
            },
            "name": "RO-Crate created",
            "endTime": "2024-08-27 11:01:48",
            "instrument": {
                "@id": "https://www.ai4green.app",
                "@type": "SoftwareApplication",
                "name": "AI4Green",
                "version": "1.6.0",
                "git_commit_hash": "b6e1157",
                "identifier": "https://www.ai4green.app"
            },
            "actionStatus": {
                "@id": "http://schema.org/CompletedActionStatus"
            }
        },
        {
            "@id": "./",
            "@type": [
                "Dataset"
            ],
            "hasPart": [
                {
                    "@id": "./AI4-001/"
                }
            ]
        },
        {
            "@id": "./AI4-001/",
            "@type": "Dataset",
            "name": "Amidation",
            "author": {
                "@id": "./author/7"
            },
            "dateCreated": "2024-07-18 15:56:12",
            "dateModified": "2024-07-18 16:05:51",
            "comment": [
                {
                    "@id": "comment-id/AI4-001/5"
                }
            ],
            "hasPart": [
                {
                    "@id": "./AI4-001/AI4-001.rxn"
                },
                {
                    "@id": "./AI4-001/AI4-001.json"
                },
                {
                    "@id": "./AI4-001/AI4-001-summary.pdf"
                }
            ],
            "description": "Benzoic acid, ethylamine, diisopropylamine and HATU were mixed at RT for 2 hours. The reaction mixture was washed with aqueous sodium chloride and extracted in ethyl acetate. The resultant mixture was concentrated under vacuum and purified by silica gel, eluting at 70% ethyl acetate 30% cyclohexane. This yielded an off-white solid (100 mg, 82%). ",
            "text": "<h2>AI4-001</h2><div>Reaction Smiles: OC(=O)C1=CC=CC=C1.CCN>>CCNC(=O)C1=CC=CC=C1<div id=\"section-to-print\">\n<table class=\"table table-sm\">\n<tbody><tr>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>№</b></td>\n<td style=\"width:30%; background-color: rgb(184, 184, 184);\"><b>Reactants/catalysts/reagents</b></td>\n<td style=\"width:10%; background-color: rgb(184, 184, 184);\"><b>Mol.Wt</b></td>\n<td style=\"width:10%; background-color: rgb(184, 184, 184);\"><b>Density (g/mL)</b></td>\n<td style=\"width:10%; background-color: rgb(184, 184, 184);\"><b>Conc. (M)</b></td>\n<td style=\"width:10%; background-color: rgb(184, 184, 184);\"><b>Equiv.</b></td>\n<td style=\"width:10%; background-color: rgb(184, 184, 184);\"><b>Amount (mmol)</b></td>\n<td style=\"width:10%; background-color: rgb(184, 184, 184);\"><b>Volume (mL)</b></td>\n<td style=\"width:10%;background-color: rgb(184, 184, 184);\"><b>Mass (mg)</b></td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">1</td>\n<td>Benzoic Acid</td>\n<td>122.12</td>\n<td><input readonly=\"\" style=\"width:80px; border:none\" type=\"number\" value=\"\"/></td>\n<td><input readonly=\"\" style=\"width:80px; border:none\" type=\"number\" value=\"\"/></td>\n<td>1</td>\n<td>0.82</td>\n<td>0.00</td>\n<td>100</td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">2</td>\n<td>Ethylamine</td>\n<td>45.08</td>\n<td><input readonly=\"\" style=\"width:80px; border:none\" type=\"number\" value=\"\"/></td>\n<td><input readonly=\"\" style=\"width:80px; border:none\" type=\"number\" value=\"\"/></td>\n<td>2</td>\n<td>1.64</td>\n<td>0.00</td>\n<td>73.8</td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">3</td>\n<td>Diisopropylamine</td>\n<td>101.19</td>\n<td>0.717</td>\n<td><input readonly=\"\" style=\"width:80px; border:none\" type=\"number\" value=\"\"/></td>\n<td>1.4</td>\n<td>1.15</td>\n<td>0.16</td>\n<td>116</td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">4</td>\n<td>O-(7-Azabenzotriazol-1-yl)-N,N,N',N'-tetramethyluronium hexafluorophosphate</td>\n<td>380.23</td>\n<td><input readonly=\"\" style=\"width:80px; border:none\" type=\"number\" value=\"\"/></td>\n<td><input readonly=\"\" style=\"width:80px; border:none\" type=\"number\" value=\"\"/></td>\n<td>1.2</td>\n<td>0.98</td>\n<td>0.00</td>\n<td>374</td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\"></td>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>Solvents</b></td>\n<td style=\"background-color: rgb(184, 184, 184);\"></td>\n<td style=\"background-color: rgb(184, 184, 184);\"></td>\n<td style=\"background-color: rgb(184, 184, 184);\"></td>\n<td id=\"scrollToUnreacted\" style=\"background-color: rgb(184, 184, 184);\"></td>\n<td style=\"background-color: rgb(184, 184, 184);\"></td>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>Volume (mL)</b></td>\n<td style=\"background-color: rgb(184, 184, 184);\"></td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">5</td>\n<td>Dimethylformamide</td>\n<td></td>\n<td></td>\n<td></td>\n<td></td>\n<td></td>\n<td>1</td>\n<td></td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\"></td>\n<td id=\"summary-product-cell\" style=\"background-color: rgb(184, 184, 184);\"><b>Product</b></td>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>Mol.Wt</b></td>\n<td colspan=\"2\" style=\"background-color: rgb(184, 184, 184);\"><b>Theoretical Yield (mg)</b></td>\n<td style=\"background-color: rgb(184, 184, 184);\" title=\"The approximate mass of the limiting reactant which has not reacted. Used to calculate the reaction conversion.\"><b>Unreacted (mg)</b><i class=\"bi bi-info-circle\"></i></td>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>Product Mass (mg)</b></td>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>% Yield</b></td>\n<td style=\"background-color: rgb(184, 184, 184);\"></td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">6</td>\n<td>N-Ethylbenzamide</td>\n<td>149.19</td>\n<td colspan=\"2\">122</td>\n<td>5</td>\n<td>100</td>\n<td>81.86</td>\n<td></td>\n</tr>\n<input id=\"js-limited-reactant-mass\" type=\"hidden\" value=\"100\"/>\n<input id=\"js-main-product-mass\" type=\"hidden\" value=\"122.16672125777923\"/>\n<tr><td colspan=\"9\"> </td></tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\"></td>\n<td colspan=\"2\" style=\"background-color: rgb(184, 184, 184);\"><b>Hazards</b></td>\n<td colspan=\"2\" style=\"background-color: rgb(184, 184, 184);\"><b>Hazard Rating</b></td>\n<td colspan=\"2\" style=\"background-color: rgb(184, 184, 184);\"><b>Exposure Potential</b></td>\n<td colspan=\"2\" style=\"background-color: rgb(184, 184, 184);\"><b>Risk Rating</b></td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">1</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Reactant-Hazard-Sentence1\">H315 Causes skin irritation, H318 Causes serious eye damage, H372 Causes damage to organs through prolonged or repeated exposure</td>\n<td class=\"hazard-hazardous to-export-hazard-matrix\" colspan=\"2\" id=\"Reactant-Hazard-Rating1\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">VH</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Reactant-Exposure-Potential1\">L</td>\n<td class=\"hazard-reset-hazard to-export-hazard-matrix\" colspan=\"2\" id=\"Reactant-Risk-Rating1\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">H</td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">2</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Reactant-Hazard-Sentence2\">H220 Extremely flammable gas, H319 Causes serious eye irritation, H335 May cause respiratory irritation</td>\n<td class=\"hazard-reset-hazard to-export-hazard-matrix\" colspan=\"2\" id=\"Reactant-Hazard-Rating2\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">H</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Reactant-Exposure-Potential2\">H</td>\n<td class=\"hazard-reset-hazard to-export-hazard-matrix\" colspan=\"2\" id=\"Reactant-Risk-Rating2\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">H</td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">3</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Reagent-Hazard-Sentence1\">H225 Highly Flammable liquid and vapor, H302 Harmful if swallowed, H314 Causes severe skin burns and eye damage, H332 Harmful if inhaled</td>\n<td class=\"hazard-reset-hazard to-export-hazard-matrix\" colspan=\"2\" id=\"Reagent-Hazard-Rating1\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">H</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Reagent-Exposure-Potential1\">M</td>\n<td class=\"hazard-reset-hazard to-export-hazard-matrix\" colspan=\"2\" id=\"Reagent-Risk-Rating1\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">H</td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">4</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Reagent-Hazard-Sentence2\">H228 Flammable solid, H315 Causes skin irritation, H317 May cause an allergic skin reaction, H319 Causes serious eye irritation, H335 May cause respiratory irritation</td>\n<td class=\"hazard-hazardous to-export-hazard-matrix\" colspan=\"2\" id=\"Reagent-Hazard-Rating2\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">VH</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Reagent-Exposure-Potential2\">L</td>\n<td class=\"hazard-reset-hazard to-export-hazard-matrix\" colspan=\"2\" id=\"Reagent-Risk-Rating2\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">H</td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">5</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Solvent-Hazard-Sentence1\">H226 Flammable liquid and vapor, H312 Harmful in contact with skin, H319 Causes serious eye irritation, H332 Harmful if inhaled, H360D May damage the unborn child</td>\n<td class=\"hazard-reset-hazard to-export-hazard-matrix\" colspan=\"2\" id=\"Solvent-Hazard-Rating1\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">VH</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Solvent-Exposure-Potential1\">L</td>\n<td class=\"hazard-reset-hazard to-export-hazard-matrix\" colspan=\"2\" id=\"Solvent-Risk-Rating1\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">H</td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\">6</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Product-Hazard-Sentence1\">H302 Harmful if swallowed</td>\n<td class=\"hazard-reset-hazard to-export-hazard-matrix\" colspan=\"2\" id=\"Product-Hazard-Rating1\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">M</td>\n<td class=\"to-export-hazard-matrix\" colspan=\"2\" id=\"Product-Exposure-Potential1\">L</td>\n<td class=\"hazard-reset-hazard to-export-hazard-matrix\" colspan=\"2\" id=\"Product-Risk-Rating1\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">L</td>\n</tr>\n<tr>\n<td colspan=\"5\"></td>\n<td colspan=\"2\">Risk Rating:</td>\n<td class=\"hazard-hazardous to-export-hazard-matrix\" colspan=\"2\" id=\"Overall-Risk-Rating\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">VH</td>\n</tr>\n<tr><td colspan=\"9\"> </td></tr>\n<tr><td colspan=\"9\" style=\"background-color: rgb(184, 184, 184);\"><b>Sustainability (CHEM21)</b></td></tr>\n<tr>\n<td colspan=\"2\" style=\"vertical-align: top;\">\n<table class=\"table table-sm w-auto\">\n<tbody><tr>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>Solvents</b></td>\n</tr>\n<tr>\n<td class=\"hazard-hazardous\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">Dimethylformamide</td>\n</tr>\n</tbody></table>\n</td>\n<td colspan=\"7\" style=\"vertical-align: top;\">\n<table class=\"nested-table\">\n<tbody><tr>\n<td style=\"width: 14%; background-color: rgb(184, 184, 184);\"><b>Safety</b></td>\n<td style=\"width: 14%; background-color: rgb(184, 184, 184);\"><b>Temp ℃</b></td>\n<td style=\"width: 14%; background-color: rgb(184, 184, 184);\">\n<a href=\"https://ai4green.app/element_sustainability\" style=\"color: #333333\" target=\"_blank\">\n<b>Elements <i class=\"fa fa-external-link\"></i></b>\n</a>\n</td>\n<td style=\"width: 14%; background-color: rgb(184, 184, 184);\"><b>Batch/flow</b></td>\n<td style=\"width: 14%; background-color: rgb(184, 184, 184);\"><b>Isolation</b></td>\n<td style=\"width: 14%; background-color: rgb(184, 184, 184);\"><b>Stoichiometry</b></td>\n<td style=\"width: 14%; background-color: rgb(184, 184, 184);\"><b>Cat. Recovery</b></td>\n</tr>\n<tr>\n<td class=\"hazard-hazardous\" id=\"js-safety-cell\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">VH</td>\n<td class=\"hazard-acceptable\" id=\"js-temperature-cell\" style=\"background-color: rgb(0, 255, 0) !important; color: rgb(0, 0, 0);\">20</td>\n<td class=\"hazard-warning\" id=\"js-elements-cell\" style=\"background-color: rgb(255, 255, 0) !important; color: rgb(0, 0, 0);\"><select class=\"hazard-warning\" id=\"js-elements\" size=\"1\" style=\"background-color: rgb(255, 255, 0) !important; color: rgb(0, 0, 0);\">\n\n\n<option class=\"hazard-warning\" selected=\"\" style=\"background-color: rgb(255, 255, 0) !important; color: rgb(0, 0, 0);\">50-500 years</option>\n\n</select></td>\n<td class=\"hazard-warning\" id=\"js-batch-flow-cell\" style=\"background-color: rgb(255, 255, 0) !important; color: rgb(0, 0, 0);\"><select class=\"hazard-warning\" id=\"js-batch-flow\" size=\"1\" style=\"background-color: rgb(255, 255, 0) !important; color: rgb(0, 0, 0);\">\n\n<option class=\"hazard-warning\" style=\"background-color: rgb(255, 255, 0) !important; color: rgb(0, 0, 0);\">Batch</option>\n\n</select></td>\n<td class=\"hazard-hazardous\" id=\"js-isolation-cell\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\"><select class=\"hazard-hazardous\" id=\"js-isolation\" size=\"1\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">\n\n<option class=\"hazard-hazardous\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">Column</option>\n\n\n\n\n\n\n\n</select></td>\n<td class=\"hazard-hazardous\" id=\"js-catalyst-cell\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\"><select class=\"hazard-hazardous\" id=\"js-catalyst\" size=\"1\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">\n\n\n\n\n<option class=\"hazard-hazardous\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">Excess reagents</option>\n</select></td>\n<td class=\"hazard-reset-hazard\" id=\"js-recovery-cell\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\"><select class=\"hazard-reset-hazard\" id=\"js-recovery\" size=\"1\" style=\"background-color: rgb(255, 255, 255) !important; color: rgb(0, 0, 0);\">\n\n\n\n</select></td>\n</tr>\n<tr>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>Atom Efficiency</b></td>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>Mass Efficiency</b></td>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>Yield</b></td>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>Conversion</b></td>\n<td style=\"background-color: rgb(184, 184, 184);\"><b>Selectivity</b></td>\n<td colspan=\"2\" style=\"background-color: rgb(184, 184, 184);\"></td>\n</tr>\n<tr>\n<td class=\"hazard-hazardous\" id=\"js-ae-cell\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">23.0</td>\n<td class=\"hazard-hazardous\" id=\"js-me-cell\" style=\"background-color: rgb(255, 0, 0) !important; color: rgb(0, 0, 0);\">15</td>\n<td class=\"hazard-warning\" id=\"js-yield-cell\" style=\"background-color: rgb(255, 255, 0) !important; color: rgb(0, 0, 0);\">81.86</td>\n<td class=\"hazard-acceptable\" id=\"js-conversion-cell\" style=\"background-color: rgb(0, 255, 0) !important; color: rgb(0, 0, 0);\">95</td>\n<td class=\"hazard-warning\" id=\"js-selectivity-cell\" style=\"background-color: rgb(255, 255, 0) !important; color: rgb(0, 0, 0);\">86</td>\n<td colspan=\"2\"></td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n<tr>\n<td colspan=\"9\" style=\"background-color: rgb(184, 184, 184);\"><b>Standard Protocols:</b></td>\n</tr>\n<tr>\n<td colspan=\"9\">\n<table class=\"table table-sm w-auto\">\n<tbody><tr>\n\n\n\n\n\n<td></td>\n</tr>\n<tr>\n\n\n\n\n\n<td></td>\n</tr>\n<tr>\n\n\n\n\n\n<td></td>\n</tr>\n<tr>\n<td colspan=\"6\" style=\"background-color: rgb(184, 184, 184);\"><b>Disposal of Waste Materials:</b></td>\n</tr>\n<tr>\n<td><input class=\"to-export-checkbox\" id=\"nonHalogenatedSolvent\" name=\"Disposal Non-Halogenated Solvent\" type=\"checkbox\"/><label for=\"nonHalogenatedSolvent\">Non-Halogenated Solvent</label></td>\n\n\n\n<td></td>\n<td></td>\n</tr>\n<tr>\n<td colspan=\"6\" style=\"background-color: rgb(184, 184, 184);\"><b>Spillage Procedure:</b></td>\n</tr>\n<tr>\n<td><input class=\"to-export-checkbox\" id=\"standardSpillResponse\" name=\"Spillage Procedure Standard\" type=\"checkbox\"/><label for=\"standardSpillResponse\">Standard Spill Response</label></td>\n\n<td></td>\n<td></td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n<tr>\n<td colspan=\"9\" style=\"background-color: rgb(184, 184, 184);\">\n<b>Other Risks, controls, containment, location and PPE.</b><br/>\n            (Hazardous by Products. Exothermic reactions. The need to inform others of risks. Lab and hood number.)</td>\n</tr>\n<tr>\n<td colspan=\"9\"><textarea class=\"text-in-table\" id=\"other-risks-textbox\" style=\"width: 100%; background-color: white;\"></textarea></td>\n</tr>\n<tr>\n<td colspan=\"9\" style=\"background-color: rgb(184, 184, 184);\"><b>Hazard categorisation given GLP and other controls\n                specified</b></td>\n</tr>\n<tr>\n<td colspan=\"9\">\n<table class=\"nested-table-noborder\">\n<tbody><tr>\n<td style=\"width: 25%\">Hazard<br/><i>Potential to cause harm</i></td>\n<td style=\"width: 25%\">\n<input class=\"js-hazard to-export-risk\" id=\"slight\" name=\"hazard\" type=\"radio\" value=\"1\"/>\n<label for=\"slight\"><b>1. Slight</b></label><br/>\n<input class=\"js-hazard to-export-risk\" id=\"serious\" name=\"hazard\" type=\"radio\" value=\"2\"/>\n<label for=\"serious\">2. Serious</label><br/>\n<input class=\"js-hazard to-export-risk\" id=\"major\" name=\"hazard\" type=\"radio\" value=\"3\"/>\n<label for=\"major\">3. Major</label></td>\n<td style=\"width: 25%\"><b>Risk Category (A-D)<br/>\n<br/><input disabled=\"\" id=\"categoryA\" name=\"category\" type=\"radio\" value=\"A\"/>\n<label for=\"categoryA\">A (10-27)</label></b></td>\n<td style=\"width: 25%\"><b>Risk Score HxRxC</b></td>\n</tr>\n<tr>\n<td>Risk<br/><i>Likelihood of exposure</i></td>\n<td>\n<input class=\"js-risk to-export-risk\" id=\"lowLikelihood\" name=\"risk\" type=\"radio\" value=\"1\"/>\n<label for=\"lowLikelihood\">1. Low likelihood</label><br/>\n<input class=\"js-risk to-export-risk\" id=\"possible\" name=\"risk\" type=\"radio\" value=\"2\"/>\n<label for=\"possible\"><b>2. Possible</b></label><br/>\n<input class=\"js-risk to-export-risk\" id=\"frequentOccur\" name=\"risk\" type=\"radio\" value=\"3\"/>\n<label for=\"frequentOccur\">3. Frequent Occur</label></td>\n<td><br/><b><input disabled=\"\" id=\"categoryB\" name=\"category\" type=\"radio\" value=\"B\"/>\n<label for=\"categoryB\">B (6-9)</label></b></td>\n<td>4</td>\n</tr>\n<tr>\n<td>Consequences<br/><i>Who will be affected</i></td>\n<td>\n<input class=\"js-consequences to-export-risk\" id=\"individual\" name=\"consequences\" type=\"radio\" value=\"1\"/>\n<label for=\"individual\">1. Individual</label><br/>\n<input class=\"js-consequences to-export-risk\" id=\"localLabs\" name=\"consequences\" type=\"radio\" value=\"2\"/>\n<label for=\"localLabs\"><b>2. Local Labs</b></label><br/>\n<input class=\"js-consequences to-export-risk\" id=\"buildingWide\" name=\"consequences\" type=\"radio\" value=\"3\"/>\n<label for=\"buildingWide\">3. Building wide</label>\n</td>\n<td><b><input class=\"js-consequences\" disabled=\"\" id=\"categoryC\" name=\"category\" type=\"radio\" value=\"C\"/>\n<label for=\"categoryC\">C (3-5)</label><br/>\n<br/><input disabled=\"\" id=\"categoryD\" name=\"category\" type=\"radio\" value=\"D\"/>\n<label for=\"categoryD\">D (1-2)</label></b></td>\n<td></td>\n</tr>\n<tr>\n<td>Signed:</td><td></td><td></td><td></td>\n</tr>\n<tr>\n<td colspan=\"4\"><br/></td>\n</tr>\n<tr>\n<td colspan=\"2\">Researcher:Joe Davies</td>\n<td colspan=\"2\">Supervisor:Super Joe Davies</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody></table>\n</div></div>",
            "encodingFormat": "text/html",
            "url": "https://www.ai4green.app/Development-Workgroup/Export%20workbook/AI4-001/no"
        },
        {
            "@id": "./AI4-001/AI4-001.rxn",
            "@type": "File",
            "name": "AI4-001.rxn",
            "description": "A Chemistry specific format with molecules represented in a Chemical Table format and assigned as reactants, products, or agents",
            "encodingFormat": "chemical/x-mdl-rxn",
            "contentSize": "5462",
            "sha256": "62d571bac873051fee6cc8ee5f1c82d0ede91485ec65f5778aceba2fdb889bd5",
            "dateModified": "2024-08-27 11:01:48"
        },
        {
            "@id": "./AI4-001/AI4-001.json",
            "@type": "File",
            "name": "AI4-001.json",
            "description": "A structured data format commonly used for exchanging information between servers and web applications. Keys and values are used to describe reaction metadata",
            "encodingFormat": "application/json",
            "contentSize": "3130",
            "sha256": "76b8252281b387d436d198a828e2e6e3d3e24d44d76164ac65f545f2ab83d873",
            "dateModified": "2024-08-27 11:01:48"
        },
        {
            "@id": "./AI4-001/AI4-001-summary.pdf",
            "@type": "File",
            "name": "AI4-001-summary.pdf",
            "description": "Reaction data uploaded by user",
            "encodingFormat": "application/pdf",
            "contentSize": "853054",
            "sha256": "2d08aa4e44fd2ad86dbb30e48ace404c4b621e0571bc57f36deb6ccf071ed897",
            "dateModified": "2024-07-18T16:05:59.731019"
        },
        {
            "@id": "comment-id/AI4-001/5",
            "@type": "Comment",
            "dateCreated": "2024-07-18T15:08:59.608458",
            "text": "Some compound may have been lost in the aqueous phase during the extraction",
            "author": {
                "@id": "./author/7"
            }
        },
        {
            "@id": "./author/7",
            "@type": "Person",
            "givenName": "Joe",
            "familyName": "Davies",
            "email": "joseph.davies@nottingham.ac.uk"
        }
    ]
}
```