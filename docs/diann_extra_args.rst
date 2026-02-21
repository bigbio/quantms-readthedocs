DIA-NN extra arguments reference
=================================

quantms exposes a ``--diann_extra_args`` parameter that lets users pass additional DIA-NN
command-line arguments to all five DIA-NN steps. Each step validates the extra arguments and
automatically **strips flags that are managed by the pipeline**, printing a warning when it does so.

This page documents which flags are blocked in each step, which flags trigger warnings, and why.

.. contents:: On this page
   :local:
   :depth: 2

How the validation works
------------------------

Every DIA-NN module contains a blocklist of flags. When ``ext.args`` (populated from
``--diann_extra_args`` or from a user's custom Nextflow config) is processed:

1. Each blocked flag is matched using a **word-boundary regex** so that, for example, ``--f``
   does not accidentally match inside ``--fasta``.
2. Blocked flags are checked in **length-descending order**, so ``--mass-acc-ms1`` is matched
   before ``--mass-acc``.
3. If a blocked flag is found, it and its value(s) are removed and a ``log.warn`` message is
   printed. The pipeline does **not** fail.

Flags not in the blocklist are passed through to DIA-NN unchanged. In particular,
``--var-mod`` and ``--fixed-mod`` (modification declarations) are never blocked — users can
add extra modifications via ``--diann_extra_args``.

Blocked flags by step
---------------------

The tables below list every blocked flag per step, whether it appears in the DIA-NN command
line for that step, and the reason it is blocked.

.. _insilico-library-generation:

Step 1: INSILICO_LIBRARY_GENERATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generates an in-silico predicted spectral library from the FASTA database.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Blocked flag
     - In command?
     - Reason
   * - ``--fasta``
     - Yes
     - Managed by the pipeline (input FASTA file).
   * - ``--fasta-search``
     - Yes
     - Hardcoded — required for in-silico library generation.
   * - ``--predictor``
     - Yes
     - Hardcoded — enables deep learning prediction.
   * - ``--gen-spec-lib``
     - Yes
     - Hardcoded — instructs DIA-NN to generate the spectral library.
   * - ``--threads``
     - Yes
     - Managed by Nextflow (``task.cpus``).
   * - ``--verbose``
     - Yes
     - Managed by ``--diann_debug`` parameter.
   * - ``--missed-cleavages``
     - Yes
     - Managed by ``--allowed_missed_cleavages`` parameter.
   * - ``--min-pep-len``
     - Yes
     - Managed by ``--min_peptide_length`` parameter.
   * - ``--max-pep-len``
     - Yes
     - Managed by ``--max_peptide_length`` parameter.
   * - ``--min-pr-charge``
     - Yes
     - Managed by ``--min_precursor_charge`` parameter.
   * - ``--max-pr-charge``
     - Yes
     - Managed by ``--max_precursor_charge`` parameter.
   * - ``--var-mods``
     - Yes
     - Managed by ``--max_mods`` parameter (max variable modifications per peptide).
   * - ``--min-pr-mz``
     - Yes
     - Managed by ``--min_pr_mz`` parameter.
   * - ``--max-pr-mz``
     - Yes
     - Managed by ``--max_pr_mz`` parameter.
   * - ``--min-fr-mz``
     - Yes
     - Managed by ``--min_fr_mz`` parameter.
   * - ``--max-fr-mz``
     - Yes
     - Managed by ``--max_fr_mz`` parameter.
   * - ``--met-excision``
     - Yes
     - Managed by ``--met_excision`` parameter.
   * - ``--lib``
     - No
     - This step creates a library from scratch; loading an existing library would skip prediction.
   * - ``--f``
     - No
     - No MS files are processed during library generation.
   * - ``--use-quant``
     - No
     - No ``.quant`` files exist at this stage.
   * - ``--no-main-report``
     - No
     - No main report is relevant for library generation.
   * - ``--matrices``
     - No
     - No quantification matrices in library generation.
   * - ``--out``
     - No
     - Pipeline expects default output naming (``*.predicted.speclib``).
   * - ``--temp``
     - No
     - Overriding the temp directory could break output collection.

.. _preliminary-analysis:

Step 2: PRELIMINARY_ANALYSIS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per-file calibration run that determines optimal mass accuracy and scan window.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Blocked flag
     - In command?
     - Reason
   * - ``--lib``
     - Yes
     - Managed by the pipeline (predicted spectral library from Step 1).
   * - ``--f``
     - Yes
     - Managed by the pipeline (MS file input).
   * - ``--fasta``
     - No
     - Adding ``--fasta`` would enable FASTA search / MBR features during what should be a pure calibration step, changing the analysis mode.
   * - ``--threads``
     - Yes
     - Managed by Nextflow (``task.cpus``).
   * - ``--verbose``
     - Yes
     - Managed by ``--diann_debug`` parameter.
   * - ``--temp``
     - Yes
     - Managed by the pipeline (``--temp ./``).
   * - ``--mass-acc``
     - Conditional
     - Managed by the pipeline: either auto-determined or taken from SDRF tolerance values.
   * - ``--mass-acc-ms1``
     - Conditional
     - Same as ``--mass-acc``.
   * - ``--window``
     - Conditional
     - Managed by ``--scan_window_automatic`` / ``--scan_window`` parameters.
   * - ``--quick-mass-acc``
     - Conditional
     - Managed by ``--quick_mass_acc`` parameter.
   * - ``--min-corr``
     - Conditional
     - Managed by ``--performance_mode`` parameter (sets ``--min-corr 2``).
   * - ``--corr-diff``
     - Conditional
     - Managed by ``--performance_mode`` parameter (sets ``--corr-diff 1``).
   * - ``--time-corr-only``
     - Conditional
     - Managed by ``--performance_mode`` parameter.
   * - ``--use-quant``
     - No
     - This step processes raw MS files directly.
   * - ``--gen-spec-lib``
     - No
     - Not generating a spectral library.
   * - ``--out-lib``
     - No
     - Not outputting a library.
   * - ``--matrices``
     - No
     - No matrices needed for calibration.
   * - ``--out``
     - No
     - Pipeline renames output via ``cp``.

.. _assemble-empirical-library:

Step 3: ASSEMBLE_EMPIRICAL_LIBRARY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assembles an empirical spectral library from all per-file ``.quant`` results with RT profiling.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Blocked flag
     - In command?
     - Reason
   * - ``--lib``
     - Yes
     - Managed by the pipeline (predicted library from Step 1).
   * - ``--f``
     - Yes
     - Managed by the pipeline (all MS files).
   * - ``--fasta``
     - No
     - Adding ``--fasta`` would enable FASTA search during library assembly, changing the empirical library content.
   * - ``--threads``
     - Yes
     - Managed by Nextflow (``task.cpus``).
   * - ``--verbose``
     - Yes
     - Managed by ``--diann_debug`` parameter.
   * - ``--temp``
     - Yes
     - Managed by the pipeline (``--temp ./quant/``).
   * - ``--out-lib``
     - Yes
     - Managed by the pipeline (``empirical_library``).
   * - ``--use-quant``
     - Yes
     - Hardcoded — reuses ``.quant`` files from Step 2.
   * - ``--gen-spec-lib``
     - Yes
     - Hardcoded — generates empirical spectral library.
   * - ``--rt-profiling``
     - Yes
     - Hardcoded — enables retention time profiling for the empirical library.
   * - ``--mass-acc``
     - Conditional
     - Managed by the pipeline: either ``--individual-mass-acc`` or explicit values from SDRF.
   * - ``--mass-acc-ms1``
     - Conditional
     - Same as ``--mass-acc``.
   * - ``--window``
     - Conditional
     - Managed by ``--scan_window_automatic`` / ``--scan_window`` parameters.
   * - ``--individual-mass-acc``
     - Conditional
     - Used when ``--mass_acc_automatic`` is true.
   * - ``--individual-windows``
     - Conditional
     - Used when ``--scan_window_automatic`` is true.
   * - ``--no-main-report``
     - No
     - The main output is the library; blocking prevents unexpected report suppression.
   * - ``--no-ifs-removal``
     - No
     - Interference signal removal should stay on (default) for quality library assembly.
   * - ``--matrices``
     - No
     - No matrices needed for library assembly.
   * - ``--out``
     - No
     - Pipeline expects default output naming.

.. _individual-analysis:

Step 4: INDIVIDUAL_ANALYSIS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per-file quantification using the empirical library with calibrated mass accuracy and scan window.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Blocked flag
     - In command?
     - Reason
   * - ``--lib``
     - Yes
     - Managed by the pipeline (empirical library from Step 3).
   * - ``--f``
     - Yes
     - Managed by the pipeline (MS file input).
   * - ``--fasta``
     - Yes
     - Managed by the pipeline (FASTA database input).
   * - ``--threads``
     - Yes
     - Managed by Nextflow (``task.cpus``).
   * - ``--verbose``
     - Yes
     - Managed by ``--diann_debug`` parameter.
   * - ``--temp``
     - Yes
     - Managed by the pipeline (``--temp ./``).
   * - ``--mass-acc``
     - Yes
     - Pipeline computes from PRELIMINARY_ANALYSIS log or SDRF tolerance values.
   * - ``--mass-acc-ms1``
     - Yes
     - Same as ``--mass-acc``.
   * - ``--window``
     - Yes
     - Pipeline computes from PRELIMINARY_ANALYSIS log or ``--scan_window`` parameter.
   * - ``--no-ifs-removal``
     - Yes
     - Hardcoded — enables high-precision quantification.
   * - ``--no-main-report``
     - Yes
     - Hardcoded — the output is ``.quant`` files, not a report.
   * - ``--relaxed-prot-inf``
     - Yes
     - Hardcoded — enables relaxed protein inference mode.
   * - ``--pg-level``
     - Yes
     - Managed by ``--pg_level`` parameter.
   * - ``--use-quant``
     - No
     - This step processes raw files, not reusing ``.quant``.
   * - ``--gen-spec-lib``
     - No
     - Not generating a spectral library.
   * - ``--out-lib``
     - No
     - Not outputting a library.
   * - ``--matrices``
     - No
     - No matrices at per-file level.
   * - ``--out``
     - No
     - Pipeline renames output via ``cp``.
   * - ``--rt-profiling``
     - No
     - Not used in individual analysis.

**Warning-only flags** (not blocked, but a warning is printed):

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Flag
     - Warning
   * - ``--individual-windows``
     - Overrides the scan window values computed by the PRELIMINARY_ANALYSIS step. The pipeline
       calibrates scan windows across all files in Step 2; using ``--individual-windows`` here
       would discard those calibrated values and let DIA-NN re-determine them per file.
   * - ``--individual-mass-acc``
     - Overrides the mass accuracy values computed by the PRELIMINARY_ANALYSIS step. Same
       reasoning as above.

.. _final-quantification:

Step 5: FINAL_QUANTIFICATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Final multi-file quantification using ``.quant`` files and the empirical library.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Blocked flag
     - In command?
     - Reason
   * - ``--lib``
     - Yes
     - Managed by the pipeline (empirical library from Step 3).
   * - ``--fasta``
     - Yes
     - Managed by the pipeline (FASTA database input).
   * - ``--f``
     - Yes
     - Managed by the pipeline (all MS files).
   * - ``--threads``
     - Yes
     - Managed by Nextflow (``task.cpus``).
   * - ``--verbose``
     - Yes
     - Managed by ``--diann_debug`` parameter.
   * - ``--temp``
     - Yes
     - Managed by the pipeline (``--temp ./quant/``).
   * - ``--use-quant``
     - Yes
     - Hardcoded — reuses ``.quant`` files from Step 4.
   * - ``--matrices``
     - Yes
     - Hardcoded — generates quantification matrices.
   * - ``--out``
     - Yes
     - Managed by the pipeline (``diann_report.tsv``).
   * - ``--relaxed-prot-inf``
     - Yes
     - Hardcoded — enables relaxed protein inference.
   * - ``--pg-level``
     - Yes
     - Managed by ``--pg_level`` parameter.
   * - ``--qvalue``
     - Yes
     - Managed by ``--protein_level_fdr_cutoff`` parameter.
   * - ``--window``
     - Conditional
     - Managed by ``--scan_window`` / ``--scan_window_automatic`` parameters.
   * - ``--individual-windows``
     - Conditional
     - Used when ``--scan_window_automatic`` is true.
   * - ``--species-genes``
     - Conditional
     - Managed by ``--species_genes`` parameter.
   * - ``--report-decoys``
     - Conditional
     - Managed by ``--diann_report_decoys`` parameter.
   * - ``--xic``
     - Conditional
     - Managed by ``--diann_export_xic`` parameter.
   * - ``--no-main-report``
     - No
     - The main report (``diann_report.tsv``) is a critical output — suppressing it would break the pipeline.
   * - ``--gen-spec-lib``
     - No
     - Not generating a spectral library.
   * - ``--out-lib``
     - No
     - Not outputting a library.
   * - ``--no-ifs-removal``
     - No
     - Interference signal removal should stay on for final quantification quality.

Flags that are safe to pass
----------------------------

The following DIA-NN flags are **not blocked** in any step and can be used via
``--diann_extra_args``:

- ``--var-mod`` / ``--fixed-mod``: Add extra modification declarations beyond what is in the SDRF.
- ``--cut``: Override the protease specificity (use with caution — the pipeline already sets this from the SDRF via ``diann_config.cfg``).
- ``--full-unimod``: Load the complete UniMod database.
- ``--original-mods``: Prevent modification conversion to UniMod.
- ``--mass-acc-cal``: Set calibration mass accuracy.
- ``--dl-no-fr`` / ``--dl-no-rt`` / ``--dl-no-im``: Disable specific deep learning predictions.
- ``--reuse``: Reuse existing ``.quant`` files.
- ``--no-maxlfq``: Disable MaxLFQ calculation (FINAL_QUANTIFICATION).
- ``--matrix-spec-q``: Set FDR threshold for protein matrices (FINAL_QUANTIFICATION).
- ``--channels``: Define multiplexing channels.
- ``--im-window``: Set ion mobility window width.
- ``--quant-train-runs`` / ``--quant-sel-runs`` / ``--quant-params``: QuantUMS training parameters (FINAL_QUANTIFICATION).
- ``--dg-*``: Decoy generation parameters.
- ``--tune-*``: Model fine-tuning parameters.
- ``--cfg``: Reference a DIA-NN configuration file.

.. note:: Some flags that are safe to pass only make sense in certain steps. For example,
   ``--no-maxlfq`` only affects the FINAL_QUANTIFICATION step. Since ``--diann_extra_args``
   is passed to all steps, irrelevant flags are silently ignored by DIA-NN.

Step-specific overrides
-----------------------

For advanced use cases where different extra flags are needed per step, use a custom Nextflow
configuration file instead of ``--diann_extra_args``:

.. code-block:: groovy

   // custom.config
   process {
     withName: ".*:DIA:FINAL_QUANTIFICATION" {
       ext.args = { (params.diann_extra_args ?: '') + " --report-lib-info" }
     }
   }

Then run with:

.. code-block:: bash

   nextflow run bigbio/quantms -c custom.config ...

.. warning:: Even with custom configs, the blocked-flag validation in each module's script
   block will still strip managed flags. This is by design — it prevents silent conflicts
   regardless of how ``ext.args`` is set.

Important considerations
-------------------------

1. **Modifications from the SDRF** (``--var-mod`` and ``--fixed-mod`` in ``diann_config.cfg``)
   are automatically passed to all DIA-NN steps. You do not need to re-declare them via
   ``--diann_extra_args``.

2. **Per-file steps** (PRELIMINARY_ANALYSIS, INDIVIDUAL_ANALYSIS) process a single file per
   Nextflow task. Multi-run DIA-NN flags like ``--unrelated-runs`` or ``--quant-train-runs``
   have no effect in these steps.

3. **Performance flags** (``--quick-mass-acc``, ``--min-corr``, ``--corr-diff``,
   ``--time-corr-only``) are only relevant in the PRELIMINARY_ANALYSIS step and are managed
   by the ``--quick_mass_acc`` and ``--performance_mode`` pipeline parameters.
