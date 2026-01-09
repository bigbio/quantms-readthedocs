quantms: A cloud-based workflow for peptide and protein quantification
=======================================================================

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 10px; color: white; text-align: center; margin: 20px 0;">
      <h2 style="margin: 0; font-size: 24px;">🧬 Welcome to quantms</h2>
      <p style="margin: 10px 0; font-size: 18px;">A comprehensive, reproducible workflow for mass spectrometry-based proteomics quantification</p>
   </div>

.. image:: images/quantms.png
   :width: 600
   :align: center

Quickstart: 5-minute test
==========================

.. raw:: html

   <div style="background: linear-gradient(135deg, #059669 0%, #10b981 100%); padding: 25px; border-radius: 10px; color: white; text-align: center; margin: 20px 0;">
      <h3 style="margin: 0; font-size: 20px;">⚡ Get quantms running in 5 minutes</h3>
      <p style="margin: 10px 0;">Test the pipeline with Docker using our sample dataset</p>
   </div>

.. raw:: html

   <div style="background: #1f2937; color: #f9fafb; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
         <span style="background: #22c55e; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 15px;">1</span>
         <span style="font-size: 18px; font-weight: bold;">Install Nextflow (one-time setup)</span>
      </div>
      <div style="background: #374151; padding: 15px; border-radius: 6px; font-family: monospace; font-size: 14px; margin: 10px 0;">
         curl -s https://get.nextflow.io | bash<br>
         mv nextflow ~/.local/bin/
      </div>
   </div>

.. raw:: html

   <div style="background: #1f2937; color: #f9fafb; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
         <span style="background: #3b82f6; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 15px;">2</span>
         <span style="font-size: 18px; font-weight: bold;">Run the test</span>
      </div>
      <div style="background: #374151; padding: 15px; border-radius: 6px; font-family: monospace; font-size: 14px; margin: 10px 0;">
         nextflow run bigbio/quantms -r 1.7.0 -profile test_lfq,docker
      </div>
      <div style="background: #065f46; padding: 10px; border-radius: 4px; margin-top: 10px;">
         <strong>✅ Success:</strong> You should see "Pipeline completed successfully!" after 5-10 minutes
      </div>
   </div>

.. note::
   **Prerequisites**: Make sure you have Java 11+ and Docker installed.

.. raw:: html

   <div style="background: #ede9fe; padding: 20px; border-radius: 8px; border-left: 4px solid #8b5cf6; margin: 20px 0;">
      <h4 style="margin: 0 0 10px 0; color: #8b5cf6;">🎯 Ready for your own data?</h4>
      <p style="margin: 0 0 15px 0;">Replace the test files with your own:</p>
      <div style="background: #1f2937; color: #f9fafb; padding: 15px; border-radius: 6px; font-family: monospace; font-size: 12px; margin: 10px 0;">
         nextflow run bigbio/quantms -r 1.7.0 \<br>
         &nbsp;&nbsp;--input YOUR_EXPERIMENT.sdrf.tsv \<br>
         &nbsp;&nbsp;--database YOUR_PROTEOME.fasta \<br>
         &nbsp;&nbsp;-profile docker
      </div>
   </div>

Navigate to the right section
=============================

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #007bff;">
         <h3 style="margin: 0 0 10px 0; color: #007bff;">📖 Learn the Basics</h3>
         <p style="margin: 0 0 15px 0;">Understand prerequisites and core concepts</p>
         <a href="getting_started.html" style="color: #007bff; text-decoration: none; font-weight: bold;">→ Getting started guide</a>
      </div>
      
      <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #ffc107;">
         <h3 style="margin: 0 0 10px 0; color: #e68900;">🎯 Step-by-Step</h3>
         <p style="margin: 0 0 15px 0;">Follow detailed tutorials for your data type</p>
         <a href="tutorials.html" style="color: #e68900; text-decoration: none; font-weight: bold;">→ View tutorials</a>
      </div>
      
      <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #28a745;">
         <h3 style="margin: 0 0 10px 0; color: #28a745;">⚙️ Configure</h3>
         <p style="margin: 0 0 15px 0;">Customize parameters for your analysis</p>
         <a href="parameters.html" style="color: #28a745; text-decoration: none; font-weight: bold;">→ Parameter reference</a>
      </div>
   </div>

.. raw:: html

   <div style="background: #e8f4fd; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <h3 style="margin: 0 0 15px 0; color: #0c5aa6;">🔬 What type of data do you have?</h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
         <div style="background: white; padding: 15px; border-radius: 6px; text-align: center;">
            <strong>DDA</strong><br>
            <small>Data-Dependent Acquisition</small><br>
            <a href="dda.html" style="color: #0c5aa6;">→ DDA Analysis</a>
         </div>
         <div style="background: white; padding: 15px; border-radius: 6px; text-align: center;">
            <strong>DIA</strong><br>
            <small>Data-Independent Acquisition</small><br>
            <a href="dia.html" style="color: #0c5aa6;">→ DIA Analysis</a>
         </div>
         <div style="background: white; padding: 15px; border-radius: 6px; text-align: center;">
            <strong>TMT/iTRAQ</strong><br>
            <small>Isobaric Labeling</small><br>
            <a href="iso.html" style="color: #0c5aa6;">→ Isobaric Analysis</a>
         </div>
         <div style="background: white; padding: 15px; border-radius: 6px; text-align: center;">
            <strong>Label-Free</strong><br>
            <small>LFQ Quantification</small><br>
            <a href="lfq.html" style="color: #0c5aa6;">→ LFQ Analysis</a>
         </div>
      </div>
   </div>

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">
      
      <div style="background: #fff3cd; padding: 20px; border-radius: 8px; border-left: 4px solid #856404;">
         <h4 style="margin: 0 0 10px 0; color: #856404;">📚 Documentation</h4>
         <ul style="margin: 0; padding-left: 20px;">
            <li><a href="usage.html">Usage & Installation</a></li>
            <li><a href="introduction.html">Introduction</a></li>
            <li><a href="parameters.html">Parameter Reference</a></li>
            <li><a href="inputs_outputs.html">Inputs & Outputs</a></li>
         </ul>
      </div>
      
      <div style="background: #d1ecf1; padding: 20px; border-radius: 8px; border-left: 4px solid #0c5aa6;">
         <h4 style="margin: 0 0 10px 0; color: #0c5aa6;">🔬 Analysis Types</h4>
         <ul style="margin: 0; padding-left: 20px;">
            <li><a href="dda.html">DDA Analysis</a></li>
            <li><a href="dia.html">DIA Analysis</a></li>
            <li><a href="iso.html">Isobaric Labeling</a></li>
            <li><a href="lfq.html">Label-Free Quantification</a></li>
         </ul>
      </div>
      
      <div style="background: #d4edda; padding: 20px; border-radius: 8px; border-left: 4px solid #155724;">
         <h4 style="margin: 0 0 10px 0; color: #155724;">⚙️ Advanced</h4>
         <ul style="margin: 0; padding-left: 20px;">
            <li><a href="preprocessing.html">Preprocessing</a></li>
            <li><a href="identification.html">Identification</a></li>
            <li><a href="modlocal.html">Modification localization</a></li>
            <li><a href="protein_database.html">Protein Databases</a></li>
            <li><a href="statistics.html">Statistics</a></li>
         </ul>
      </div>
      
      <div style="background: #f8d7da; padding: 20px; border-radius: 8px; border-left: 4px solid #721c24;">
         <h4 style="margin: 0 0 10px 0; color: #721c24;">🛠️ Tools & QC</h4>
         <ul style="margin: 0; padding-left: 20px;">
            <li><a href="pmultiqc.html">Quality Control</a></li>
            <li><a href="benchmarks.html">Benchmarks</a></li>
            <li><a href="comparison.html">Tool Comparison</a></li>
            <li><a href="capabilities.html">Features Timeline</a></li>
         </ul>
      </div>
      
      <div style="background: #e2e3e5; padding: 20px; border-radius: 8px; border-left: 4px solid #495057;">
         <h4 style="margin: 0 0 10px 0; color: #495057;">📞 Help & Support</h4>
         <ul style="margin: 0; padding-left: 20px;">
            <li><a href="glossary.html">Glossary</a></li>
            <li><a href="troubleshooting.html">Troubleshooting</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="contact.html">Contact</a></li>
         </ul>
      </div>
      
      <div style="background: #f0f4ff; padding: 20px; border-radius: 8px; border-left: 4px solid #6366f1;">
         <h4 style="margin: 0 0 10px 0; color: #6366f1;">🔧 Development</h4>
         <ul style="margin: 0; padding-left: 20px;">
            <li><a href="dev.html">Contributing</a></li>
            <li><a href="debug.html">Debugging</a></li>
            <li><a href="presentations.html">Presentations</a></li>
         </ul>
      </div>
   </div>

.. toctree::
   :maxdepth: 1
   :hidden:

   getting_started
   tutorials
   usage
   introduction
   preprocessing
   protein_database
   identification
   modlocal
   dda
   dia
   statistics
   parameters
   inputs_outputs
   pmultiqc
   benchmarks
   comparison
   capabilities
   glossary
   troubleshooting
   debug
   faq
   presentations
   dev
   contact

|

The following links should be followed to get support and help with the quantms maintainers:

|Get help on Slack|   |Report Issue| |Get help on GitHub Forum|

.. |Get help on Slack| image:: https://img.shields.io/badge/slack-nf--core%20%23quantms-4A154B?labelColor=000000&logo=slack
                   :target: https://nfcore.slack.com/channels/quantms

.. |Report Issue| image:: https://img.shields.io/github/issues/bigbio/quantms
                   :target: https://github.com/bigbio/quantms/issues

.. |Get help on GitHub Forum| image:: https://img.shields.io/badge/Github-Discussions-green
                   :target: https://github.com/bigbio/quantms/discussions



What's new and capabilities
---------------------------

- See a concise overview of what quantms can do and when features were introduced in `Capabilities <capabilities.html>`_.
- For a quick orientation on how quantms compares to other tools, check `Comparison <comparison.html>`_.



