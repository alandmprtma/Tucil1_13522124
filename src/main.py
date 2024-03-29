# Library/Pustaka Python
from colorama import init, Fore, Back, Style
import os
import time
import random

running = True
while (running == True):
    # Prosedur Input Program melalui .txt
    def readfromfile(filename):
        matrix = []
        sequences = []
        sequences_score = []
        with open(filename, 'r') as file:
            buffer_size = int(file.readline().strip())
            matrix_width , matrix_height = map(int, file.readline().strip().split())
            
            for _ in range(matrix_height):
                row = file.readline().strip().split()
                matrix.append(row)
            num_sequences = int(file.readline().strip())
            for _ in range(num_sequences):
                sequence = file.readline().strip().split()
                score = int(file.readline().strip())
                sequences.append(sequence)
                sequences_score.append(score)
        return matrix_width, matrix_height, buffer_size, matrix, sequences, sequences_score

    # Prosedur generate input secara random
    def generaterandominput():
        # Maksimum jumlah kolom dan baris
        max_rows = random.randint(3,6)
        max_columns = random.randint(3,6)
        
        # Maksimum jumlah sequences dan sequences_score
        max_sequences = random.randint(1, 3)
        
        # Generate code matrix
        code_matrix = [[random.choice(['7A', '55', 'E9', '1C', 'BD']) for _ in range(max_columns)] for _ in range(max_rows)]
        
        # Generate buffer size
        buffer_size = random.randint(1, 7)
        
        # Generate sequences and sequences_score
        sequences = []
        sequences_score = []
        for _ in range(max_sequences):
            sequence_length = random.randint(2, 4)  # Jumlah token pada sekuens
            sequence = [random.choice(['7A', '55', 'E9', '1C', 'BD']) for _ in range(sequence_length)]
            sequences.append(sequence)
            sequences_score.append(random.randint(1, 5)*10*sequence_length)  # Nilai score secara acak antara 1 hingga 50
        
        return max_columns, max_rows, code_matrix, buffer_size, sequences, sequences_score


    # Inisialisasi colorama
    init()

    # Fungsi untuk mencetak teks berwarna hijau neon (Bertujuan untuk mencetak text cyberpunk 2077 breach protocol solver ketika diclear)
    def print_neon(text):
        print(Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)

    # Teks yang akan dicetak
    text_to_print = """
    ______________.___._________________________________________ ____ __________   ____  __. _________________________________                         
    \_   ___ \__  |   |\______   \_   _____/\______   \______   \    |   \      \ |    |/ _| \_____  \   _  \______  \______  \                        
    /    \  \//   |   | |    |  _/|    __)_  |       _/|     ___/    |   /   |   \|      <    /  ____/  /_\  \  /    /   /    /                        
    \     \___\____   | |    |   \|        \ |    |   \|    |   |    |  /    |    \    |  \  /       \  \_/   \/    /   /    /                         
    \______  / ______| |______  /_______  / |____|_  /|____|   |______/\____|__  /____|__ \ \_______ \_____  /____/   /____/                          
            \/\/               \/        \/         \/                          \/        \/         \/     \/                                         
    __________                              .__      __________                __                      .__      _________      .__                     
    \______   \_______   ____ _____    ____ |  |__   \______   \_______  _____/  |_  ____   ____  ____ |  |    /   _____/ ____ |  |___  __ ___________ 
    |    |  _/\_  __ \_/ __ \\__  \ _/ ___\|  |  \   |     ___/\_  __ \/  _ \   __\/  _ \_/ ___\/  _ \|  |    \_____  \ /  _ \|  |\  \/ // __ \_  __ \
    |    |   \ |  | \/\  ___/ / __ \\  \___|   Y  \  |    |     |  | \(  <_> )  | (  <_> )  \__(  <_> )  |__  /        (  <_> )  |_\   /\  ___/|  | \/
    |______  / |__|    \___  >____  /\___  >___|  /  |____|     |__|   \____/|__|  \____/ \___  >____/|____/ /_______  /\____/|____/\_/  \___  >__|   
            \/              \/     \/     \/     \/                                            \/                     \/                      \/     
    """

    # Cetak teks
    print_neon(text_to_print)
    print(Fore.RED + "welcome to Cyberpunk 2077 Breach Protocol Solver by Aland Mulia Pratama - 13522124!")
    print("Please choose one of the input methods for the breach protocol solver program:")
    print("1. Input from file.txt (from the config folder)")
    print("2. Generate random input")
    print(">> ", end = "")

    # Input pilihan
    input_method = input()
    while (input_method != "1" and input_method != "2"):
        print("Please input a valid option (1 or 2)")
        print(">> ", end = "")
        input_method = input()
    os.system("cls" if os.name == "nt" else "clear")

    # Jika input method adalah 1
    if input_method == "1":
        print_neon(text_to_print)
        print(Fore.RED + "Please input the filename (without the .txt extension) from the config folder")
        print(">> ", end = "")
        filename = "../config/" + input() + ".txt"
        matrix_width, matrix_height, buffer_size, code_matrix, sequences, sequences_score = readfromfile(filename)
        os.system("cls" if os.name == "nt" else "clear") #membersihkan layar CLI
    elif input_method == "2":
        matrix_width, matrix_height, code_matrix, buffer_size, sequences, sequences_score = generaterandominput()
        os.system("cls" if os.name == "nt" else "clear") #membersihkan layar CLI 

    # mencetak code_matrix
    print_neon(text_to_print)
    print(Fore.RED + "The protocol has been successfully loaded!")
    print("buffer size: ", buffer_size)
    print("\n")
    print("MATRIX OF TOKENS")
    for i in range(len(code_matrix)):
        for j in range(len(code_matrix[i])):
            print(code_matrix[i][j], end = " ")
        print("")
    print("\n")
    print("SEQUENCES | REWARD LEVELS")
    for i in range(len(sequences)):
        print(sequences[i], " | ", sequences_score[i])
    print("\n")
    print("Please wait for a moment, the program is currently solving the breach protocol...\n")

    # memulai program utama
    start_time = time.time()

    class DuplicatedCoordinateException(Exception):
        pass

    # lintasan koordinat memenuhi syarat seperti berikut:
    # [(a, 1), (a, b), (c, b), (c, d), ...]

    class Path():
        def __init__(self, coords=[]):
            self.coords = coords

        def __add__(self, other):
            new_coords = self.coords + other.coords
            if any(map(lambda coord: coord in self.coords, other.coords)):
                raise DuplicatedCoordinateException()
            return Path(new_coords)

        def __repr__(self):
            return str(self.coords)


    class SequenceScore():
        def __init__(self, sequence, buffer_size, reward_level=0):
            self.max_progress = len(sequence)
            self.sequence = sequence
            self.score = 0
            self.reward_level = reward_level
            self.buffer_size = buffer_size

        def compute(self, compare):
            if not self.__completed():
                if self.sequence[self.score] == compare:
                    self.__increase()
                else:
                    self.__decrease()

        # Ketika kepala urutan cocok dengan node yang ditargetkan, tambah skornya sebesar 1
        # Jika urutannya sudah selesai, atur skornya tergantung level hadiahnya
        def __increase(self):
            self.buffer_size -= 1
            self.score += 1

            if self.__completed():
                self.score = 10 ** (self.reward_level + 1)

        # Ketika nilai yang salah dicocokkan dengan urutan teratas saat ini, skor dikurangi 1 (tidak boleh di bawah 0)
        # Jika urutannya tidak dapat diselesaikan, tetapkan skor ke nilai negatif tergantung pada hadiahnya 
        def __decrease(self):
            self.buffer_size -= 1
            if self.score > 0:
                self.score -= 1
            if self.__completed():
                self.score = -self.reward_level - 1

        # Suatu urutan dianggap selesai jika tidak ada kemajuan lebih lanjut yang mungkin atau tidak diperlukan
        def __completed(self):
            return self.score < 0 or self.score >= self.max_progress or self.buffer_size < self.max_progress - self.score


    class PathScore():
        def __init__(self, path, sequences, buffer_size):
            self.score = None
            self.path = path
            self.sequence_scores = [SequenceScore(sequence, buffer_size, reward_level) for reward_level, sequence in enumerate(sequences)]

        def compute(self): # Mengembalikan jumlah skor urutan individu
            if self.score != None:
                return self.score
            for row, column in self.path.coords:
                for seq_score in self.sequence_scores:
                    seq_score.compute(code_matrix[row][column])
            self.score = sum(map(lambda seq_score: seq_score.score, self.sequence_scores))
            return self.score
    
    def generate_paths_square(buffer_size):
        completed_paths = []
        # Kembalikan baris/kolom berikutnya yang tersedia untuk belokan dan koordinat tertentu.
        # Jika giliran pertama indeksnya adalah 0 maka next_line akan mengembalikannya
        # baris pertama. Untuk putaran kedua, kolom ke-n akan dikembalikan, dengan n
        # menjadi baris koordinat
        def candidate_coords(turn=0, coordinate=(0,0)):
            if turn % 2 == 0:
                return [(coordinate[0], column) for column in range(len(code_matrix))]
            else:
                return [(row, coordinate[1]) for row in range(len(code_matrix))]
        # berisi semua kemungkinan lintasan yang dilalui

        def _walk_paths(buffer_size, completed_paths, partial_paths_stack = [Path()], turn = 0, candidates = candidate_coords()):
            path = partial_paths_stack.pop()            
            for coord in candidates:
                try:
                    new_path = path + Path([coord])
                # Lewati koordinat jika sudah pernah dikunjungi (Tidak ada token yang dilalui dua kali)
                except DuplicatedCoordinateException:
                    continue

                # Jalur lengkap ditambahkan ke daftar pengembalian akhir dan dihapus dari tumpukan jalur parsial
                if len(new_path.coords) == buffer_size:
                    completed_paths.append(new_path) 
                else: # Tambahkan jalur parsial baru yang lebih panjang kembali ke tumpukan
                    partial_paths_stack.append(new_path) 
                    _walk_paths(buffer_size, completed_paths, partial_paths_stack, turn + 1, candidate_coords(turn + 1, coord))
        _walk_paths(buffer_size, completed_paths)
        return completed_paths

    def generate_paths(buffer_size, max_rows, max_columns):
        completed_paths = []
        """ Mengembalikan baris/kolom berikutnya yang tersedia untuk belokan dan koordinat tertentu.
        Jika giliran pertama indeksnya adalah 0 sehingga next_line akan mengembalikan 
        baris pertama. Untuk putaran kedua, kolom ke-n akan dikembalikan, dengan n menjadi baris koordinat """

        def candidate_coords(turn=0, coordinate=(0,0)):
            row, col = coordinate
            candidates = []
            if row < max_rows - 1:
                candidates.append((row + 1, col))  # Langkah ke bawah
            if col < max_columns - 1:
                candidates.append((row, col + 1))  # Langkah ke kanan
            return candidates

        def _walk_paths(buffer_size, completed_paths, partial_paths_stack=[Path()], turn=0, candidates=candidate_coords()):
            path = partial_paths_stack.pop()

            for coord in candidates:
                try:
                    new_path = path + Path([coord])
                except DuplicatedCoordinateException:
                    continue

                if len(new_path.coords) == buffer_size:
                    completed_paths.append(new_path) 
                else:
                    partial_paths_stack.append(new_path) 
                    _walk_paths(buffer_size, completed_paths, partial_paths_stack, turn + 1, candidate_coords(turn + 1, coord))

        _walk_paths(buffer_size, completed_paths)
        return completed_paths

    #Membedakan cara kerja dalam memperoleh lintasan untuk matriks persegi dan tidak
    if (matrix_width == matrix_height):
        paths = [(path, PathScore(path, sequences, buffer_size).compute()) for path in generate_paths_square(buffer_size)]
    else:
        paths = [(path, PathScore(path, sequences, buffer_size).compute()) for path in generate_paths(buffer_size, len(code_matrix), len(code_matrix[0]))]

    max_path = max(paths, key=lambda path: path[1])

    def is_sublist(list1, list2):
        # Menggunakan nested loop untuk mencocokkan potongan list1 pada setiap elemen list2
        for i in range(len(list2) - len(list1) + 1):
            if list2[i:i+len(list1)] == list1:
                return True
        return False

    def save_to_txt(max_score, solution, buffer_size, sumbuX, sumbuY, execution_time, filename):
        with open(filename, 'w') as file:
            file.write(f"Max Score: {max_score}\n\n")
            file.write("Solution:\n")
            for item in solution:
                file.write(f"{item} ")
            file.write("\n\nCoordinates:\n")
            for i in range(buffer_size):
                file.write(f"{sumbuX[i]} {sumbuY[i]}\n")
            file.write("\nExecution Time:\n")
            file.write(f"{round(execution_time*1000)} ms\n")

    # Memperbaiki urutan koordinat sebelum mencetak

    # PROGRAM UTAMA
    sumbuX = []
    sumbuY = []
    for coord in max_path[0].coords:
        sumbuX.append(coord[1] + 1)
        sumbuY.append(coord[0] + 1)

    solution = []
    for i in range (buffer_size):
        solution.append(code_matrix[sumbuY[i]-1][sumbuX[i]-1])

    count = 0
    max_score = 0
    for section in sequences:
        if is_sublist(section,solution):
            max_score += sequences_score[count]
        count += 1

    if (max_score == 0):
        print("There is no sequence fulfilled with every possible step!")
        end_time = time.time()
        execution_time = end_time - start_time
        print(round(execution_time*1000), " ms")
        print("\n")
        check = True
        while check == True:
            print("Would you like to solve another breach protocol? (y/n): ")
            response = input(">> ").strip().lower()
            if response == 'y' or response == 'n':
                if response == 'y':
                    os.system("cls" if os.name == "nt" else "clear")
                else:
                    print(Fore.RED + "Thank you for using Cyberpunk 2077 Breach Protocol Solver by Aland Mulia Pratama - 13522124!")
                    print("Goodbye!")
                    running = False
                check = False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    else:
        print(max_score)

        for i in range (len(solution)):
            print(solution[i], end = " ")

        print("")

        for i in range (buffer_size):
            print(sumbuX[i],"",sumbuY[i])
        print("")
        end_time = time.time()
        execution_time = end_time - start_time
        print(round(execution_time*1000), " ms")
        print("\n")
        check = True
        while check == True:
            print("Do you want to save the solution to a .txt file? (y/n): ")
            response = input(">> ").strip().lower()
            if response in ['y', 'n']:
                if response == 'y':
                    print("Please input name of the file you would like to save to the test folder (without the .txt extension)")
                    print(">> ", end = "")
                    filename = "../test/" + input() + ".txt"
                    save_to_txt(max_score, solution, buffer_size, sumbuX, sumbuY, execution_time, filename)
                    print("Solution has been saved to ", filename, " !")
                    check = False
                elif response == 'n':
                    check = False
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        check = True
        while check == True:
            print("Would you like to solve another breach protocol? (y/n): ")
            response = input(">> ").strip().lower()
            if response == 'y' or response == 'n':
                if response == 'y':
                    os.system("cls" if os.name == "nt" else "clear")
                else:
                    print(Fore.RED + "Thank you for using Cyberpunk 2077 Breach Protocol Solver by Aland Mulia Pratama - 13522124!")
                    print("Goodbye!")
                    running = False
                check = False # menghentikan program
            else:
                print("Invalid input. Please enter 'y' or 'n'.")