import numpy as np


##################################functions ########################################################

def diastaseis_pinaka():
    print("ΠΙΝΑΚΑΣ ")
    while True:
        try:
            rows_n = int(input("Γραμμές: "))
            if rows_n > 0:
                break
            else:
                print("Ο αριθμός γραμμών πρέπει να είναι > 0.")
        except:
            print("Λάθος τύπος δεδομένων! Ξαναπροσπαθήστε εισάγοντας ακέραιο >0!")  # Μήνυμα λάθους
    while True:
        try:
            cols_n = int(input("Στήλες: "))
            if cols_n > 0:
                break
            else:
                print("Ο αριθμός στηλών πρέπει να είναι > 0.")
        except:
            print("Λάθος τύπος δεδομένων! Ξαναπροσπαθήστε εισάγοντας ακέραιο >0!")  # Μήνυμα λάθους
    return rows_n, cols_n


def eisagogi_pinaka(rows, cols):
    pin = np.zeros((rows, cols), dtype=float)  # αρχικοποίηση πίνακα με μηδενικά
    print(f"\nΔώστε τα στοιχεία του πίνακα [{rows}x{cols}]:")

    for i in range(rows):
        for j in range(cols):
            while True:
                try:
                    pin[i][j] = float(input(f"Στοιχείο [{i + 1}.{j + 1}]: "))  # Εισαγωγή στοιχείου
                    break
                except ValueError:
                    print("Λάθος τύπος δεδομένων! Ξαναπροσπαθήστε εισάγοντας αριθμό!")  # Μήνυμα λάθους
        print("")

    return pin


def ektiposi_pinaka(pin):
    rows, cols = pin.shape  # για να πάρουμε τις διαστάσεις του πίνακα που περνάμε στη συνάρτηση
    print(f"Πίνακας [{rows}x{cols}]:")
    for i in range(rows):
        for j in range(cols):
            print(f"{pin[i][j]:8.3f}", end=" ")
        print("")


def metatroph_gauss(A):
    rows, cols = A.shape  # για να πάρουμε τις διαστάσεις του πίνακα που περνάμε στη συνάρτηση
    for i in range(rows):
        # Βρίσκουμε τον κύριο στοιχείο (οδηγό στοιχείο)
        if A[i][i] == 0:  # αν έχουμε 0
            found_mh_mhdeniko = False  # θέτουμε τη boolean σε false
            for j in range(i + 1, rows):  # ψάχνουμε το πρώτο μη μηδενικο
                if A[j][i] != 0:
                    A[[i, j]] = A[[j, i]]  # ανταλλάσουμε γραμμές με numpy
                    found_mh_mhdeniko = True
                    break

            # Αν δεν βρούμε κανένα μη μηδενικό στοιχείο, το σύστημα είναι αδύνατο
            if not found_mh_mhdeniko:
                print("Το σύστημα είναι αδύνατο!")
                return None  

        A[i] = A[i] / A[i][i]  # κάνουμε την γραμμή με την κατάλληλη διαίρεση να έχει οδηγό στοιχείο 1

        # Κάνουμε τα στοιχεία πάνω και κάτω από το κύριο στοιχείο 0.
        for j in range(rows):
            if j != i:  # για να παρακάμψουμε την τρέχουσα γραμμή
                A[j] = A[j] - A[j][i] * A[i]  # γραμμοπράξη για μηδενισμό

    return A


##################### ΚΥΡΙΩΣ ΠΡΟΓΡΑΜΜΑ ################################################

# Τίτλος εφαρμογής
print("\n" + "=" * 12 + " ΑΝΑΛΥΣΗ ΠΙΝΑΚΑ " + "=" * 12 + "\n")

# Διαστάσεις Πίνακα (εισαγωγή με κλήση συνάρτησης)
A_rows, A_cols = diastaseis_pinaka()

# Εισαγωγή στοιχείων Πίνακα με κλήση αντίστοιχης συνάρτησης
A = eisagogi_pinaka(A_rows, A_cols)

# Εκτύπωση Πίνακα με κλήση αντίστοιχης συνάρτησης
print("\nΑρχικός Πίνακας:")
ektiposi_pinaka(A)

# Εφαρμόζουμε Gauss-Jordan για να μετατραπεί σε ανηγμένο κλιμακωτό
A_reduced = metatroph_gauss(A)

# Εκτύπωση του ανηγμένου κλιμακωτού πίνακα
if A_reduced is not None:
    print("\nΠίνακας σε ανηγμένη κλιμακωτή μορφή:")
    ektiposi_pinaka(A_reduced)