#!/bin/bash


python3 runTableMaker.py configs/configTableMakerDataRun2.json -runData --arg table-maker:processBarrelOnlyWithCov:true event-selection-task:syst:pp internal-dpl-aod-reader:aod-file:@run2_conv_LHC17p_ForTM_sample.txt table-maker:cfgQA:true table-maker:cfgBarrelTrackCuts:jpsiO2MCdebugCuts2 --add_col_conv --add_fdd_conv 
