# Scripts

This directory contains lightweight command-line scripts for reproducing key parts of the workflow.

## Files

### `clean_data.py`

Loads raw resistance sweep data, standardizes column names, recomputes gain from measured voltages, and saves a cleaned dataset.

### `run_reconstruction.py`

Runs parameter reconstruction for each resistance sweep using the non-ideal RLC model.

### `generate_figures.py`

Generates basic figures from processed data.

## Purpose

These scripts are not meant to replace the notebooks.

The notebooks explain the analysis step by step, while the scripts show that the workflow can be partially automated and reproduced from the command line.
