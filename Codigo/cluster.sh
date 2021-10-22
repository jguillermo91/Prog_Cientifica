#!/bin/bash
#
#
#PBS -N Transformando
#PBS -l nodes=4:ppn=5
#PBS -M j.guillermo91@gmail.com
#PBS -t 0-7
#echo jobid=$PBS_ARRAYID

python  /home/programacion2/jguillermo/programas/procesar.py
