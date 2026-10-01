CHAINS = [16, 14, 12, 10, 8, 6, 4]

SPECIES = {}

idx = 0

for chain in CHAINS:

    SPECIES[f"acylcoa_C{chain}"] = idx
    idx += 1

    SPECIES[f"enoyl_C{chain}"] = idx
    idx += 1

    SPECIES[f"hydroxy_C{chain}"] = idx
    idx += 1

    SPECIES[f"keto_C{chain}"] = idx
    idx += 1

SPECIES["acetylcoa"] = idx
idx += 1

SPECIES["nad"] = idx
idx += 1

SPECIES["nadh"] = idx
idx += 1

SPECIES["fad"] = idx
idx += 1

SPECIES["fadh2"] = idx
idx += 1

SPECIES["atp"] = idx
idx += 1

SPECIES["oxaloacetate"] = idx
idx += 1

SPECIES["malate"] = idx
idx += 1

SPECIES["acetoacetate"] = idx
idx += 1

SPECIES["bhb"] = idx
idx += 1

SPECIES["ferricyanide_signal"] = idx
idx += 1

N_SPECIES = idx