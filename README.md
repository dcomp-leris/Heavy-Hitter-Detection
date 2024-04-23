# Network-Wide Heavy Hitters Detection with Multi-Pipes Switches

## Description

This repository contains an emulator for detecting *Heavy Hitters* in a *Network-Wide* setting with multi-pipes switches. The emulator supports two distinct approaches for this detection: the Accumulator (*A*) approach and the Local-Pipe (*LP*) approach. Each approach has its corresponding implementation in the source code, identified by the letters *A* and *LP* in the program names.

Furthermore, both approaches offer two options for detection methods: with Adaptive Limits and with Fixed Limit.

Both approaches provide adaptable detection options, allowing the user to adjust the following parameters:

- **Number of Switches**: The number of switches involved in detection can be specified by the user.

- **Limit**: The user can set a global limit for detecting *Heavy Hitters*, whether adaptive or fixed.

- **Smoothing Factor**: Smoothing can be customized with a user-chosen factor. The Smoothing Factor refers to the variable responsible for the adaptive limit.

- **Pipes**: The user can configure the number of pipes as needed, up to 16 pipes.

## Approaches

- **Accumulator Approach (*A*)**: This approach uses an accumulator in the switch for counting and communication with the control plane.

- **Local Pipe Approach (*LP*)**: This approach communicates individually through a pipe with the control plane.

## Execution

We use the CAIDA Equinix-NYC Trace, which has been divided into parts for each switch, aiming to simulate the distribution of data flow across different switches in the network. The complete trace is contained in the file "f1Score.py", which performs the actual counting for obtaining the F1-Score metric.

To execute the code, it is necessary to run the file "terminalA.py" for the Accumulator or "terminalLP.py" for the Local-Pipe. If you wish to modify the trace, you will need to make changes in the network switches and in the code "f1Score.py".

To run the code using adaptive or fixed limits, you need to make changes in the switches of the respective approach and in the coordinator (the location of the change is indicated as a comment). If you want to increase the number of switches in the network, you will need to make changes in the terminal corresponding to the desired approach.
