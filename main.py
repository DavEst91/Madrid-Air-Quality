import sys, pandas, os, numpy
from src.cleaning_data import *
from argparse import ArgumentParser
from src.obtain_new_contamination_data import *
from src.obtain_data_from_AEMET import *
parser = ArgumentParser(description="Este programa es para obtener información sobre la calidad del aire")
parser.add_argument("--estacion",help="este es el número de la estacion meteorologica de la que desea obtener información meteorológica", default=49)
args = parser.parse_args()

print_data_from_AEMET(get_data_from_AEMET())
get_last_year_data(args.estacion)
get_dataset_today(args.estacion)

