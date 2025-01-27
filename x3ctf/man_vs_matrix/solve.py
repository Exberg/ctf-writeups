from sage.all import *
from Crypto.Util.number import long_to_bytes

samples = [6192533, 82371, 86024, 4218430, 12259879, 16442850, 6736271, 7418630, 15483781]

p = next_prime(2**24)
F = GF(p)
gen = F(2)

# Compute all states S0 to S9
states = []
current_state = vector(F, [ord(c) for c in "Mvm"])  # S0
states.append(current_state)
for _ in range(9):
    next_state = vector(F, [gen**int(s) for s in current_state])
    states.append(next_state)
    current_state = next_state

# Prepare the coefficient matrix A and vector b
A = []
b = []
for k in range(9):
    S_prev = states[k]
    S_curr = states[k+1]
    equation = []
    # Expand (M * S_prev) ⋅ S_curr = sum_{i,j} M[i,j] * S_prev[j] * S_curr[i]
    for i in range(3):
        for j in range(3):
            equation.append(S_prev[j] * S_curr[i])
    A.append(equation)
    b.append(samples[k])

# Solve the system A * M_flattened = b
A_matrix = matrix(F, A)
b_vector = vector(F, b)
M_flattened = A_matrix.solve_right(b_vector)

# Reshape the flattened matrix into 3x3
M = matrix(F, 3, 3, M_flattened)

# Extract seed from matrix M
seed_bytes = b""
for element in M.list():
    seed_bytes += int(element).to_bytes(3, 'big')

# Construct the flag
flag = b"MVM{" + seed_bytes + b"}"
print(flag.decode('latin1'))
