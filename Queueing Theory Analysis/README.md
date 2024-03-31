# Queueing Theory Analysis

This project analyzes a queueing system using Sagemath. The script calculates the probability distribution of the number of customers in the system, the expected number of customers, and the expected waiting time.

## Overview

The script is divided into 3 sections:

1. **Recurrence Relation for P(n)**: We define a function `P(n)` that calculates the probability of having `n` customers in the system using a recurrence relation. The base cases for `n = 0` and `n = 1` are defined, and the cases with `n > 1` are defined in terms of `P(n-1)`.

2. **Closed-form Expression for P(n)**: Then we define a closed-form expression for `P(n)` as `rho^n * (1 - rho)`
( `rho` - traffic intensity of the system)

3. **Expected Number of Customers (L) and Expected Waiting Time (W)**: Here we calculate the expected number of customers in the system `L` and the expected waiting time in the queue `W`. The script the closed-form expression for `P(n)` to calculate `L`, and then uses `L` to calculate `W`.


## Mathematical Background

This script is based on the theory of M/M/1 queues, which are a type of queueing system where arrivals follow a Poisson process, service times have exponential distribution, and there is a single server. The parameters of the system are `lam` (arrival rate) and `mu` (service rate). `rho` - traffic intensity is important for determining behavior of system.
