# Python quiz game

# 1️⃣ As perguntas do quiz
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

# 2️⃣ As opções de cada pergunta (na mesma ordem)
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# 3️⃣ As respostas corretas
answers = ("C", "D", "A", "A", "B")

# 4️⃣ Variáveis auxiliares
guesses = []   # Onde ficam armazenadas as respostas do jogador
score = 0      # Contador de acertos
question_num = 0  # Índice da pergunta atual

# 5️⃣ Loop principal: faz as perguntas
for question in questions:
    print("-------------------------")
    print(question)  # Mostra a pergunta

    for option in options[question_num]:  # Mostra as opções correspondentes
        print(option)

    # Recebe o palpite do jogador
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)  # Guarda o palpite na lista

    # Verifica se está certo
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1  # Passa pra próxima pergunta

# 6️⃣ Depois que o loop termina, mostra os resultados
print("------------------------------")
print("            RESULTS           ")
print("------------------------------")

# Mostra todas as respostas corretas
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

# Mostra os palpites do jogador
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Calcula a porcentagem de acertos
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
