"""
Parameters file for the RxnNet
"""

MOLECULE_NAME = 'trichodiene'
MOLECULE_SMILE = '[CH2+]/C=C(\C)CC/C=C(\C)CCC=C(C)C'
REACTION_LIST_NAME = 'carbocations'

# MOLECULE_NAME = 'retigerane'
# MOLECULE_SMILE = 'CC([C@@H]1CC[C@](C/C=C2C)([C@H]1C[CH+]/C(C)=C/CC/C(C)=C/CC\\2)C)C' #retigerane
# REACTION_LIST_NAME = 'carbocations'

# MOLECULE_NAME = 'cyclooctatenol'
# MOLECULE_SMILE = 'C/C1=C\C[C@@]2(C)CC[C@H]([C+](C)C)[C@@H]2CC/C(C)=C/CC1' #J1
# REACTION_LIST_NAME = 'carbocations'

OUT_FILE_FOR_RUN = f"{MOLECULE_NAME}.log"
MAX_PATH_LENGTH_TO_RUN = 5
ELIMINATE = ['=C=', '=[N+]=', '[CH2+]']
MAX_TFD_VALUE = 1 # optional - maximum value is 1
IMPOSSIBLE_SMILES = ['C[C@]12CCCCC[C@@H]1C2', 'C[C@@]12CCCCC[C@H]1C2']
##########################################################################################################

#keywords for Analysis
SOURCE_SMILE = MOLECULE_SMILE
SMILE_TO_ANALYZE = 'CC1=CC[C@@](C)([C@@]2(C)CCC[C+]2C)CC1'   #trichodiene
# SMILE_TO_ANALYZE = 'CC(C)[C@H]1CC[C@]2(C)C[C@@H]3[C@H](C)CC[C@H]3[C@@]3(C)C[C@H]3[C+]12' #cyclooctatenol
# SMILE_TO_ANALYZE = 'C/C1=C\CC[C+](C)[C@H]2C[C@@]3(C)CC[C@@H](C(C)C)[C@@H]3C[C@@H]2/C(C)=C/CC1'  #K3
# SMILE_TO_ANALYZE = 'C/C1=C\C[C@@]2(C)CC[C@@H](C(C)C)[C@@H]2C/C=C(\C)[C@@H]2CC[C+](C)[C@H]2CC1'  #K2

MAX_PATH_LENGTH_TO_ANALYZE = 5
OUT_FILE_FOR_ANALYZE = f"{MOLECULE_NAME}_analyze.log"
TS_NUM_FRAMES = 18
ALIGN_TO_PRODUCT = False     # True for template-based approach
                             # False for distance-restraint-based approach
NUM_CONFS_TO_GENERATE = 100  # Number of conformers initially generated
############################################################################################################

# QM
FOLDER_NAME = ''            # Add the folder name in which geodesic MEPs are generated
OUT_FILE_FOR_QM = f"{MOLECULE_NAME}_QM.log"
QM_SET_FOLDERS = 'set0'     #Optional: run QM only for these subfolders under Results/MOLECULE_NAME/FOLDER_NAME
                            #If omitted or None, all folders with prefix "set" are used.
CHARGE = 1
MULTIPLICITY = 1
ORCA_PATH = ''              # Path where ORCA is installed
OMPI_PATH = ''              # OpenMPI root path
XTB_PATH = ''               # XTB root path
ORCA_PATH = f'{ORCA_PATH}/orca'
OMPI_BIN_PATH = '{OMPI_PATH}/bin/'
OMPI_LIB_PATH = '{OMPI_PATH}/lib/'

SEMI_EMPIRICAL = True                  # True for performing SE NEB calculation
SEMI_EMPIRICAL_METHOD = 'GFN2-xTB'
SEMI_EMPIRICAL_KEYWORDS = []
SEMI_EMPIRICAL_NPROCS = 16
SE_INITIAL_GUESS = True                # True using geodesic paths as initial guess for NEB
SEMI_EMPIRICAL_MAXITER_GEOM = 200 
SEMI_EMPIRICAL_MAXITER_SCF = 500 

DFT = False                            # True for DFT NEB 
DFT_INPUT_ONLY = True                  # True for only writing the DFT input files
DFT_INITIAL_GUESS = True               # True to use XTB NEB MEP as initial guess
DFT_METHOD = 'M062X'
DFT_BASIS_SET = 'def2-TZVP'
DFT_KEYWORDS = ['defgrid3', 'RIJCOSX', 'def2/J']
DFT_NPROCS = 16
DFT_MAXITER_GEOM = 500 
DFT_MAXITER_SCF = 500
NEB_MAXITER = 500 


