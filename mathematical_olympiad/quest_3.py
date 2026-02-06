# Tomášovi pohlednice

for Norsko in range(1, 39):
    for Island in range(1, 39):
        for Anglie in range(1, 39):
            if Norsko + Anglie + Island == 40 and \
            Anglie > Norsko and \
            (Anglie * 5 < Island < Anglie * 6):
                print(f"Norsko: {Norsko}, Anglie: {Anglie}, Island: {Island}")

# Možnost | Norsko | Anglie | Island
#    A    |    1   |    6   |   33
#    B    |    2   |    6   |   32
#    C    |    3   |    6   |   31
#
# Odpověď: Jdou udělat 3 kombinace,
# kde Anglie bude mít všude stejou hondnotu – 6