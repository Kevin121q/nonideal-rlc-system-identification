# Source Code

This directory contains reusable Python modules used throughout the RLC system-identification project.

## Files

### `models.py`

Contains physical models for the circuit, including:

- non-ideal series RLC gain model
- LC resonance frequency calculation

### `fitting.py`

Contains parameter-estimation utilities, including:

- RMSE calculation
- single-resistance curve fitting
- extraction of effective hidden resistance, inductance, and capacitance

### `plotting.py`

Contains reusable plotting functions for producing consistent GitHub/report-quality figures.

## Purpose

The goal of this directory is to separate reusable computational code from exploratory notebook analysis.

The notebooks remain the main analysis workflow, while `src/` stores model, fitting, and plotting functions that may be reused across notebooks and scripts.
