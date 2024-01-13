# home-build-python
This dir is mainly used to store home build python scripts
==============================================================
Script #1: create_file_for_allmaps.py
   As is shown in the script name, the script was used to create input files for ALLMAPs in JCVI package (https://github.com/tanghaibao/jcvi/wiki/ALLMAPS).
   
   The usage is like: python create_file_for_allmaps.py blast_out_file.outfmt6 genetic_map_file.tab > files_for_allmaps 
   
   For creating blast_out_file.outfmt6 file above, maker sequences from certain genetic map should be first blast into the reference genome, blastn with parameter "--task blastn-short" was a better choice,
   and "outfmt -6" format of blast was assumed.
   
   The genetic_map_file.tab file was a common tab format, usually output by many linkage map construction programs, such as Joinmap. It includes columns "MarkerID", "Linkage group ID" and "cM position".
   The out of the script is also in tab format, including the columns "markerID", "Reference chrom", "cM position", "sseqid of blast_outfmt6", "qstart  of blast_outfmt6", 
                                                                      "qend of blast_outfmt6", "sstart of blast_outfmt6", "send of blast_outfmt6" and "maker new postion on the refrence genome".
                                                                      
   The information need in ALLMAPs, including Scaffold ID, scaffold position, LG, genetic position, lies within.
