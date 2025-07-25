# ML4Porous
Summarize the machine learning research on porous materials such as COF/MOF/Zeolite so far.<br><br>                                                                
![Reported database, software and tools](/figs/years.png "years")                   
                                                 
                                      
### Band gap models
**unit**: eV
| DOI | Model | ${R^{2}}$ | MAE | RMSE | SRCC | Year | Database (# of Total Points) | Train: Val: Test |
|:----------|:------|:---|:----|:-----|:-----|:------|:------|:------|
| 10.1016/j.matt.2021.02.015   | [CGCNN](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning/cgcnn) | 0.876 | 0.274 | - | 0.932 | 2021 | [QMOF](https://github.com/Andrew-S-Rosen/QMOF)-PBE-D3(BJ) (14,482) | 0.8 : 0.1 : 0.1 |
| | [KRR (SOAP)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning/soap_kernel) | 0.822 | 0.357 | - | 0.910 | 2021 | QMOF-PBE-D3(BJ) (14,482) | 0.8 : - : 0.2 |
| | [KRR (Orbital field matrix)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning/orbital_field_matrix) | 0.763 | 0.417 | - | 0.863 | 2021 | QMOF-PBE-D3(BJ) (14,482) | 0.8 : - : 0.2 |
| | [KRR (Stoichiometric-120)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning/meredig_stoichiometric_120) | 0.750 | 0.433 | - | 0.847 | 2021 | QMOF-PBE-D3(BJ) (14,482) | 0.8 : - : 0.2 |
| | [KRR (Stoichiometric-45)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning/he_stoichiometric_45) | 0.743 | 0.437 | - | 0.842 | 2021 | QMOF-PBE-D3(BJ) (14,482) | 0.8 : - : 0.2 |
| | [KRR (Sine Coulomb matrix)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning/sine_matrix) | 0.643 | 0.529 | - | 0.787 | 2021 | QMOF-PBE-D3(BJ) (14,482) | 0.8 : - : 0.2 |
| | [KRR (Constant mean model)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning) | - | 0.973 | - | - | 2021 | QMOF-PBE-D3(BJ) (14,482) | 0.8 : - : 0.2 |
| 10.1107/S1600576722009797    | [CNN from PXRD](https://github.com/gomezperalta/band-gap_pxrd/) | - | 0.492 | 0.674 | - | 2022 | QMOF-PBE-D3(BJ) (16,029) | 0.8 : - : 0.2 |
| 10.1021/acsami.3c10323       | [PMTransformer](https://github.com/hspark1212/MOFTransformer)  | - | 0.216 | - | - | 2023 | QMOF-PBE-D3(BJ) (20,000) | 0.8 : 0.1 : 0.1 |
| 10.1038/s42256-023-00628-2   | [MOFTransformer](https://github.com/hspark1212/MOFTransformer) | - | 0.224 | - | - | 2023 | QMOF-PBE-D3(BJ) (20,000) | 0.8 : 0.1 : 0.1 |
| 10.1021/jacs.2c11420         | [MOFormer](https://github.com/zcao0420/MOFormer) | - | 0.387 | - | - | 2023 | QMOF-PBE-D3(BJ) (7,466) | 0.8 : - : 0.2 |
| 10.1021/acs.jpclett.3c00187  | CGCNN | 0.709 | 0.393 | 0.585 | - | 2023 | QMOF-HSE06 (10,811) | 0.8 : 0.1 : 0.1 |
| | MEGNet | 0.767 | 0.368 | 0.523 | - |  2023 | QMOF-HSE06 (10,811) | 0.8 : 0.1 : 0.1 |
| | MEGNet-tuned | 0.787 | 0.332 | 0.500 | - |  2023 | QMOF-HSE06 (10,811) | 0.8 : 0.1 : 0.1 |
| 10.1002/adfm.202313596       | CGCNN | 0.820 | 0.330 | - | - | 2023 | QMOF-HSE06 (10,811) | 0.8 : 0.1 : 0.1 |
| 10.26434/chemrxiv-2024-0mkw8 | RR | 0.169 | 0.091 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | LIR | 0.000 | 0.099 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | SGD | -0.001 | 0.099 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | PAR | 0.178 | 0.091 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | SVR | 0.355 | 0.080 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | KNR | 0.315 | 0.080 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | NNR | 0.180 | 0.086 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | ETR | 0.542 | 0.063 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | GBR | 0.436 | 0.075 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | BR  | 0.475 | 0.067 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | ABR | 0.391 | 0.083 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| | RFR | 0.424 | 0.066 | - | - | 2023 | [EC-MOF](https://ec-mof.njit.edu/)-PBE-D3-U (1,063) | 0.9 : - : 0.1 |
| [AI2ASE 2025](https://ai-2-ase.github.io/papers/27_1_AAAI_2025_AI4ASE_workshop_MOF.pdf) | [M-MOFormer](https://github.com/IkeYang/M-MOFormer) | - | 0.359 | - | - | 2025 | QMOF-PBE-D3(BJ) (unknown) | 0.7 : 0.15 : 0.15 |
| 10.1039/D3RA02142D       | CGCNN |  | 0.149 | 0.208 | - | 2023 | QMOF-HSE06 | 0.8 : 0.2 |             
|        | GCN |  | 0.146 | 0.277 | - | 2023 | QMOF & PMOF - PBE | 0.8 : 0.2 : - |           
|        | MEGNet | | 0.154 | 0.267 | - | 2023 | QMOF & PMOF - PBE | 0.8 : 0.2 : - |           
|        | SchNet |  | 0.241 | 0.368 | - | 2023 |QMOF & PMOF - PBE | 0.8 : 0.2 : - |           






### Partial atomic charge models
**unit**: e
| Reference | Model | ${R^{2}}$ | MAE | RMSE | Target | Framework | Year | Database (# of Total Points) | Train: Val: Test |
|:----------|:----------|:-------|:-------|:-------|:-------|:-----------|:-----|:-----|:-----|
| 10.1021/acs.jpcc.0c04903 | [MPNN](https://github.com/SimonEnsemble/mpn_charges) | - | 0.0250 | - | DDEC | MOF | 2020 | [CoRE MOF 2014 DDEC (2,266)](https://zenodo.org/records/3986573) | 0.7 : 0.1 : 0.2 |
| 10.1021/acs.chemmater.0c02468 | [GBDT](https://github.com/scidatasoft/mof/) | - | 0.0096 | 0.0176 | DDEC | MOF | 2020 | CoRE MOF 2014 DDEC (2,932)| 0.9 : - : 0.1 |
|  |  | - | 0.0500 | - | DDEC | COF | 2020 | CURATED COF (460) | 0.9 : - : 0.1 |
| 10.1021/acs.jctc.0c01229 | [PACMOF-v1](https://github.com/arung-northwestern/pacmof) | 0.9952 | 0.0192 | 0.0337 | DDEC6 | MOF | 2021 |  [CoRE MOF 2019 (2,974)](https://zenodo.org/records/14184621) | 0.8 : 0.2 |
|  |  | 0.9241 | 0.0570 | - | DDEC | porous molecular crystals | 2021 |  CoRE MOF 2019 (2,974) | 0.8 : 0.2 |
|  |  | 0.9969 | 0.0100 | - | CM5 | MOF | 2021 |  CoRE MOF 2019 (2,974) | 0.8 : 0.2 |
|  |  | 0.9175 | 0.0360 | - | CM5 | porous molecular crystals | 2021 |  CoRE MOF 2019 (2,974) | 0.8 : 0.2 |
| 10.1038/s41524-024-01277-8 | [AL-GNN](https://github.com/tummfm/mof-al) | - | 0.0290 | - | DDEC6 | MOF | 2024 | QMOF (11,173) | 0.8 : 0.08 : 0.12 |
|  | | - | 0.0368 | - | DDEC6 | Zeolite | 2024 | [ARC-MOF](https://zenodo.org/records/13891643) (without DB12 and DB1) | benchmark |
|  | | - | 0.0239 | - | DDEC6 | MOF | 2024 | ARC-MOF (without DB12 and DB1) | benchmark |
| 10.1021/acs.jctc.4c00434 | [PACMAN](https://github.com/mtap-research/PACMAN-charge) | 0.9994 | 0.0055 | 0.0094 | DDEC6 | MOF | 2024 | QMOF (16,779) | 0.8 : 0.1 : 0.1 |
|  | | 0.9996 | 0.0032 | 0.0051 | CM5 | MOF | 2024 | QMOF (16,779) | 0.8 : 0.1 : 0.1 |
|  | | 0.9976 | 0.0224 | 0.0358 | Bader | MOF | 2024 | QMOF (11,230) | 0.8 : 0.1 : 0.1 |
|  | | 0.9722 | 0.0419 | 0.0419 | REPEAT | MOF | 2024 | ARC-MOF (40,000) | 0.8 : 0.1 : 0.1 |
|  | | 0.9927 | 0.0095 | 0.0159 | DDEC6 | COF | 2024 | [CURATED COF](https://github.com/danieleongari/CURATED-COFs) (612) | benchmark |
|  | | - | 0.0245 | - | DDEC6 | Zeolite | 2024 | [IZA DB](https://www.iza-structure.org/databases/) (258) | benchmark |
| 10.1038/s41524-024-01413-4 | [MEPO-ML](https://github.com/uowoolab/MEPO-ML) | - | 0.0250 | - | REPEAT | MOF | 2024 | ARC-MOF (279,632) | 0.8 : 0.1 : 0.1 |
| 10.1021/acs.jpcc.4c04879 | [PACMOF-v2](https://github.com/snurr-group/pacmof2) | 0.9937 | 0.0229 | 0.0376 | DDEC6 | neutral-MOF | 2024 | CoRE MOF 2019 (3,378) & QMOF (19,961) & CSD MOF (18,928) | 0.8 : - : 0.2 |
|  | | 0.9930 | 0.0240 | 0.0380 | DDEC6 | ionic-MOF | 2024 | [CSD MOF](https://www.ccdc.cam.ac.uk/free-products/csd-mof-collection/) (7,598) | 0.8 : - : 0.2 |
|  | | 0.9700 | 0.0200 | 0.0330 | DDEC6 | COF | 2024 | CURATED COF (792) | benchmark |
|  | | 0.9980 | 0.0290 | 0.0550 | DDEC6 | Zeolite | 2024 | [Zeo-1 DB](https://archive.materialscloud.org/record/2021.171) (220) | benchmark |

### Large language models
| DOI | Model | Purpose | Year |
|:----------|:------|:-------|:-----|
| 10.1109/BigData55660.2022.10020568 | [Pre-Trained Language Models](https://github.com/anyuanay/MOF) | domain PLMs outperform in MOF KG extraction, but gaps remain | 2022 |
| 10.48550/arXiv.2201.08174  | [MOF-KG](https://github.com/KGQA/leaderboard) | KGQA4MAT: ChatGPT-enabled MOF knowledge graph querying benchmark | 2022 |
| 10.1021/jacs.3c05819       | [CCA](https://github.com/zach-zhiling-zheng/ChatGPT_Chemistry_Assistant) | information extraction from publications | 2023 |
| 10.1021/jacs.3c12086       | [fine-tuning GPT](https://github.com/zach-zhiling-zheng/Linker-Mutation) | GPT-assisted MOF linker generation via mutation | 2023 |
| 10.1002/anie.202311983     | [fine-tuning GPT-4](https://github.com/zach-zhiling-zheng/Reticular_Chemist) | GPT-4 guides MOF synthesis via human-AI iterative feedback | 2023 |
| 10.1021/acscentsci.3c01087 | [ChatGPT-Lab](https://github.com/zach-zhiling-zheng/ChatGPT-Lab) | Multi-AI system accelerates MOF/COF synthesis via ChatGPT and Bayesian search | 2023 |
| 10.1038/s41467-024-48998-4 | [ChatMOF](https://github.com/Yeonghun1675/ChatMOF) | property-based structure generation | 2024 |
| 10.26434/chemrxiv-2024-7kds2 | GPT-4 and GPT-4o-based | LLM-powered MOFsyn Agent optimizes synthesis and catalysis | 2024 |
| 10.1038/s41467-024-45563-x | [fine-tuned GPT-3, Llama-2](https://github.com/LBNLP/NERRE) | LLMs enable flexible extraction of structured materials science knowledge | 2024 |
| 10.1021/acs.jcim.4c00065   | [Llama2–7B, ChatGLM2–6B, …](https://github.com/MontageBai/Evaluation-of-open-source-large-language-models-for-metal-organic-frameworks-research) | benchmark for different LLM models | 2024 |
| 10.1021/jacs.4c11085       | [L2M3](https://github.com/Yeonghun1675/L2M3) | prepare a dataset with information from ~40,000 papers | 2025 |
| 10.1039/D5TA01139F         | [fine-tuning Gemini-1.5](https://github.com/xiaoyu961031/Fine-tuned-Gemini) | hydrophobicity of MOFs | 2025 |

### Adsorption / separation models
**unit**: mmol/g, ${cm^{3}}$/g,...
| DOI | Model  | ${R^{2}}$ | MAPE (%) | MAE | RMSE | SRCC | Adsorbate | Condition	| Adsorbent | Year | Database (# of Total Points) | Train: Val: Test |
|:----------|:-------|:-------|:-----------|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| 10.1021/acs.chemmater.5b01475 | [RF](http://nanoporousmaterials.org/xekrseparations/) | | | | 2.21 | | Xe/Kr selectivity | 20%Xe:80%Kr,1atm,298K | MOF,PPN,Zeolite | 2015 | Exp MOF (3,640), hMOF (2,750), hPPN (1,000), hZeolite (2,319), IZA (194), hZIF (3,757), hCOF (834)| - : - : -|
| 10.1021/acscombsci.7b00056 | RF | 0.97,0.92 | 8.75,9.22 | | | | CH4 (cm3/g),(cm3/cm3) | 35bar,298K | MOF | 2017 | [hMOF (130,398)](http://hmofs.northwestern.edu/) | 0.08 : - : 0.92 |
| 10.1039/C8ME00050F | LASSO | 0.96 | | 2.4 | 3.1 | | WC of H2 | 100-2bar,77K | hMOF | 2018 | hMOF (137,953) & CSD MOF (54,776) | 0.08 : - : 0.92 |
| 10.1021/acs.chemmater.8b02257 | RF | 0.905,0.905,0.855,0.870,0.515 | | | | 0.921,0.950,0.938,0.914,0.751 | CO2/N2 selectivity,CO2,CO2/H2 selectivity,WC of CO2,WC of CO2 | 15%CO2:85%N2@1bar,1bar,20%CO2:80%H2@20bar,20%CO2:80%H2@20bar,15%CO2:85%N2@1bar | MOF | 2018 | ToBaCCo MOF (400) | 0.8 : - : 0.2 |
| 10.1021/acs.jpcc.8b09420 | ANN | | | 2.93,1.84,1.78,1.59,1.33,1.57,1.38,1.07,0.99,1.06,1.09,1.24,1.14,1.06,0.84,0.83,0.91,0.75 | | | H2 | 0.1,1,5,35,65,100bar,77,160,295K | MOF | 2019 | ToBaCCo (105) | 0.8 : - : 0.2 |
| 10.1021/acs.jctc.9b00940 | [ANN](https://pubs.acs.org/doi/suppl/10.1021/acs.jctc.9b00940/suppl_file/ct9b00940_si_002.zip) | 0.998,0.998,0.998,0.998,0.998,0.998 | 4.4,4.6,4.7,4.5,4.3,4.0 | 0.17,0.24,0.30,0.42,0.42,0.14 | | | Ar,CH4,Kr,Xe,C2H6,N2 | 1-100bar | MOF | 2020 | [ToBaCCo MOF (2,400)](https://pubs.acs.org/doi/suppl/10.1021/acs.jctc.9b00940/suppl_file/ct9b00940_si_002.zip) | 9 : 1 : 2 |
| 10.1021/acs.chemmater.9b05322 | LR,LR,RF,LR | 0.988,0.985,0.925,0.992 | | | | | WC of C2H6,WC of C2H4,C2H6/C2H4 selectivity,C2H6/C2H4 selectivity | 1-0.1bar,1-0.1bar,1bar,0.1bar,298K | MOF (UiO-66) | 2020 | CoRE MOF (425) | 0.8 : - : 0.2 |
| 10.1021/acs.jpcc.9b10766 | RF | 0.889,0.824,0.857,0.874 | | 8,16.1,18.2,25.5 | 12.1,23.6,26.4,37.5 | | CH4,CO2,H2S,H2 | 5.8bar@298K,1bar@300K,1bar@300K,2bar,77K | MOF | 2020 | CoRE MOF 2014 DDEC (2,932) | 0.34 : - : 0.66 |
| 10.1021/jacs.9b11084 | RF | 0.74,0.76 | | 12.5,11.5 | 17.1,17.3 | | CH4,CO2 | 5.8bar@298K,0.5bar@298K | MOF | 2020 | hMOF (78,000) | 50-10,000 for taining |
| 10.1021/acsomega.1c00100 | XGBoost | 0.951,0.973 | | | 0.055,0.255 | | Xe,Xe/Kr separation | 20%Xe:80%Kr,1bar,298K | MOF | 2021 | [G-MOFs (-)](https://figshare.com/s/ec378d7315581e48f1e4) | 0.3 : - : 0.7 |
| 10.1021/acs.jcim.2c00876 | [MOFNet](https://github.com/Matgen-project/MOFNet) | | | 2.355,2.233,2.231,2.206,2.196,2.197,2.224,2.212,2.626,2.559,2.516,2.527,2.394,2.352,2.325,2.303,0.208,0.288,0.339,0.378,0.497,0.595,0.778,0.844 | | | N2,CO2,CH4 | 0.2/5/10/20/40/60/80/100,10/50/100/500/1000/1500/20000/50000,50/100/150/200/500/1000/5000/10000kPa | MOF | 2022 | CSD MOF (7,304) (6,997) (8,539) | 0.8 : 0.1 : 0.1 |
| 10.1021/acsami.2c08977 | [LASSO,GBR,ETR,GBR](https://github.com/hdaglar/MOF-basedMMMs_ML) | 0.99,0.80,0.73,0.84 | | 1.30E-3,5.45E-3,0.212,5.62E-2 | 1.70E-3,9.23E-3,0.339,0.104 | |  He,H2,CH4,N2 | 1bar,298K | MOF Membranes | 2022 | hMOF(677)(2,715)(5,215)(5,224) | 0.8 : - : 0.2 |
| 10.1021/acs.iecr.3c02211 | GBR | 0.951,0.989 | | 0.565,0.157 | 0.782,0.370 | | Xe,Kr saturation loading | 298K | MOF | 2023 | CoRE MOF 2019 (1,081) | 0.8 : - : 0.2 |
| 10.1021/acsami.3c10323 | [PMTransformer](https://github.com/hspark1212/MOFTransformer) | | | 5.963,0.069,0.053,2.126,1.009,2.995,0.461 |	|	|	H2,N2,O2,CH4,CH4,CH4,CH4 | 100/1/65/5.8/65/1bar | MOF | 2023 | [hMOF by PORMAKE](https://figshare.com/articles/dataset/dx_doi_org_10_6084_m9_figshare_21155506/21155506?file=37511746) (60,000) | 0.8 : 0.1 : 0.1 |
| 10.1038/s42256-023-00628-2  | [MOFTransformer](https://github.com/hspark1212/MOFTransformer) | | | 6.377,0.071,0.051,2.268,0.999,3.187,0.493 |	|	|	H2,N2,O2,CH4,CH4,CH4,CH4 | 100/1/65/5.8/65/1bar | MOF | 2023 | [hMOF by PORMAKE](https://figshare.com/articles/dataset/dx_doi_org_10_6084_m9_figshare_21155506/21155506?file=37511746) (60,000) | 0.8 : 0.1 : 0.1 |
| 10.1021/acsami.3c02130 | [tree-based](https://github.com/hdaglar/BMIM.BF4.MOF_Composites_ML) | 0.712,0.874 | | 0.379,0.0234 | 0.552,0.0331 | 0.852,0.937 | CO2,N2 | 1bar,298K | IL/MOF | 2023 | CSD MOF (941) | 0.8 : - : 0.2 |
| 10.1021/jacs.2c11420 | [MOFormer](https://github.com/zcao0420/MOFormer) | | | 0.158,0.545,0.982,0.033,0.161,0.384 | | | CO2,CO2,CO2,CH4,CH4,CH4 | 0.05bar,0.5bar,2.5bar,0.04bar,0.5bar,2.5bar | MOF | 2023 | hMOF (102,858) | 0.7 : 0.15 : 0.15 |
| 10.1021/acsami.3c10951 | GC-Trans | 0.9811 | | 0.1913 | 0.5319 | 0.9906 | CO2,N2 | 0.1-30bar,273-313K | MOF | 2023 | CSD MOF (3,101) | 0.8 : 0.1 : 0.1 |
| 10.1038/s41467-024-46276-x | [Uni-MOF](https://github.com/dptech-corp/Uni-MOF) | 0.983 | | |	|	|	CO2,N2,CH4,Kr,Xe | 273K,298K,0.01-10Pa | MOF | 2024 | [hMOF_MOFX-DB & CoRE_MOFX-DB (2,477,494 points)](https://figshare.com/articles/dataset/Source_Data_file_zip/24996317?file=44038835) | 0.8 : 0.1 : 0.1 |
| | | 0.916 | | |	|	|	Ar,N2 | 77K,87K,1Pa-1bar | MOF | 2024 | hMOF_MOFX-DB & CoRE_MOFX-DB (464,824 points) | 0.8 : 0.1 : 0.1 |
| | | 0.834 | | |	|	|	CH4,CO2,Ar,Kr,Xe,O2,He | 150-300K, 1Pa-3bar | MOF | 2024 | hMOF_MOFX-DB & CoRE_MOFX-DB (99,200 points) | 0.8 : 0.1 : 0.1 |
| 10.1021/jacs.3c14610 | [RF](https://pubs.acs.org/doi/suppl/10.1021/jacs.3c14610/suppl_file/ja3c14610_si_003.zip) | 0.83 | | | | | C3H8/C3H6 selectivity | 50%C3H8:50%C3H6@1bar@298K | MOF | 2024 | CoRE MOF (4,685) | 0.9 : - : 0.1 |
| 10.1021/acsami.4c11953| [GBR](https://github.com/sxm13/H2-COF-functionalization) | 0.995,0.994 | | 0.073,0.396 | 0.119,0.642 | | H2 (wt.%) (g/L) | 5,100bar,111,231,296K | Functionalized COF | 2024 | CURATED COF (807) | 0.8 : - : 0.2 |
| 10.1002/anie.202500783 | [XGBoost](https://github.com/breezy-ying/Data-and-ML-Models) | 0.968,0.984 | | | | | C2H6/C2H4 selectivity,C2H6 | 10%C2H6:90%C2H4@1bar | MOF-5 Analogs | 2025 | CSD MOF (2,824) | 0.8 : - : 0.2 |

### Machine learning potential
| DOI | Model | Purpose | Year | Dataset | 
|:----------|:------|:-------|:-----|:-----|
| 10.1039/D1MA01152A | DNN | [CO2,H2O@MOF-74](https://www.rsc.org/suppdata/d1/ma/d1ma01152a/d1ma01152a1.zip) | 2022 | Energy,PBE-D3 |
| 10.1038/s41524-023-00969-x | [NequIP](https://doi.org/10.5281/zenodo.7539133) | [UiO-66(Zr),MIL-53(Al)](https://doi.org/10.5281/zenodo.6359970) | 2023 | QM energy,PBE-D3 |
| 10.1021/acs.jctc.3c00495 | NequIP | [ZIF-8,Mg-MOF-74](https://zenodo.org/records/7904959) | 2023 | 0-32 CO2@ZIF-8/Mg-MOF-74,relax,PBE-D3 (BJ)|
| 10.1039/D3NR05966A | DeePMD-kit | [2D MOF(NiF2(pyrazine)2)](https://zenodo.org/records/7904959) | 2024 | AIMD,NVT(100,200,300K),10,000*0.5fs,PBE |
| 10.1039/D3SC05612K | DeePMD-kit | [H2@Al-soc-MOF-1d](https://doi.org/10.5281/zenodo.10686480)  | 2024 | 0.31-5.25wt.%H2,AIMD,NVT(10-100K),1,000*0.5fs,PBE-D3 |
| 10.1038/s41524-024-01427-y | [SNAP](https://github.com/asharma-ms/MOF_MLP_2024) | [ZIF-8,MOF-5](https://doi.org/10.5281/zenodo.11176257) | 2024 | AIMD,NVT(100-1,000K),2,000*0.5fs,PBE |
| 10.1038/s41524-024-01205-w | [SkoltechMLIP](https://mlip.skoltech.ru/download) | [MIL-53,MOF-74,MOF-5,UiO-66](https://repository.tugraz.at/records/wyc7s-8en40) | 2024 | relax,PBE-D3(BJ) |
| 10.1021/acsnano.4c12369 | [NequIP] | [Zn-based MOFs](https://zenodo.org/records/13989347) | 2025 | isotopic strain and randomly perturbing atoms for 2,966 MOFs from QMOF(19,705),PBE-D3(BJ) |

### Other models
| DOI | Model  | Accuracy | AUC | ${R^{2}}$ | MAE | SRCC | Purpose  | Materials | Year | Database (# of Total Points) | Train: Val: Test |
|:----------|:-------|:-------|:-----------|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| 10.1021/acs.jpclett.8b01707 | NN | 0.67 | | | | | metallic | MOF | 2018 | CoRE MOF 2014 DDEC (2,932) | 0.7 : - : 0.3 |
| 10.1021/acs.jpclett.0c01518 | [LASSO](https://pubs.acs.org/doi/suppl/10.1021/acs.jpclett.0c01518/suppl_file/jz0c01518_si_003.zip) | | | 0.960 | | | True monolayer area | MOF | 2020 | CoRE MOF (300) | 0.4 : - : 0.6 |
| 10.1038/s42256-020-00249-z | [RF](https://doi.org/10.5281/zenodo.4014333) | 0.88 | | | | | Water stability | MOF | 2020 | [Butch et al (207)](https://pubs.acs.org/doi/10.1021/cr5002589) | 0.8 : - : 0.2 |
| 10.1021/jacs.1c07217 | [ANN](https://github.com/hjkgrp/MOFSimplify) | | | | 44-47 | | Thermal stability | MOF | 2020 | CoRE MOF 2019 (3,132 points) | 0.8 : - : 0.2 |
| | | 0.76 | 0.79 | | | | Solvent removal stability | MOF | 2020 | CoRE MOF 2019 (-) | 0.8 : - : 0.2 |
| 10.1038/s41563-022-01374-3 | [GBR](https://github.com/SeyedMohamadMoosavi/tools-cp-porousmat) | | | | 0.02 | 0.98 | Heat capacity | MOF/COF/Zeolite | 2022 | CoRE MOF 2019, QMOF, IZA, CURATED COF (232) | 0.9 : - : 0.1 |
| 10.1021/jacs.4c05879 | [RF](https://github.com/hjkgrp/MOFSimplify) | 0.75 | 0.80 | | | | Water stability | MOF | 2024 | [WS24 (964)](https://doi.org/10.5281/zenodo.10982960) | 0.8 : - : 0.2 |
| 10.1002/adma.202500943 | [XGBoost](https://github.com/gfengITP/MOF-IL) | | | 0.92,0.80,0.86 | 11.8,7.74,0.17 | | Gravimetric, volumetric capacitance, logarithmic current desity | MOF | 2024 | QMOF (20,375) | 0.8 : - : 0.2 |

