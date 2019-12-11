metal_numbers = [3, 4, 11, 12, 13] +\
    list(range(19, 32)) + list(range(37, 51)) + list(range(55, 85))

electronegs = {'Ti': 1.54, 'V': 1.63, 'Cr': 1.66, 'Mn': 1.55,
               'Fe': 1.83, 'Co': 1.88, 'Ni': 1.91, 'Cu': 1.90,
               'Zn': 1.65, 'Zr': 1.33, 'Nb': 1.6, 'Mo': 2.16,
               'Tc': 1.9, 'Ru': 2.2, 'Rh': 2.28, 'Pd': 2.20,
               'Ag': 1.93, 'Cd': 1.69, 'Y': 1.22, 'W': 2.36,
               'Ta': 1.5}


prefered_O_state = {'Co': 2,
                    'Sc': 3,
                    'Cr': 3,
                    'Ni': 2,
                    'Cu': 2,
                    'Mn': 2,
                    'Mo': 6,
                    'W': 6,
                    'Ru': 5,
                    'Ta': 5,
                    'Ti': 4,
                    'V': 5,
                    'Fe': 3,
                    'Zn': 2,
                    'Y': 3,
                    'Zr': 4,
                    'Nb': 5,
                    'Rh': 4,
                    'Pd': 2,
                    'Re': 6,
                    'Au': 3,
                    'Ag': 1,
                    'Cd': 2,
                    'Ir': 4,
                    }


favored_O_connections = {'Co': {'2': [3, 4, 5, 6],
                                '3': [4, 5, 6],
                                '4': [4, 6]},
                         'Cr': {'2': [4, 5, 6, 7],
                                '3': [6],
                                '4': [4, 5, 6],
                                '5': [4, 5, 6],
                                '6': [4]},
                         'Ni': {'2': [4, 5, 6],
                                '3': [4, 6],
                                '4': [4, 6]},
                         'Cu': {'1': [2, 4, 6, 8],
                                '2': [4, 5, 6],
                                '3': [4, 5, 6]},
                         'Mn': {'2': [4, 5, 6, 7, 8],
                                '3': [4, 5, 6],
                                '4': [6]},
                         'Mo': {'4': [6],
                                '5': [4, 6],
                                '6': [4, 5, 6]},
                         'W': {'5': [6],
                               '6': [4, 5, 6]},
                         'Ru': {'4': [6, 8],
                                '5': [6]},
                         'Ta': {'5': [4, 6, 7, 8]},
                         'Ti': {'3': [6],
                                '4': [4, 5, 6]},
                         'V': {'3': [6],
                               '4': [4, 5, 6],
                               '5': [4, 5, 6]},
                         'Fe': {'2': [3, 4, 5, 6, 8],
                                '3': [4, 5, 6]},
                         'Zn': {'2': [3, 4, 5, 6]},
                         'Y': {'3': [6, 7, 8],
                               '4': [6, 8]},
                         'Zr': {'4': [6, 7, 8]},
                         'Nb': {'3': [4, 5, 6],
                                '4': [4, 5, 6],
                                '5': [4, 5, 6]},
                         'Rh': {'3': [6],
                                '4': [6]},
                         'Pd': {'2': 4},
                         'Au': {'3': [4]},
                         'Ag': {'1': [2, 3, 4, 5, 6, 7, 8, 9]},
                         'Cd': {'2': [4, 5, 6, 7, 8, 12]},
                         'Sc': {'3': [6, 8]},
                         'Ir': {'4': [4, 6],
                                '5': [6]},
                         'Re': {'5': [4, 6],
                                '6': [6],
                                '7': [4, 6]}
                         }