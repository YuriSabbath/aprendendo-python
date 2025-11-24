# Python quiz game

# 1️⃣ Perguntas do quiz
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

# 2️⃣ Opções de resposta (na mesma ordem das perguntas)
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# 3️⃣ Respostas corretas
answers = ("C", "D", "A", "A", "B")

# 4️⃣ Estado do jogo
guesses = []          # Armazena as respostas do jogador
score = 0             # Total de acertos
question_num = 0      # Índice da pergunta atual

# 5️⃣ Loop principal do quiz
for question in questions:
    print("-------------------------")
    print(question)                 # Exibe a pergunta atual

    for option in options[question_num]:
        print(option)               # Exibe as opções da pergunta

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)           # Guarda o palpite

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")           # Resposta certa
    else:
        print("INCORRECT!")         # Resposta errada
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1               # Avança para a próxima pergunta

# 6️⃣ Resultados finais
print("------------------------------")
print("            RESULTS           ")
print("------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")          # Lista de respostas corretas
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")           # Lista de palpites do jogador
print()

score = int(score / len(questions) * 100)   # Porcentagem final
print(f"Your score is: {score}%")
