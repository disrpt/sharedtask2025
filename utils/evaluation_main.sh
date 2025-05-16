#!/bin/bash
################################################################################
#                              evaluation_main.sh                              #
#                                                                              #
# Main script to run disrpt evaluation                                         #
#                                                                              #
#                                                                              #
# Change History                                                               #
# 2024/04  Laura Rivière    Original code.                                     #
#                                                                              #
#                           Add new history entries as needed.                 #
#                                                                              #
#                                                                              #
################################################################################

# TODO add log of all cmd ??

################################################################################
# Help                                                                         #
################################################################################
Help()
{
    # Display Help
    echo 
    echo "Script to run DISRPT evaluations over not 2 files but two directories of files"
    echo -e "Syntax: evaluation_main.sh -g \e[4mPATH\e[0m -p \e[4mPATH\e[0m -o \e[4mPATH\e[0m [-d] [-b] [-y] [-s] [-h]"
    echo "Arguments:"
    echo -e "-g, --gold_dir \e[4mPATH\e[0m          Path to parent gold directory (.../data)."
    echo -e "-p, --pred_dir \e[4mPATH\e[0m          Path to parent predictions directory (.../data)."
    echo -e "-o, --out_eval_dir \e[4mPATH\e[0m      Path to output directory to print results files."
    echo "-d, --division_set                     Datasets division to evaluate to 'dev. Default='test'."
    echo "-b, --no_boundary_edu                   Option for TASK-1/.conllu. Evaluate only intra-sentential EDUs."
    echo "-y, --rel_type                         Option for TASK-3. Evaluate TYPES instead of LABELS (cf.PDTB) plus metrics for each type."
    echo "-s, --string_input                     Whether inputs are strings instead of file names."
    echo "-h, --help)                            Print help."
    echo 
}

################################################################################
# Initialize variables                                                         #
################################################################################
OPT_STRING_INPUT=false
OPT_NO_BOUNDARY_EDU=false
OPT_REL_TYPE=false
GOLD_DIR="/home/lriviere/disrpt_lau/latest/data" # dev
PRED_DIR="/home/lriviere/disrpt_lau/latest/data" # dev
EVAL_DIR=/home/lriviere/disrpt_lau/lrec24/disrpt/scripts/eval_test # dev
PART="test" #"dev" # dev

################################################################################
# Process input options                                                        #
################################################################################
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -g|--gold_dir) GOLD_DIR="$2"
            ;;
        -p|--pred_dir) PRED_DIR="$2"
            ;;
        -o|--out_eval_dir) EVAL_DIR="$2"
            ;;
        -d|--division_set) PART="dev" # va peutetre poser pb pour les test-only ??
            ;;
        -b|--no_boudary_edu) OPT_NO_BOUNDARY_EDU=true
            ;;
        -y|--rel_type) OPT_REL_TYPE=true
            ;;
        -s|--string_input) OPT_STRING_INPUT=true
            ;;
        -h|--help) Help
            exit;;
    esac
    shift
done

echo
echo "gold dir: $GOLD_DIR"
echo "predictions dir: $PRED_DIR"
echo "output dir: $EVAL_DIR"
echo "division: $PART"
echo "options: string_input=$OPT_STRING_INPUT, no_boundary_edus=$OPT_NO_BOUNDARY_EDU, rel_type=$OPT_REL_TYPE"
echo

################################################################################
# Main program                                                                 #
################################################################################

Evaluation() 
{   #datasetname #extension #task #opt
    eval=$1"_"$PART".$2"
    file_eval=$EVAL_DIR"/"$eval"_eval"
    file_gold=$GOLD_DIR"/"$1"/"$eval
    file_pred=$PRED_DIR"/"$1"/"$eval
    args="-g $file_gold -p $file_pred -t $3 $4"
    echo "# Processing $eval...from $args"
    cmd=$(python disrpt_eval_2024.py $args) 
    echo "$cmd" > $file_eval
}

################################################################################
# DISRPT TASK-1: EDUS SEGMENTATION                                             #
# RST, SDRT, DEP datasets.                                                     #
################################################################################

for dataset in deu.rst.pcc eng.dep.covdtb eng.dep.scidtb eng.rst.gum eng.rst.rstdt eng.sdrt.stac eus.rst.ert fas.rst.prstc fra.sdrt.annodis nld.rst.nldt por.rst.cstn rus.rst.rrt spa.rst.rststb spa.rst.sctb zho.dep.scidtb zho.rst.gcdt zho.rst.sctb 

do
    DATASET_NAME=${dataset}

    OPT=""
    if [ "$OPT_STRING_INPUT" = true ]; then OPT="-s"; fi
    Evaluation "$DATASET_NAME" "tok" "S" "$OPT"


    if [ "$OPT_NO_BOUNDARY_EDU" = true ]; then OPT=$OPT" -nb"; fi
    Evaluation "$DATASET_NAME" "conllu" "S" "$OPT"

done


################################################################################
# DISRPT TASK-2: CONNECTIVES IDENTIFICATION                                    #
# PDTB datasets                                                                #
################################################################################

for dataset in eng.pdtb.gum eng.pdtb.pdtb eng.pdtb.tedm ita.pdtb.luna por.pdtb.crpc por.pdtb.tedm tha.pdtb.tdtb tur.pdtb.tdb tur.pdtb.tedm zho.pdtb.cdtb

do
    DATASET_NAME=${dataset}

    OPT=""
    if [ "$OPT_STRING_INPUT" = true ]; then OPT="-s"; fi

    Evaluation "$DATASET_NAME" "tok" "C" "$OPT"

    Evaluation "$DATASET_NAME" "conllu" "C" "$OPT"

done


################################################################################
# DISRPT TASK-3: RELATIONS CLASSIFICATION                                      #
# All datasets                                                                 #
################################################################################

for dataset in deu.rst.pcc eng.dep.covdtb eng.dep.scidtb eng.pdtb.pdtb eng.pdtb.tedm eng.rst.gum eng.rst.rstdt eng.sdrt.stac eus.rst.ert fas.rst.prstc fra.sdrt.annodis ita.pdtb.luna nld.rst.nldt por.pdtb.crpc por.pdtb.tedm por.rst.cstn rus.rst.rrt spa.rst.rststb spa.rst.sctb tha.pdtb.tdtb tur.pdtb.tdb tur.pdtb.tedm zho.dep.scidtb zho.pdtb.cdtb zho.rst.gcdt zho.rst.sctb 

do 
    DATASET_NAME=${dataset}

    OPT=""
    if [ "$OPT_STRING_INPUT" = true ]; then OPT="-s"; fi
    if [ "$OPT_REL_TYPE" = true ]; then OPT=$OPT" -rt"; fi

    Evaluation "$DATASET_NAME" "rels" "R" "$OPT"

done

