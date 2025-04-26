# ML4Porous
Summarize the machine learning research on porous materials such as COF/MOF/Zeolite so far.

### Bandgap Predition
| DOI | Model | R² | MAE | RMSE | SRCC | Year | Database | Split Ratio | # of test points |
|:----------|:------|:---|:----|:-----|:-----|:------|:------|:------|:------|
| 10.1021/acsami.3c10323     | [PMTransformer](https://github.com/hspark1212/MOFTransformer) | - | 0.216 | - | - | - |
| 10.1038/s42256-023-00628-2 | MOFTransformer | - | 0.224 | - | - | - |
| 10.1016/j.matt.2021.02.015 | [CGCNN](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning) | 0.876 | 0.274 | - | 0.932 | - |
| 10.1016/j.matt.2021.02.015 | [KRR (SOAP)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning) | 0.822 | 0.357 | - | 0.910 | - |
| 10.1016/j.matt.2021.02.015 | [KRR (Orbital field matrix)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning) | 0.763 | 0.417 | - | 0.863 | - |
| 10.1016/j.matt.2021.02.015 | [KRR (Stoichiometric-120)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning) | 0.750 | 0.433 | - | 0.847 | - |
| 10.1016/j.matt.2021.02.015 | [KRR (Stoichiometric-45)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning) | 0.743 | 0.437 | - | 0.842 | - |
| 10.1016/j.matt.2021.02.015 | [KRR (Sine Coulomb matrix)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning) | 0.643 | 0.529 | - | 0.787 | - |
| 10.1016/j.matt.2021.02.015 | [KRR (Constant mean model)](https://github.com/Andrew-S-Rosen/QMOF/tree/main/machine_learning) | - | 0.973 | - | - | - |
| 10.1107/S1600576722009797  | [CNN from PXRD](https://github.com/gomezperalta/band-gap_pxrd/) | - | 0.492 | 0.674 | - | - |
| 10.1021/jacs.2c11420       | [MOFormer](https://github.com/zcao0420/MOFormer) | - | 0.387 | - | - | - |
| [AI2ASE 2025](https://ai-2-ase.github.io/papers/27_1_AAAI_2025_AI4ASE_workshop_MOF.pdf) | [M-MOFormer](https://github.com/IkeYang/M-MOFormer) | - | 0.359 | - | - | - |
| 10.1021/acs.jpclett.3c00187 | CGCNN | 0.709 | 0.393 | 0.585 | - | - |
| 10.1021/acs.jpclett.3c00187 | MEGNet | 0.767 | 0.368 | 0.523 | - | - |
| 10.1021/acs.jpclett.3c00187 | MEGNet-tuned | 0.787 | 0.332 | 0.500 | - | - |
| 10.1002/adfm.202313596 | CGCNN | 0.820 | 0.330 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | RR | 0.169 | 0.091 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | LIR | 0.000 | 0.099 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | SGD | -0.001 | 0.099 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | PAR | 0.178 | 0.091 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | SVR | 0.355 | 0.080 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | KNR | 0.315 | 0.080 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | NNR | 0.180 | 0.086 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | ETR | 0.542 | 0.063 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | GBR | 0.436 | 0.075 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | BR | 0.475 | 0.067 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | ABR | 0.391 | 0.083 | - | - | - |
| 10.26434/chemrxiv-2024-0mkw8 | RFR | 0.424 | 0.066 | - | - | - |
