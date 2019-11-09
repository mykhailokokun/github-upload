def spisok():
    differentnames = {
        0: "Stanislav",
        1: "Roman",
        2: "Dmytro",
        3: "Nataliia",
        4: "Mykhailo",
        5: "Nazar",
        6: "Galina",
        7: "Denis",
        8: "Vasil",
        9: "Anya",
        10: "Tanya",
        11: "Yuriy",
        12: "Oksana",
        13: "Uliya",
        14: "Irina",
        15: "Kateryna",
        16: "Vadim",
        17: "Vladislav",
        18: "Volodymyr",
        19: "Sergiy",
        20: "Oleksandr",
    }

    return differentnames.get(4)

print(spisok())