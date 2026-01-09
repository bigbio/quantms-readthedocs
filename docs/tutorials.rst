Tutorials
=========

.. raw:: html

   <div style="background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%); padding: 25px; border-radius: 10px; color: white; text-align: center; margin: 20px 0;">
      <h2 style="margin: 0; font-size: 22px;">🎯 Step-by-step tutorials</h2>
      <p style="margin: 10px 0;">Learn quantms with real examples</p>
   </div>

.. raw:: html

   <div style="background: #f1f5f9; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0; color: #475569;">📚 Choose your learning path based on experience:</h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
         
         <div style="background: #dbeafe; padding: 15px; border-radius: 6px; text-align: center;">
            <div style="font-size: 24px; margin-bottom: 5px;">🌱</div>
            <strong style="color: #1d4ed8;">Beginner</strong><br>
            <small>First time with quantms</small>
         </div>
         
         <div style="background: #dcfce7; padding: 15px; border-radius: 6px; text-align: center;">
            <div style="font-size: 24px; margin-bottom: 5px;">🌿</div>
            <strong style="color: #166534;">Intermediate</strong><br>
            <small>Some proteomics experience</small>
         </div>
         
         <div style="background: #fef3c7; padding: 15px; border-radius: 6px; text-align: center;">
            <div style="font-size: 24px; margin-bottom: 5px;">🚀</div>
            <strong style="color: #92400e;">Advanced</strong><br>
            <small>Power user features</small>
         </div>
      </div>
   </div>

🌱 Beginner: DDA Label-Free Quantification
-------------------------------------------

.. raw:: html

   <div style="background: #f0f9ff; padding: 20px; border-radius: 8px; border-left: 4px solid #3b82f6; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0; color: #3b82f6;">Perfect for: First-time users with DDA data</h4>
      <p style="margin: 0 0 10px 0;"><strong>What you'll learn:</strong> Basic quantms workflow from SDRF to results</p>
      <p style="margin: 0;"><strong>Time needed:</strong> 30 minutes + analysis time</p>
   </div>

**Step 1: Prepare your inputs** ⚙️

.. raw:: html

   <div style="background: #f8fafc; padding: 15px; border-radius: 6px; margin: 15px 0;">
      <strong>Required files:</strong>
      <ul style="margin: 5px 0; padding-left: 20px;">
         <li><code>project.sdrf.tsv</code> - Experimental design</li>
         <li><code>proteome_plus_contaminants.fasta</code> - Protein database</li>
         <li><code>*.mzML</code> files - Mass spec data</li>
      </ul>
   </div>

See :doc:`getting_started` for file preparation details and :doc:`protein_database` for FASTA creation.

**Step 2: Run the analysis** 🚀

.. code-block:: bash

   nextflow run bigbio/quantms -r 1.7.0 \
     --input project.sdrf.tsv \
     --database proteome_plus_contaminants.fasta \
     -profile docker

**Step 3: Inspect outputs** 📊

Your results will be in the `results/` directory. Key files to check:

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin: 15px 0;">
      
      <div style="background: #f0f9ff; padding: 15px; border-radius: 6px;">
         <strong style="color: #3b82f6;">📊 Quantification Tables</strong><br>
         <code>*.mztab</code><br>
         <small>Protein and peptide abundances</small>
      </div>
      
      <div style="background: #f0fdf4; padding: 15px; border-radius: 6px;">
         <strong style="color: #22c55e;">📈 QC Report</strong><br>
         <code>multiqc_report.html</code><br>
         <small>Quality control metrics</small>
      </div>
   </div>

See :doc:`quantms_output` for complete output descriptions.

**Step 4: Statistical analysis** 📈

.. raw:: html

   <div style="background: #ecfdf5; padding: 15px; border-radius: 6px; border-left: 3px solid #22c55e; margin: 15px 0;">
      <strong style="color: #22c55e;">Next step:</strong> Use MSstats for differential expression analysis.<br>
      <a href="msstats.html" style="color: #22c55e;">→ MSstats tutorial</a>
   </div>

🌿 Intermediate: DIA Library-Free Analysis
-------------------------------------------

.. raw:: html

   <div style="background: #f0fdf4; padding: 20px; border-radius: 8px; border-left: 4px solid #22c55e; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0; color: #22c55e;">Perfect for: Users familiar with DIA and DIA-NN</h4>
      <p style="margin: 0 0 10px 0;"><strong>What you'll learn:</strong> DIA-NN integration and library-free workflow</p>
      <p style="margin: 0;"><strong>Time needed:</strong> 45 minutes + analysis time</p>
   </div>

**Step 1: Prepare DIA-specific FASTA** 🧬

.. tip::
   For DIA-NN gene grouping, use a contaminants database with protein descriptions:

.. code-block:: bash

   # Download recommended FASTA for DIA
   wget https://github.com/bigbio/quantms-test-datasets/raw/quantms/databases/contaminants-202105-uniprot-description.fasta

See :doc:`protein_database` for detailed FASTA preparation with contaminants and gene names.

**Step 2: Run DIA analysis** 🔬

.. code-block:: bash

   nextflow run bigbio/quantms -r 1.7.0 \
     --input project.sdrf.tsv \
     --database proteome_plus_contaminants_with_descriptions.fasta \
     --acquisition_method dia \
     -profile docker

.. important::
   **DIA-specific notes:**
   
   - No decoys needed in FASTA (DIA-NN handles internally)
   - Use FASTA with gene names for proper grouping
   - Consider setting `--dia_library_free true` (default)

**Step 3: Review DIA-NN settings** ⚙️

Key parameters to understand: :doc:`dia`

**Step 4: Quality control** 📊

DIA generates additional QC metrics. Review: :doc:`pmultiqc`

🚀 Advanced: Rescoring and Custom Models
-----------------------------------------

.. raw:: html

   <div style="background: #fef3c7; padding: 20px; border-radius: 8px; border-left: 4px solid #f59e0b; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0; color: #f59e0b;">Perfect for: Power users wanting to optimize results</h4>
      <p style="margin: 0 0 10px 0;"><strong>What you'll learn:</strong> Advanced rescoring options and model selection</p>
      <p style="margin: 0;"><strong>Time needed:</strong> 1+ hours + experimentation</p>
   </div>

**Rescoring strategies** 🎯

Explore advanced rescoring options and deep learning models:

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin: 15px 0;">
      
      <div style="background: #f0f9ff; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
         <strong style="color: #3b82f6;">🧠 Percolator</strong><br>
         <small>Semi-supervised machine learning</small><br>
         <a href="percolator.html" style="color: #3b82f6;">→ Setup guide</a>
      </div>
      
      <div style="background: #f0fdf4; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
         <strong style="color: #22c55e;">🔬 MS²PIP</strong><br>
         <small>Deep learning models</small><br>
         <a href="rescoring.html" style="color: #22c55e;">→ Model selection</a>
      </div>
      
      <div style="background: #fef3c7; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
         <strong style="color: #f59e0b;">⚡ IDPEP</strong><br>
         <small>Retention time prediction</small><br>
         <a href="idpep.html" style="color: #f59e0b;">→ Configuration</a>
      </div>
   </div>

See :doc:`rescoring` for comprehensive rescoring framework details.

Interactive learning paths
---------------------------

.. raw:: html

   <div style="background: #1e293b; color: #f1f5f9; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0;">🎓 Structured learning paths</h4>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
         
         <div style="background: #334155; padding: 15px; border-radius: 6px;">
            <strong style="color: #60a5fa;">📋 Complete Workflow</strong><br>
            <small>
               <a href="quickstart.html" style="color: #93c5fd;">1. Quickstart</a> →
               <a href="getting_started.html" style="color: #93c5fd;">2. Setup</a> →
               <a href="#beginner-dda-label-free-quantification" style="color: #93c5fd;">3. Tutorial</a> →
               <a href="pmultiqc.html" style="color: #93c5fd;">4. QC</a>
            </small>
         </div>
         
         <div style="background: #334155; padding: 15px; border-radius: 6px;">
            <strong style="color: #34d399;">🔬 Analysis-Specific</strong><br>
            <small>
               Choose: <a href="dda.html" style="color: #6ee7b7;">DDA</a> |
               <a href="dia.html" style="color: #6ee7b7;">DIA</a> |
               <a href="iso.html" style="color: #6ee7b7;">TMT</a> |
               <a href="lfq.html" style="color: #6ee7b7;">LFQ</a>
            </small>
         </div>
         
         <div style="background: #334155; padding: 15px; border-radius: 6px;">
            <strong style="color: #fbbf24;">⚙️ Advanced Topics</strong><br>
            <small>
               <a href="rescoring.html" style="color: #fcd34d;">Rescoring</a> →
               <a href="parameters.html" style="color: #fcd34d;">Parameters</a> →
               <a href="benchmarks.html" style="color: #fcd34d;">Benchmarks</a>
            </small>
         </div>
      </div>
   </div>

Need help?
----------

- 🤔 **Stuck?** Check our :doc:`troubleshooting` guide
- 📖 **Terms unclear?** See the :doc:`glossary`
- 💬 **Questions?** Visit our :doc:`contact` page


