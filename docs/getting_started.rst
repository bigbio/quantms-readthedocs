Getting started
===============

.. raw:: html

   <div style="background: linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%); padding: 25px; border-radius: 10px; color: white; text-align: center; margin: 20px 0;">
      <h2 style="margin: 0; font-size: 22px;">🚀 Your first quantms analysis in 4 steps</h2>
      <p style="margin: 10px 0;">From zero to results in 10 minutes</p>
   </div>

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: #f0f9ff; padding: 20px; border-radius: 8px; border-left: 4px solid #0ea5e9; position: relative;">
         <div style="position: absolute; top: -10px; left: 20px; background: #0ea5e9; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">1</div>
         <h3 style="margin: 10px 0 10px 0; color: #0ea5e9;">💻 Prerequisites</h3>
         <ul style="margin: 0; padding-left: 20px;">
            <li>Linux or macOS</li>
            <li>Java 11+ (<code>java -version</code>)</li>
            <li>Docker installed</li>
         </ul>
      </div>
      
      <div style="background: #f0fdf4; padding: 20px; border-radius: 8px; border-left: 4px solid #22c55e; position: relative;">
         <div style="position: absolute; top: -10px; left: 20px; background: #22c55e; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">2</div>
         <h3 style="margin: 10px 0 10px 0; color: #22c55e;">⬇️ Install Nextflow</h3>
         <div style="background: #1f2937; color: #f9fafb; padding: 10px; border-radius: 4px; font-family: monospace; font-size: 12px; margin: 10px 0;">
            curl -s https://get.nextflow.io | bash<br>
            mv nextflow ~/.local/bin/
         </div>
      </div>
      
      <div style="background: #fef3c7; padding: 20px; border-radius: 8px; border-left: 4px solid #f59e0b; position: relative;">
         <div style="position: absolute; top: -10px; left: 20px; background: #f59e0b; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">3</div>
         <h3 style="margin: 10px 0 10px 0; color: #f59e0b;">🧪 Run Test</h3>
         <div style="background: #1f2937; color: #f9fafb; padding: 10px; border-radius: 4px; font-family: monospace; font-size: 12px; margin: 10px 0;">
            nextflow run bigbio/quantms \<br>
            &nbsp;&nbsp;-r 1.7.0 -profile test_lfq,docker
         </div>
         <small>Takes 5-10 minutes</small>
      </div>
      
      <div style="background: #fdf2f8; padding: 20px; border-radius: 8px; border-left: 4px solid #ec4899; position: relative;">
         <div style="position: absolute; top: -10px; left: 20px; background: #ec4899; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">4</div>
         <h3 style="margin: 10px 0 10px 0; color: #ec4899;">🎯 Your Data</h3>
         <p style="margin: 0; font-size: 14px;">Replace test files with your own SDRF and FASTA files</p>
      </div>
   </div>

.. note::
   **✅ Success indicator**: You should see "Pipeline completed successfully" at the end of step 3.

Choose your data type
---------------------

.. raw:: html

   <div style="background: #f8fafc; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0; color: #475569;">🔬 What type of mass spectrometry data do you have?</h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 2px solid #e2e8f0; transition: all 0.2s;">
            <strong style="color: #3b82f6;">🎯 DDA (Data-Dependent)</strong><br>
            <small style="color: #64748b;">MS/MS triggered by precursor intensity</small><br>
            <div style="margin: 10px 0;">
               <span style="background: #dbeafe; color: #1d4ed8; padding: 2px 6px; border-radius: 3px; font-size: 11px;">MOST COMMON</span>
            </div>
            <a href="dda.html" style="color: #3b82f6; text-decoration: none; font-weight: bold;">→ DDA Analysis Guide</a>
         </div>
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 2px solid #e2e8f0;">
            <strong style="color: #10b981;">📊 DIA (Data-Independent)</strong><br>
            <small style="color: #64748b;">Systematic fragmentation of m/z windows</small><br>
            <div style="margin: 10px 0;">
               <span style="background: #d1fae5; color: #065f46; padding: 2px 6px; border-radius: 3px; font-size: 11px;">REPRODUCIBLE</span>
            </div>
            <a href="dia.html" style="color: #10b981; text-decoration: none; font-weight: bold;">→ DIA Analysis Guide</a>
         </div>
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 2px solid #e2e8f0;">
            <strong style="color: #f59e0b;">🏷️ TMT/iTRAQ</strong><br>
            <small style="color: #64748b;">Isobaric labeling for multiplexing</small><br>
            <div style="margin: 10px 0;">
               <span style="background: #fef3c7; color: #92400e; padding: 2px 6px; border-radius: 3px; font-size: 11px;">QUANTITATIVE</span>
            </div>
            <a href="iso.html" style="color: #f59e0b; text-decoration: none; font-weight: bold;">→ Isobaric Analysis Guide</a>
         </div>
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 2px solid #e2e8f0;">
            <strong style="color: #8b5cf6;">📈 Label-Free (LFQ)</strong><br>
            <small style="color: #64748b;">Intensity-based quantification</small><br>
            <div style="margin: 10px 0;">
               <span style="background: #ede9fe; color: #5b21b6; padding: 2px 6px; border-radius: 3px; font-size: 11px;">SIMPLE</span>
            </div>
            <a href="lfq.html" style="color: #8b5cf6; text-decoration: none; font-weight: bold;">→ LFQ Analysis Guide</a>
         </div>
      </div>
   </div>

Prepare your inputs
-------------------

.. warning::
   **Before running on your data**, ensure you have:

   1. **SDRF file**: Experimental design in SDRF format (:doc:`usage`)
   2. **FASTA database**: Protein sequences with contaminants (:doc:`protein_database`)
   3. **Raw files**: mzML or vendor format in accessible locations (:doc:`formats`)

.. raw:: html

   <div style="background: #ecfdf5; padding: 20px; border-radius: 8px; border-left: 4px solid #10b981; margin: 20px 0;">
      <h4 style="margin: 0 0 10px 0; color: #10b981;">💡 Pro Tips</h4>
      <ul style="margin: 0; padding-left: 20px;">
         <li><strong>Start small</strong>: Use 2-3 files first to test your setup</li>
         <li><strong>Check parameters</strong>: Review <a href="parameters.html" style="color: #10b981;">parameter reference</a> for your instrument</li>
         <li><strong>Use test profiles</strong>: Try <code>test_lfq</code>, <code>test_dia</code>, or <code>test_tmt</code> first</li>
      </ul>
   </div>

Running your analysis
---------------------

.. code-block:: bash

   # Template command for your data
   nextflow run bigbio/quantms -r 1.7.0 \
     --input path/to/your.sdrf.tsv \
     --database path/to/proteome_plus_contaminants.fasta \
     --acquisition_method [dda|dia] \
     -profile docker

.. tip::
   **Need help with file paths?** See our :doc:`troubleshooting` guide for common path issues.

Understanding outputs
---------------------

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin: 20px 0;">
      
      <div style="background: #f0f9ff; padding: 15px; border-radius: 6px; border-left: 3px solid #3b82f6;">
         <strong style="color: #3b82f6;">📊 Results Tables</strong><br>
         <small>Protein/peptide quantification tables</small><br>
         <a href="quantms_output.html" style="color: #3b82f6;">→ Output Structure</a>
      </div>
      
      <div style="background: #f0fdf4; padding: 15px; border-radius: 6px; border-left: 3px solid #22c55e;">
         <strong style="color: #22c55e;">📈 QC Reports</strong><br>
         <small>Quality control and metrics</small><br>
         <a href="pmultiqc.html" style="color: #22c55e;">→ pMultiQC Guide</a>
      </div>
      
      <div style="background: #fef3c7; padding: 15px; border-radius: 6px; border-left: 3px solid #f59e0b;">
         <strong style="color: #f59e0b;">📊 Statistics</strong><br>
         <small>Differential expression analysis</small><br>
         <a href="msstats.html" style="color: #f59e0b;">→ MSstats Integration</a>
      </div>
   </div>

What's next?
------------

.. raw:: html

   <div style="background: #1e293b; color: #f1f5f9; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0;">🎯 Recommended Learning Path</h4>
      <ol style="margin: 0; padding-left: 20px;">
         <li><strong>Run the test successfully</strong> (this page)</li>
         <li><strong>Try with your data type</strong>: <a href="tutorials.html" style="color: #60a5fa;">Step-by-step tutorials</a></li>
         <li><strong>Understand parameters</strong>: <a href="parameters.html" style="color: #60a5fa;">Parameter reference</a></li>
         <li><strong>Quality control</strong>: <a href="pmultiqc.html" style="color: #60a5fa;">Interpret QC reports</a></li>
         <li><strong>Statistical analysis</strong>: <a href="msstats.html" style="color: #60a5fa;">Downstream statistics</a></li>
      </ol>
   </div>

Need help?
----------

- 🤔 **Confused?** Check our :doc:`glossary` for term definitions
- 🐛 **Something wrong?** See :doc:`troubleshooting` for common issues
- ❓ **Questions?** Visit our :doc:`faq` or :doc:`contact` page


