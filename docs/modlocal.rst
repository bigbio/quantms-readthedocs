Modification localization
=========================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 10px; color: white; text-align: center; margin: 20px 0;">
      <h2 style="margin: 0; font-size: 24px;">🔬 Modification localization</h2>
      <p style="margin: 10px 0; font-size: 18px;">Confident PTM site assignment with multiple algorithms</p>
   </div>

Introduction
------------

Mass spectrometry-based proteomics is widely used to identify and quantify post-translational modifications (PTMs) in complex biological samples. While search engines like Comet and MS-GF+ can identify peptide sequences with PTMs, they often lack robust confidence metrics for PTM site assignments when multiple potential sites exist.

**onsite** is a comprehensive Python package that provides three complementary algorithms for confident phosphorylation site localization:

- **AScore**: Fast probability-based scoring using binomial statistics
- **PhosphoRS**: Compomics-style scoring with detailed isomer analysis  
- **LucXor (LuciPHOr2)**: Two-stage processing with false localization rate (FLR) estimation

.. note::
   Robust metrics for local and global false localization rates (FLR) should always be computed to complement the false discovery rate (FDR) metrics commonly reported for peptide identification results.

Why Phosphorylation Site Localization Matters
----------------------------------------------

.. raw:: html

   <div style="background: #fff3cd; padding: 20px; border-radius: 8px; border-left: 4px solid #856404; margin: 20px 0;">
      <h4 style="margin: 0 0 10px 0; color: #856404;">⚠️ The Challenge</h4>
      <p style="margin: 0;">When a peptide contains multiple potential phosphorylation sites (e.g., multiple S, T, or Y residues), search engines may correctly identify the peptide but incorrectly assign the modification site. Without proper localization scoring, you cannot distinguish between:</p>
      <ul style="margin: 10px 0;">
         <li><strong>Confidently localized sites</strong>: High-quality MS/MS data clearly indicates the modification position</li>
         <li><strong>Ambiguous sites</strong>: Insufficient fragment ion evidence to distinguish between possible positions</li>
      </ul>
   </div>

**Example**: Consider the peptide ``AAASSSAAA`` with one phosphorylation. The search engine might report ``AAAp[S]SSAAA``, but without localization scoring, you don't know if the phosphorylation is truly on the first serine or if it could equally be on the second or third serine.

Using onsite in quantms
------------------------

.. raw:: html

   <div style="background: #d1ecf1; padding: 20px; border-radius: 8px; border-left: 4px solid #0c5aa6; margin: 20px 0;">
      <h4 style="margin: 0 0 10px 0; color: #0c5aa6;">🚀 Quick Start</h4>
      <p style="margin: 0;">Enable phosphorylation site localization in your quantms workflow with a single parameter:</p>
   </div>

Basic Usage
^^^^^^^^^^^

To enable PTM localization analysis in quantms, use the ``--enable_mod_localization`` parameter:

.. code-block:: bash

   nextflow run bigbio/quantms -r 1.6.0 \
     --input experiment.sdrf.tsv \
     --database proteome.fasta \
     --enable_mod_localization true \
     -profile docker

By default, this will run the **LucXor** algorithm for phosphorylation site localization on S, T, and Y residues.

Choosing an Algorithm
^^^^^^^^^^^^^^^^^^^^^

You can specify which algorithm to use with the ``--mod_localization_algorithm`` parameter:

.. code-block:: bash

   # Use AScore (fastest)
   nextflow run bigbio/quantms -r 1.6.0 \
     --input experiment.sdrf.tsv \
     --enable_mod_localization true \
     --onsite_algorithm ascore \
     -profile docker

   # Use PhosphoRS (detailed probabilities)
   nextflow run bigbio/quantms -r 1.6.0 \
     --input experiment.sdrf.tsv \
     --enable_mod_localization true \
     --onsite_algorithm phosphors \
     -profile docker

   # Use LucXor (with FLR estimation, default)
   nextflow run bigbio/quantms -r 1.6.0 \
     --input experiment.sdrf.tsv \
     --enable_mod_localization true \
     --onsite_algorithm lucxor \
     -profile docker

Running All Algorithms
^^^^^^^^^^^^^^^^^^^^^^

For comprehensive analysis, you can run all three algorithms and compare results:

.. code-block:: bash

   nextflow run bigbio/quantms -r 1.6.0 \
     --input experiment.sdrf.tsv \
     --enable_mod_localization true \
     --onsite_compute_all_scores true \
     -profile docker

This will add scores from all three algorithms to your output files, allowing you to compare their results.

Algorithm Details
-----------------

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #007bff;">
         <h3 style="margin: 0 0 10px 0; color: #007bff;">⚡ AScore</h3>
         <p style="margin: 0 0 10px 0;"><strong>Best for:</strong> Fast processing, large datasets</p>
         <p style="margin: 0; font-size: 14px;">Probability-based approach using binomial statistics to identify site-determining ions</p>
      </div>
      
      <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #28a745;">
         <h3 style="margin: 0 0 10px 0; color: #28a745;">📊 PhosphoRS</h3>
         <p style="margin: 0 0 10px 0;"><strong>Best for:</strong> Detailed site probabilities</p>
         <p style="margin: 0; font-size: 14px;">Compomics-style scoring with comprehensive isomer analysis and site-specific probabilities</p>
      </div>
      
      <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #ffc107;">
         <h3 style="margin: 0 0 10px 0; color: #e68900;">🎯 LucXor</h3>
         <p style="margin: 0 0 10px 0;"><strong>Best for:</strong> FLR estimation, publication</p>
         <p style="margin: 0; font-size: 14px;">Two-stage processing with false localization rate calculation using decoy-based validation</p>
      </div>
   </div>

1. AScore Algorithm
^^^^^^^^^^^^^^^^^^^

**Method**: Probability-based approach using binomial statistics

**Key Features**:

- Fast processing suitable for large-scale datasets
- Site-determining ion analysis
- Weighted peptide scoring across multiple peak depths
- Unambiguous site detection

**Output Metrics**:

- ``AScore_pep_score``: Overall peptide localization score
- ``AScore_1, AScore_2, ...``: Individual site scores (higher is better)
- ``ProForma``: Standardized sequence notation with confidence scores

**Interpretation**:

- **AScore > 19**: High confidence localization (p < 0.01)
- **AScore 13-19**: Moderate confidence (p < 0.05)
- **AScore < 13**: Low confidence, ambiguous localization

**Citation**: Beausoleil et al. (2006) *Nature Biotechnology* [BEAUSOLEIL2006]_

2. PhosphoRS Algorithm
^^^^^^^^^^^^^^^^^^^^^^

**Method**: Compomics-style scoring with isomer analysis

**Key Features**:

- Generates all possible phosphorylation isomers
- Theoretical spectrum matching with binomial probability
- Site-specific probability calculation
- Detailed isomer scoring

**Output Metrics**:

- Site-specific probability scores (0-100%)
- Isomer details with sequences and scores
- Confidence metrics for each potential site

**Interpretation**:

- **Probability > 99%**: High confidence localization
- **Probability 75-99%**: Moderate confidence
- **Probability < 75%**: Low confidence, consider ambiguous

**Citation**: Taus et al. (2011) *Journal of Proteome Research* [TAUS2011]_

3. LucXor (LuciPHOr2) Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Method**: Two-stage processing with FLR estimation

**Key Features**:

- Stage 1: Calculate FLR estimates using real and decoy permutations
- Stage 2: Assign FLR values to PSMs
- Charge state-specific modeling
- Global and local FLR calculation

**Output Metrics**:

- ``Luciphor_delta_score``: Main localization score (difference between top two candidates)
- ``Luciphor_pep_score``: Peptide identification score
- ``Luciphor_global_flr``: Global false localization rate
- ``Luciphor_local_flr``: Local false localization rate (charge-specific)

**Interpretation**:

- **Delta Score > 10**: High confidence localization
- **Delta Score 5-10**: Moderate confidence
- **Delta Score < 5**: Low confidence
- **Global FLR < 0.01**: 1% false localization rate
- **Local FLR < 0.01**: 1% charge-specific false localization rate

**Citation**: Fermin et al. (2013, 2015) *MCP* and *Bioinformatics* [FERMIN2013]_ [FERMIN2015]_

Parameter Reference
-------------------

AScore-Specific Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 35 15 50
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``--in-file`` / ``-in``
     - (required)
     - Input mzML file path
   * - ``--id-file`` / ``-id``
     - (required)
     - Input idXML file path
   * - ``--out-file`` / ``-out``
     - (required)
     - Output idXML file path
   * - ``--fragment-mass-tolerance``
     - ``0.05``
     - Fragment mass tolerance value
   * - ``--fragment-mass-unit``
     - ``Da``
     - Tolerance unit (Da or ppm)
   * - ``--threads``
     - ``1``
     - Number of parallel threads
   * - ``--add-decoys``
     - ``false``
     - Include A (PhosphoDecoy) as potential phosphorylation site
   * - ``--compute-all-scores``
     - ``false``
     - Run all three algorithms and merge results
   * - ``--debug``
     - ``false``
     - Enable debug output and write debug log

PhosphoRS-Specific Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 35 15 50
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``--in-file`` / ``-in``
     - (required)
     - Input mzML file path
   * - ``--id-file`` / ``-id``
     - (required)
     - Input idXML file path
   * - ``--out-file`` / ``-out``
     - (required)
     - Output idXML file path
   * - ``--fragment-mass-tolerance``
     - ``0.05``
     - Fragment mass tolerance value
   * - ``--fragment-mass-unit``
     - ``Da``
     - Tolerance unit (Da or ppm)
   * - ``--threads``
     - ``1``
     - Number of parallel processes
   * - ``--add-decoys``
     - ``false``
     - Include A (PhosphoDecoy) as potential phosphorylation site
   * - ``--compute-all-scores``
     - ``false``
     - Run all three algorithms and merge results
   * - ``--debug``
     - ``false``
     - Enable debug output and write debug log

LucXor-Specific Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 35 15 50
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - ``--input-spectrum`` / ``-in``
     - (required)
     - Input spectrum file (mzML)
   * - ``--input-id`` / ``-id``
     - (required)
     - Input identification file (idXML)
   * - ``--output`` / ``-out``
     - (required)
     - Output file (idXML)
   * - ``--fragment-method``
     - ``CID``
     - Fragmentation method (CID or HCD)
   * - ``--fragment-mass-tolerance``
     - ``0.5``
     - Tolerance of the peaks in the fragment spectrum
   * - ``--fragment-error-units``
     - ``Da``
     - Unit of fragment mass tolerance (Da or ppm)
   * - ``--min-mz``
     - ``150.0``
     - Do not consider peaks below this value
   * - ``--target-modifications``
     - ``Phospho (S), Phospho (T), Phospho (Y)``
     - List of target modifications
   * - ``--neutral-losses``
     - ``sty -H3PO4 -97.97690``
     - List of neutral losses
   * - ``--decoy-mass``
     - ``79.966331``
     - Mass to add for decoy generation
   * - ``--decoy-neutral-losses``
     - ``X -H3PO4 -97.97690``
     - List of decoy neutral losses
   * - ``--max-charge-state``
     - ``5``
     - Maximum charge state to consider
   * - ``--max-peptide-length``
     - ``40``
     - Maximum peptide length
   * - ``--max-num-perm``
     - ``16384``
     - Maximum number of permutations
   * - ``--modeling-score-threshold``
     - ``0.95``
     - Minimum score for modeling
   * - ``--scoring-threshold``
     - ``0.0``
     - Minimum score threshold
   * - ``--min-num-psms-model``
     - ``50``
     - Minimum number of PSMs for modeling
   * - ``--threads``
     - ``1``
     - Number of threads to use
   * - ``--rt-tolerance``
     - ``0.01``
     - Retention time tolerance
   * - ``--disable-split-by-charge``
     - ``false``
     - Disable splitting PSMs by charge state for model training
   * - ``--compute-all-scores``
     - ``false``
     - Run all three algorithms and merge results
   * - ``--debug``
     - ``false``
     - Enable debug mode
   * - ``--log-file``
     - ``{output}_debug.log``
     - Log file path (only used in debug mode)

Output and Results
------------------

Localization Scores in mzTab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When PTM localization is enabled, scores are added to the mzTab output file (:doc:`formats`) for each PSM:

**AScore Output**:

.. code-block:: text

   opt_global_AScore_pep_score: 45.23
   opt_global_AScore_1: 23.45
   opt_global_AScore_2: 12.34
   opt_global_ProForma: AAAS[Phospho|score=0.9876]SSAAA

**PhosphoRS Output**:

.. code-block:: text

   opt_global_PhosphoRS_site_1_probability: 95.6
   opt_global_PhosphoRS_site_2_probability: 3.2
   opt_global_PhosphoRS_site_3_probability: 1.2

**LucXor Output**:

.. code-block:: text

   opt_global_Luciphor_delta_score: 15.67
   opt_global_Luciphor_pep_score: 89.34
   opt_global_Luciphor_global_flr: 0.005
   opt_global_Luciphor_local_flr: 0.008

Quality Control
^^^^^^^^^^^^^^^

.. raw:: html

   <div style="background: #d4edda; padding: 20px; border-radius: 8px; border-left: 4px solid #155724; margin: 20px 0;">
      <h4 style="margin: 0 0 10px 0; color: #155724;">✅ Quality Control Recommendations</h4>
   </div>

**Important**: quantms does not automatically filter peptides based on PTM localization scores. You must evaluate the quality of site assignments based on your experimental requirements.

**Recommended Thresholds**:

1. **High Confidence Sites**:
   
   - AScore > 19 (p < 0.01)
   - PhosphoRS probability > 99%
   - LucXor local FLR < 0.01

2. **Moderate Confidence Sites**:
   
   - AScore 13-19 (p < 0.05)
   - PhosphoRS probability 75-99%
   - LucXor local FLR 0.01-0.05

3. **Ambiguous Sites** (consider excluding):
   
   - AScore < 13
   - PhosphoRS probability < 75%
   - LucXor local FLR > 0.05

Example Workflows
-----------------

Basic Phosphorylation Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Standard phosphorylation analysis with LucXor
   nextflow run bigbio/quantms -r 1.6.0 \
     --input phospho_experiment.sdrf.tsv \
     --database human_proteome.fasta \
     --enable_mod_localization true \
     --onsite_algorithm lucxor \
     --onsite_fragment_method HCD \
     --onsite_fragment_tolerance 0.02 \
     --onsite_fragment_error_units Da \
     -profile docker

High-Confidence Site Identification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Run all algorithms for comprehensive analysis
   nextflow run bigbio/quantms -r 1.6.0 \
     --input phospho_experiment.sdrf.tsv \
     --database human_proteome.fasta \
     --enable_mod_localization true \
     --onsite_compute_all_scores true \
     --onsite_fragment_tolerance 0.02 \
     --onsite_fragment_error_units Da \
     --onsite_threads 8 \
     -profile docker

Large-Scale Dataset
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Fast processing with AScore
   nextflow run bigbio/quantms -r 1.6.0 \
     --input large_phospho_dataset.sdrf.tsv \
     --database proteome.fasta \
     --enable_mod_localization true \
     --onsite_algorithm ascore \
     --onsite_fragment_tolerance 0.5 \
     --onsite_threads 16 \
     -profile docker

Frequently Asked Questions
--------------------------

**Q: Which algorithm should I use?**

A: It depends on your needs:

- **Speed**: AScore
- **Detailed probabilities**: PhosphoRS
- **FLR estimation**: LucXor
- **Comprehensive**: All three (``--compute-all-scores``)

**Q: Can I use onsite for modifications other than phosphorylation?**

A: Currently, onsite is optimized for phosphorylation (S, T, Y). Support for other PTMs is planned for future releases.

**Q: How do I interpret conflicting results from different algorithms?**

A: When algorithms disagree:

1. Check the confidence scores for each algorithm
2. Manually inspect the MS/MS spectrum
3. Consider the site ambiguous if scores are low across all algorithms
4. Trust high-confidence results that agree across multiple algorithms

**Q: Should I filter my results based on localization scores?**

A: Yes, you should apply appropriate thresholds based on your experimental requirements. quantms does not automatically filter results. See the Quality Control section for recommended thresholds.

**Q: Can I run localization on previously processed data?**

A: Yes, you can run onsite standalone on idXML files:

.. code-block:: bash

   # Run AScore standalone
   onsite ascore -in spectra.mzML -id identifications.idXML -out results.idXML

   # Run PhosphoRS standalone
   onsite phosphors -in spectra.mzML -id identifications.idXML -out results.idXML

   # Run LucXor standalone
   onsite lucxor -in spectra.mzML -id identifications.idXML -out results.idXML

**Q: How do I cite onsite in my publication?**

A: Cite the original algorithm papers and the onsite package:

- **AScore**: Beausoleil et al. (2006) *Nature Biotechnology*
- **PhosphoRS**: Taus et al. (2011) *Journal of Proteome Research*
- **LucXor**: Fermin et al. (2013) *MCP* and Fermin et al. (2015) *Bioinformatics*
- **onsite**: https://github.com/bigbio/onsite

Additional Resources
--------------------

Documentation
^^^^^^^^^^^^^

- `onsite GitHub Repository <https://github.com/bigbio/onsite>`_
- `onsite on PyPI <https://pypi.org/project/pyonsite/>`_
- :doc:`identification` - Peptide Identification
- :doc:`formats` - Output Formats

Related Topics
^^^^^^^^^^^^^^

- :doc:`fdr` - False Discovery Rate
- :doc:`pmultiqc` - Quality Control
- :doc:`statistics` - Statistical Analysis
- :doc:`identification` - Peptide Identification

Get Help
^^^^^^^^

- `Report Issues <https://github.com/bigbio/onsite/issues>`_
- `Slack Channel <https://nfcore.slack.com/channels/quantms>`_
- :doc:`troubleshooting` - Troubleshooting Guide
- :doc:`faq` - FAQ

References
----------

.. [BEAUSOLEIL2006] Beausoleil SA, Villén J, Gerber SA, Rush J, Gygi SP. A probability-based approach for high-throughput protein phosphorylation analysis and site localization. *Nat Biotechnol.* 2006;24(10):1285-1292. doi:10.1038/nbt1240

.. [TAUS2011] Taus T, Köcher T, Pichler P, et al. Universal and confident phosphorylation site localization using phosphoRS. *J Proteome Res.* 2011;10(12):5354-5362. doi:10.1021/pr200611n

.. [FERMIN2013] Fermin D, Walmsley SJ, Gingras AC, Choi H, Nesvizhskii AI. LuciPHOr: algorithm for phosphorylation site localization with false localization rate estimation using modified target-decoy approach. *Mol Cell Proteomics.* 2013;12(11):3409-3419. doi:10.1074/mcp.M113.028928

.. [FERMIN2015] Fermin D, Avtonomov D, Choi H, Nesvizhskii AI. LuciPHOr2: site localization of generic post-translational modifications from tandem mass spectrometry data. *Bioinformatics.* 2015;31(7):1141-1143. doi:10.1093/bioinformatics/btu788
