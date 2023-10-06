def create_large_maze_file():
    # Dimensões do labirinto
    rows = 10
    cols = 10

    # Crie um labirinto grande preenchido aleatoriamente com espaços vazios
    import random
    maze = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

    # Garanta que o ponto de partida e o ponto de chegada sejam espaços vazios
    maze[0][1] = 1
    maze[9][9] = 1

    # Salve o labirinto no arquivo "labirinto.txt"
    with open("labirinto.txt", "w") as file:
        for row in maze:
            file.write("".join(map(str, row)) + "\n")

if __name__ == "__main__":
    # Criar o arquivo de labirinto grande
    create_large_maze_file()
