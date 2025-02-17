import random
import numpy as np


# Fungsi untuk menghitung nilai z
def calculate_z(n, x):
    return np.dot(n, x)


# Fungsi untuk memeriksa apakah nilai n memenuhi batasan
def is_valid(n, M, constraints):
    n_sum = sum(n)
    constraints_sum = sum(constraints)
    if n_sum != constraints_sum:
        return False

    n_accum = 0
    for i in range(len(constraints)):
        n_accum += n[i] - constraints[i]
        if not (0 <= n_accum <= M):
            return False
    return True


# Fungsi untuk menghasilkan solusi acak yang valid
def generate_random_solution(M, constraints):
    num_vars = len(constraints)
    while True:
        n = [random.randint(constraints[i], M) for i in range(num_vars - 1)]
        n_sum = sum(n)
        n_last = sum(constraints) - n_sum
        if n_last >= 0:
            n.append(n_last)
            if is_valid(n, M, constraints):
                return n


# Fungsi untuk menjalankan algoritma PSO
def particle_swarm_optimization(
    x, M, constraints, num_particles=50, num_iterations=100, w=0.5, c1=1.5, c2=1.5
):
    num_vars = len(constraints)

    # Inisialisasi partikel
    particles = [generate_random_solution(M, constraints) for _ in range(num_particles)]
    velocities = [np.random.uniform(-1, 1, num_vars) for _ in range(num_particles)]
    personal_best_positions = particles.copy()
    personal_best_scores = [calculate_z(p, x) for p in particles]
    global_best_position = min(particles, key=lambda p: calculate_z(p, x))
    global_best_score = calculate_z(global_best_position, x)

    for _ in range(num_iterations):
        for i, particle in enumerate(particles):
            r1, r2 = random.random(), random.random()
            velocities[i] = (
                w * velocities[i]
                + c1 * r1 * (np.array(personal_best_positions[i]) - np.array(particle))
                + c2 * r2 * (np.array(global_best_position) - np.array(particle))
            )
            new_position = np.array(particle) + velocities[i]
            new_position = [
                int(np.clip(new_position[j], 0, M)) for j in range(num_vars)
            ]
            new_position[-1] = sum(constraints) - sum(new_position[:-1])

            if new_position[-1] >= 0 and is_valid(new_position, M, constraints):
                particles[i] = new_position
                current_score = calculate_z(new_position, x)
                if current_score < personal_best_scores[i]:
                    personal_best_positions[i] = new_position
                    personal_best_scores[i] = current_score
                if current_score < global_best_score:
                    global_best_position = new_position
                    global_best_score = current_score

    return global_best_position, global_best_score
