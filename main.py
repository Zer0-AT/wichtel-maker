import random
import os

def wichteln(names):
    if len(names) < 2:
        print("Alleine gehts nit xD")
        return

    # Output shit
    output_folder = "wichtel_ergebnisse"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Zuweisung
    givers = names[:]
    receivers = names[:]
    random.shuffle(receivers)

    # Damit wichteln funktioniert
    for _ in range(100):  # unlucky
        if all(g != r for g, r in zip(givers, receivers)):
            break
        random.shuffle(receivers)
    else:
        print("Du hasch echt pech ^^")
        return

    # Save
    for giver, receiver in zip(givers, receivers):
        file_path = os.path.join(output_folder, f"{giver}.txt")
        with open(file_path, "w") as file:
            file.write(f"Hallo {giver}, dein Wichtel ist {receiver}.\n")

    print(f"Sellt funktioniert habn und habs da unter '{output_folder}' gpeichert!")


namen = ["Baum", "Maus", "Suppe", "Box"]
wichteln(namen)
