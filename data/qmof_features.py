import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
from ase.io import read
from scipy.stats.mstats import gmean
from matminer.featurizers.composition import Meredig
from ase.io import read
from pymatgen.io.ase import AseAtomsAdaptor
from matminer.featurizers.structure import OrbitalFieldMatrix, SineCoulombMatrix
from dscribe.descriptors import SOAP

def get_stats(atomic_nums: np.ndarray, tabulated_data: np.ndarray):
    vals = np.full_like(atomic_nums, np.nan, dtype=float)

    for i in range(len(tabulated_data)):
        mask = (atomic_nums == (i + 1))
        vals[mask] = tabulated_data[i]
 
    clean = vals[~np.isnan(vals)]
    if clean.size == 0:
        return (np.nan, np.nan, np.nan, np.nan, np.nan)
    stdmean   = clean.mean()
    geomean   = gmean(np.abs(clean))
    stdev     = clean.std()
    maxval    = clean.max()
    minval    = clean.min()
    return stdmean, geomean, stdev, maxval, minval


def get_stoichiometric_45(cif_path: str) -> pd.DataFrame:
    group_data = np.array([ 1.,18., 1., 2.,13.,14.,15.,16.,17.,18.,
                            1., 2.,13.,14.,15.,16.,17.,18., 1., 2.,
                            3., 4., 5., 6., 7., 8., 9.,10.,11.,12.,
                           13.,14.,15.,16.,17.,18., 1., 2., 3., 4.,
                            5., 6., 7., 8., 9.,10.,11.,12.,13.,14.
                         ])
    period_data = np.array([1.,1.,2.,2.,2.,2.,2.,2.,2.,2.,
                            3.,3.,3.,3.,3.,3.,3.,3.,4.,4.,
                            4.,4.,4.,4.,4.,4.,4.,4.,4.,4.,
                            4.,4.,4.,4.,4.,4.,5.,5.,5.,5.,
                            5.,5.,5.,5.,5.,5.,5.,5.,5.,5.
                         ])
    electroneg_data = np.array([
        2.20,  np.nan,0.98,1.57,2.04,2.55,3.04,3.44,3.98,np.nan,
        0.93, 1.31,1.61,1.90,2.19,2.58,3.16,np.nan,0.82,1.00,
        1.36, 1.54,1.63,1.66,1.55,1.83,1.88,1.91,1.90,1.65,
        1.81, 2.01,2.18,2.55,2.96,3.00,0.82,0.95,1.22,1.33,
        1.60, 2.16,1.90,2.20,2.28,2.20,1.93,1.69,1.78,1.96,
        2.05, 2.10,2.66,2.60,0.79,0.89,1.10,1.12,1.13,1.14,
        np.nan,1.17,np.nan,1.20,np.nan,1.22,1.23,1.24,1.25,np.nan,
        1.27, 1.30,1.50,2.36,1.90,2.20,2.20,2.28,2.54,2.00,
        1.62, 2.33,2.02,2.00,2.20,np.nan,0.70,0.90,1.10,1.30,
        1.50, 1.38,1.36,1.28,1.30,1.30,1.30,1.30,1.30,1.30,
        1.30, 1.30,1.30,np.nan,np.nan,np.nan,np.nan,np.nan,
        np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan
    ])
    electron_affin_data = np.array([
         72.8,   0.0,  59.6,   0.0,  26.7, 153.9,   7.0, 141.0,
        328.0,   0.0,  52.8,   0.0,  42.5, 133.6,  71.0, 200.0,
        349.0,   0.0,  48.4,   2.37, 18.1,   7.6,  50.6,  64.3,
          0.0,  15.7,  63.7, 112.0,118.4,   0.0,  28.9, 119.0,
         78.0, 195.0, 324.6,   0.0,  46.9,   5.03,29.6,  41.1,
         86.1,  71.9,  53.0, 101.3,109.7,  53.7,125.6,   0.0,
         28.9,107.3,103.2,190.2,295.2,   0.0, 45.5,  13.95,
         48.0,  50.0,  50.0,  50.0,  50.0,  50.0,  50.0,  50.0,
         50.0,  50.0,  50.0,  50.0,  50.0,  50.0,  50.0,   0.0,
         31.0,  78.6,  14.5, 106.1,151.0,205.3,222.8,   0.0,
         19.2,  35.1,  91.2,183.3,270.1,   0.0] + [np.nan]*20
    )
    melting_data = np.array([  14.01, np.nan,453.69,1560.15,2348.15,3823.15,  63.05,  54.85,
                              53.55, 24.56,370.87,923.15,933.47,1687.15,317.35,388.36,
                              171.65, 83.85,336.53,1115.15,1814.15,1941.15,2183.15,2180.15,
                              1519.15,1811.15,1768.15,1728.15,1357.77, 692.68,302.91,1211.45,
                              1090.15,494.15,265.85,115.79,312.46,1050.15,1799.15,2128.15,
                              2750.15,2896.15,2430.15,2607.15,2237.15,1828.05,1234.93,594.22,
                              429.75,505.08,903.78,722.66,386.85,161.35,301.59,1000.15,
                              1192.15,1071.15,1204.15,1294.15,1373.15,1345.15,1095.15,
                              1586.15,1629.15,1685.15,1747.15,1770.15,1818.15,1092.15,
                              1936.15,2506.15,3290.15,3695.15,3459.15,3306.15,2739.15,
                              2041.45,1337.33,234.32,577.15,600.61,544.45,527.15,575.15,
                              202.15, np.nan,973.15,1323.15,2023.15,1845.15,1408.15,917.15,
                              913.15,1449.15,1618.15,1323.15,1173.15,1133.15,1800.15,
                              1101.15,1101.15,1900.15] + [np.nan]*10
    )
    boiling_data = np.array([  20.28,  4.22,1615.15,2743.15,4273.15,4300.15,  77.36,  90.25,
                              85.03, 27.07,1156.15,1363.15,2792.15,3173.15,553.65,717.87,
                              239.11, 87.35,1032.15,1757.15,3103.15,3560.15,3680.15,2944.15,
                              2334.15,3134.15,3200.15,3186.15,2835.15,1180.15,2477.15,3093.15,
                              887.15,958.15,332.15,119.93,961.15,1655.15,3618.15,4682.15,
                              5017.15,4912.15,4538.15,4423.15,3968.15,3236.15,2435.15,1040.15,
                              2345.15,2875.15,1860.15,1261.15,457.45,165.15,944.15,2143.15,
                              3737.15,3633.15,3563.15,3373.15,3273.15,2076.15,1800.15,3523.15,
                              3503.15,2840.15,2973.15,3141.15,2223.15,1469.15,3675.15,4876.15,
                              5731.15,5828.15,5869.15,5285.15,4701.15,4098.15,3129.15,629.88,
                              1746.15,2022.15,1837.15,1235.15,   np.nan,211.45,   np.nan,
                              2010.15,3473.15,5093.15,4273.15,4200.15,4273.15,3503.15,2284.15,
                              3383.15] + [np.nan]*10
    )
    density_data = np.array([
        0.0899,0.1785,535.0,1848.0,2460.0,2260.0,1.251,1.429,1.696,0.900,
        968.0,1738.0,2700.0,2330.0,1823.0,1960.0,3.214,1.784,856.0,1550.0,
        2985.0,4507.0,6110.0,7190.0,7470.0,7874.0,8900.0,8908.0,8960.0,7140.0,
        5904.0,5323.0,5727.0,4819.0,3120.0,3.750,1532.0,2630.0,4472.0,6511.0,
        8570.0,10280.0,11500.0,12370.0,12450.0,12023.0,10490.0,8650.0,7310.0,
        7310.0,6697.0,5900.0,5.900,1879.0,3510.0,6146.0,6689.0,6640.0,7010.0,
        7264.0,7353.0,5244.0,7901.0,8219.0,8551.0,8795.0,9066.0,9320.0,6570.0,
        9841.0,13310.0,16650.0,19250.0,21020.0,22590.0,22560.0,21450.0,19300.0,
        13534.0,11850.0,11340.0,9780.0,9196.0] + [np.nan]*10
    )
    ionization_data = np.array([
        1312.0,2372.3,520.2,899.5,800.6,1086.5,1402.3,1313.9,1681.0,2080.7,
        495.8,737.7,577.5,786.5,1011.8,999.6,1251.2,1520.6,418.8,589.8,633.1,
        658.8,650.9,652.9,717.3,762.5,760.4,737.1,745.5,906.4,578.8,762.0,947.0,
        941.0,1139.9,1350.8,403.0,549.5,600.0,640.1,652.1,684.3,702.0,710.2,
        719.7,804.4,731.0,867.8,558.3,708.6,834.0,869.3,1008.4,1170.4,375.7,
        502.9,538.1,534.4,527.0,533.1,540.0,544.5,547.1,593.4,565.8,573.0,581.0,
        589.3,596.7,603.4,523.5,658.5,761.0,770.0,760.0,840.0,880.0,870.0,890.1,
        1007.1,589.4,715.6,703.0,812.1,920.0,1037.0
    ] + [np.nan]*10
    )

    prop_map = {
        'group':           group_data,
        'period':          period_data,
        'electronegativity': electroneg_data,
        'electron_affinity': electron_affin_data,
        'melting_point':     melting_data,
        'boiling_point':     boiling_data,
        'density':           density_data,
        'ionization_energy': ionization_data,
    }

    colnames = []
    colnames += ['atomic_num_mean', 'atomic_num_geometric_mean',
                 'atomic_num_std',  'atomic_num_max',  'atomic_num_min']
    for prop in prop_map:
        colnames += [
            f'{prop}_mean',
            f'{prop}_geometric_mean',
            f'{prop}_std',
            f'{prop}_max',
            f'{prop}_min',
        ]

    try:
        mof = read(cif_path)
        atomic_nums = np.array(mof.get_atomic_numbers(), dtype=int)
    except Exception as e:
        raise RuntimeError(f"Failed to read {cif_path}: {e}")

    stats = []

    stats += [
        atomic_nums.mean(),
        gmean(atomic_nums),
        atomic_nums.std(),
        atomic_nums.max(),
        atomic_nums.min(),
    ]
    for arr in prop_map.values():
        stats.extend(get_stats(atomic_nums, np.array(arr, dtype=float)))

    return pd.DataFrame([stats], columns=colnames)


def get_stoichiometric_120(cif_path: str) -> pd.DataFrame:
    featurizer = Meredig()
    labels = featurizer.feature_labels()

    ase_mof = read(cif_path)
    adaptor = AseAtomsAdaptor()
    pm_mof = adaptor.get_structure(ase_mof)

    fingerprint = featurizer.featurize(pm_mof.composition)
    df = pd.DataFrame([fingerprint], columns=labels)
    return df


def get_ofm(cif_path: str) -> pd.DataFrame:
    featurizer = OrbitalFieldMatrix(period_tag=True)
    labels = featurizer.feature_labels()

    ase_mof = read(cif_path)
    adaptor = AseAtomsAdaptor()
    pm_mof = adaptor.get_structure(ase_mof)

    fingerprint = featurizer.featurize(pm_mof)

    df = pd.DataFrame([fingerprint], columns=labels)
    return df


def get_sm(cif_path: str) -> pd.DataFrame:
    
    ase_mofs = read(cif_path, index=':') 
    adaptor = AseAtomsAdaptor()
    max_atoms = np.inf
    pm_mofs = [adaptor.get_structure(ase_mof) for ase_mof in ase_mofs if len(ase_mof) <= max_atoms]
    featurizer = SineCoulombMatrix()
    featurizer.fit(pm_mofs)
    labels = featurizer.feature_labels()
    fingerprint = featurizer.featurize(pm_mofs[0])

    df = pd.DataFrame([fingerprint], columns=labels)
    return df
	

def get_soap(cif_path: str):

    structure = read(cif_path)

    syms = structure.get_chemical_symbols()
    species = sorted(set(syms))

    soap_params = {
        'rcut':     4.0,
        'sigma':    0.1,
        'nmax':     9,
        'lmax':     9,
        'rbf':      'gto',
        'average':  'off',
    }

    soap = SOAP(
        species=species,
        periodic=True,
        r_cut=soap_params['rcut'],
        sigma=soap_params['sigma'],
        n_max=soap_params['nmax'],
        l_max=soap_params['lmax'],
        rbf=soap_params['rbf'],
        average=soap_params['average'],
        sparse=False
    )
    soap_matrix = soap.create(structure)

    return soap_matrix
