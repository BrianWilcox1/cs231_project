# cs231_project
6/7/2018
Steps to try to replicate results:
1. Download PROSTATEx-v1-doinlp.jnlp file from ProstateX website :https://wiki.cancerimagingarchive.net/plugins/servlet/mobile?contentId=23691656#content/view/23691656 
2. Depending on your operating system, find a way to open and run the file to the get the dicom image data: https://fileinfo.com/extension/jnlp. This is a lot of data (1.5 GB unaugmented)
3. Navigate to PROSTATEX directory and run the dicom_reader.py script. This will convert all of the T2-weighted and ADC images from dicom files to png files. Then run the generate_datasets.py or generate_datasets_b.py (with data augmentation).

Note on training these GANs: The group used the Sherlock Cluster at Stanford University to train these models on GPU nodes. For specs on the hardware, please see: https://www.sherlock.stanford.edu/docs/overview/specs/. Depending on the hyperparameters/job scheduling, these can take anyhwere from 6 hours to 2 days to run on this hardware.

4. To run the DualGAN code simply copy over the datasets directory and its contents to the DualGAN/datasets directory. Alternatively, one can append the initial file path. (This will be cleaned up in a later version). Then follow the instructions as specified in the local directories README.md
5. To run the CycleGAN code, do the same as specified above.
6. Upon finishing the runs, run the distance.py and neighbor.py scripts to generate the quantitative and qualitative results.
