Frequently asked questions
==========================

How does MSGF+ pick CID or HCD spectra?
----------------------------------------

MSGF+ will pick specified spectra based on fragmentation method in SDRF or ``ms2_fragment_method`` parameter from nextflow config file (Default HCD).
Also there is a ``quant_activation_method`` parameter (default HCD auto) for ``IsobaricAnalyzer``.
The ``ms2_fragment_method`` should be CID, and ``quant_activation_method`` should be HCD if MS2 uses CID and MS3 uses HCD in TMT MS3 experiment.
For other MS2 experiment, we only consider ``ms2_fragment_method`` and just set it up correctly.

