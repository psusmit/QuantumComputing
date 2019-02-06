import cirq
import numpy as np
from cirq import Circuit
from cirq.devices import GridQubit
from cirq.google import XmonSimulator# creating circuit with 4 qubits
#define length of qubits
l=4
#setting up qubits on grid
qubits = [cirq.GridQubit(x,y) for x in range(l) for y in range(l)]
#defining the cirquit
circuit = cirq.Circuit()
#all the gates r applied to the circuit man its like deep learninig neural model
h1 = cirq.H(qubits[2])
toffoli = cirq.TOFFOLI(qubits[2],qubits[3],qubits[4])
h2 = cirq.H(qubits[1])
h3 = cirq.H(qubits[2])
h4 = cirq.H(qubits[3])
cz1 = cirq.CZ(qubits[2],qubits[1])
cz2 = cirq.CZ(qubits[2],qubits[3])
#constructing moments of gates to apply on circuit
moment1 = cirq.Moment([h1])
moment2 = cirq.Moment([toffoli])
moment3 = cirq.Moment([h1])
moment4 = cirq.Moment([h2,h3,h4])
moment5 = cirq.Moment([cz1])
moment6 = cirq.Moment([cz2])
moment7 = cirq.Moment([h2,h3,h4])
circuit = cirq.Circuit((moment1,moment2,moment3,moment4,moment5,moment6,moment7))
simulator = cirq.google.XmonSimulator()
result = simulator.simulate(circuit)
#print(result)
print(circuit)
