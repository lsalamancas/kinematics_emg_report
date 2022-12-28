# kinematics_emg_report
This repository contains the code for the automatic generation of kinematic and EMG walking graph and ranges report.

## How to use? 

1. Move patient folder into project folder.
2. Import "walking.mdx" files into SmartAnalyzer. 
3. Export to text in the patient folder the next variables:
   - From all the runs:
      * 1D Angles Cycle sequences as  _"angles{run}.emt"_. 
   - From the selected run:
      * Scalars as _"scalars.emt"_
      * EMG Tracks as _"emg.emt"_
      * Times as _"times.emt"_
      * Event Sequences as _"events.emt"_
      * 1D Force Cycle Sequences as _"forces.emt"_
      * 1D Torque Cycle Sequences as _"torques.emt"_
      * Power Cycle Sequences as _"power.emt"_
4. Run main.py (I recommend executing from windows cmd)

**If you want to change the filenames to read, go to _config.yaml_ and do it**

