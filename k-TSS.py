
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This project is about implementing various simple algorithms of
# grammatical inference.
# 
# Copyright (C) 2011 Hugo Mougard & Gregoire Jadi
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def k_TSS2DFA(S, I, F, T, C) :
	Q = {pu[:i] for pu in I | C for i in range(len(pu) + 1)}
	Q |= {au[1:] for au in T}
	Q |= {ua[:-1] for ua in T}
	delta_data = {(pau[:i], pau[i], pau[:i + 1]) for pau in I | C for i\
			in range(len(pau))}
	delta_data |= {(aub[:-1], aub[-1], aub[1:]) for aub in T}
	Fa = {u for u in F | C}
	# Let's transform our set of transitions into a function
	print delta_data
	def delta(Qd, t) :
		for x in delta_data :
			if x[0] == Qd and x[1] == t :
				return x[2]

	return S, Q, '', Fa, delta


# Input: a sample S, a parameter k
def sample2k_TSS(S, k) :
	Si = {x for y in S for x in y}
	I = {x[:k - 1] for x in S if len(x) >= k - 1}
	C = {x for x in S if len(x) < k}
	F = {x[-k + 1:] for x in S if len(x) >= k - 1}
	T = {x[i:i + k] for x in S for i in range(len(x) - k + 1) if\
			len(x) >= k}
	return Si, I, F, T, C

sample = {"a", "aa", "abba", "abbbba"}
print("Sample : ", sample)
k3_TSS = sample2k_TSS(sample, 3)
print("Machine : ", k3_TSS)
DFA = k_TSS2DFA(* k3_TSS)
print("Automata : ", DFA)

